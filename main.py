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

def tarifrechner():
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print(" Bitte geben Sie Ihr Alter ein:")
    alter_gast = int(input())

    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(f" Preis: {preis_kinder} Euro ")
    elif 14 <= alter_gast <= 17:
        print(" ### Eintritt Jugendlicher ### ")
        print(f" Preis: {preis_jugendlicher} Euro ")
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Geben Sie ein: 'p' für Premium-Mitglied, 'b' für Basis-Mitglied, oder eine beliebige Taste für kein Mitglied.")
        mitgliedschaft = input()
        if mitgliedschaft == "p":
            print(" ### Eintritt Premium-Mitglied ### ")
            print(f" Preis: {preis_premium} Euro ")
            print(" Möchten Sie für 0,75 € ein Glas Sekt? (j/n)")
            sekt = input()
            if sekt == "j":
                print(" ### Mit Sekt ### ")
                print(f" Gesamtpreis: {preis_premium + 0.75} Euro ")
        elif mitgliedschaft == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            print(f" Preis: {preis_basis} Euro ")
        else:
            print(" ### Eintritt Erwachsene ### ")
            print(f" Preis: {preis_erwachsene} Euro ")

    print(" Möchten Sie ein Ticket für einen halben oder ganzen Tag? (h/g)")
    ticket_dauer = input()

    if ticket_dauer == "g":
        if alter_gast < 14:
            print(f" Tagesticket Kinder: {preis_tages_kinder} Euro ")
        elif 14 <= alter_gast <= 17:
            print(f" Tagesticket Jugendliche: {preis_tages_jugendlicher} Euro ")
        elif mitgliedschaft == "p":
            print(f" Tagesticket Premium: {preis_tages_premium} Euro ")
        elif mitgliedschaft == "b":
            print(f" Tagesticket Basis: {preis_tages_basis} Euro ")
        else:
            print(f" Tagesticket Erwachsene: {preis_tages_erwachsene} Euro ")
    elif ticket_dauer != "h":
        print("Fehlerhafte Eingabe, versuchen sie es erneut")
        ticket_dauer = input() 
    print(" Viel Spaß!")
    print(" Möchten Sie einen weiteren Tarif abfragen? (j/n)")
    weitere_abfrage = input()
    if weitere_abfrage == "j":
        tarifrechner()

# Start des Programms
tarifrechner()
