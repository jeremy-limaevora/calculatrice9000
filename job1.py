def calculatrice():
    historique = []

    while True:
        expression = input("Entrez un calcul (+, -, *, /) ou pour quitter écrire 'annuler': ")
        
        if expression == 'annuler':
            break
        
        operateur = None
        for op in ['+', '-', '*', '/']:
            if op in expression:
                operateur = op
                nombres = expression.split(op)
                if len(nombres) != 2:
                    print("Expression non valide. Utilisez un seul opérateur (+, -, *, /).")
                    continue
                
                nombre1_str, nombre2_str = nombres
                try:
                    nombre1 = float(nombre1_str)
                    nombre2 = float(nombre2_str)
                    resultat = None
                    
                    if operateur == '+':
                        resultat = nombre1 + nombre2
                    elif operateur == '-':
                        resultat = nombre1 - nombre2
                    elif operateur == '*':
                        resultat = nombre1 * nombre2
                    elif operateur == '/':
                        if nombre2 != 0:
                            resultat = nombre1 / nombre2
                        else:
                            print("Division par zéro impossible.")
                            continue

                    if resultat is not None:
                        historique.append(f"{expression} = {resultat:.2f}")
                        print(f"Le résultat de {expression} est : {resultat:.2f}")
                    else:
                        print("Opérateur non valide.")
                    
                    break  # break permet de sortir de la boucle une fois que le resultat a été affiché ou que l'erreur a été notifié
                except ValueError:
                    print("Veuillez entrer des nombres valides.")
                    continue
        
        else:
            print("Expression non valide. Veuillez entrer un calcul avec un opérateur (+, -, *, /).")

    print("\nHistorique des opérations :")
    for operation in historique:
        print(operation)

calculatrice()
