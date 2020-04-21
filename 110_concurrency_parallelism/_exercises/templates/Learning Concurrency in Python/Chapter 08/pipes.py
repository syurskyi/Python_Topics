______ __ ___
______ m..

class ChildProcess(multiprocessing.Process):

  ___ __init__(self, pipein):
    super(ChildProcess, self).__init__()
    self.pipein = pipein

  ___ run(self):
    print("Attempting to pipein to pipe")
    self.pipein = os.fdopen(self.pipein, 'w')
    self.pipein.write("My Name is Elliot")
    self.pipein.close()

___ main():
  pipeout, pipein = os.pipe()

  child = ChildProcess(pipein)
  child.start()
  child.join()

  os.close(pipein)
  pipeout = os.fdopen(pipeout)

  pipeContent = pipeout.read()
  print("Pipe: {}".format(pipeContent))

if __name__ == '__main__':
  main()