def get_profile(name,age,*args,**kwargs):
    print(args,kwargs)

    if type(age) != int:
        raise ValueError("age must be interger")



    if len(args) > 5:
        raise ValueError("at most 5 sports")

    
    
    result =  {'name': name,'age': age}

    if args:
        result['sports'] = sorted(args)


    if kwargs:
        result['awards'] = kwargs

    return result            








