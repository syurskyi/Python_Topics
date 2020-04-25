______ struct

f _ o..("win-ntfs.dd", __)

bpb _ b_a_
___
    bpb _ f.r..(512)
f..
    f.c..

bytespersector _ struct.unpack("<h", bpb[0x00B:0x00D])
print(bytespersector)

sectorspercluster _ bpb[0x00D]
print(sectorspercluster)

clustersize _ bytespersector[0] * in.(sectorspercluster)
print(clustersize)

# sectors in volume
secs _ struct.unpack("<Q", bpb[0x028:0x030])
print(secs)

#  quad word for the first cluster
mftloc _ struct.unpack("<Q", bpb[0x030:0x038])
mftmirrloc _ struct.unpack("<Q", bpb[0x038:0x040])
print(mftloc)
print(mftmirrloc)

#  calculate the first MFT sector location in bytes
firstmftsector _ mftmirrloc[0] * clustersize
print(firstmftsector)
