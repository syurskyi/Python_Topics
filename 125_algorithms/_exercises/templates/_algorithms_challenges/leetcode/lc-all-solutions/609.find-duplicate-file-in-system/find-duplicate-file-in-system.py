c_ Solution(o..
  ___ findDuplicate  paths
    """
    :type paths: List[str]
    :rtype: List[List[str]]
    """
    d = c...defaultdict(l..)
    ___ p.. __ paths:
      raw = p...s..(" ")
      dirPath = raw[0]
      ___ data __ raw[1:]:
        name, sign = data.s..("(")
        d[sign].a..(dirPath + "/" + name)
    r.. filter(l.... x: l..(x) > 1, d.values
