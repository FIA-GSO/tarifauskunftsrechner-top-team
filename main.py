# Tarifpreise
preis_kinder = 2.5
preis_jugendlicher = 3.5
preis_erwachsene = 5.0
preis_basis = 4.0
preis_premium = 3.0
preis_tages_erwachsene = 10.0
preis_tages_basis = 8.0
preis_tages_premium = 6.0
preis_tages_kinder = 5.0
preis_tages_jugendlicher = 6.0
gesamtsumme = 0  # Globale Variable
     
def tarifrechner():
    
    global gesamtsumme  # Zugriff auf die globale Variable
    
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print(" Bitte geben Sie Ihr Alter ein:")
    alter_gast = int(input())

    mitgliedschaft = None  # Standardwert
    
    if alter_gast < 14:
        
        print(" ### Eintritt Kinder Halbtags ### ")
        print(f" Preis: {preis_kinder} Euro ")
        gesamtsumme += preis_kinder
        
    elif 14 <= alter_gast <= 17:
        
        print(" ### Eintritt Jugendlicher Halbtags ### ")
        print(f" Preis: {preis_jugendlicher} Euro ")
        gesamtsumme += preis_jugendlicher
        
    else:
        
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Geben Sie ein: 'p' für Premium-Mitglied, 'b' für Basis-Mitglied, oder eine beliebige Taste für kein Mitglied.")
        
        mitgliedschaft = input()
        
        if mitgliedschaft == "p":
            
            print(" ### Eintritt Premium-Mitglied Halbtags ### ")
            print(f" Preis: {preis_premium} Euro ")
            gesamtsumme += preis_premium
            print(" Möchten Sie für 0,75 € ein Glas Sekt? (j/n)")
            sekt = input()
            if sekt == "j":
                gesamtsumme += 0.75
                
        elif mitgliedschaft == "b":
            
            print(" ### Eintritt Basis-Mitglied Halbtags Halbtags ### ")
            print(f" Preis: {preis_basis} Euro ")
            gesamtsumme += preis_basis
            
        else:
            print(" ### Eintritt Erwachsene Halbtags ### ")
            print(f" Preis: {preis_erwachsene} Euro ")
            gesamtsumme += preis_erwachsene

    print(" Möchten Sie ein Ticket für einen halben oder ganzen Tag? (h/g)")
    ticket_dauer = input()

    while ticket_dauer not in ["h", "g"]:
        
        print("Fehlerhafte Eingabe, versuchen Sie es erneut (h/g):")
        ticket_dauer = input()

    if ticket_dauer == "g":
        if alter_gast < 14:
            
            print(f" ### Tagesticket Kinder: {preis_tages_kinder} Euro ### ")
            gesamtsumme += preis_tages_kinder
            
        elif 14 <= alter_gast <= 17:
            
            print(f" ### Tagesticket Jugendliche: {preis_tages_jugendlicher} Euro ### ")
            gesamtsumme += preis_tages_jugendlicher
            
        elif mitgliedschaft == "p":
            
            print(f" ###Tagesticket Premium: {preis_tages_premium} Euro ### ")
            gesamtsumme += preis_tages_premium
            
        elif mitgliedschaft == "b":
            
            print(f" ### Tagesticket Basis: {preis_tages_basis} Euro ### ")
            gesamtsumme += preis_tages_basis
            
        else:
            
            print(f" ### Tagesticket Erwachsene: {preis_tages_erwachsene} Euro ### ")
            gesamtsumme += preis_tages_erwachsene

    print(" Möchten Sie einen weiteren Tarif abfragen? (j/n)")
    weitere_abfrage = input()
    if weitere_abfrage == "j":
        tarifrechner()

    print(f" Viel Spaß! Gesamtsumme: {gesamtsumme} Euro")
    
    
def tarifrechnerEN():
    global gesamtsumme  # Zugriff auf die globale Variable
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print(" Please enter your age:")
    alter_gast = int(input())

    mitgliedschaft = None  # Standardwert
    if alter_gast < 14:
        print(" ### Entry Children ### ")
        print(f" Price: {preis_kinder} Euro ")
        gesamtsumme += preis_kinder
    elif 14 <= alter_gast <= 17:
        print(" ### Eintritt Jugendlicher ### ")
        print(f" Preis: {preis_jugendlicher} Euro ")
        gesamtsumme += preis_jugendlicher
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Geben Sie ein: 'p' für Premium-Mitglied, 'b' für Basis-Mitglied, oder eine beliebige Taste für kein Mitglied.")
        mitgliedschaft = input()
        if mitgliedschaft == "p":
            print(" ### Eintritt Premium-Mitglied ### ")
            print(f" Preis: {preis_premium} Euro ")
            gesamtsumme += preis_premium
            print(" Möchten Sie für 0,75 € ein Glas Sekt? (j/n)")
            sekt = input()
            if sekt == "j":
                gesamtsumme += 0.75
        elif mitgliedschaft == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            print(f" Preis: {preis_basis} Euro ")
            gesamtsumme += preis_basis
        else:
            print(" ### Eintritt Erwachsene ### ")
            print(f" Preis: {preis_erwachsene} Euro ")
            gesamtsumme += preis_erwachsene

    print(" Möchten Sie ein Ticket für einen halben oder ganzen Tag? (h/g)")
    ticket_dauer = input()
    
    while ticket_dauer not in ["h", "g"]:
        print("Fehlerhafte Eingabe, versuchen Sie es erneut (h/g):")
        ticket_dauer = input()

    if ticket_dauer == "g":
        if alter_gast < 14:
            print(f" Tagesticket Kinder: {preis_tages_kinder} Euro ")
            gesamtsumme += preis_tages_kinder
        elif 14 <= alter_gast <= 17:
            print(f" Tagesticket Jugendliche: {preis_tages_jugendlicher} Euro ")
            gesamtsumme += preis_tages_jugendlicher
        elif mitgliedschaft == "p":
            print(f" Tagesticket Premium: {preis_tages_premium} Euro ")
            gesamtsumme += preis_tages_premium
        elif mitgliedschaft == "b":
            print(f" Tagesticket Basis: {preis_tages_basis} Euro ")
            gesamtsumme += preis_tages_basis
        else:
            print(f" Tagesticket Erwachsene: {preis_tages_erwachsene} Euro ")
            gesamtsumme += preis_tages_erwachsene

    print(" Möchten Sie einen weiteren Tarif abfragen? (j/n)")
    weitere_abfrage = input()
    if weitere_abfrage == "j":
        tarifrechner()

    print("Viel Spaß!")
    print(f" ### Gesamtsumme: {gesamtsumme} Euro ### ")    


# Start des Programms
print("Sprachauswahl / Language Selection")
print("DE / EN")

sprache = input()
while sprache not in "DE" or "EN":
    sprache = input()
    if sprache == "DE": 
        tarifrechner()
    elif sprache == "EN":
        tarifrechnerEN()
    else:
        print("Fehlerhafte Eingabe, versuchen sie es erneut. / Wrong Input, please try again.")   
