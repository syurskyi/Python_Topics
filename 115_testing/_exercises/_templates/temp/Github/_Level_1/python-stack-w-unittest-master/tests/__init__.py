______ sys, os

myPath _ os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')
