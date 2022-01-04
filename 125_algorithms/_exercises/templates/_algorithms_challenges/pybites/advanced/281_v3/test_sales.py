_______ pandas __ pd
_______ pytest

____ sales _______ get_data, process_data, summary_report, yearly_report, URL


@pytest.fixture(scope="function")
___ df
    r.. process_data(URL)


___ test_data(df):
    ... isi..(df, pd.DataFrame)


@pytest.mark.parametrize(
    "line, expected",
    [
        (0, "sum          mean        max"),
        (1, "year"),
        (2, "2013  484247.51  40353.959167   81777.35"),
        (3, "2014  470532.51  39211.042500   75972.56"),
        (4, "2015  608473.83  50706.152500   97237.42"),
        (5, "2016  733947.03  61162.252500  118447.83"),
    ],
)
___ test_summary_report(df, capfd, line, expected):
    summary_report(df)
    output = capfd.readouterr()[0].s..("\n")
    ... output[line].s.. __ expected


@pytest.mark.parametrize(
    "lst, expected", [(["median"], "median"), (["min", "max"], "min        max"),]
)
___ test_summary_report_custom(df, capfd, lst, expected):
    summary_report(df, lst)
    output = capfd.readouterr()[0].s..("\n")
    ... output[0].s.. __ expected


@pytest.mark.parametrize(
    "year, expected",
    [
        (2013, "6      34595.13"),
        (2014, "6      24797.29"),
        (2015, "6      39430.44"),
        (2016, "6       52981.73"),
    ],
)
___ test_yearly_report(df, capfd, year, expected):
    yearly_report(df, year)
    output = capfd.readouterr()[0].s..("\n")
    ... output[9] __ expected


@pytest.mark.parametrize("year", [1972, 2000, 2020])
___ test_yearly_report_with_invalid_year(df, year):
    msg = f"<ExceptionInfo ValueError('The year {year} is not included in the report!') tblen=2>"
    with pytest.raises(ValueError) __ e:
        yearly_report(df, year)
    ... s..(e) __ msg