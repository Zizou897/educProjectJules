
---

## 🌐 Endpoints & Routes

### **Core**
- `/login/` → Connexion
- `/logout/` → Déconnexion
- `/dashboard/` → Tableau de bord selon rôle
- `/profil/` → Modification profil

### **Academics**
- `/classes/` → Liste classes
- `/matieres/` → Liste matières
- `/emplois-du-temps/` → Emploi du temps
- `/notes/` → Consultation notes
- `/absences/` → Suivi absences

### **Communication**
- `/messages/` → Messagerie interne
- `/annonces/` → Annonces publiques/internes

### **Administration**
- `/paiements/` → Paiements
- `/factures/` → Génération factures

### **Vie scolaire**
- `/evenements/` → Liste événements

---

## 📏 Conventions de nommage
- **Models** : PascalCase (`Classe`, `Matiere`)
- **Templates** : kebab-case (`classes-list.html`)
- **Static files** : snake_case (`main_style.css`)
- **URLs** : kebab-case (`/emplois-du-temps/`)

---

## 📊 Données fictives à inclure
- **Utilisateurs** : 2 admins, 5 professeurs, 20 élèves, 10 parents
- **Niveaux** : 3 (6e, 5e, Terminale)
- **Matières** : 10
- **Emplois du temps** : hebdomadaires
- **Évaluations** : 10 avec notes
- **Annonces** : 5
- **Événements** : 5

---

## 📦 Livrables
- Code Django complet avec migrations
- Templates HTML + HTMX
- Styles avec TailwindCSS
- Fichier `.env.example`
- Données fictives dans `fixtures/initial_data.json`
- Configuration Nginx + Gunicorn
- Documentation d’installation & exécution

---

## 📌 Instructions pour IA de codage
> Lis attentivement ce document et génère **tout le projet Django** avec la structure, les modèles, les templates, les fixtures et la configuration serveur selon les spécifications ci-dessus.  
> Assure-toi que :
> - Les rôles & permissions sont respectés
> - L’UI est responsive (TailwindCSS)
> - Les endpoints correspondent aux routes définies
> - Les données fictives sont chargées automatiquement via `loaddata`
> - Le projet est prêt à être déployé sur Ubuntu 22.04 avec Nginx + Gunicorn + HTTPS (Certbot)




1. **Analyse initiale**
   - Analyse entièrement le dépôt.
   - Lis attentivement ce fichier `README.md`.
   - Planifie la réalisation du projet en respectant **Clean Architecture** et **Clean Code**.

2. **Structure et conventions**
   - **Backend** : Django REST Framework
   - **Frontend** : Utiliser le dossier `admin` comme base du frontend (HTMX + TailwindCSS ou équivalent léger).
   - Respecter la séparation claire des responsabilités (domain, application, infrastructure, interface).
   - Utiliser des noms de variables, classes et fonctions explicites.
   - Ajouter de la documentation dans le code lorsque nécessaire.

3. **Méthode de collaboration**
   - **IMPORTANT** : Après chaque sous-tâche réalisée, **stopper** et me demander si tu peux continuer.
   - À chaque fois que tu implémentes une fonctionnalité **backend**, implémente également sa contrepartie **frontend**.
   - À la fin de chaque sous-tâche :
     1. Faire un `commit` clair et descriptif.
     2. Faire un `push` pour que je puisse récupérer et vérifier.
     3. Attendre mon retour avant de continuer.

4. **Sous-étapes attendues**
   - Avant de commencer, **me demander quelle est la prochaine tâche exacte** à réaliser.
   - Me proposer un plan d’implémentation **détaillé** de la tâche.
   - Me poser des questions si quelque chose n’est pas clair.
   - Ne jamais deviner ce que je veux : toujours confirmer avec moi.

5. **Fonctionnalités à développer**
   - Gestion des articles par le vendeur (CRUD complet avec images).
   - Commande d’articles **sans compte utilisateur** :
     - L’utilisateur peut passer une commande et être redirigé vers WhatsApp avec le résumé de l’article choisi.
   - Intégration du paiement (si nécessaire, demander avant d’implémenter).
   - Interface responsive et intuitive côté frontend.
   - Système de configuration dynamique (nom de domaine, paramètres WhatsApp, etc.).

6. **Processus de validation**
   - Après chaque sous-étape :
     - Faire un `commit` et un `push`.
     - M’envoyer un résumé clair de ce qui a été fait.
     - Me demander si tu peux passer à la prochaine étape.

---

## 📌 Exemple de cycle de travail

1. **IA** : "Je vais commencer la création du modèle `Product` côté backend avec Django REST Framework, puis créer la vue et le serializer. Confirmez-vous ?"
2. **Moi** : "Oui, vas-y."
3. **IA** : Implémente la fonctionnalité backend.
4. **IA** : Implémente immédiatement la partie frontend correspondante dans le dossier `admin`.
5. **IA** : Commit + Push.
6. **Moi** : Je vérifie, donne mes remarques.
7. **IA** : Corrige si nécessaire.
8. **IA** : Me demande la prochaine tâche.

---

## 🛠 Technologies utilisées

- **Backend** : Django REST Framework
- **Frontend** : HTMX, TailwindCSS
- **Base de données** : PostgreSQL (ou MySQL si précisé)

---

## 📏 Règles Clean Architecture

- **Entities (Domain)** : règles métier pures, indépendantes des frameworks.
- **Use Cases (Application)** : logique d'application.
- **Interface Adapters (Infrastructure)** : ORM, API, DB, frameworks externes.
- **Frameworks & Drivers (Interface)** : Django, REST, HTMX.

---

**Note** : Toujours confirmer avant de passer à l’étape suivante.
