# https://pkgstore.datahub.io/core/gold-prices/annual_csv/data/343f626dd4f7bae813cfaac23fccd1bc/annual_csv.csv
gold_prices = """
1950-12,34.720 1951-12,34.660 1952-12,34.790 1953-12,34.850 1954-12,35.040
1955-12,34.970 1956-12,34.900 1957-12,34.990 1958-12,35.090 1959-12,35.050
1960-12,35.540 1961-12,35.150 1962-12,35.080 1963-12,35.080 1964-12,35.120
1965-12,35.130 1966-12,35.180 1967-12,35.190 1968-12,41.113 1969-12,35.189
1970-12,37.434 1971-12,43.455 1972-12,63.779 1973-12,106.236 1974-12,183.683
1975-12,139.279 1976-12,133.674 1977-12,160.480 1978-12,207.895 1979-12,463.666
1980-12,596.712 1981-12,410.119 1982-12,444.776 1983-12,388.060 1984-12,319.622
1985-12,321.985 1986-12,391.595 1987-12,487.079 1988-12,419.248 1989-12,409.655
1990-12,378.161 1991-12,361.875 1992-12,334.657 1993-12,383.243 1994-12,379.480
1995-12,387.445 1996-12,369.338 1997-12,288.776 1998-12,291.357 1999-12,283.743
2000-12,271.892 2001-12,275.992 2002-12,333.300 2003-12,407.674 2004-12,442.974
2005-12,509.423 2006-12,629.513 2007-12,803.618 2008-12,819.940 2009-12,1135.012
2010-12,1393.512 2011-12,1652.725 2012-12,1687.342 2013-12,1221.588 2014-12,1200.440
2015-12,1068.317 2016-12,1152.165 2017-12,1265.674 2018-12,1249.887
"""  # noqa E501


___ years_gold_value_decreased(gold_prices: str = gold_prices):
   """Analyze gold_prices returning a tuple of the year the gold price
      decreased the most and the year the gold price increased the most.
   """
   price_delta = {}
   prices_lines = gold_prices.strip().split("\n")
   ___ price_line __ prices_lines:
      ___ line __ price_line.split(" "):
         year = int(line[:line.find("-")])
         price = float(line[line.find(",") +1:])
         price_delta[year] = price

   min_year, max_year = m..(price_delta), max(price_delta)
   decrease_largest, decrease_year, increase_largest, increase_year = 0, 0, 0, 0
   ___ year __ r..(min_year +1, max_year + 1, 1):
      previous_year_price = price_delta[year -1]
      current_year_price = price_delta[year]
   
      delta = abs(current_year_price - previous_year_price)
      __ current_year_price < previous_year_price:
         # Decrease
         __ delta > decrease_largest:
            decrease_largest = delta
            decrease_year = year
      ____:
         # Increase
         __ delta > increase_largest:
            increase_largest = delta
            increase_year = year

   r.. (decrease_year, increase_year)


# if __name__ == "__main__":
#    print(years_gold_value_decreased())