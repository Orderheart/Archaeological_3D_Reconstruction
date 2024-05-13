import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "千映：基于高斯喷溅的端边云田野考古三维重建系统",
    version = "1.3",
    description = "Modern GUI for Python applications",
    author = "四川大学 千映团队",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
