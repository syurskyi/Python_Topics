class FileNode(object
  ___ __init__(self, name
    self.isFolder = True
    self.childs = {}
    self.name = name
    self.data = ""

  ___ appendData(self, data
    self.data += data

  ___ readAll(self
    r_ self.data


class FileSystem(object
  ___ __init__(self
    self.root = FileNode("/")

  ___ ls(self, path
    """
    :type path: str
    :rtype: List[str]
    """
    fd = self.lookup(path, False)
    __ not fd:
      r_ []
    __ not fd.isFolder:
      r_ [fd.name]
    files = []
    for file in fd.childs:
      files.append(file)
    files.sort()
    r_ files

  ___ lookup(self, path, isAutoCreate
    path = path.split("/")
    p = self.root
    for name in path:
      __ not name:
        continue
      __ name not in p.childs:
        __ isAutoCreate:
          p.childs[name] = FileNode(name)
        ____
          r_ None
      p = p.childs[name]
    r_ p

  ___ mkdir(self, path
    """
    :type path: str
    :rtype: void
    """
    self.lookup(path, True)

  ___ addContentToFile(self, filePath, content
    """
    :type filePath: str
    :type content: str
    :rtype: void
    """
    fd = self.lookup(filePath, True)
    fd.isFolder = False
    fd.appendData(content)

  ___ readContentFromFile(self, filePath
    """
    :type filePath: str
    :rtype: str
    """
    fd = self.lookup(filePath, False)
    __ fd:
      r_ fd.readAll()
    r_ ""

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
