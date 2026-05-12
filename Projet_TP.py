def clean_value(valeur):
    v = valeur.strip()
    valeurs_invalides = ['??', '#BOŞ!', '#BOÞ!', '']
    if v in valeurs_invalides:
        return "N/A"
    v_modifiee = v.replace(',', '.')
    try:
        float(v_modifiee)
        return v_modifiee
    except ValueError:
        return v

donnees_nettoyees = []

with open('c:\\temp\\data.csv', 'r', encoding='latin-1') as fin:
    next(fin)
    for ligne in fin:
        token = ligne.strip().split(';')

        try:
            if len(token) >= 20:
                ligne_propre = [
                    clean_value(token[1]),  # Sex
                    clean_value(token[2]),  # Age
                    clean_value(token[4]),  # Arrival mode
                    clean_value(token[5]),  # Injury
                    clean_value(token[7]),  # Mental
                    clean_value(token[8]),  # Pain
                    clean_value(token[9]),  # NRS_pain
                    clean_value(token[10]), # SBP
                    clean_value(token[11]), # DBP
                    clean_value(token[12]), # HR
                    clean_value(token[13]), # RR
                    clean_value(token[14]), # BT
                    clean_value(token[15]), # Saturation
                    clean_value(token[19])  # KTAS_expert
                ]
                donnees_nettoyees.append(ligne_propre)

        except IndexError:
            continue

print(f"Tableau créé avec {len(donnees_nettoyees)} lignes.")
