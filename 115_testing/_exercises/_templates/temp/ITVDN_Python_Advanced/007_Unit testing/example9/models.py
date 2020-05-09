______ json
______ os
______ uuid
____ typing ______ ClassVar


c_ Counter:
    counter: ClassVar[int] _ 0

    ___  -   fixture
        if fixture:
            update_counter()

    ___ update_counter
        __class__.counter +_ 1
        name _ __class__.__name__.lower()
        data _ {}
        if os.path.exists('results.json'
            with open('results.json', 'r') as f:
                data _ json.load(f)
        data.setdefault(name, 0)
        data[name] +_ 1
        with open('results.json', 'w') as f:
            json.dump(data, f)


c_ User(Counter

    ___  -   email, first_name, last_name, uid_None, fixture_False
        super(). - (fixture)
        email _ email
        first_name _ first_name
        last_name _ last_name
        id _ uid o. uuid.uuid4()

    ___ get_full_name
        r_ '{first_name} {last_name}'.f..(
            first_name_first_name,
            last_name_last_name
        )

    ___ __str__
        r_ 'User: <{id}: {name}>'.f..(
            id_id,
            name_get_full_name()
        )


c_ Post(Counter

    ___  -   user, comment: st., fixture_False
        super(). - (fixture)
        user _ user
        comment _ comment
