import logging as logcuBABA

    
def whoami():
    logcuBABA.info("Now I'm there")

def foo():
    logcuBABA.info("I'm here")
    whoami()
    logcuBABA.info("I'm back here again")

logcuBABA.basicConfig(
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
    level=logcuBABA.INFO)
foo()


if __name__ == '__main__':
    