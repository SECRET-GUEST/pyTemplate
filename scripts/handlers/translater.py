#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|


from PyQt5.QtCore import QLocale
from googletrans import Translator


#____ _ _  _ ___  _    ____    ___ ____ ____ _  _ ____ _    ____ ___ ____ ____ 
#[__  | |\/| |__] |    |___     |  |__/ |__| |\ | [__  |    |__|  |  |___ |__/ 
#___] | |  | |    |___ |___     |  |  \ |  | | \| ___] |___ |  |  |  |___ |  \ 
                                                                              

class translating:
    def __init__(self):
        self.translator = Translator()
        self.system_locale = QLocale.system().name()[:2]  # Get the two-letter language code

    def translate(self, msg):
        if self.system_locale != 'en':
            try:
                translated_msg = self.translator.translate(msg, dest=self.system_locale).text
            except Exception as e:
                translated_msg = msg  # If translation fails, default to the original message
        else:
            translated_msg = msg

        return translated_msg
