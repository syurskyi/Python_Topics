"""the Profile class purpose is to store a name, an age, and a job for a specific person.
"""


class Profile:
    def __init__(self, name, aga, job):
        self._name = name
        self._aga = aga
        self._job = job

    def print_name(self):
        print(self._name)

    def print_age(self):
        print(self._aga)

    def print_job(self):
        print(self._job)