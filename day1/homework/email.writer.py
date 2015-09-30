# -*- coding: utf-8 -*-
"""
Skriv en funktion som tar ett namn och en domän.
Gör namnet mejlkompatibelt och skriv ut en fullständig e-postadress.
"""
"""
     Koden ska göra följande:
     1) Ersätta mellanslag med punkter i namnet.
     2) Göra alla tecken till små bokstäver
     3) Ersätta specialtecken (å,ä,ö,é) med tecken som funkar
     i en e-postadress.
     4) Printa den kompletta adressen! 
    """


def emailify(name, domain):
    
    """först måste man ange villkoren"""  
     
    name = name.lower()
    name = name.replace(" ",".")
    name = name.replace("ö", "o")
    name = name.replace("å", "a")
    name = name.replace("ä", "a")
    name = name.replace("é", "e")
    print (name +"@"+ domain) #här skrivs det ut
  


emailify("Annie Lööf", "riksdagen.se")
emailify("David Lång", "riksdagen.se")
emailify("Emma Nohrén", "riksdagen.se")
emailify("阿部慎太郎", "asahi.co.jp")
emailify("Östen Rubin", "dn.se")


