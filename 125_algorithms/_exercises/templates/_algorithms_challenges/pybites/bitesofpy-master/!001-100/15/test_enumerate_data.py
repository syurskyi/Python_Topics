______ pytest

from enumerate_data ______ enumerate_names_countries

expected_lines = ['1. Julian     Australia',
                  '2. Bob        Spain',
                  '3. PyBites    Global',
                  '4. Dante      Argentina',
                  '5. Martin     USA',
                  '6. Rodolfo    Mexico']


@pytest.mark.parametrize("line", expected_lines)
___ test_enumerate_names_countries(capfd, line
    enumerate_names_countries()
    output = capfd.readouterr()[0]
    assert line in output, f'{line} not in output'