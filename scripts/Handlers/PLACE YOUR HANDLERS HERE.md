# Instructions for Handling Scripts

To ensure the proper functionality of your application, follow these steps:

1. **Placing Handlers:** All handler scripts should be placed in the designated folder.

2. **Provided Scripts:** We've supplied various example scripts to guide you:
   - `loadingSpinner`: A spinner animation for queue in CMD.
   - `paths` : A path manager which you can use as an argument for classes (e.g., `class MainWindow(pathHandler)`).
   - `pathHelp`: A ressource path manager to avoid paths issues  

### Usage Instructions for pathHelp :

 To make the resource_path function work, especially when compiling the script to an executable,
 you need to replace all your relative paths with calls to the resource_path function. 
 This ensures the paths remain correct whether running as Python script or as a compiled executable.

Step 1: Import the function in your script:
---
from handlers.pathHelp import resource_path

Step 2: Use the function to get the correct paths to your resources:
---
example_path = resource_path('path/to/your/resource.png')



