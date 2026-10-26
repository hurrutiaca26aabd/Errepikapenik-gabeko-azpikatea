katea = input("Sartu letra kate bat (adbz: 'abcabcbb'): ")

azpikate_luzeena = 0

for i in range(len(katea)):
    ikusitakoak = []

    for j in range(i, len(katea)):
        uneko_letra = katea[j]

        if uneko_letra in ikusitakoak:
            break

        ikusitakoak.append(uneko_letra)

    if len(ikusitakoak) > azpikate_luzeena:
        azpikate_luzeena = len(ikusitakoak)

print(f"Errepikatutako karakterik gabeko azpikate luzeena: {azpikate_luzeena}")