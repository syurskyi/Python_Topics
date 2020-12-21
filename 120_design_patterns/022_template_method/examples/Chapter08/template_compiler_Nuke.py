import abc

class Compiler(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def collectSource(self):
        pass

    @abc.abstractmethod
    def compileToObject(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

class iOSCompiler(Compiler):
    def collectSource(self):
        print("Collecting Swift Source Code")

    def compileToObject(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program runing on runtime environment")


iOS = iOSCompiler()
iOS.compileAndRun()
