import os
import sys
from pathlib import Path
# sys.path.append(__file__ + "/..")
# print(os.getcwd())

print(os.path.realpath("/.."))

mod_path = Path(__file__).parent
print(mod_path)

dirname = os.path.dirname(__file__)
print(dirname)
tasks = os.path.join(dirname, "/../tasks.py")
print(tasks)
import tasks
print(a)
