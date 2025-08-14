from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Annonce(models.Model):
    """
    Represents a public or internal announcement.
    """
    class Audience(models.TextChoices):
        PUBLIC = "PUBLIC", _("Publique")
        INTERNE = "INTERNE", _("Interne")

    titre = models.CharField(_("titre"), max_length=200)
    contenu = models.TextField(_("contenu"))
    auteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="annonces",
        limit_choices_to={"role__in": ["ADMIN", "PROFESSOR"]},
    )
    audience = models.CharField(
        _("audience"), max_length=10, choices=Audience.choices, default=Audience.INTERNE
    )
    date_creation = models.DateTimeField(_("date de création"), default=timezone.now)

    class Meta:
        verbose_name = _("Annonce")
        verbose_name_plural = _("Annonces")
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre


class Message(models.Model):
    """
    Represents a message in the internal messaging system.
    """
    expediteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="messages_envoyes",
    )
    destinataire = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="messages_recus",
    )
    sujet = models.CharField(_("sujet"), max_length=150)
    corps = models.TextField(_("corps"))
    date_envoi = models.DateTimeField(_("date d'envoi"), default=timezone.now)
    lu_le = models.DateTimeField(_("lu le"), null=True, blank=True)

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
        ordering = ['-date_envoi']

    def __str__(self):
        return f"From {self.expediteur} to {self.destinataire}: {self.sujet}"

    def is_read(self):
        return self.lu_le is not None

    def mark_as_read(self):
        if not self.is_read():
            self.lu_le = timezone.now()
            self.save()
