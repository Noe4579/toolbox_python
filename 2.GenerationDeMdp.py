import time
listeCaractere = "abcdefghijklmnopqrstuvwxyz"
def generer_mots_recursif(x, prefixe=""):
    if x == 0 :
        return [prefixe]
    mots = []
    for carac in listeCaractere:
        mots += generer_mots_recursif(x - 1, prefixe + carac)
    return mots 

#exemple d'utilisation
st = time.time()
taille = 3
liste_pwds = generer_mots_recursif(taille)
liste_pwds=str(liste_pwds)
with open("2.MdpGeneres.txt", "w") as fichier:
    # Écrire le résultat dans le fichier
    fichier.write(liste_pwds)
end = time.time()
tmptt= end - st
print("le programe a mis",tmptt,"s a s'effectuer.")