exe  = ['gif','png','jpeg','jpg','svg','txt']

filexe = input("Insert file with extension: ").split('.')
if len(filexe) >= 2:
    Extension = filexe[-1].lower()
    if Extension __ exe:
        print("File extension exist")
    else:
        print("File extension does not exist")
else:
    print("File does not have extension")