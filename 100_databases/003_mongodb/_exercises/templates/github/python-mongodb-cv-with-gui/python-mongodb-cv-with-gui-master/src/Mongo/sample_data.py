# a basic class for fetching random data
c_ SampleData:
    ___  -
        names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
        company_type = ['LLC','Inc','Company','Corporation']
        company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian','Mexican', 'American', 'Sushi Bar', 'Vegetarian']
    
    ___ PrintSampleData
        print('Printing Sample Data:')
        print('names=',names)
        print('company_types=',company_type)
        print('company_cuisine=',company_cuisine)

    ___ GetRandomName
        tmp_name=names[randint(0, (le.(names)-1))]
        tmp_company_type=company_type[randint(0,(le.(company_type)-1))]
        final_name=tmp_name+' '+tmp_company_type
        return final_name
    ___ GetRandomRating
        return randint(1, 5)
    ___ GetRandomCuisine
        tmp_company_cuisine=company_cuisine[randint(0,(le.(company_cuisine)-1))]
        return tmp_company_cuisine