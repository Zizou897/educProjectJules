from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Niveau(models.Model):
    """
    Represents a school level (e.g., 6e, 5e, Terminale).
    """
    nom = models.CharField(_("nom"), max_length=50, unique=True)

    class Meta:
        verbose_name = _("Niveau")
        verbose_name_plural = _("Niveaux")

    def __str__(self):
        return self.nom


class Classe(models.Model):
    """
    Represents a class within a level (e.g., 6e A).
    """
    nom = models.CharField(_("nom"), max_length=50)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, related_name="classes")
    professeurs = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="classes_taught",
        limit_choices_to={"role": "PROFESSOR"},
        blank=True
    )
    eleves = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="classes_enrolled",
        limit_choices_to={"role": "STUDENT"},
        blank=True
    )

    class Meta:
        verbose_name = _("Classe")
        verbose_name_plural = _("Classes")
        unique_together = ('nom', 'niveau')

    def __str__(self):
        return f"{self.nom} ({self.niveau})"


class Matiere(models.Model):
    """
    Represents a subject (e.g., Mathématiques, Physique).
    """
    nom = models.CharField(_("nom"), max_length=100, unique=True)
    professeurs = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="matieres_taught",
        limit_choices_to={"role": "PROFESSOR"},
        blank=True
    )

    class Meta:
        verbose_name = _("Matière")
        verbose_name_plural = _("Matières")

    def __str__(self):
        return self.nom


class Evaluation(models.Model):
    """
    Represents a specific test or assignment.
    """
    titre = models.CharField(_("titre"), max_length=200)
    date = models.DateField(_("date"))
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="evaluations")
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name="evaluations")
    professeur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="evaluations_given",
        limit_choices_to={"role": "PROFESSOR"},
    )

    class Meta:
        verbose_name = _("Évaluation")
        verbose_name_plural = _("Évaluations")

    def __str__(self):
        return f"{self.titre} - {self.matiere} - {self.classe}"


class Note(models.Model):
    """
    Represents a student's grade for an evaluation.
    """
    eleve = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes",
        limit_choices_to={"role": "STUDENT"},
    )
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name="notes")
    note = models.DecimalField(_("note"), max_digits=5, decimal_places=2)
    commentaire = models.TextField(_("commentaire"), blank=True)

    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")
        unique_together = ('eleve', 'evaluation')

    def __str__(self):
        return f"{self.eleve}: {self.note} in {self.evaluation}"


class EmploiDuTemps(models.Model):
    """
    Represents a weekly timetable slot.
    """
    class Jour(models.TextChoices):
        LUNDI = "LUNDI", _("Lundi")
        MARDI = "MARDI", _("Mardi")
        MERCREDI = "MERCREDI", _("Mercredi")
        JEUDI = "JEUDI", _("Jeudi")
        VENDREDI = "VENDREDI", _("Vendredi")
        SAMEDI = "SAMEDI", _("Samedi")

    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name="emploi_du_temps")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    professeur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="cours_timetable",
        limit_choices_to={"role": "PROFESSOR"},
    )
    jour = models.CharField(_("jour"), max_length=10, choices=Jour.choices)
    heure_debut = models.TimeField(_("heure de début"))
    heure_fin = models.TimeField(_("heure de fin"))

    class Meta:
        verbose_name = _("Emploi du temps")
        verbose_name_plural = _("Emplois du temps")
        ordering = ['jour', 'heure_debut']

    def __str__(self):
        return f"{self.classe} - {self.matiere} ({self.jour} {self.heure_debut}-{self.heure_fin})"


class Absence(models.Model):
    """
    Represents a student's absence from a class.
    """
    eleve = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="absences",
        limit_choices_to={"role": "STUDENT"},
    )
    cours = models.ForeignKey(EmploiDuTemps, on_delete=models.CASCADE, related_name="absences")
    date = models.DateField(_("date"))
    justifiee = models.BooleanField(_("justifiée"), default=False)
    motif = models.TextField(_("motif"), blank=True)

    class Meta:
        verbose_name = _("Absence")
        verbose_name_plural = _("Absences")

    def __str__(self):
        return f"Absence for {self.eleve} on {self.date} for {self.cours}"
