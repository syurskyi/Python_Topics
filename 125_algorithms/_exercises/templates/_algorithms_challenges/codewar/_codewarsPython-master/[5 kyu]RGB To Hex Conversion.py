___ rgb(r, g, b
    r,g,b = [element __ element <= 255 else 255 ___ element in (r,g,b)]
    r,g,b = [element __ element >= 0 else 0 ___ element in (r,g,b)]
    r_ ''.join([hex(element)[2:].upper().zfill(2) ___ element in (r,g,b)])

print(rgb(255,255,300))
print(rgb(1,2,3))
print(rgb(0,0,0))