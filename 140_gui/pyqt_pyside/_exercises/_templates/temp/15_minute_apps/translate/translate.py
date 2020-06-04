____ ?.QtGui ______ *
____ ?.QtWidgets ______ *
____ ?.?C.. ______ *

____ MainWindow ______ Ui_MainWindow

___
    ____ googletrans ______ Translator
    GOOGLE_TRANSLATE_AVAILABLE = T..

_____ ImportError:
    GOOGLE_TRANSLATE_AVAILABLE = F..

______ json
____ urllib ______ parse
______ requests

LANGUAGES = {
    '<Detect language>': None,
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Arabic': 'ar',
    'Azerbaijani': 'az',
    'Basque': 'eu',
    'Bengali': 'bn',
    'Belarusian': 'be',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Chinese Simplified': 'zh-CN',
    'Chinese Traditional': 'zh-TW',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'tl',
    'Finnish': 'fi',
    'French': 'fr',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian Creole': 'ht',
    'Hebrew': 'iw',
    'Hindi': 'hi',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Kannada': 'kn',
    'Korean': 'ko',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Macedonian': 'mk',
    'Malay': 'ms',
    'Maltese': 'mt',
    'Norwegian': 'no',
    'Persian': 'fa',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Serbian': 'sr',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Spanish': 'es',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Yiddish': 'yi'
}


c_ MainWindow(?MW.., Ui_MainWindow):

    ___  - (self, $ $$
        s__(MainWindow, self). - ($ $$)
        setupUi

        translator = Translator()

        destTextEdit.setReadOnly( st.

        if GOOGLE_TRANSLATE_AVAILABLE:
            srcLanguage.aI..(LANGUAGES.keys())
            srcLanguage.cTC..[st.].c__(update_src_language)
            srcLanguage.sCT..('English')
        ____:
            srcLanguage.hide()

        translateButton.pressed.c__(translate)

        s..

    ___ update_src_language(self, l):
        language_src = LANGUAGES[l]

    ___ google_translate(self, text):
        params = dict(
            dest='en',
            text=text
        )

        if language_src:
            params['src'] = language_src

        ___
            tr = translator.translate(**params)

        _____ E..:
            destTextEdit.setPlainText('Google translate error :(. Try translating from English')
            return F..

        ____:
            return tr.text

    ___ translate
        # Perform pre-translation to English via Google Translate.
        if language_src != 'en':
            text = google_translate(srcTextEdit.toPlainText())
            if not text:
                return F..

        # Already in English.
        ____:
            text = srcTextEdit.toPlainText()

        # Perform translation to piraat.
        r = requests.get(
            'http://api.funtranslations.com/translate/pirate.json?%s' %
            parse.urlencode({'text': text})
        )

        data = json.loads(r.text)
        if 'error' __ data:
            destTextEdit.setPlainText("%s\n\n%s" % (data['error']['message'], text))
        ____:
            destTextEdit.setPlainText(data['contents']['translated'])



if __name__ __ '__main__':

    app = ?A..([])
    window = MainWindow()
    app.e..()