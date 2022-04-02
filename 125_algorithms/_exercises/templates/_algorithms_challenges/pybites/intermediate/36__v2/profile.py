____ typing _______ Type


___ get_profile(name, age, *args, **kwargs

    # Validations
    __ n.. isi..(age, i..
        r.. ValueError

    __ l..(args) > 5:
        r.. ValueError

    user_profile    # dict

    user_profile["name"] = name
    user_profile["age"] = age

    __ l..(args) > 0:
        sport_list = [arg ___ arg __ args]
        sport_list.s..()
        user_profile["sports"] = sport_list

    __ l..(kwargs) > 0:
        award_dict = {key: value ___ key, value __ kwargs.i..}
        user_profile["awards"] = award_dict
    
    r.. user_profile

#if __name__ == "__main__":
    #print(get_profile('tim', 36, 'tennis', 'basketball', champ='helped out team in crisis'))
    #print(get_profile('tim', 36, 'tennis'))