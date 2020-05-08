"""the Profile class purpose is to store a name, an age, and a job for a specific person.
"""


class Profile:
    def __init__(self, name, age, job):
        self._name = name
        self._age = age
        self._job = job

    def print_name(self):
        print(self._name)

    def print_age(self):
        print(self._age)

    def print_job(self):
        print(self._job)

profile = Profile("Mohammad Mahjoub", 21, "student")
profile.print_name()
profile.print_age()
profile.print_job()