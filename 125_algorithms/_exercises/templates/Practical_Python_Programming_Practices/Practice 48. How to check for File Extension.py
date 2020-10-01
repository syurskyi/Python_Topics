exe  _ ['gif','png','jpeg','jpg','svg','txt']

filexe _ i..("Insert file with extension: ").sp..('.')
__ le.(filexe) >_ 2:
    Extension _ filexe[-1].l..
    __ Extension __ exe:
        print("File extension exist")
    ____
        print("File extension does not exist")
____
    print("File does not have extension")