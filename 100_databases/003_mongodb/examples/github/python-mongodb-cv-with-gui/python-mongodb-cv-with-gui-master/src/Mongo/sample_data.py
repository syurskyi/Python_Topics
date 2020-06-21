# a basic class for fetching random data
class SampleData:    
    def __init__(self):
        self.names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
        self.company_type = ['LLC','Inc','Company','Corporation']
        self.company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian','Mexican', 'American', 'Sushi Bar', 'Vegetarian']
    
    def PrintSampleData(self):
        print('Printing Sample Data:')
        print('names=',self.names)
        print('company_types=',self.company_type)
        print('company_cuisine=',self.company_cuisine)

    def GetRandomName(self):
        tmp_name=self.names[randint(0, (len(self.names)-1))]
        tmp_company_type=self.company_type[randint(0,(len(self.company_type)-1))]
        final_name=tmp_name+' '+tmp_company_type
        return final_name
    def GetRandomRating(self):
        return randint(1, 5)
    def GetRandomCuisine(self):
        tmp_company_cuisine=self.company_cuisine[randint(0,(len(self.company_cuisine)-1))]
        return tmp_company_cuisine