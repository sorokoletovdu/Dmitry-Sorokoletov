## N26 Home Challenge
## Overview
This is the solution for N26 Home Challenge

This is python (pytest) project.

### Running tests

For test running you need to run swagger server according to the [instruction](https://github.com/swagger-api/swagger-petstore)

Install requirements from project folder:
```
pip install -r requirements.txt
```
Once you've got all the requirements in place, you should be able to simply run

```
pytest -rpP api/tests/test_user.py
```
