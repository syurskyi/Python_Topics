____ merge _______ get_person_age, NOT_FOUND


___ test_regular_name():
    ... get_person_age('tim') __ 30
    ... get_person_age('helen') __ 26
    ... get_person_age('otto') __ 44


___ test_case_insensitive_lookup():
    ... get_person_age('Tim') __ 30
    ... get_person_age('BOB') __ 17
    ... get_person_age('BrEnDa') __ 17


___ test_name_not_found():
    ... get_person_age('timothy') __ NOT_FOUND
    ... get_person_age(N..) __ NOT_FOUND
    ... get_person_age(F..) __ NOT_FOUND
    ... get_person_age(-1) __ NOT_FOUND


___ test_duplicate_name():
    ... get_person_age('thomas') __ 46
    ... get_person_age('ana') __ 26