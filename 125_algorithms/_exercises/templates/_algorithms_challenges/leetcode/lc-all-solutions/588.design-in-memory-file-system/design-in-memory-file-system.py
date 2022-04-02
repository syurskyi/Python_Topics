c_ FileNode(o..
  ___ - , name
    isFolder = T..
    childs    # dict
    name = name
    data = ""

  ___ appendData  data
    data += data

  ___ readAll
    r.. data


c_ FileSystem(o..
  ___ -
    root = FileNode("/")

  ___ ls  path
    """
    :type path: str
    :rtype: List[str]
    """
    fd = lookup(path, F..)
    __ n.. fd:
      r.. []
    __ n.. fd.isFolder:
      r.. [fd.name]
    files    # list
    ___ file __ fd.childs:
      files.a..(file)
    files.s..()
    r.. files

  ___ lookup  path, isAutoCreate
    path = path.s..("/")
    p = root
    ___ name __ path:
      __ n.. name:
        _____
      __ name n.. __ p.childs:
        __ isAutoCreate:
          p.childs[name] = FileNode(name)
        ____:
          r.. N..
      p = p.childs[name]
    r.. p

  ___ mkdir  path
    """
    :type path: str
    :rtype: void
    """
    lookup(path, T..)

  ___ addContentToFile  filePath, content
    """
    :type filePath: str
    :type content: str
    :rtype: void
    """
    fd = lookup(filePath, T..)
    fd.isFolder = F..
    fd.appendData(content)

  ___ readContentFromFile  filePath
    """
    :type filePath: str
    :rtype: str
    """
    fd = lookup(filePath, F..)
    __ fd:
      r.. fd.readAll()
    r.. ""

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
