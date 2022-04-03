import json
import re
import tempfile
import os


class Request:

    def __init__(self, data):
        self.data = data
        self.headers = data.headers
        self.path: str = data.path
        self.request_type: str = data.command
        self.server_address: str = data.client_address
        self.server_version: str = data.server_version
        self.protocol_version: str = data.protocol_version

        self.query = self._parse_query()
        self.body = self._parse_body()
        self.files = self._parse_files()

    def _parse_files(self):
        content_type = self.get('Content-Type')
        result = {}
        if content_type is None or 'multipart/form-data' not in content_type:
            return result

        boundary = content_type.split('=')[1]
        content_length = int(self.get('Content-Length'))
        line = self.data.rfile.readline().decode('utf8')
        content_length -= len(line)

        if boundary not in line:
            raise IOError('Content not begin with boundary')

        while content_length > 0:
            line = self.data.rfile.readline().decode('utf8')
            content_length -= len(line)
            fn = re.findall(r'Content-Disposition.*name="(.*)"; filename="(.*)"', line)[0]
            filename = fn[0]

            if not fn:
                raise FileNotFoundError('Can\'t find out file name...')

            fn = os.path.join(os.getcwd(), fn[1])

            line = self.data.rfile.readline()
            content_length -= len(line)
            line = self.data.rfile.readline()
            content_length -= len(line)

            temp = tempfile.TemporaryFile()

            pre_line = self.data.rfile.readline()
            content_length -= len(pre_line)
            while content_length > 0:
                line = self.data.rfile.readline()
                content_length -= len(line)
                if bytes(boundary, 'ascii') in line:
                    pre_line = pre_line[0:-1]
                    if pre_line.endswith(b'\r'):
                        pre_line = pre_line[0:-1]
                    temp.write(pre_line)
                    result[filename] = temp
                    break
                else:
                    temp.write(pre_line)
                    pre_line = line
        return result

    def _parse_body(self):
        content_length = self.get('Content-Length')
        content_type = self.get('Content-Type')
        result = {}
        if content_type is None or 'multipart/form-data' in content_type:
            return result
        if content_length:
            body = self.data.rfile.read(int(content_length))
            if body:
                body = body.decode('utf8').replace("'", '"')
                result = json.loads(body)
        return result

    def _parse_query(self):
        chars = self.path.split('?')
        if len(chars) < 2:
            return {}
        chars = chars.pop().split('&')
        queries = {}
        for char in chars:
            char = char.split('=')
            queries[char[0]] = char[1]
        return queries

    def get(self, value) -> str:
        return self.headers.get(value)

    def accepts(self) -> str:
        return self.headers.get('accept')
