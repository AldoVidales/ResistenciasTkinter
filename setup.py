import sys
from cx_Freeze import setup, Executable
from credits import  resource_path
import os
icon=resource_path('icon.ico')

PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
include_files = [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),os.path.join('lib','tk86.dll')),
                 (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),os.path.join('lib','tcl86.dll'))]


base=None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables=[Executable('main.py',base=base,icon=icon,shortcut_name="Calculadora de resistencias",shortcut_dir="DesktopFolder")]

setup(name='Calculadora de resistencias installer',
      version='1.0',
      author='Aldo Vidales',
      description='Calculadora de resistencias installer',
      options={"build_exe": {"include_files": include_files}},
      executables=executables)



