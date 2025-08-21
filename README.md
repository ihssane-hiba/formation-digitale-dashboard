# 📊 Dashboard d'Analyse des Tendances de Formation Digitale

## 🎯 Description

Ce projet présente une analyse complète des tendances du marché de la formation digitale en France, combinant **collecte de données**, **analyse exploratoire**, **modélisation prédictive** et **visualisation interactive**.

## 🚀 Fonctionnalités

### 📈 **Dashboard Interactif**
- **Vue d'ensemble** du marché de la formation digitale
- **Analytics avancées** avec filtres dynamiques
- **Analyse des formations** par catégorie et certification
- **Prédictions IA** avec simulateur de demande
- **Comparaisons** offre vs demande
- **Exploration des données** brutes

### 🤖 **Modélisation Prédictive**
- **6 modèles de Machine Learning** testés
- **XGBoost** : Meilleur modèle (R² = 0.73, RMSE = 152.99)
- **Simulateur de prédiction** en temps réel
- **Évaluation comparative** des performances

### 📊 **Visualisations Avancées**
- Graphiques interactifs avec **Matplotlib** et **Seaborn**
- **Heatmaps** de corrélation
- **Analyses temporelles** Google Trends
- **Comparaisons multi-dimensionnelles**

## 🛠️ Technologies Utilisées

- **Python 3.8+**
- **Streamlit** - Interface web interactive
- **Pandas** - Manipulation de données
- **NumPy** - Calculs numériques
- **Matplotlib/Seaborn** - Visualisations
- **Scikit-learn** - Machine Learning
- **XGBoost** - Modèles avancés
- **NLTK** - Traitement du texte

## 📁 Structure du Projet

```
stage_4_eme_annee/
├── stage.py                 # Script principal d'analyse
├── dashboard.py             # Dashboard Streamlit
├── requirements.txt         # Dépendances Python
├── README.md               # Documentation
├── .gitignore              # Fichiers à ignorer
├── run_dashboard.bat       # Lancement Windows
├── run_dashboard.sh        # Lancement Linux/Mac
├── create_presentation.py  # Génération PowerPoint
└── data/                   # Données (optionnel)
    ├── df_final_clean_no_empty.csv
    ├── tendances_google_france.csv
    └── ...
```

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/ihssane-hiba/formation-digitale-dashboard.git
cd formation-digitale-dashboard
```

2. **Créer un environnement virtuel** (recommandé)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

## 🎮 Utilisation

### Lancement du Dashboard

**Option 1 : Commande directe**
```bash
streamlit run dashboard.py
```

**Option 2 : Scripts de lancement**
```bash
# Windows
run_dashboard.bat

# Linux/Mac
chmod +x run_dashboard.sh
./run_dashboard.sh
```

### Accès au Dashboard
- **URL locale** : http://localhost:8501
- **URL réseau** : http://votre-ip:8501

### Navigation
1. **🏠 Vue d'ensemble** - Métriques principales et graphiques
2. **📈 Tendances du marché** - Analyses filtrées
3. **🎓 Analyse des formations** - Détails par formation
4. **🔮 Prédictions** - Modèles IA et simulateur
5. **📊 Comparaisons** - Analyses croisées
6. **📋 Données brutes** - Exploration des datasets

## 📊 Principales Découvertes

### 🎯 **Insights Clés**
- **Data Engineer** : Formation la plus demandée (1,109 offres)
- **XGBoost** : Meilleur modèle prédictif (R² = 0.73)
- **Certifications** : 95%+ des formations sont certifiantes
- **Durée moyenne** : ~1,800 heures par formation

### 📈 **Tendances Identifiées**
- Forte demande en **Data Science** et **Développement**
- **Certifications** : Facteur clé de succès
- **Formations longues** : Meilleur taux de placement
- **Évolution temporelle** : Croissance des thématiques IA/ML

## 🤖 Modèles de Machine Learning

| Modèle | RMSE | R² Score | Temps |
|--------|------|----------|-------|
| **XGBoost** | 152.99 | 0.73 | 12.4s |
| Linear Regression | 161.80 | 0.69 | 2.3s |
| Gradient Boosting | 167.35 | 0.67 | 8.7s |
| Ridge Regression | 186.98 | 0.59 | 1.8s |
| Lasso Regression | 194.05 | 0.56 | 2.1s |
| Random Forest | 198.20 | 0.54 | 15.2s |

## 📋 Données Utilisées

### Sources de Données
- **OpenClassrooms** : Catalogue des formations
- **Google Trends** : Tendances de recherche
- **Remotive** : Offres d'emploi remote
- **Adzuna** : Offres d'emploi générales
- **Stack Overflow** : Tendances développeurs

### Variables Analysées
- **Demande** : Nombre d'offres d'emploi
- **Durée** : Heures de formation
- **Certification** : Type de certification
- **Catégorie** : Domaine de formation
- **Ratio** : Demande/étudiants

## 🔧 Configuration

### Variables d'Environnement
```bash
# Optionnel : Configuration avancée
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### Personnalisation
- Modifier `dashboard.py` pour adapter l'interface
- Ajuster les filtres dans les sections
- Personnaliser les couleurs et styles

## 📈 Métriques de Performance

- **Temps de chargement** : < 3 secondes
- **Précision prédictive** : 73% (R²)
- **Couvrage** : 80+ formations analysées
- **Mise à jour** : Données en temps réel

## 🤝 Contribution

Les contributions sont les bienvenues ! 

1. **Fork** le projet
2. **Créer** une branche feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** les changements (`git commit -m 'Add AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrir** une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Ihssane El Moumen** - Étudiant en Data Science
- **Email** : lmoumneihssan@gmail.com
- **LinkedIn** : [Votre Profil LinkedIn](#)
- **GitHub** : [@ihssane-hiba](https://github.com/ihssane-hiba)

## 🙏 Remerciements

- **OpenClassrooms** pour les données de formations
- **Google Trends** pour les données de tendances
- **Streamlit** pour l'interface interactive
- **Scikit-learn** pour les outils de ML

## 📞 Support

Pour toute question ou problème :
- **Issues GitHub** : [Créer une issue](https://github.com/ihssane-hiba/formation-digitale-dashboard/issues)
- **Email** : lmoumneihssan@gmail.com

---

⭐ **N'oubliez pas de donner une étoile au projet si vous l'aimez !**
