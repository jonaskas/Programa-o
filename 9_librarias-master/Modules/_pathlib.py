"""
pathlib
See: https://docs.python.org/3.6/library/pathlib.html
"""

from pathlib import Path

path = Path(r"C:\Program Files").parent
print(path)

path = path.joinpath("Temp")
print(path)
