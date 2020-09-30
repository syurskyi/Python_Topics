import datetime

vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!",
    "what time is it" : datetime.datetime.now().strftime("%H:%M")
}

___ foo(query, vocabulary):
    if query __ vocabulary:
        r_ vocabulary[query]
    else:
        r_ "I don't understand that!"