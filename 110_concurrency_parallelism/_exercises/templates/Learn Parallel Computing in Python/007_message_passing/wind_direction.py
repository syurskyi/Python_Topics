______ __
______ __
____ _ ______ Pipe
____ __.p.. ______ j..

______ t___
____ _.context ______ P..

WIND_REGEX = "\d* METAR.*EGLL \d*Z [A-Z ]*(\d{5}KT|VRB\d{2}KT).*="
WIND_EX_REGEX = "(\d{5}KT|VRB\d{2}KT)"
VARIABLE_WIND_REGEX = ".*VRB\d{2}KT"
VALID_WIND_REGEX = "\d{5}KT"
WIND_DIR_ONLY_REGEX = "(\d{3})\d{2}KT"
TAF_REGEX = ".*TAF.*"
COMMENT_REGEX = "\w*#.*"
METAR_CLOSE_REGEX = ".*="


___ parse_to_array(text_conn, metars_conn):
    text = text_conn.r..
    w... text is not None:
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
        metars_conn.s..(metars)
        text = text_conn.r..
    metars_conn.s..(None)


___ extract_wind_direction(metars_conn, winds_conn):
    metars = metars_conn.r..
    w... metars is not None:
        winds = []
        ___ metar __ metars:
            __ __.search(WIND_REGEX, metar):
                ___ token __ metar.split
                    __ __.match(WIND_EX_REGEX, token): winds.a..(__.match(WIND_EX_REGEX, token).g..(1))
        winds_conn.s..(winds)
        metars = metars_conn.r..
    winds_conn.s..(None)


___ mine_wind_distribution(winds_conn, wind_dist_conn):
    wind_dist = [0] * 8
    winds = winds_conn.r..
    w... winds is not None:
        ___ wind __ winds:
            __ __.search(VARIABLE_WIND_REGEX, wind):
                ___ i __ r...(8):
                    wind_dist[i] += 1
            elif __.search(VALID_WIND_REGEX, wind):
                d = i..(__.match(WIND_DIR_ONLY_REGEX, wind).g..(1))
                dir_index = round(d / 45.0) % 8
                wind_dist[dir_index] += 1
        winds = winds_conn.r..
    wind_dist_conn.s..(wind_dist)


__ _____ __ _____
    text_conn_a, text_conn_b = Pipe()
    metars_conn_a, metars_conn_b = Pipe()
    winds_conn_a, winds_conn_b = Pipe()
    winds_dist_conn_a, winds_dist_conn_b = Pipe()
    P..(t.._parse_to_array, a.._(text_conn_b, metars_conn_a)).s..
    P..(t.._extract_wind_direction, a.._(metars_conn_b, winds_conn_a)).s..
    P..(t.._mine_wind_distribution, a.._(winds_conn_b, winds_dist_conn_a)).s..
    path_with_files = "../metarfiles"
    start = t___.t___()
    ___ file __ __.listdir(path_with_files):
        f = o..(j..(path_with_files, file), "r")
        text = f.r..
        text_conn_a.s..(text)
    text_conn_a.s..(None)
    wind_dist = winds_dist_conn_b.r..
    end = t___.t___()
    print(wind_dist)
    print("Time taken", ? -  ?