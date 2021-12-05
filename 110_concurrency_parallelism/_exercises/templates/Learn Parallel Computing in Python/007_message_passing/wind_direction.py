______ os
______ re
from _ ______ Pipe
from os.path ______ join

______ time
from _.context ______ P..

WIND_REGEX = "\d* METAR.*EGLL \d*Z [A-Z ]*(\d{5}KT|VRB\d{2}KT).*="
WIND_EX_REGEX = "(\d{5}KT|VRB\d{2}KT)"
VARIABLE_WIND_REGEX = ".*VRB\d{2}KT"
VALID_WIND_REGEX = "\d{5}KT"
WIND_DIR_ONLY_REGEX = "(\d{3})\d{2}KT"
TAF_REGEX = ".*TAF.*"
COMMENT_REGEX = "\w*#.*"
METAR_CLOSE_REGEX = ".*="


___ parse_to_array(text_conn, metars_conn):
    text = text_conn.recv()
    while text is not None:
        lines = text.splitlines()
        metar_str = ""
        metars = []
        ___ line __ lines:
            if re.search(TAF_REGEX, line):
                break
            if not re.search(COMMENT_REGEX, line):
                metar_str += line.strip()
            if re.search(METAR_CLOSE_REGEX, line):
                metars.append(metar_str)
                metar_str = ""
        metars_conn.send(metars)
        text = text_conn.recv()
    metars_conn.send(None)


___ extract_wind_direction(metars_conn, winds_conn):
    metars = metars_conn.recv()
    while metars is not None:
        winds = []
        ___ metar __ metars:
            if re.search(WIND_REGEX, metar):
                ___ token __ metar.split
                    if re.match(WIND_EX_REGEX, token): winds.append(re.match(WIND_EX_REGEX, token).group(1))
        winds_conn.send(winds)
        metars = metars_conn.recv()
    winds_conn.send(None)


___ mine_wind_distribution(winds_conn, wind_dist_conn):
    wind_dist = [0] * 8
    winds = winds_conn.recv()
    while winds is not None:
        ___ wind __ winds:
            if re.search(VARIABLE_WIND_REGEX, wind):
                ___ i __ r...(8):
                    wind_dist[i] += 1
            elif re.search(VALID_WIND_REGEX, wind):
                d = int(re.match(WIND_DIR_ONLY_REGEX, wind).group(1))
                dir_index = round(d / 45.0) % 8
                wind_dist[dir_index] += 1
        winds = winds_conn.recv()
    wind_dist_conn.send(wind_dist)


__ _____ __ _____
    text_conn_a, text_conn_b = Pipe()
    metars_conn_a, metars_conn_b = Pipe()
    winds_conn_a, winds_conn_b = Pipe()
    winds_dist_conn_a, winds_dist_conn_b = Pipe()
    P..(t.._parse_to_array, a.._(text_conn_b, metars_conn_a)).start()
    P..(t.._extract_wind_direction, a.._(metars_conn_b, winds_conn_a)).start()
    P..(t.._mine_wind_distribution, a.._(winds_conn_b, winds_dist_conn_a)).start()
    path_with_files = "../metarfiles"
    start = time.time()
    ___ file __ os.listdir(path_with_files):
        f = open(join(path_with_files, file), "r")
        text = f.read()
        text_conn_a.send(text)
    text_conn_a.send(None)
    wind_dist = winds_dist_conn_b.recv()
    end = time.time()
    print(wind_dist)
    print("Time taken", end - start)