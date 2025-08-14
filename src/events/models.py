from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Evenement(models.Model):
    """
    Represents a school event.
    """
    titre = models.CharField(_("titre"), max_length=200)
    description = models.TextField(_("description"))
    auteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="evenements_crees",
        limit_choices_to={"role__in": ["ADMIN", "PROFESSOR"]},
    )
    date_debut = models.DateTimeField(_("date de début"), default=timezone.now)
    date_fin = models.DateTimeField(_("date de fin"))

    class Meta:
        verbose_name = _("Événement")
        verbose_name_plural = _("Événements")
        ordering = ['date_debut']

    def __str__(self):
        return self.titre
