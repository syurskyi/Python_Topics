Example of API tests using python's unittest and nose

To run tests:
- if test contains:

```
if __name__ == '__main__':
    unittest.main()
```

it can be run via `python` + filename

- else:
use `nosetests` + filename to run one particular test, or `nosetests` to run all tests

Dependencies:
- unittest
- nose
- requests
- xmltodict
- pyyaml
