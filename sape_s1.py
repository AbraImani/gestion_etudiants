
from gestionnaire_sape import * #importation de toutes les fonctions et BD des etudisnts

BASE_DONNEES_ETUDIANTS = []
# point d'entrée du programme
if __name__ == "__main__":

    print("Programme principale en cours... ")
    # exporter_en_json(BASE_DONNEES_ETUDIANTS,"donnes.json")

    BASE_DONNEES_ETUDIANTS = importer_donnees("donnes.json")
    # print(importer_donnees("donnes.json"))
    for i in BASE_DONNEES_ETUDIANTS:
        print(i)
    programme_principale()





