# -*- coding: utf-8 -*-

""" Se robot_writer.md för instruktioner domentet i samma mapp
"""

total_unemployment_2009 = 5.9
total_unemployment_2014 = 8.0

def write_story(municipality, unemployment_2009, unemployment_2014):
    """text = ("Arbetslösheten var i Bengtsfors 2014 %s procentenheter högre  änefter finnanskrisen 2009. Det har gått upp från" )
    print(text)"""
    """Lolos försök"""
    change_percent=(unemployment_2014 / unemployment_2009*100-100)
    print ("Arbetslösheten var i " + municipality + "var år 2014 %s procentenheter högre än efter finnanskrisen 2009." %(change_percent))
    print ("Den har gått upp från %s procent till %s." % (unemployment_2009, unemployment_2014))

    """Nu ska jag göra IF-satsen som kommenterar utvecklingen: 
    Utvecklingen för kommunen har varit något sämre än i hela landet där arbetslöshet under samma tid vuxit med 0,3 procentenheter.
    alt:
    Utvecklingen för kommunen har varit något bättre än i hela landet där arbetslöshet under samma tid vuxit med 0,3 procentenheter. 
    """
    if change_percent>0.3:
            print "Utvecklingen för kommunen har varit något bättre än i hela landet där arbetslöshet under samma tid vuxit med 0,3 procentenheter"
    else:
            print "Utvecklingen för kommunen har varit något sämre än i hela landet där arbetslöshet under samma tid vuxit med 0,3 procentenheter"

""" Teta roboten!
"""
write_story("Bengtsfors", 9.9,10.3)
print("***************")

write_story("Stockholm", 7.1,6.6) 
print("**************")

write_story("Kiruna", 7.6,4.2) 
print("**************")

write_story("Lessebo", 9.5,13.2) 
print("**************")

"""
Källa: http://www.ekonomifakta.se/sv/Fakta/Regional-statistik/Din-kommun-i-siffror/
"""