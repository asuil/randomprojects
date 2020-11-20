import sys
from cx_Freeze import setup, Executable

packages = ["pygame","os"]
resources = []

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": packages,"include_files":resources}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Last Raindrops",
        version = "0.1",
        description = "lr-reteam",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])
