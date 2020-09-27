user1 = "bob"
password1 = "123"

user2 = "ann"
password2 = "pass123"

user3 = "mike"
password3 = "password123"

user4 = "liz"
password4 = "pass123"

oddelovac = 50 * "-"

TEXT1 = '''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. '''

TEXT2 = '''
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.'''

TEXT3 = '''
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''

while True:
    print(oddelovac)
    print("Welcome to the app. Please log in:")
    uzivatel_username = input("USERNAME: ")
    uzivatel_pw = input("PASSWORD: ")
    print(oddelovac)

    if uzivatel_username == user1 and uzivatel_pw == password1 or uzivatel_username == user2 and uzivatel_pw == password2 or uzivatel_username == user3 and uzivatel_pw == password3 or uzivatel_username == user4 and uzivatel_pw == password4:
        break
    else:
        print("Wrong Username or password! Try it again!")
        continue



zvoleni_textu = input("We have 3 texts to be analyzed.\nEnter a number btw. 1 and 3 to select: ")
print(oddelovac)

if zvoleni_textu == "1":
    jednotliva_slova = TEXT1.split()
    vycistena_slova = [slovo.strip("., ") for slovo in jednotliva_slova]

    novy_list_title = []
    for jmeno in vycistena_slova:
        if jmeno.istitle():
            novy_list_title.append(jmeno)

    novy_list_uppercase = []
    for jmeno in vycistena_slova:
        if jmeno.isupper():
            novy_list_uppercase.append(jmeno)

    novy_list_lowercase = []
    for jmeno in vycistena_slova:
        if jmeno.islower():
            novy_list_lowercase.append(jmeno)

    novy_list_numer = []
    for jmeno in vycistena_slova:
        if jmeno.isnumeric():
            novy_list_numer.append(jmeno)

    pocet_slov = (len(vycistena_slova))
    pocet_title_slov = len(novy_list_title)
    pocet_upper_slov = len(novy_list_uppercase)
    pocet_lower_slov = len(novy_list_lowercase)
    pocet_num_slov = len(novy_list_numer)

    print(f"There are {pocet_slov} words in the selected text.")
    print(f"There are {pocet_title_slov} titlecase words.")
    print(f"There are {pocet_upper_slov} uppercase words.")
    print(f"There are {pocet_lower_slov} lowercase words.")
    print(f"There are {pocet_num_slov} numeric strings.")
    print(oddelovac)

    delka_slova = {}
    for slovo in vycistena_slova:
        delka_slova[len(slovo)] = delka_slova.get(len(slovo), 0) + 1

    spravne_poradi = sorted(delka_slova)

    for item, _ in enumerate(range(len(spravne_poradi), 0, -1), 1):
        for item in spravne_poradi:
            hodnota = "*" * delka_slova[item]
            print(f"{item}{hodnota}{delka_slova[item]}")
            spravne_poradi.remove(item)
            break
    print(oddelovac)

elif zvoleni_textu == "2":
    jednotliva_slova = TEXT2.split()
    vycistena_slova = [slovo.strip("., ") for slovo in jednotliva_slova]

    novy_list_title = []
    for jmeno in vycistena_slova:
        if jmeno.istitle():
            novy_list_title.append(jmeno)

    novy_list_uppercase = []
    for jmeno in vycistena_slova:
        if jmeno.isupper():
            novy_list_uppercase.append(jmeno)

    novy_list_lowercase = []
    for jmeno in vycistena_slova:
        if jmeno.islower():
            novy_list_lowercase.append(jmeno)

    novy_list_numer = []
    for jmeno in vycistena_slova:
        if jmeno.isnumeric():
            novy_list_numer.append(jmeno)

    pocet_slov = (len(vycistena_slova))
    pocet_title_slov = len(novy_list_title)
    pocet_upper_slov = len(novy_list_uppercase)
    pocet_lower_slov = len(novy_list_lowercase)
    pocet_num_slov = len(novy_list_numer)

    print(f"There are {pocet_slov} words in the selected text.")
    print(f"There are {pocet_title_slov} titlecase words.")
    print(f"There are {pocet_upper_slov} uppercase words.")
    print(f"There are {pocet_lower_slov} lowercase words.")
    print(f"There are {pocet_num_slov} numeric strings.")
    print(oddelovac)

    delka_slova = {}
    for slovo in vycistena_slova:
        delka_slova[len(slovo)] = delka_slova.get(len(slovo), 0) + 1

    spravne_poradi = sorted(delka_slova)

    for item, _ in enumerate(range(len(spravne_poradi), 0, -1), 1):
        for item in spravne_poradi:
            hodnota = "*" * delka_slova[item]
            print(f"{item}{hodnota}{delka_slova[item]}")
            spravne_poradi.remove(item)
            break
    print(oddelovac)

elif zvoleni_textu == "3":
    jednotliva_slova = TEXT3.split()
    vycistena_slova = [slovo.strip("., ") for slovo in jednotliva_slova]

    novy_list_title = []
    for jmeno in vycistena_slova:
        if jmeno.istitle():
            novy_list_title.append(jmeno)

    novy_list_uppercase = []
    for jmeno in vycistena_slova:
        if jmeno.isupper():
            novy_list_uppercase.append(jmeno)

    novy_list_lowercase = []
    for jmeno in vycistena_slova:
        if jmeno.islower():
            novy_list_lowercase.append(jmeno)

    novy_list_numer = []
    for jmeno in vycistena_slova:
        if jmeno.isnumeric():
            novy_list_numer.append(jmeno)

    pocet_slov = (len(vycistena_slova))
    pocet_title_slov = len(novy_list_title)
    pocet_upper_slov = len(novy_list_uppercase)
    pocet_lower_slov = len(novy_list_lowercase)
    pocet_num_slov = len(novy_list_numer)

    print(f"There are {pocet_slov} words in the selected text.")
    print(f"There are {pocet_title_slov} titlecase words.")
    print(f"There are {pocet_upper_slov} uppercase words.")
    print(f"There are {pocet_lower_slov} lowercase words.")
    print(f"There are {pocet_num_slov} numeric strings.")
    print(oddelovac)

    delka_slova = {}
    for slovo in vycistena_slova:
        delka_slova[len(slovo)] = delka_slova.get(len(slovo), 0) + 1

    spravne_poradi = sorted(delka_slova)

    for item, _ in enumerate(range(len(spravne_poradi), 0, -1), 1):
        for item in spravne_poradi:
            hodnota = "*" * delka_slova[item]
            print(f"{item}{hodnota}{delka_slova[item]}")
            spravne_poradi.remove(item)
            break
    print(oddelovac)