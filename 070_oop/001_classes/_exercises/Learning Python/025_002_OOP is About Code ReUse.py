class Employee:                      # General superclass

    def computeSalary(self):      # Common or default behavior
        pass

    def giveRaise(self):
        pass

    def promote(self):
        pass

    def retire(self):
        pass


class Engineer(Employee):            # Specialized subclass
     def computeSalary(self):    # Something custom here
         pass


bob = Employee()                     # Default behavior
mel = Engineer()                     # Custom salary calculator


company = [bob, mel]                   # A composite object
for emp in company:
    print(emp.computeSalary())         # Run this object's version


def processor(reader, converter, writer):
    while 1:
        data = reader.read()
        if not data: break
        data = converter(data)
        writer.write(data)


class Reader:
    def read(self):              # Default behavior and tools
        pass

    def other(self):
        pass


class FileReader(Reader):
    def read(self):               # Read from a local file
        pass


class SocketReader(Reader):
    def read(self):               # Read from a network socket
        pass

# processor(FileReader(...),   Converter,  FileWriter(...))
# processor(SocketReader(...), Converter,  TapeWriter(...))
# processor(FtpReader(...),    Converter,  XmlWriter(...))