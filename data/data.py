from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    department: str = None
    email: str = None
    age: int = None
    salary: int = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None

@dataclass
class Color:
    color_name: list = None

@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None

