_____ struct
f _ o..("win-ntfs.dd", __)

bpb _ b_a_
___
    bpb _ f.r..(512)
f..
    f.c..

#  figure out the size of a cluster
bytespersector _ struct.unpack("<h", bpb[0x00B:0x00D])
sectorspercluster _ bpb[0x00D]
clustersize _ bytespersector[0] * in.(sectorspercluster)

#  quad word for the first cluster
mftloc _ struct.unpack("<Q", bpb[0x030:0x038])
mftmirrloc _ struct.unpack("<Q", bpb[0x038:0x040])

#  calculate the first MFT sector location in bytes
firstmftsector _ mftmirrloc[0] * clustersize
print(firstmftsector)

f _ o..("win-ntfs.dd", __)
f.s..(firstmftsector)
# $mft
#  read 1024, which is the size of an attribute in NTFS
mft _ f.r..(1024)
#  get the first 4 bytes, which should be FILE
value _ mft[0x00:0x04]
print(value)
#  sequence number of the record
seqno _ struct.unpack("<h", mft[0x010:0x012])
print(seqno)
#  actual size of the record
recsize _ struct.unpack("<I", mft[0x018:0x01C])
print(recsize)
