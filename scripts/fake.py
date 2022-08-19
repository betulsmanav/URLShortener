from django.contrib.auth.models import User
import secrets
import django
import os
import random
import secrets
from django.contrib.auth.models import User
from faker import Faker

from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings.base'
django.setup()



users = []


def set_user():
    fake = Faker(['en_US'])
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = f'{first_name.lower()}_{last_name.lower()}'
    email = f'{last_name}@{fake.domain_name()}'
    is_staff = fake.boolean(chance_of_getting_true=5)

    user_check = User.objects.filter(username=username)
    while user_check.exists():
        username = username + str(random.randrange(1, 99))
        user_check = User.objects.filter(username=username)

    user = User(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        is_staff=is_staff
    )
    user.set_password('testing321..')
    user.save()
    users.append(user)
    print(user)