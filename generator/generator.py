import random
from data.data import Person, Color, Date
from faker import Faker

faker_us = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_us.first_name() + " " + faker_us.last_name() + "",
        first_name=faker_us.first_name(),
        last_name=faker_us.last_name(),
        age=random.randint(18,70),
        department=faker_us.job(),
        salary=random.randint(1800,7000),
        email=faker_us.email(),
        current_address=faker_us.address(),
        permanent_address=faker_us.address(),
        mobile=faker_us.msisdn(),


    )

def generated_file():
    path = f'/Users/igorkorobchenko/Documents/Automation projects/{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path

def generated_color():
    yield Color(
        color_name = ['Red', 'Blue', 'Green', 'Yellow','Purple', 'Black', 'White', 'Violet', 'Indigo', 'Magenta', 'Aqua']
    )

def generated_date():
    yield Date(
        year = faker_us.year(),
        month = faker_us.month_name(),
        day = faker_us.day_of_month(),
        time = "12:00"
    )
