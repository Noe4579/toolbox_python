mdpatrouver = "P@wN3d"
wordlist = open("1.ListeMdpBruteForce.txt","r")
lignes = wordlist.readlines()
mdppropose = ""
for ligne in lignes:
    ligne = ligne.strip()
    mdppropose = ligne
    if mdppropose == mdpatrouver:
        print("le mdp est:",ligne)