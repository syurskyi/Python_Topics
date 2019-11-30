import sys
print(sys.path)
# ['', 'C:\\PP4thEd\\Examples', ...plus standard library paths deleted... ]
# ######################################################################################################################

sys.path.append(r'C:\mydir')
print(sys.path)
# ['', 'C:\\PP4thEd\\Examples', ...more deleted..., 'C:\\mydir']
# ######################################################################################################################