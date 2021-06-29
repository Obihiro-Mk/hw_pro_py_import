print('Start main.py')
import datetime
from application import salary
from application.db import people

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print('Текущая дата:', datetime.datetime.today())

print('End main.py')
