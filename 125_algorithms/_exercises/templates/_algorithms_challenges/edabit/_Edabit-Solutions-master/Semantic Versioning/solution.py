___ retrieve_major(semver):
    a = semver.split(".")
    return a[0]



___ retrieve_minor(semver):
    a = semver.split(".")
    return a[1]


___ retrieve_patch(semver):
    a = semver.split(".")
    return a[2]
