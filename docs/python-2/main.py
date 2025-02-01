import sqlite3

# Connexion à la base de donnée nommée music
base_donnees = sqlite3.connect("music.sqlite")

# Exécution de la requête
requete = base_donnees.execute("select * from artist;")

# Lecture des données
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne :
for resultat in resultats:
  print(resultat)
