from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

def debug(message, success):
    print(f'[DEBUG TEST] {message} : {("❌", "✅")[success]}')