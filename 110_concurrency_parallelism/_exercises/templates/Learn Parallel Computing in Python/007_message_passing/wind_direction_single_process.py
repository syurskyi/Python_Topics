______ __
______ __
____ __.p.. ______ j..

______ t___

WIND_REGEX = "\d* METAR.*EGLL \d*Z [A-Z ]*(\d{5}KT|VRB\d{2}KT).*="
WIND_EX_REGEX = "(\d{5}KT|VRB\d{2}KT)"
VARIABLE_WIND_REGEX = ".*VRB\d{2}KT"
VALID_WIND_REGEX = "\d{5}KT"
WIND_DIR_ONLY_REGEX = "(\d{3})\d{2}KT"
TAF_REGEX = ".*TAF.*"
COMMENT_REGEX = "\w*#.*"
METAR_CLOSE_REGEX = ".*="


___ parse_to_array(text):
    lines = text.s...
    metar_str = ""
    metars = []
    ___ line __ lines:
        __ __.search(TAF_REGEX, line):
            _____
        __ not __.search(COMMENT_REGEX, line):
            metar_str += line.strip()
        __ __.search(METAR_CLOSE_REGEX, line):
            metars.a..(metar_str)
            metar_str = ""
    return metars


___ extract_wind_direction(metars):
    winds = []
    ___ metar __ metars:
        __ __.search(WIND_REGEX, metar):
            ___ token __ metar.split
                __ __.match(WIND_EX_REGEX, token): winds.a..(__.match(WIND_EX_REGEX, token).g..(1))
    return winds


___ mine_wind_distribution(winds, wind_dist):
    ___ wind __ winds:
        __ __.search(VARIABLE_WIND_REGEX, wind):
            ___ i __ r...(8):
                wind_dist[i] += 1
        elif __.search(VALID_WIND_REGEX, wind):
            d = i..(__.match(WIND_DIR_ONLY_REGEX, wind).g..(1))
            dir_index = round(d / 45.0) % 8
            wind_dist[dir_index] += 1
    return wind_dist


__ _____ __ _____
    path_with_files = "../metarfiles"
    wind_dist = [0] * 8
    start = t___.t___()
    ___ file __ __.listdir(path_with_files):
        f = o..(j..(path_with_files, file), "r")
        text = f.r..
        metars = parse_to_array(text)
        winds = extract_wind_direction(metars)
        wind_dist = mine_wind_distribution(winds, wind_dist)
    end = t___.t___()
    print(wind_dist)
    print("Time taken", end - start)