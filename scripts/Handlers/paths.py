#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|



import os
from translater import translating
from loadingSpinner import Spinner   

#____ ____ ____ ___ _ ____ _  _ _  _ ____ _ ____ ____    ___  ____ ____    ____ _  _ ____ _  _ _ _  _ ____ 
#| __ |___ [__   |  | |  | |\ | |\ | |__| | |__/ |___    |  \ |___ [__     |    |__| |___ |\/| | |\ | [__  
#|__] |___ ___]  |  | |__| | \| | \| |  | | |  \ |___    |__/ |___ ___]    |___ |  | |___ |  | | | \| ___] 
                                                                                                          

# Evite la récursivité 
class PathHandler:
    def __init__(self, root_dir=None, working_folder_path=None):
        self.root_dir = root_dir if root_dir else os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        self.working_folder_path = working_folder_path if working_folder_path else ""

        self.spinner = Spinner()
        self.translate = translating()



