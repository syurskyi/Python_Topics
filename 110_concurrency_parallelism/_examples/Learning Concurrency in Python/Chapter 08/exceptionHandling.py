______ m..
______ __ ___
______ tr..

class MyProcess(multiprocessing.Process):
  
  ___ __init__(self, pipein):
    super(MyProcess, self).__init__()
    self.pipein = pipein

  ___ run(self):
    try:
      raise Exception("This broke stuff")
    except:
      except_type, except_class, tb = sys.exc_info()

      self.pipein = os.fdopen(self.pipein, 'w')
      self.pipein.write(str(tb))
      self.pipein.close()

___ main():
  pipeout, pipein = os.pipe()

  childProcess = MyProcess(pipein)
  childProcess.start()
  childProcess.join()

  os.close(pipein)
  pipeout = os.fdopen(pipeout)

  pipeContent = pipeout.read()
  print("Exception: {}".format(pipeContent))

if __name__ == '__main__':
  main()
