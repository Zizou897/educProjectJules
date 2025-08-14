from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User model to include roles and relationships.
    """

    class Role(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        PROFESSOR = "PROFESSOR", _("Professor")
        STUDENT = "STUDENT", _("Student")
        PARENT = "PARENT", _("Parent")

    role = models.CharField(
        _("role"), max_length=10, choices=Role.choices, default=Role.STUDENT
    )

    # This field will link parents to their children (students).
    # A parent can have multiple children, and a child can have multiple parents.
    children = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="parents",
        blank=True,
        limit_choices_to={"role": Role.STUDENT},
    )

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"
