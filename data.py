import faker

def get_sign_up_date():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()
    return email, password, name


