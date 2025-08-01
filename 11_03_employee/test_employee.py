import pytest
from employee import Employee


@pytest.fixture
def employee():
    return Employee('John', 'Doe', 50000)

def test_give_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 60000
