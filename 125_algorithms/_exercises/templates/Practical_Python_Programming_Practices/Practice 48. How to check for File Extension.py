exe  _ ['gif','png','jpeg','jpg','svg','txt']

filexe _ input("Insert file with extension: ").split('.')
__ le.(filexe) >_ 2:
    Extension _ filexe[-1].lower()
    __ Extension __ exe:
        print("File extension exist")
    ____
        print("File extension does not exist")
____
    print("File does not have extension")