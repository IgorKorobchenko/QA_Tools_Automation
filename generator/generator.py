import random
from data.data import Person
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

    )

def generated_file():
    path = f'/Users/igorkorobchenko/Documents/Automation projects/{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path