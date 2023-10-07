#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|
    

import sys, os

#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3

def resource_path(relative_path: str) -> str:
    # The application is compiled (using PyInstaller or InnoSetup)
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS

    else:
        # The application is not compiled and is running from Python source

        # Adjust the base path to point to the project root directory (removing an os path dirname for example)
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    return os.path.join(base_path, relative_path)


# Usage Instructions:
# To make the resource_path function work, especially when compiling the script to an executable,
# you need to replace all your relative paths with calls to the resource_path function. 
# This ensures the paths remain correct whether running as Python script or as a compiled executable.
#
# Step 1: Import the function in your script:
# from handlers.pathHelp import resource_path
#
# Step 2: Use the function to get the correct paths to your resources:
# example_path = resource_path('path/to/your/resource.png')
#
