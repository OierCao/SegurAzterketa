def letrak_lekuz_aldatu(textua, letra1, letra2):
    # Textua karaktere lista bat bihurtu
    karaktere = list(textua)
    
    # Textu osotik joan eta aldatu nahi ditugun letrak trukatu
    for i in range(len(karaktere)):
        if karaktere[i] == letra1:
            karaktere[i] = letra2
        elif karaktere[i] == letra2:
            karaktere[i] = letra1
    
    # JTextu bat sortu karaktere guztiekin berriro (aldatuekin)
    textu_berria = ''.join(karaktere)
    
    return textu_berria

while True:
    textua = input("Textua sartu ('-1' amaitzeko): ")
    
    if textua.lower() == '-1':
        break
    
    letra1 = input("Aldatu nahi duzun letra bat: ")
    letra2 = input("Beste letra: ")

    # Funtzioa deitu
    emaitza = letrak_lekuz_aldatu(textua, letra1, letra2)

    # Display the modified text
    print("Textu aldatua: ", emaitza)

