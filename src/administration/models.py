from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Facture(models.Model):
    """
    Represents an invoice for a student.
    """
    class Statut(models.TextChoices):
        BROUILLON = "BROUILLON", _("Brouillon")
        ENVOYEE = "ENVOYEE", _("Envoyée")
        PAYEE = "PAYEE", _("Payée")
        ANNULEE = "ANNULEE", _("Annulée")

    eleve = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="factures",
        limit_choices_to={"role": "STUDENT"},
    )
    montant_total = models.DecimalField(_("montant total"), max_digits=10, decimal_places=2)
    date_emission = models.DateField(_("date d'émission"), default=timezone.now)
    date_echeance = models.DateField(_("date d'échéance"))
    statut = models.CharField(
        _("statut"), max_length=10, choices=Statut.choices, default=Statut.BROUILLON
    )

    class Meta:
        verbose_name = _("Facture")
        verbose_name_plural = _("Factures")
        ordering = ['-date_emission']

    def __str__(self):
        return f"Facture {self.id} for {self.eleve} - {self.montant_total}€"

    @property
    def montant_paye(self):
        return self.paiements.aggregate(total=models.Sum('montant'))['total'] or 0

    @property
    def solde_restant(self):
        return self.montant_total - self.montant_paye

    def update_statut(self):
        if self.solde_restant <= 0:
            self.statut = self.Statut.PAYEE
        else:
            # If a payment was made but it's not fully paid, it's still 'Envoyée'
            # We don't revert to Brouillon or Envoyee from Payee automatically
            if self.statut != self.Statut.PAYEE:
                 self.statut = self.Statut.ENVOYEE
        self.save()


class Paiement(models.Model):
    """
    Represents a payment made for an invoice.
    """
    class Methode(models.TextChoices):
        CARTE = "CARTE", _("Carte de crédit")
        VIREMENT = "VIREMENT", _("Virement bancaire")
        ESPECES = "ESPECES", _("Espèces")

    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name="paiements")
    montant = models.DecimalField(_("montant"), max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(_("date de paiement"), default=timezone.now)
    methode = models.CharField(_("méthode"), max_length=10, choices=Methode.choices)

    class Meta:
        verbose_name = _("Paiement")
        verbose_name_plural = _("Paiements")
        ordering = ['-date_paiement']

    def __str__(self):
        return f"Paiement of {self.montant}€ for Facture {self.facture.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.facture.update_statut()

    def delete(self, *args, **kwargs):
        facture = self.facture
        super().delete(*args, **kwargs)
        facture.update_statut()
