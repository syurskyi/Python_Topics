from bmi ______ person_max_bmi, data


___ test_person_max_bmi(
    assert person_max_bmi() __ ('Yoda', 39.03)


___ test_person_max_bmi_smaller_dataset(
    newdata = '\n'.join(data.splitlines()[:10])
    assert person_max_bmi(newdata) __ ('Owen Lars', 37.87)


___ test_person_max_bmi_another_smaller_dataset(
    newdata = '\n'.join([row for row in data.splitlines()
                         __ row.lstrip()[:4] not in ('Owen', 'Yoda')])
    assert person_max_bmi(newdata) __ ('IG-88', 35.0)