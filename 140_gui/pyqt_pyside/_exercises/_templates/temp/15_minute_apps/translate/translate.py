____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *

____ MainWindow ______ Ui_MainWindow

___
    ____ googletrans ______ Translator
    GOOGLE_TRANSLATE_AVAILABLE _ T..

_____ ImportError:
    GOOGLE_TRANSLATE_AVAILABLE _ F..

______ ____
____ urllib ______ parse
______ requests

LANGUAGES _ {
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

    ___  -   $ $$
        s__(MainWindow, self). - ($ $$)
        setupUi

        translator _ Translator()

        destTextEdit.sRO..( st.

        __ GOOGLE_TRANSLATE_AVAILABLE:
            srcLanguage.aI..(LANGUAGES.keys())
            srcLanguage.cTC..[st.].c__(update_src_language)
            srcLanguage.sCT..('English')
        ____:
            srcLanguage.hide()

        translateButton.pressed.c__(translate)

        s..

    ___ update_src_language  l):
        language_src _ LANGUAGES[l]

    ___ google_translate  text):
        params _ dict(
            dest_'en',
            text_text
        )

        __ language_src:
            params['src'] _ language_src

        ___
            tr _ translator.translate(**params)

        _____ E..:
            destTextEdit.setPlainText('Google translate error :(. Try translating from English')
            r_ F..

        ____:
            r_ tr.text

    ___ translate
        # Perform pre-translation to English via Google Translate.
        __ language_src !_ 'en':
            text _ google_translate(srcTextEdit.toPlainText())
            __ not text:
                r_ F..

        # Already in English.
        ____:
            text _ srcTextEdit.toPlainText()

        # Perform translation to piraat.
        r _ requests.get(
            'http://api.funtranslations.com/translate/pirate.json?%s' %
            parse.urlencode({'text': text})
        )

        data _ ____.loads(r.text)
        __ 'error' __ data:
            destTextEdit.setPlainText("%s\n\n%s" % (data['error']['message'], text))
        ____:
            destTextEdit.setPlainText(data['contents']['translated'])



__ __name__ __ '__main__':

    app _ ?A..([])
    window _ MainWindow()
    app.e..()