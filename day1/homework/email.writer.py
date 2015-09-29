# -*- coding: utf-8 -*-
"""
Skriv en funktion som tar ett namn och en domän.
Gör namnet mejlkompatibelt och skriv ut en fullständig e-postadress.
"""



def emailify(name, domain):
    """
     Koden ska göra följande:
     1) Ersätta mellanslag med punkter i namnet.
     2) Göra alla tecken till små bokstäver
     3) Ersätta specialtecken (å,ä,ö,é) med tecken som funkar
     i en e-postadress.
     4) Printa den kompletta adressen! 
    """
    # Skriv din kod här!
    print (name +"@"+ domain) 
    
    if  "hur anger jag att name ska fatta nedanstående här behövs som jag ser en ifsats?"
    small_name = name.lower()
    small_english_name = name.lower ()
    english_name = name.replace(" ",".")
    english_name = name.replace("ö", "o")
    english_name = name.replace("å", "a")
    english_name = name.replace("ä", "a")
    english_name = name.replace("é", "e")
    """ nu kommer en fuling - vet inte hur jag anger dessa specialtecken"""
    english_name = name.replace("阿部慎太郎", "asahi.co.jp")

emailify("Annie Lööf", "riksdagen.se")
emailify("David Lång", "riksdagen.se")
emailify("Emma Nohrén", "riksdagen.se")
emailify("阿部慎太郎", "asahi.co.jp")
emailify("Östen Rubin", "dn.se")

""" Test av roboten"""
write_emailify("Annie Lööf", "riksdagen.se")
print("***************")

write_emailify("David Lång", "riksdagen.se")
print("***************")

write_emailify("Emma Nohrén", "riksdagen.se")
print("***************")

write_emailify("阿部慎太郎", "asahi.co.jp")
print("***************")

write_emailify("Östen Rubin", "dn.se")
print("***************")