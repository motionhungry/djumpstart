import pytest
from django.conf import settings
from django.test import TestCase, override_settings
from django.core.exceptions import ValidationError

from {{ project_name }}.users.models import User, UserProfile

from . import factories


pytestmark = pytest.mark.django_db


class UserModelTest(TestCase):

    def test_get_full_name(self):
        """
        It should return the user's name
        """
        user = factories.UserFactory(first_name='Doug', last_name='Funny')
        self.assertEqual(user.get_full_name(), 'Doug Funny')

    def test_get_short_name(self):
        """
        It should return an empty string
        """
        user = factories.UserFactory(first_name='Doug', last_name='Funny')
        self.assertEqual(user.get_short_name(), 'Doug')

    def test_email_is_unique(self):
        """
        It should raise a validation error if a email is taken
        """
        user1 = factories.UserFactory(email='foo@bar.com')
        user2 = factories.UserFactory()

        with self.assertRaises(ValidationError) as context:
            user2.email = 'foo@bar.com'
            user2.validate_unique()
        self.assertTrue('email' in context.exception.error_dict)

    def test_str(self):
        """
        It should return the email
        """
        email = 'foo@bar.com'
        user = factories.UserFactory(email=email)
        self.assertEqual(user.__str__(), 'foo@bar.com')
