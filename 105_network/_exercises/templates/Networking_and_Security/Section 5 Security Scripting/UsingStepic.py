# need PIL and stepic packages
______ Image, stepic

i _ Image.o..("bullpuppies.jpg")
i.show
#  could open a file here
# f = open("myfile", "r")
# text = f.read()

steg _ stepic.en..(i, "This is some text")
# steg = stepic.encode(i, text)

steg.save("steg.jpg", "JPEG")

i2 _ Image.o..("steg.jpg")
i2.show
