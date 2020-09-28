from cx_Freeze import setup, Executable
import sys

build_exe_options = {'packages': ['os'], 'include_files': ['data/'], 'excludes': ['mpl_toolkits']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

# buildOptions = dict(include_files=['data/'])


setup(name='Sudoku',
      version='0.2',
      description='Sudoki with autosolver and generator',
      options=dict(build_exe=build_exe_options),
      author="Florian Lang",
      executables=[Executable('sudoku.py', base=base, icon='data/sudoku.ico')])
