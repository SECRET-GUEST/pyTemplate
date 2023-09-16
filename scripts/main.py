#     |               |                                 |
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  |                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    |
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                 |                     |
#  |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#          |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#  |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#               |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#       |                              blablablablabla some desctiption                   |                                           |               |                                           |               |                                           |                    |                                           |
                
#                          /                      |    v    |                    \
#                     here or wherever you want this is just a random art you can delete
#                   s       |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |  
#     |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                               |                                   |     |                  
#                  |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#             |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                        =)
                
#
#                               |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#             |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#     |                        |                                         |                                |
                
#
#                                                    !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#     |               |                                 !
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  !                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    !
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                                                |
              
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|

from PyQt5.QtWidgets import QMainWindow,QVBoxLayout, QApplication
from PyQt5.QtGui import QIcon
import sys


# Handlers
from handlers.paths import PathHandler
from handlers.pathHelp import resource_path

from handlers.zoom_handler import enable_zoom
from handlers.logInfo import logz
from handlers.cypunk1 import cypunk3MainWindow




#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3



##### Just some example who works with the theme and the handlers, can be deleted#
##################################################################################

logger = None #To use Logger in all applications


# Faster to integrate with this window's inception method 
# TODO : rework.class windowCeption(cypunk1Window) to integrate the 2nd main window

class windowCeption(cypunk3MainWindow):
    def __init__(self):
        super().__init__(
            title="Oh hi Mark",
            window_size=("300x100"),
            btn_minimize="ico/hide.png",
            btn_show="ico/open.png",
            stylesheet_path= None
        )
        global logger
        # If logger is provided, use it, otherwise create a new logz object with the specified settings
        self.logger = logger or logz.configLogs("Macara", "ERRORS.log", use_qt_dialogs=True)

        # Create an instance of logz to access the ThemeChangedSignal class
        logz_instance = logz("")

        # Create an instance of ThemeChangedSignal to manage theme change events
        self.theme_changed_signal = logz_instance.ThemeChangedSignal()

        # Load the last used theme from the configuration file
        last_theme = self.logger.load_config()

        # Update the theme of the window based on the last used theme
        self.logger.update_theme(self, last_theme)

        # Connect the theme_changed signal to the update_theme_slot method to handle theme changes
        self.theme_changed_signal.theme_changed.connect(self.update_theme_slot)

        # Configure the error handler
        #self.tables = DarthBMO(self.logger)

        # Put the main app in the custom window represented by this class
        self.Vlay = QVBoxLayout()
        self.main_page = MainWindow(parent=self)
        #self.main_page.set_overlay(self.overlay)
        self.Vlay.addSpacing(28)
        self.Vlay.addWidget(self.main_page)

        self.central_widget.setLayout(self.Vlay)

    # Update themes
    def update_theme_slot(self, theme):
        self.logger.update_theme(self, theme)



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the logger, overlay, and tables attributes from the parent window
        self.logger = parent.logger
        #self.overlay = parent.overlay
        #self.tables = parent.tables
        #self.recorder = parent.recorder

        # Theme initialization
        self.theme_changed_signal = parent.theme_changed_signal

        # Create a dictionary to store widget instances
        self.widget_instances = {}

        # Enable zooming for this window
        enable_zoom(self)

        self.setWindowIcon(QIcon(self.logger.ressource_path("ico/macara.png")))

        self.initUI()
        self.initMenu()



    # Connect the theme_changed signal to the update_theme_slot method of the Overlay instance
    def set_overlay(self, overlay_instance):
        self.overlay = overlay_instance
        self.theme_changed_signal.theme_changed.connect(self.overlay.update_theme_slot)

        # Add the Overlay instance to the widget_instances dictionary
        self.widget_instances["overlay"] = self.overlay

    def update_all_widgets_theme(self, theme):
        for widget_instance in self.widget_instances.values():
            self.logger.update_theme(widget_instance, theme)



##################################################################################




class myApp(PathHandler):
    def __init__(self):

        pass


    
#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = windowCeption()
    mainApp.show()
    sys.exit(app.exec_())
