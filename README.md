
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
