___ generate_affiliation_link(url
    beginning = "".j..(url.s..('/')[:3])
    beginning1 = beginning.r..(beginning, "http://www.amazon.com")
    mid = "".j..(url.rsplit('/')[5])
    end_chop = url.rsplit('/', 1)[1]
    r.. f"{beginning1}/dp/{mid}/?tag=pyb0f-20".r..(end_chop, "")