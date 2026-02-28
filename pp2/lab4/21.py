import sys
import importlib

for _ in range(int(sys.stdin.readline())):
    m_path, attr = sys.stdin.readline().split()
    try:
        m = importlib.import_module(m_path)
        if hasattr(m, attr):
            print("CALLABLE" if callable(getattr(m, attr)) else "VALUE")
        else:
            print("ATTRIBUTE_NOT_FOUND")
    except ImportError:
        print("MODULE_NOT_FOUND")