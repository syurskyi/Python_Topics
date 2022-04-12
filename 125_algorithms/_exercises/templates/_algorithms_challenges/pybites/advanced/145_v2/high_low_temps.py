_______ c__
_______ __
_______ __
_______ u__.r..
____ c.. _______ n..
____ d__ _______ d__

_______ p.... __ pd

DATA_FILE "http://projects.bobbelderbos.com/pcc/weather-ann-arbor.csv"
STATION n..("Station", "ID Date Value")

TMP '/tmp'
LOCAL_FILE __.p...j..('/tmp', 'weather-ann-arbor.csv')
__ n.. __.p...i..(LOCAL_FILE
    u__.r...u..(DATA_FILE, LOCAL_FILE)


___ high_low_record_breakers_for_2015
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value

    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    w__ o.. LOCAL_FILE) __ f:
        the_data s..([{
            'id': x 'ID' ,
            'date': d__.s..(x 'Date' , '_Y-%m-_d').date(),
            'element': x 'Element' ,
            'value': i..(x 'Data_Value' )
        } ___ x __ c__.DictReader(f) __ n.. __.m.. _ \d{4}-02-29', x 'Date' )],
            key=l.... x: (x 'id'  + x 'date' .s..('%m%d_Y')))
    dataset [{'id': x 'id' ,
                'monthday': x 'date' .s..('%m_d'),
                'year': x 'date' .year,
                'element': x 'element' ,
                'value': x 'value'
                } ___ x __ the_data]

    data_before_2015_left pd.DataFrame(x ___ x __ dataset __ x 'year'  < 2015 a.. x 'element'  __ 'TMIN').drop(
         'element', 'year' , axis=1).set_index( 'id', 'monthday' ).groupby(
         'id', 'monthday' ).m..(level='monthday').rename(columns={'value': 'mina'})

    data_before_2015_right pd.DataFrame(x ___ x __ dataset __ x 'year'  < 2015 a.. x 'element'  __ 'TMAX').drop(
         'element', 'year' , axis=1).set_index( 'id', 'monthday' ).groupby(
         'id', 'monthday' ).m..(level='monthday').rename(columns={'value': 'maxa'})

    early_dataset data_before_2015_left.j..(data_before_2015_right, lsuffix='_l', rsuffix='_r')

    data_for_2015_left pd.DataFrame(x ___ x __ dataset __ x 'year'  __ 2015 a.. x 'element'  __ 'TMIN').drop(
         'element', 'year' , axis=1).set_index( 'id', 'monthday' ).groupby(
         'id', 'monthday' ).m..(level='monthday').rename(columns={'value': 'minb'})

    data_for_2015_right pd.DataFrame(x ___ x __ dataset __ x 'year'  __ 2015 a.. x 'element'  __ 'TMAX').drop(
         'element', 'year' , axis=1).set_index( 'id', 'monthday' ).groupby(
         'id', 'monthday' ).m..(level='monthday').rename(columns={'value': 'maxb'})

    late_dataset data_for_2015_left.j..(data_for_2015_right)

    compare_set early_dataset.j..(late_dataset)

    result {'min': [], 'max': []}
    ___ row __ compare_set.itertuples
        __ row.mina > row.minb:
            result 'min' .a..(
                STATION(row.Index[0], d__.s.. _*2015{row.Index[1]}', '_Y%m_d').date(), row.minb / 10.0))
        __ row.maxa < row.maxb:
            result 'max' .a..(
                STATION(row.Index[0], d__.s.. _*2015{row.Index[1]}', '_Y%m_d').date(), row.maxb / 10.0))

    r.. m..(result 'max' , key=l.... x: x.Value), m..(result 'min' , key=l.... x: x.Value)
