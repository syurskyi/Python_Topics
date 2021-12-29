def generate_affiliation_link(url):
    tag = "?tag=pyb0f-20"
    sub_str1 = "/dp"
    sub_str2 = ".com/"
    start_occurrence = url.find(sub_str2)
    mid_occurrence = url.find(sub_str1)
    value = 0
    for i in range(0, start_occurrence):
        start_chop = url.find(sub_str2, value) + 4
    for i in range(0, mid_occurrence):
        mid_chop = url.find(sub_str1, value)
    end_chop = url.rsplit('/', 1)[1]
    return "{}{}{}".format(url[:start_chop], url[mid_chop:], tag).replace("https:", "http:").replace(end_chop, "")
