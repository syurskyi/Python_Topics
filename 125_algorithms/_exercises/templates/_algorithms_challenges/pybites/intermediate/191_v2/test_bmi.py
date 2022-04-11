____ bmi _______ person_max_bmi, data


___ test_person_max_bmi
    ... person_max_bmi() __ ('Yoda', 39.03)


___ test_person_max_bmi_smaller_dataset
    newdata '\n'.j..(data.s.. [:10])
    ... person_max_bmi(newdata) __ ('Owen Lars', 37.87)


___ test_person_max_bmi_another_smaller_dataset
    newdata '\n'.j..([row ___ row __ data.s..
                         __ row.l..[:4] n.. __ ('Owen', 'Yoda')])
    ... person_max_bmi(newdata) __ ('IG-88', 35.0)
