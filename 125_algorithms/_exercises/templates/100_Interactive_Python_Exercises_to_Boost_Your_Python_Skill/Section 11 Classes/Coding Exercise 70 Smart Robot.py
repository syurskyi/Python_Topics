class Robot:

    def __init__(self):
        pass

    def speak(self, query):
        if query == 'hi robot':
            return 'hi human'
        else:
            return "I don't know"