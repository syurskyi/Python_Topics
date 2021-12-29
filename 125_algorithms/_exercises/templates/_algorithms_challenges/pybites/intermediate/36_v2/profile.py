___ get_profile(name,age,*args,**kwargs):
    print(args,kwargs)

    __ type(age) != int:
        raise ValueError("age must be interger")



    __ len(args) > 5:
        raise ValueError("at most 5 sports")

    
    
    result =  {'name': name,'age': age}

    __ args:
        result['sports'] = sorted(args)


    __ kwargs:
        result['awards'] = kwargs

    return result            








