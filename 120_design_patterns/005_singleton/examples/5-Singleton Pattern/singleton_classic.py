class Singleton(object):
    ans = None

    @staticmethod
    def instance():
        if  '_instance' not in Singleton.__dict__:
             Singleton._instance = Singleton()
        return Singleton._instance

s1 = Singleton.instance()
s2 = Singleton.instance()

a__ s1 is s2

s1.ans = 42

a__ s2.ans == s1.ans
print('Assertions passed.')
     