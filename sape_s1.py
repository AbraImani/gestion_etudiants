
from gestionnaire_sape import charger_donnees, programme_principale

# Point d'entrée du programme
if __name__ == "__main__":
    #print("Programme principal en cours...")
    #print("-" * 40)
    
    # Charger les données depuis le fichier JSON
    etudiants = charger_donnees("donnes.json")
    
    #print(f"Nombre d'étudiants chargés: {len(etudiants)}")
    #print("-" * 40)
    
    #for etudiant in etudiants:
        #print(etudiant)
    
    # Lancer le menu principal
    programme_principale()

