from data.data import Person
from faker import Faker

faker_us = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_us.first_name() + " " + faker_us.last_name() + "",
        email=faker_us.email(),
        current_address=faker_us.address(),
        permanent_address=faker_us.address()
    )
