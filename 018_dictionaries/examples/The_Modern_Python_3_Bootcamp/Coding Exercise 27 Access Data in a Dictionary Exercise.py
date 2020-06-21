# Concatenation Solution
#
# Solution using string concatenation:

artist = {
    "first": "Neil",
    "last": "Young",
}

# concat first and last name with a space
full_name = artist["first"] + " " + artist["last"]

# Format() Solution
#
# Solution using the format() method:

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = "{} {}".format(artist["first"], artist["last"])

# F-String Solution

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = f"{artist['first']} {artist['last']}"

