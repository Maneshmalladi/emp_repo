import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','fbvproject.settings')

import django
django.setup()

from testapp.models import Employee

from random import *

from faker import Faker

faker=Faker()

def phonenum():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(10000,20000)
        fephn=phonenum()
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(
            eno=feno,
            ename=fename,
            esal=fesal,
            ephn=fephn,
            eaddr=feaddr
        )

n = int(input('Enter number of employees:'))
populate(n)
print(f'{n} Records inserted successfully..........')

