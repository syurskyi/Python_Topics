______ struct

f _ o..("mbr.dd", __)

mbr _ b_a_
___
    mbr _ f.r..(512)
f..
    f.c..

sig _ struct.unpack("<I", mbr[0x1B8:0x1BC])
print("Disk signature: ", sig[0])
active _ mbr[0x1BE]
__ active __ 0x80:
	print("Active flag: Active")
____
	print("Active flag: Not active")

lb__tart _ struct.unpack("<I", mbr[0x1C6:0x1CA])
print("Partition Start (LBA): ", lb__tart[0])
lbaend _ struct.unpack("<I", mbr[0x1C9:0x1CD])
print("Partition End (LBA): ", lbaend[0])

