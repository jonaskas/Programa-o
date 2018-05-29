"""
Files - example
"""

import os
import time
from pathlib import Path

file = open("_test_files/example.txt", "r")
backup = open("_test_files/backup.txt", "w")

backup.write(file.read())

file.close()
backup.close()
