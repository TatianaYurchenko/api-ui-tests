from faker import Faker

fake = Faker() # создаем объект класса Farer
print(fake.name())
print(fake.email())


def generate_random_int(n):
    return [i for i in range(1, n)]


def generate_random_name(n):
    return [fake.name() for i in range(1, n)]


emploe = dict(zip(generate_random_int(6), generate_random_name(6)))
print(emploe)