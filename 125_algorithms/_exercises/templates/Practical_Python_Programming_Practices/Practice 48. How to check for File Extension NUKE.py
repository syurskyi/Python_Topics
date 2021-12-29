exe   ['gif','png','jpeg','jpg','svg','txt']

filexe  input("Insert file with extension: ").split('.')
__ l..(filexe) > 2:
    Extension  filexe[-1].l..
    __ Extension __ exe:
        print("File extension exist")
    ____:
        print("File extension does not exist")
____:
    print("File does not have extension")