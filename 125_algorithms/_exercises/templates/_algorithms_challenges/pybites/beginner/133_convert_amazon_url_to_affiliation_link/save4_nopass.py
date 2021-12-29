___ generate_affiliation_link(url):
    beginning = "".join(url.split('/')[:3])
    beginning1 = beginning.replace(beginning, "http://www.amazon.com")
    mid = "".join(url.rsplit('/')[5])
    end_chop = url.rsplit('/', 1)[1]
    return f"{beginning1}/dp/{mid}/?tag=pyb0f-20".replace(end_chop, "")