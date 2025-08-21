#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de configuration automatique pour GitHub
Configure Git et prépare le repository pour GitHub
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Succès")
            if result.stdout:
                print(f"   Sortie: {result.stdout.strip()}")
        else:
            print(f"❌ {description} - Erreur")
            if result.stderr:
                print(f"   Erreur: {result.stderr.strip()}")
        return result.returncode == 0
    except Exception as e:
        print(f"❌ {description} - Exception: {e}")
        return False

def check_git_installed():
    """Vérifie si Git est installé"""
    return run_command("git --version", "Vérification de Git")

def init_git_repo():
    """Initialise le repository Git"""
    if not os.path.exists(".git"):
        return run_command("git init", "Initialisation du repository Git")
    else:
        print("ℹ️ Repository Git déjà initialisé")
        return True

def add_files():
    """Ajoute tous les fichiers au staging"""
    return run_command("git add .", "Ajout des fichiers au staging")

def initial_commit():
    """Fait le commit initial"""
    return run_command(
        'git commit -m "Initial commit: Dashboard Formation Digitale"',
        "Commit initial"
    )

def setup_remote():
    """Configure le remote GitHub"""
    print("\n🌐 Configuration du remote GitHub")
    print("=" * 50)
    
    username = input("Entrez votre nom d'utilisateur GitHub: ").strip()
    repo_name = input("Entrez le nom du repository (ou appuyez sur Entrée pour 'formation-digitale-dashboard'): ").strip()
    
    if not repo_name:
        repo_name = "formation-digitale-dashboard"
    
    remote_url = f"https://github.com/{username}/{repo_name}.git"
    
    print(f"\n📋 URL du remote: {remote_url}")
    confirm = input("Confirmer ? (y/N): ").strip().lower()
    
    if confirm == 'y':
        return run_command(f"git remote add origin {remote_url}", "Ajout du remote GitHub")
    else:
        print("❌ Configuration du remote annulée")
        return False

def push_to_github():
    """Pousse le code vers GitHub"""
    return run_command("git push -u origin main", "Push vers GitHub")

def create_branch():
    """Crée et bascule sur la branche main si nécessaire"""
    result = subprocess.run("git branch --show-current", shell=True, capture_output=True, text=True)
    current_branch = result.stdout.strip()
    
    if current_branch == "master":
        run_command("git branch -M main", "Renommage de master vers main")
        return True
    elif current_branch == "main":
        print("ℹ️ Déjà sur la branche main")
        return True
    else:
        print(f"⚠️ Branche actuelle: {current_branch}")
        return True

def update_readme():
    """Met à jour le README avec les informations personnelles"""
    print("\n📝 Personnalisation du README")
    print("=" * 50)
    
    name = input("Entrez votre nom complet: ").strip()
    email = input("Entrez votre email: ").strip()
    linkedin = input("Entrez votre profil LinkedIn (optionnel): ").strip()
    github_username = input("Entrez votre nom d'utilisateur GitHub: ").strip()
    
    # Lire le README actuel
    readme_path = Path("README.md")
    if readme_path.exists():
        content = readme_path.read_text(encoding='utf-8')
        
        # Remplacer les placeholders
        content = content.replace("Votre Nom", name)
        content = content.replace("votre.email@example.com", email)
        content = content.replace("https://linkedin.com/in/votre-profil", linkedin if linkedin else "#")
        content = content.replace("votre-username", github_username)
        content = content.replace("https://github.com/votre-username/formation-digitale-dashboard", f"https://github.com/{github_username}/formation-digitale-dashboard")
        
        # Écrire le README mis à jour
        readme_path.write_text(content, encoding='utf-8')
        print("✅ README mis à jour avec vos informations")
        return True
    else:
        print("❌ Fichier README.md non trouvé")
        return False

def main():
    """Fonction principale"""
    print("🚀 Configuration automatique pour GitHub")
    print("=" * 50)
    
    # Vérifications préliminaires
    if not check_git_installed():
        print("❌ Git n'est pas installé. Veuillez l'installer d'abord.")
        return
    
    # Configuration Git
    if not init_git_repo():
        print("❌ Impossible d'initialiser le repository Git")
        return
    
    if not create_branch():
        print("❌ Problème avec la branche")
        return
    
    # Personnalisation
    update_readme()
    
    # Ajout et commit
    if not add_files():
        print("❌ Impossible d'ajouter les fichiers")
        return
    
    if not initial_commit():
        print("❌ Impossible de faire le commit initial")
        return
    
    # Configuration GitHub
    if setup_remote():
        print("\n🎉 Configuration terminée !")
        print("\n📋 Prochaines étapes:")
        print("1. Créez le repository sur GitHub (si pas déjà fait)")
        print("2. Exécutez: git push -u origin main")
        print("3. Vérifiez que tout fonctionne sur GitHub")
        
        push_confirm = input("\nVoulez-vous pousser vers GitHub maintenant ? (y/N): ").strip().lower()
        if push_confirm == 'y':
            push_to_github()
    else:
        print("\n📋 Configuration locale terminée !")
        print("Vous pouvez configurer le remote GitHub manuellement plus tard.")

if __name__ == "__main__":
    main()
