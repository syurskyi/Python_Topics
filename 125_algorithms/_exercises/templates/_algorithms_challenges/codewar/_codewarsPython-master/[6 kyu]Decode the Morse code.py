MORSE_CODE {'.-...': '&', '--..--': ',', '....-': '4',
'.....': '5', '...---...': 'SOS', '-...': 'B', '-..-': 'X',
'.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I',
'..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U',
'..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6',
'-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
'....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
'-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
'--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C',
'---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$',
'.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(',
'---..': '8', '...--': '3'}

___ decodeMorse(morseCode
    MORSE_CODE '@'  = ' '
    morseCode morseCode.s...r..('  ',' @ ')
    r.. ''.j..([MORSE_CODE[code] ___ code __ morseCode.s.. ])


print(decodeMorse('.... . -.--   .--- ..- -.. .   '
#                  H    E Y      J    U   D   E  