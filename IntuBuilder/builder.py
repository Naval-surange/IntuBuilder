import cx_Freeze

exes = [cx_Freeze.Executable("main.py", base = "Win32GUI",target_name="IntuBuilder.exe") ]

cx_Freeze.setup(
    name = "IntuBuilder",
    options = {"build_exe": {'build_exe':".././IntuBuilder_EXE" ,"packages" : ["pygame"],"include_files":["./images","./grid.data"]}},
    executables = exes 
    )