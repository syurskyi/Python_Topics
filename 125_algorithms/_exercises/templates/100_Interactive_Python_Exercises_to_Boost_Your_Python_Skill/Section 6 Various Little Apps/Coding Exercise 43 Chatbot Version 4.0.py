______ datetime
______ difflib


vocabulary _ {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!",
    "what time is it" : datetime.datetime.now().strftime("%H:%M")
}

___ foo(query, vocabulary):
    new_vocabulary _ {key:[value, difflib.SequenceMatcher(None, query, key).ratio()]
    ___ (key,value) __ vocabulary.i..()}
    r_ new_vocabulary[ma.(new_vocabulary, key_lambda k: new_vocabulary[k][1])][0]