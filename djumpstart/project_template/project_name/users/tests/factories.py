from typing import Any, Sequence

from django.contrib.auth import get_user_model
import factory
from factory.faker import Faker


class UserProfileFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(
        '{{ project_name }}.authentication.tests.factories.UserFactory',
        profile=None
    )
    wallet_owner = factory.SubFactory(WalletOwnerFactory)

    class Meta:
        model = UserProfile
        django_get_or_create = ('user',)


class UserFactory(factory.DjangoModelFactory):
    first_name = 'John'
    last_name = 'Doe'
    email = Faker('email')
    profile = factory.RelatedFactory(UserProfileFactory, 'user')

    @factory.post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):

        password = Faker(
            'password',
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(
            extra_kwargs={}
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ('email',)
