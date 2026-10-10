from faker import Faker

fake = Faker() # создаем объект класса Faker
print(fake.name())
print(fake.email())


def generate_random_int(n):
    return [i for i in range(1, n)]


def generate_random_name(n):
    return [fake.name() for i in range(1, n)]


def create_dct(a, b):
    return dict(zip(a, b))


print(create_dct(generate_random_int(6), generate_random_name(6)))
