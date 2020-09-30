______ datetime

vocabulary _ {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!",
    "what time is it" : datetime.datetime.now().strftime("%H:%M")
}

___ foo(query, vocabulary):
    __ query __ vocabulary:
        r_ vocabulary[query]
    ____
        r_ "I don't understand that!"