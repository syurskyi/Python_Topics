# _____ struct
# f _ o.. "win-ntfs.dd" __
#
# bpb _ b_a_
# ___
#     bpb _ f.r.. 512
# f..
#     f.c..
#
# #  figure out the size of a cluster
# bytespersector _ ?.u.. "<h" ? 0x00B:0x00D
# sectorspercluster _ ? 0x00D
# clustersize _ b.. 0 * in. ?
#
# #  quad word for the first cluster
# mftloc _ ?.u..("<Q", ?[0x030:0x038
# mftmirrloc _ ?.u.. "<Q" ? 0x038:0x040
#
# #  calculate the first MFT sector location in bytes
# firstmftsector _ m.. 0 * c..
# print ?
#
# f _ o..("win-ntfs.dd", __)
# f.s.. ?
# # $mft
# #  read 1024, which is the size of an attribute in NTFS
# mft _ f.r.. 1024
# #  get the first 4 bytes, which should be FILE
# value _ ? 0x00:0x04
# print ?
# #  sequence number of the record
# seqno _ ?.u.. "<h", ? 0x010:0x012
# print ?
# #  actual size of the record
# recsize _ ?.u.. "<I" ? 0x018:0x01C
# print ?
