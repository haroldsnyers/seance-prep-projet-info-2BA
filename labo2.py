import sys
import re


# exo0
## print('Année de naissance ? ', end ='')
## sys.stdout.flush()
## data = sys.stdin.read()
## print('Vous avez ', 2016 - int(data), 'ans .')
## sys.exit(0)

# exo1-a)
number3 = input("quelle est votre numéro de teléphone?")

pattern5 = r'\+[0-9]{2} [0-9]{3} [0-9]{2} [0-9]{2} [0-9]{2}$'
p5 = re.compile(pattern5)
print(p5.match(number3))

# exo1-b)
number2 = input("Entree un chiffre entier")
pattern4 = r'[+-]?[1-9][0-9]*$'
p4 = re.compile(pattern4)
print(p4.match(number2))
print("")

# exo1-c)
number1 = input("entree immatriculation")

pattern3 = r'[1-9]?[a-zA-Z]{3}[0-9]{3}|[1-9]?[0-9]{3}[a-zA-Z]{3}$'
p3 = re.compile(pattern3)
print(p3.match(number1))
print("")

# exo1-d)
number = input("entree volume sous windows")

pattern2 = r'C:\\[A-Z]:\\'
p2 = re.compile(pattern2)
print(p2.match(number))
print("")

# exo2
filename = sys.argv[0]
pattern1 = r'([+-]?(?:[1-9]\d*(?:,\d+)?|(?:0(?:,\d+)?)))'
p1 = re.compile(pattern1)
with open(filename, "r") as file:
    compteur = 0
    for line in file:
        compteur += 1
        liste = p1.findall(line)
        string = "ligne " + str(compteur) + ": "
        if len(liste) != 0:
            for x in liste:
                string += x
        print(string)

print("")

# exo3
pattern = r'(?P<protocool>[a-zA-Z]+)://(?P<domain>[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+)/(?P<path>.+)$'
p = re.compile(pattern)
URL = 'http://www.this.is/big/shit'
m = p.match(URL)
print("Protocol: " + m.group("protocool"))
print("domain: " + m.group("domain"))
print("Path: " + m.group("path"))


# mots-croisé
def checkregexcrossword(linesregex, columsregex, answer):
    result = []
    # Ligne
    compteur = 0
    for x in linesregex:
        c = re.compile(linesregex[compteur])
        if (c.match(answer[compteur])) is not None:
            result.append(True)
        else:
            result.append(False)
        compteur += 1

    # Colonne
    compteur = 0
    for w in columsregex:
        c = re.compile(columsregex[compteur])
        chiffre = ""
        for i in answer:
            chiffre += i[compteur]

        if (c.match(chiffre)) is not None:
            result.append(True)
        else:
            result.append(False)

        compteur += 1

    if False in result:
        return False
    else:
        return True


print(" ")
print("mot-croisé is " + str(checkregexcrossword(["[DEF][MNO]*", "[^DJNU]P[ABC]", "[ICAN]*"], ["[JUNDT]*", "APA|OPI|OLK", "(NA|FE|HE)[CV]"],
                          ["DON", "TPA", "NIC"])))
