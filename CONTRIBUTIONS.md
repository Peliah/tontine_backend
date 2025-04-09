
### **CONTRIBUTIONS.md**
```markdown
# Guide de Contribution

## 🎯 Comment contribuer ?
1. **Forker** le dépôt
2. Créer une **branche** :
```bash
git checkout -b feature/nouvelle-fonctionnalite
```

3. **Valider** vos changements :
```bash
git commit -m "Description concise des modifications"
```

4. **Pousser** vers GitHub :
```bash
git push origin feature/nouvelle-fonctionnalite
```

5. Ouvrir une **Pull Request**

## 📌 Bonnes pratiques
- Respecter la syntaxe **PEP 8** (Python)
- Documenter les nouvelles fonctions avec des **docstrings**
- Écrire des **tests unitaires** pour les nouvelles fonctionnalités
- Maintenir des **messages de commit clairs**

## 🐛 Signaler un bug
Ouvrir une issue en décrivant :
1. Le comportement attendu
2. Le comportement actuel
3. Étapes pour reproduire le bug
4. Captures d'écran (si applicable)

## ✨ Proposer une amélioration
Expliquer clairement :
- L'avantage de la nouvelle fonctionnalité
- Son impact technique
- Des exemples d'utilisation

## 📝 Structure du code
```
app/
├── models/       # Modèles de base de données
├── schemas/      # Schémas Pydantic
├── routes/       # Points d'accès API
├── utils/        # Helpers (auth, sécurité)
└── main.py       # Configuration principale
```

## 🤝 Relecture de code
- Toutes les PR nécessitent l'approbation d'au moins **1 mainteneur**
- Les tests doivent passer avant fusion

Merci pour votre contribution ! 🎉
```

---
