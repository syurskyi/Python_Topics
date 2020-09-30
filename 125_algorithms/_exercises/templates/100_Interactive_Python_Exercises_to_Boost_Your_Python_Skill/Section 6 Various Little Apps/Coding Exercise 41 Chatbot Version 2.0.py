vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!"
}

def foo(query, vocabulary):
    if query in vocabulary:
        return vocabulary[query]
    else:
        return "I don't understand that!"