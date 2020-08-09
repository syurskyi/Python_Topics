class Solution(object
  ___ findDuplicate(self, paths
    """
    :type paths: List[str]
    :rtype: List[List[str]]
    """
    d = collections.defaultdict(list)
    ___ path in paths:
      raw = path.split(" ")
      dirPath = raw[0]
      ___ data in raw[1:]:
        name, sign = data.split("(")
        d[sign].append(dirPath + "/" + name)
    r_ filter(lambda x: le.(x) > 1, d.values())
