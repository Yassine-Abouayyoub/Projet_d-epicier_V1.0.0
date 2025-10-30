print("Le programme est en cours de développement!")
print("BONJOUR")
S = 0
while True:
    P = int(input(" ecrire le prix: "))
    if P > 0:
        S = S + P
        continue
    if P == 0:
        break
    else:
        print("ERROR, donne une vrais valeur")
        continue
print(S)


# les erreurs et points faibles identifiés dans la version V1.0.0 :
# Gestion des entrées utilisateur : Si l'utilisateur tape une lettre ou un symbole au lieu d'un nombre, le programme plante directement et affiche une exception, ce qui stoppe tout le processus.
# Validation des données : Le programme ne distingue pas entre une entrée négative et une entrée non numérique (ex : "abc", "4.2"). Il ne propose pas de message compréhensible à l'utilisateur pour chaque type d'erreur.
# Expérience utilisateur : Le message d’erreur ("ERROR, donne une vrais valeur") n’est affiché qu’en cas de nombre négatif, alors que d’autres erreurs (entrée vide, caractères non-numériques) ne sont pas gérées.
# Sécurité : Il n’y a aucune protection contre les entrées inattendues, donc risque de crash si on fait une mauvaise manipulation.
# Clarté du fonctionnement : L’utilisateur doit deviner que "0" termine la saisie. Cette règle n’est pas clairement expliquée à l’utilisation.
# Code : Le programme utilise des boucles et des branches qui pourraient être simplifiées ou améliorées pour une lecture et un entretien plus facile.
