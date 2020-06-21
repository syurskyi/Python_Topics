# ______ struct
#
# f _ o.. "win-ntfs.dd" __
#
# bpb _ b_a_
# ___
#     bpb _ f.r.. 512
# f..
#     f.c..
#
# bytespersector _ ?.u.. "<h", ? 0x00B:0x00D
# print ?
#
# sectorspercluster _ ? 0x00D
# print ?
#
# clustersize _ b.. 0 * in. s..
# print ?
#
# # sectors in volume
# secs _ ?.u..("<Q" ? 0x028:0x030
# print ?
#
# #  quad word for the first cluster
# mftloc _ ?.u..("<Q" ? 0x030:0x038
# mftmirrloc _ ?.u..("<Q" ? 0x038:0x040
# print ?
# print ?
#
# #  calculate the first MFT sector location in bytes
# firstmftsector _ m.. 0 * c..
# print f..
