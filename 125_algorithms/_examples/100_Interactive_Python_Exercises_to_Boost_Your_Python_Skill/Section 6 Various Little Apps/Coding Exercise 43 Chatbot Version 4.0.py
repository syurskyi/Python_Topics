import datetime
import difflib


vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!",
    "what time is it" : datetime.datetime.now().strftime("%H:%M")
}

def foo(query, vocabulary):
    new_vocabulary = {key:[value, difflib.SequenceMatcher(None, query, key).ratio()]
    for (key,value) in vocabulary.items()}
    return new_vocabulary[max(new_vocabulary, key=lambda k: new_vocabulary[k][1])][0]