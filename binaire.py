import time
import os

def afficher_logo():
    print("""
    BY C Y C L E A T O N
    """)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def conversion_tous_systemes(valeur):
    try:
        # Convertit d'abord en entier quelle que soit la base d'entrée (binaire, hexadécimal, décimal)
        if valeur.startswith('0b'):
            nombre = int(valeur, 2)  # Binaire -> Décimal
        elif valeur.startswith('0x') or any(c in 'abcdefABCDEF' for c in valeur):
            nombre = int(valeur, 16)  # Hexadécimal -> Décimal (même sans 0x)
        elif all(c in '01' for c in valeur):  # Vérifie si c'est une valeur binaire sans le préfixe
            nombre = int(valeur, 2)  # Interprète comme binaire
        else:
            nombre = int(valeur)  # Supposé en décimal
        
        # Convertit ensuite dans les trois systèmes
        dec = nombre  # Nombre déjà en décimal
        hexa = hex(nombre)[2:]  # Vers hexadécimal sans le préfixe '0x'
        binr = bin(nombre)[2:].zfill(8)  # Vers binaire sans le préfixe '0b', rempli de 0 pour atteindre 8 chiffres

        return f"Décimal : {dec}\nHexadécimal : {hexa}\nBinaire : {binr}"

    except ValueError:
        return "Erreur : Entrée invalide. Assurez-vous d'entrer une valeur correcte."

def afficher_animation_sortie():
    # Animation simple avec du texte qui défile vers le bas
    texte = "Merci d'avoir utilisé mon convertisseur !"
    for i in range(10):  # Nombre de lignes blanches avant d'afficher le texte
        print("\n" * i + texte)
        time.sleep(0.2)  # Pause pour l'effet d'animation
        os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran à chaque étape
    print("@ cycleaton ytb !\n")  # Affiche "LE PUTTENS" à la fin de l'animation

def main():
    afficher_logo()  # Affiche le logo Python pendant 2 secondes
    
    while True:
        # Demande la valeur à convertir
        valeur = input("Entrez une valeur (ex: décimal, hexadécimal, binaire) : ")

        # Vérifie si la valeur entrée est valide
        if valeur.startswith('0b') and not all(c in '01' for c in valeur[2:]):
            print("Erreur : Veuillez entrer une valeur binaire valide.")
            continue
        elif valeur.startswith('0x') and not all(c in '0123456789abcdefABCDEF' for c in valeur[2:]):
            print("Erreur : Veuillez entrer une valeur hexadécimale valide.")
            continue
        elif not valeur.isdigit() and not all(c in '0123456789abcdefABCDEF' for c in valeur):
            print("Erreur : Veuillez entrer une valeur décimale ou hexadécimale valide.")
            continue
        elif all(c in '01' for c in valeur):  # Vérifie si c'est une chaîne binaire
            pass  # Tout est bon, rien à faire ici

        # Affiche les conversions dans tous les systèmes
        resultat = conversion_tous_systemes(valeur)

        # Affiche le résultat
        print(resultat)

        # Vérifie si le résultat est une erreur
        if "Erreur" in resultat:
            print("\nVeuillez réessayer avec une valeur correcte.")
            continue  # Recommence la boucle si une erreur est survenue

        # Demande si l'utilisateur veut continuer ou quitter
        continuer = input("\nVoulez-vous convertir une autre valeur ? (y/n) : ").strip().lower()

        if continuer != 'y':  # Si l'utilisateur ne tape pas 'y', le programme s'arrête
            afficher_animation_sortie()  # Affiche l'animation de sortie
            break

if __name__ == '__main__':
    main()
