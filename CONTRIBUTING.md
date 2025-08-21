# 🤝 Guide de Contribution

Merci de votre intérêt pour contribuer au projet **Dashboard d'Analyse des Tendances de Formation Digitale** ! 

## 🎯 Comment Contribuer

### 📋 Types de Contributions

Nous acceptons plusieurs types de contributions :

- 🐛 **Rapports de bugs**
- 💡 **Suggestions de nouvelles fonctionnalités**
- 📚 **Amélioration de la documentation**
- 🔧 **Corrections de code**
- 🎨 **Améliorations de l'interface utilisateur**
- ⚡ **Optimisations de performance**

## 🚀 Premiers Pas

### 1. Fork et Clone

```bash
# Fork le repository sur GitHub
# Puis clonez votre fork
git clone https://github.com/votre-username/formation-digitale-dashboard.git
cd formation-digitale-dashboard
```

### 2. Configuration de l'Environnement

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Créer une Branche

```bash
# Créer une nouvelle branche pour votre contribution
git checkout -b feature/votre-nouvelle-fonctionnalite
# ou
git checkout -b fix/votre-correction
```

## 📝 Standards de Code

### Style Python

Nous suivons les conventions PEP 8 :

```python
# ✅ Bon
def calculate_metrics(data):
    """Calcule les métriques principales."""
    return {
        'mean': data.mean(),
        'std': data.std()
    }

# ❌ Éviter
def calcMetrics(data):
    return {'mean':data.mean(),'std':data.std()}
```

### Documentation

- **Docstrings** : Utilisez le format Google ou NumPy
- **Commentaires** : Expliquez le "pourquoi", pas le "quoi"
- **README** : Mettez à jour si nécessaire

### Tests

```bash
# Lancer les tests (si disponibles)
python -m pytest tests/

# Vérifier la couverture
python -m pytest --cov=.
```

## 🔄 Workflow de Contribution

### 1. Développement

```bash
# Faire vos modifications
# Tester localement
streamlit run dashboard.py

# Vérifier que tout fonctionne
```

### 2. Commit

```bash
# Ajouter vos fichiers
git add .

# Commit avec un message descriptif
git commit -m "feat: ajouter nouvelle visualisation des certifications

- Ajout d'un graphique en barres pour les certifications
- Amélioration de l'interface utilisateur
- Correction du calcul des statistiques"
```

### 3. Push et Pull Request

```bash
# Pousser vers votre fork
git push origin feature/votre-nouvelle-fonctionnalite

# Créer une Pull Request sur GitHub
```

## 📋 Template de Pull Request

```markdown
## 🎯 Description
Brève description de vos changements

## 🔧 Type de Changement
- [ ] Bug fix
- [ ] Nouvelle fonctionnalité
- [ ] Amélioration de la documentation
- [ ] Refactoring
- [ ] Test

## 🧪 Tests
- [ ] Tests unitaires ajoutés/mis à jour
- [ ] Tests d'intégration passent
- [ ] Dashboard testé localement

## 📸 Captures d'écran (si applicable)
Ajoutez des captures d'écran pour les changements UI

## ✅ Checklist
- [ ] Code suit les standards PEP 8
- [ ] Documentation mise à jour
- [ ] Tests ajoutés/mis à jour
- [ ] README mis à jour si nécessaire
```

## 🐛 Rapport de Bug

Utilisez ce template pour rapporter un bug :

```markdown
## 🐛 Description du Bug
Description claire et concise du bug

## 🔄 Étapes pour Reproduire
1. Aller à '...'
2. Cliquer sur '...'
3. Faire défiler jusqu'à '...'
4. Voir l'erreur

## ✅ Comportement Attendu
Description de ce qui devrait se passer

## 📱 Informations Système
- OS: [ex: Windows 10, macOS, Linux]
- Python: [ex: 3.8.5]
- Streamlit: [ex: 1.28.0]

## 📋 Contexte Additionnel
Toute autre information pertinente
```

## 💡 Suggestions de Fonctionnalités

```markdown
## 💡 Description
Description claire de la fonctionnalité souhaitée

## 🎯 Problème Résolu
Explication du problème que cette fonctionnalité résoudrait

## 💭 Solutions Alternatives
Autres solutions que vous avez considérées

## 📋 Contexte Additionnel
Captures d'écran, mockups, etc.
```

## 🏷️ Labels et Milestones

### Labels Utilisés
- `bug` : Problème à corriger
- `enhancement` : Amélioration
- `documentation` : Documentation
- `good first issue` : Bon pour débuter
- `help wanted` : Besoin d'aide
- `question` : Question générale

## 📞 Communication

### Canaux de Communication
- **Issues GitHub** : Pour les bugs et fonctionnalités
- **Discussions GitHub** : Pour les questions générales
- **Email** : Pour les questions privées

### Code de Conduite
- Soyez respectueux et inclusif
- Utilisez un langage constructif
- Aidez les nouveaux contributeurs
- Respectez les opinions différentes

## 🎉 Reconnaissance

Les contributeurs seront reconnus dans :
- Le fichier `CONTRIBUTORS.md`
- Les releases GitHub
- La documentation du projet

## 📚 Ressources Utiles

- [Documentation Streamlit](https://docs.streamlit.io/)
- [Guide PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

---

Merci de contribuer à ce projet ! 🚀
