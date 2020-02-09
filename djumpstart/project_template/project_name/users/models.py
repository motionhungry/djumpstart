import uuid

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model
    """
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField((_('email address')), unique=True)

    # Remove username column from the database table
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('email',)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users_user'


class UserProfile(models.Model):
    """
    User Profile model
    """
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'users_userprofile'
