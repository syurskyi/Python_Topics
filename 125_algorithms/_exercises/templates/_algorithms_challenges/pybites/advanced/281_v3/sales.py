_______ json
_______ os
____ io _______ StringIO
____ base64 _______ b64decode
____ pathlib _______ Path
____ typing _______ Dict, List, Union

_______ pandas __ pd  # type: ignore
_______ requests

URL: s.. = "https://bites-data.s3.us-east-2.amazonaws.com/MonthlySales.csv"
STATS: List[s..] = ["sum", "mean", "max"]
TMP: Path = Path(os.getenv("TMP", "/tmp")) / "MonthlySales.csv"


___ get_data(url: s..) __ Dict[s.., s..]:
    """Get data from Github

    Args:
        url (str): The URL where the data is located.

    Returns:
        Dict[str, str]: The dictionary extracted from the data
    """
    __ TMP.exists
        data = json.loads(TMP.read_text())
    ____:
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.text)
        w__ TMP.o.. "w") __ tmp:
            json.dump(data, tmp)
    r.. data


___ process_data(url: s..) __ pd.DataFrame:
    """Process the data from the Github API

    Args:
        url (str): The URL where the data is located.

    Returns:
        pd.DataFrame: Pandas DataFrame generated from the processed data
    """
    data = b64decode(get_data(url) 'content' ).d.. )
    r.. pd.read_csv(StringIO(data), parse_dates= 'month' )



___ summary_report(df: pd.DataFrame, stats: Union[List[s..], N..] = STATS) __ N..
    """Summary report generated from the DataFrame and list of stats

    Will aggregate statistics for sum, mean, and max by default.

    Args:
        df (pd.DataFrame): Pandas DataFrame of the Github API data
        stats (List[str], optional): List of summaries to aggregate. Defaults to STATS.

    Returns:
        None (prints to standard output)

        Example:
                    sum          mean        max
        year
        2013  484247.51  40353.959167   81777.35
        2014  470532.51  39211.042500   75972.56
        2015  608473.83  50706.152500   97237.42
        2016  733947.03  61162.252500  118447.83
    """
    df = df.c..
    df 'year'  = df.month.dt.year
    s = df.groupby( 'year' ).agg({'sales': stats}).__str__().s..('\n')[1:]
    print('\n'.j..(s))



___ yearly_report(df: pd.DataFrame, year: i..) __ N..
    """Generate a sales report for the given year

    Args:
        df (pd.DataFrame): Pandas DataFrame of the Github API data
        year (int): The year to generate the report for

    Raises:
        ValueError: Error raised if the year requested is not in the data.
        Should be in the form of "The year YEAR is not included in the report!"

    Returns:
        None (prints to standard output)

        Example:
        2013
                  sales
        month
        1      14236.90
        2       4519.89
        3      55691.01
        4      28295.35
        5      23648.29
        6      34595.13
        7      33946.39
        8      27909.47
        9      81777.35
        10     31453.39
        11     78628.72
        12     69545.62
    """
    __ year n.. __ df.month.dt.year.unique
        r.. ValueError _*The year {year} is not included in the report!')
    df = df.c..
    df 'year'  = df.month.dt.year
    df 'month'  = df.month.dt.month
    df = df.groupby('year').get_group(year).set_index('month')
    print _*\n{year}')
    print(df.to_string(columns= 'sales' ))


#uncomment the following for viewing/testing the reports/code
__ _______ __ _______
    data = process_data(URL)
    summary_report(data)
    ___ year __ (data["month"].dt.year).unique
        yearly_report(data, year)

    yearly_report(data, 2020)
