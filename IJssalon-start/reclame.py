from algemene_functies import mijn_functie2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    aanbieding = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
    return aanbieding
  
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw_eraf):
    totaal = sum(inkomsten)
    btw = totaal * btw_eraf
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden"

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    return totaal / aantal

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie2(korte_lijst[0], korte_lijst[1])
    return uitvoer

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]


print(inkomsten_totaal(week_inkomsten, 0.09))
print(laag_en_hoog(week_inkomsten))
print(f"De gemiddelde inkomsten van deze week zijn {gemiddelde(week_inkomsten)} euro")
print (meervoudig([10, 5 ,3, 2, 1, 9]))
print(combinatie(week_inkomsten))

