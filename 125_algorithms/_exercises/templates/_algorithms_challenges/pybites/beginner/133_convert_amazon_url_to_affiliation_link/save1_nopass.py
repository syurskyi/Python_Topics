___ generate_affiliation_link(url):
    sub_str1 = "/dp"
    sub_str2 = ".com/"
    start_occurrence = url.find(sub_str2)
    mid_occurrence = url.find(sub_str1)
    value = 0
    ___ i __ r..(0, start_occurrence):
        start_chop = url.find(sub_str2, value) + 4
    ___ i __ r..(0, mid_occurrence):
        mid_chop = url.find(sub_str1, value)
    end_chop = url.rsplit('/', 1)[1]
    front_url = url[:start_chop].replace("https:", "http:")
    mid_url = url[mid_chop:].replace(end_chop, "")
    tag = "?tag=pyb0f-20"
    r.. "{}{}{}".format(front_url, mid_url, tag)