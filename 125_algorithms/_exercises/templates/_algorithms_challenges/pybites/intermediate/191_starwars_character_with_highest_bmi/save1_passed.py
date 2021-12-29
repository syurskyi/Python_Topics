data = """Luke Skywalker,172,77
          C-3PO,167,75
          R2-D2,96,32
          Darth Vader,202,136
          Leia Organa,150,49
          Owen Lars,178,120
          Beru Whitesun lars,165,75
          R5-D4,97,32
          Biggs Darklighter,183,84
          Obi-Wan Kenobi,182,77
          Anakin Skywalker,188,84
          Chewbacca,228,112
          Han Solo,180,80
          Greedo,173,74
          Jek Tono Porkins,180,110
          Yoda,66,17
          Palpatine,170,75
          Boba Fett,183,78.2
          IG-88,200,140
          Bossk,190,113
"""


___ person_max_bmi(data=data):
    """Return (name, BMI float) of the character in data that
       has the highest BMI (rounded on 2 decimals)"""

    data = data.splitlines()

    BMI_info = []
    BMI_final = []

    i = 0
    while i < len(data):
        BMI_info.append(data[i].split(',')[1:])
        i += 1

    for x, y in BMI_info:
        BMI_final.append(float(y) / (int(x) / 100) ** 2)

    highest_BMI_position = BMI_final.index(max(BMI_final))
    highest_BMI_name = data[highest_BMI_position].strip().split(',')[0]
    highest_BMI_BMI = max(BMI_final)

    return highest_BMI_name, round(highest_BMI_BMI, 2)