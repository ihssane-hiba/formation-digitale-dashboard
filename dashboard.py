# -*- coding: utf-8 -*-
"""
Dashboard simplifié pour l'analyse des tendances de formation digitale
Version sans plotly pour test immédiat
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse des Tendances de Formation Digitale",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre principal
st.title("📊 Dashboard d'Analyse des Tendances de Formation Digitale")
st.markdown("---")

# Sidebar pour la navigation
st.sidebar.title("🎯 Navigation")
page = st.sidebar.selectbox(
    "Choisissez une section :",
    ["🏠 Vue d'ensemble", "📈 Tendances du marché", "🎓 Analyse des formations", 
     "🔮 Prédictions", "📊 Comparaisons", "📋 Données brutes"]
)

# Chargement des données
@st.cache_data
def load_data():
    """Charge et prépare toutes les données"""
    try:
        # Données principales
        df_formations = pd.read_csv("df_final_clean_no_empty.csv")
        
        # Données Google Trends
        df_google = pd.read_csv("tendances_google_france.csv")
        df_google['date'] = pd.to_datetime(df_google['date'])
        
        # Données des offres
        df_remotive = pd.read_csv("remotive_jobs_clean.csv")
        df_adzuna = pd.read_csv("adzuna_offres_brutes.csv")
        
        return df_formations, df_google, df_remotive, df_adzuna
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        return None, None, None, None

# Chargement des données
df_formations, df_google, df_remotive, df_adzuna = load_data()

if df_formations is None:
    st.error("Impossible de charger les données. Vérifiez que tous les fichiers CSV sont présents.")
    st.stop()

# ============================
# PAGE 1 : VUE D'ENSEMBLE
# ============================
if page == "🏠 Vue d'ensemble":
    st.header("🏠 Vue d'ensemble du marché de la formation digitale")
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_formations = len(df_formations)
        st.metric("Total Formations", f"{total_formations:,}")
    
    with col2:
        total_demand = df_formations['demand_offres'].sum()
        st.metric("Demande Totale", f"{total_demand:,} offres")
    
    with col3:
        avg_duration = df_formations['duree_heures'].mean()
        st.metric("Durée Moyenne", f"{avg_duration:.1f} heures")
    
    with col4:
        # Compter les formations qui ont une certification (pas vide et pas 'non')
        cert_ratio = (df_formations['certification'].notna() & 
                     (df_formations['certification'] != '') & 
                     (df_formations['certification'] != 'non')).mean() * 100
        st.metric("Formations Certifiantes", f"{cert_ratio:.1f}%")
    
    st.markdown("---")
    
    # Graphiques principaux
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Top 10 des formations les plus demandées")
        top10 = df_formations.nlargest(10, 'demand_offres')
        
        # Graphique simple avec matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        top10.plot(x='titre', y='demand_offres', kind='barh', ax=ax)
        ax.set_title("Formations les plus demandées")
        ax.set_xlabel("Nombre d'offres")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        st.subheader("🎯 Répartition par catégorie")
        cat_stats = df_formations.groupby('categorie').agg({
            'demand_offres': 'sum',
            'titre': 'count'
        }).reset_index()
        
        # Graphique circulaire
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(cat_stats['demand_offres'], labels=cat_stats['categorie'], autopct='%1.1f%%')
        ax.set_title("Répartition de la demande par catégorie")
        st.pyplot(fig)
    
    # Tableau des données
    st.subheader("📋 Données principales")
    st.dataframe(df_formations[['titre', 'categorie', 'demand_offres', 'duree_heures', 'certification']].head(10))
    
    # Analyse des certifications
    st.subheader("🏆 Analyse des certifications")
    col1, col2 = st.columns(2)
    
    with col1:
        # Top 10 des certifications les plus fréquentes
        cert_counts = df_formations['certification'].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        cert_counts.plot(kind='barh', ax=ax)
        ax.set_title("Top 10 des certifications les plus fréquentes")
        ax.set_xlabel("Nombre de formations")
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        # Répartition des formations avec/sans certification
        cert_status = df_formations['certification'].apply(
            lambda x: 'Avec certification' if pd.notna(x) and x != '' and x != 'non' else 'Sans certification'
        ).value_counts()
        
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(cert_status.values, labels=cert_status.index, autopct='%1.1f%%')
        ax.set_title("Répartition des formations par statut de certification")
        st.pyplot(fig)

# ============================
# PAGE 2 : TENDANCES DU MARCHÉ
# ============================
elif page == "📈 Tendances du marché":
    st.header("📈 Analyse des tendances du marché")
    
    # Filtres
    col1, col2 = st.columns(2)
    with col1:
        min_demand = st.slider("Demande minimum", 0, int(df_formations['demand_offres'].max()), 0)
    with col2:
        selected_categories = st.multiselect(
            "Catégories à afficher",
            options=df_formations['categorie'].unique(),
            default=df_formations['categorie'].unique()[:5]
        )
    
    # Filtrer les données
    filtered_df = df_formations[
        (df_formations['demand_offres'] >= min_demand) &
        (df_formations['categorie'].isin(selected_categories))
    ]
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Distribution de la demande")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(filtered_df['demand_offres'], bins=30, alpha=0.7, color='steelblue')
        ax.set_title("Distribution du nombre d'offres par formation")
        ax.set_xlabel("Nombre d'offres")
        ax.set_ylabel("Fréquence")
        st.pyplot(fig)
    
    with col2:
        st.subheader("🎯 Ratio demande/étudiants")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(filtered_df['demand_offres'], filtered_df['ratio_demande_etudiants'], alpha=0.6)
        ax.set_title("Relation entre demande et ratio étudiants")
        ax.set_xlabel("Demande (offres)")
        ax.set_ylabel("Ratio demande/étudiants")
        st.pyplot(fig)
    
    # Analyse des tendances par catégorie
    st.subheader("📈 Tendances par catégorie")
    cat_trends = filtered_df.groupby('categorie').agg({
        'demand_offres': ['mean', 'sum', 'count'],
        'duree_heures': 'mean',
        'ratio_demande_etudiants': 'mean'
    }).round(2)
    
    cat_trends.columns = ['Demande Moyenne', 'Demande Totale', 'Nombre Formations', 
                         'Durée Moyenne', 'Ratio Moyen']
    st.dataframe(cat_trends, use_container_width=True)

# ============================
# PAGE 3 : ANALYSE DES FORMATIONS
# ============================
elif page == "🎓 Analyse des formations":
    st.header("🎓 Analyse détaillée des formations")
    
    # Filtres avancés
    col1, col2, col3 = st.columns(3)
    with col1:
        cert_filter = st.selectbox("Certification", ["Toutes", "Certifiantes", "Non certifiantes"])
    with col2:
        min_duration = st.slider("Durée minimum (heures)", 0, int(df_formations['duree_heures'].max()), 0)
    with col3:
        max_duration = st.slider("Durée maximum (heures)", 0, int(df_formations['duree_heures'].max()), 
                                int(df_formations['duree_heures'].max()))
    
    # Application des filtres
    filtered_df = df_formations.copy()
    if cert_filter == "Certifiantes":
        filtered_df = filtered_df[filtered_df['certification'].notna() & 
                                 (filtered_df['certification'] != '') & 
                                 (filtered_df['certification'] != 'non')]
    elif cert_filter == "Non certifiantes":
        filtered_df = filtered_df[(filtered_df['certification'].isna()) | 
                                 (filtered_df['certification'] == '') | 
                                 (filtered_df['certification'] == 'non')]
    
    filtered_df = filtered_df[
        (filtered_df['duree_heures'] >= min_duration) &
        (filtered_df['duree_heures'] <= max_duration)
    ]
    
    # Métriques filtrées
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Formations filtrées", len(filtered_df))
    with col2:
        st.metric("Demande moyenne", f"{filtered_df['demand_offres'].mean():.1f}")
    with col3:
        st.metric("Durée moyenne", f"{filtered_df['duree_heures'].mean():.1f} heures")
    with col4:
        st.metric("Ratio moyen", f"{filtered_df['ratio_demande_etudiants'].mean():.2f}")
    
    # Graphiques d'analyse
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⏱️ Durée vs Demande")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(filtered_df['duree_heures'], filtered_df['demand_offres'], alpha=0.6)
        ax.set_title("Relation entre durée et demande")
        ax.set_xlabel("Durée (heures)")
        ax.set_ylabel("Demande (offres)")
        st.pyplot(fig)
    
    with col2:
        st.subheader("📊 Distribution des durées")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(filtered_df['duree_heures'], bins=20, alpha=0.7, color='green')
        ax.set_title("Distribution des durées")
        ax.set_xlabel("Durée (heures)")
        ax.set_ylabel("Fréquence")
        st.pyplot(fig)

# ============================
# PAGE 4 : PRÉDICTIONS
# ============================
elif page == "🔮 Prédictions":
    st.header("🔮 Modélisation prédictive")
    
    st.info("""
    **Modèles utilisés :**
    - Régression linéaire
    - Random Forest
    - XGBoost
    - Gradient Boosting
    """)
    
    # Résultats des modèles (basés sur votre code existant)
    model_results = {
        "Linear Regression": {"RMSE": 161.80, "R²": 0.69},
        "Ridge Regression": {"RMSE": 186.98, "R²": 0.59},
        "Lasso Regression": {"RMSE": 194.05, "R²": 0.56},
        "Random Forest": {"RMSE": 198.20, "R²": 0.54},
        "Gradient Boosting": {"RMSE": 167.35, "R²": 0.67},
        "XGBoost": {"RMSE": 152.99, "R²": 0.73}
    }
    
    # Comparaison des modèles
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Comparaison des performances")
        df_results = pd.DataFrame(model_results).T.reset_index()
        df_results.columns = ['Modèle', 'RMSE', 'R²']
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df_results['Modèle'], df_results['R²'], color='skyblue')
        ax.set_title("Score R² par modèle")
        ax.set_ylabel("R² Score")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        st.subheader("📈 Erreur RMSE par modèle")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df_results['Modèle'], df_results['RMSE'], color='lightcoral')
        ax.set_title("Erreur RMSE par modèle (plus bas = mieux)")
        ax.set_ylabel("RMSE")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    
    # Meilleur modèle
    best_model = min(model_results.items(), key=lambda x: x[1]['RMSE'])
    st.success(f"🏆 **Meilleur modèle : {best_model[0]}** (RMSE: {best_model[1]['RMSE']:.2f}, R²: {best_model[1]['R²']:.2f})")

# ============================
# PAGE 5 : COMPARAISONS
# ============================
elif page == "📊 Comparaisons":
    st.header("📊 Comparaisons et analyses croisées")
    
    # Comparaison offre vs demande
    st.subheader("⚖️ Offre vs Demande")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Analyse des offres d'emploi
        if df_remotive is not None:
            st.write("**Répartition des offres Remotive :**")
            if 'category' in df_remotive.columns:
                remotive_cats = df_remotive['category'].value_counts().head(10)
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.pie(remotive_cats.values, labels=remotive_cats.index, autopct='%1.1f%%')
                ax.set_title("Top 10 catégories d'offres Remotive")
                st.pyplot(fig)
    
    with col2:
        # Analyse des formations
        formation_cats = df_formations['categorie'].value_counts()
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.pie(formation_cats.values, labels=formation_cats.index, autopct='%1.1f%%')
        ax.set_title("Répartition des formations par catégorie")
        st.pyplot(fig)

# ============================
# PAGE 6 : DONNÉES BRUTES
# ============================
elif page == "📋 Données brutes":
    st.header("📋 Exploration des données brutes")
    
    # Sélection du dataset
    dataset_choice = st.selectbox(
        "Choisissez un dataset :",
        ["Formations", "Google Trends", "Remotive Jobs", "Adzuna Jobs"]
    )
    
    if dataset_choice == "Formations":
        st.subheader("📊 Dataset Formations")
        st.dataframe(df_formations, use_container_width=True)
        
        # Statistiques descriptives
        st.subheader("📈 Statistiques descriptives")
        st.dataframe(df_formations.describe(), use_container_width=True)
    
    elif dataset_choice == "Google Trends" and df_google is not None:
        st.subheader("📊 Dataset Google Trends")
        st.dataframe(df_google, use_container_width=True)
    
    elif dataset_choice == "Remotive Jobs" and df_remotive is not None:
        st.subheader("📊 Dataset Remotive Jobs")
        st.dataframe(df_remotive.head(100), use_container_width=True)
    
    elif dataset_choice == "Adzuna Jobs" and df_adzuna is not None:
        st.subheader("📊 Dataset Adzuna Jobs")
        st.dataframe(df_adzuna.head(100), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>📊 Dashboard d'analyse des tendances de formation digitale | 
    Développé avec Streamlit et Matplotlib</p>
</div>
""", unsafe_allow_html=True)
