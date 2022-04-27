____ c.. _______ C..

_______ r__

CAR_DATA 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

w__ r__.S.. __ s
    data s.g.. ? .j..


# your turn:
___ most_prolific_automaker(year
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    cnt C..(row["automaker"] ___ row __ data
                  __ row["year"] __ year).m..
    r.. cnt 0 0 


___ get_models(automaker, year
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    r.. s..([row["model"] ___ row __ data
                __ row["automaker"] __ automaker a..
                row["year"] __ year])