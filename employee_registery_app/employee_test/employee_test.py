from nose.tools import *
from employee.employee import Employee


def declaring_instance_test():
    emp_1 = Employee('test', 'name', 1000)
    emp_2 = Employee('tes', 'nam', 100)
    assert_equal(emp_1.fullname(), 'test name')
    assert_equal(emp_2.fullname(), 'tes nam')


def employee_count_test():
    assert_equal(Employee.employee_count, 2)


def applying_raise_test():
    emp_1 = Employee('test', 'name', 1000)
    emp_2 = Employee('tes', 'nam', 100)
    emp_1.apply_raise()
    emp_2.apply_raise()
    assert_equal(emp_1.pay, 1000*1.04)
    assert_equal(emp_2.pay, 100*1.04)
