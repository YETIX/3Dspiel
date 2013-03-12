# Spielfeld benutzen
from Spielfeld3D import *

# Spielobjekte benutzen
from Spielobjekt3D import *


#---------------------------------------------------------------------------------------
# Funktion zum Berechnen der Schwerkraft
#---------------------------------------------------------------------------------------

def schwerkraftBerechnen( spielobjekt ):

    # Schwerkraft für alle Plattformen prüfen
    if (not spielobjekt.berührt( plattform1 ) or spielobjekt.positionY + spielobjekt.höhe - 1 > plattform1.positionY) and \
       (not spielobjekt.berührt( plattform2 ) or spielobjekt.positionY + spielobjekt.höhe - 1 > plattform2.positionY) and \
     (not spielobjekt.berührt( plattform3 ) or spielobjekt.positionY + spielobjekt.höhe - 1 > plattform3.positionY) and \
	   (not spielobjekt.berührt( plattform4 ) or spielobjekt.positionY + spielobjekt.höhe - 1 > plattform4.positionY) and \
	   (not spielobjekt.berührt( plattform5 ) or spielobjekt.positionY + spielobjekt.höhe - 1 > plattform5.positionY) and \
	   (not spielobjekt.berührt( plattform6 ) or spielobjekt.positionY + spielobjekt.höhe - 1 > plattform6.positionY) and \
	   (not spielobjekt.berührt( plattform7 ) or spielobjekt.positionY + spielobjekt.höhe - 1 > plattform7.positionY) and \
	   (not spielobjekt.berührt( plattform8 ) or spielobjekt.positionY + spielobjekt.höhe - 1 > plattform8.positionY) and \
       (spielobjekt.positionY + spielobjekt.höhe < spielfeld.höhe):
        spielobjekt.positionY = spielobjekt.positionY + 10
        return( True )

    else:
        return( False )


#---------------------------------------------------------------------------------------
# Funktion zum Prüfen, ob Gymgi nach rechts laufen darf (oder ob dort ein Hindernis ist)
#---------------------------------------------------------------------------------------

def darfNachRechts( gymgi ):

    # Wenn möglich nach rechts zu gehen...
    if ((not gymgi.berührt( plattform1 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform1.positionY) or (gymgi.positionX + 10 >= plattform1.positionX + plattform1.breite) or (gymgi.positionZ <= plattform1.positionZ - 20) or (gymgi.positionZ >= plattform1.positionZ + 20)) and \
       ((not gymgi.berührt( plattform2 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform2.positionY) or (gymgi.positionX + 10 >= plattform2.positionX + plattform2.breite) or (gymgi.positionZ <= plattform2.positionZ - 20) or (gymgi.positionZ >= plattform2.positionZ + 20)) and \
	   ((not gymgi.berührt( plattform3 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform3.positionY) or (gymgi.positionX + 10 >= plattform3.positionX + plattform3.breite) or (gymgi.positionZ <= plattform3.positionZ - 20) or (gymgi.positionZ >= plattform3.positionZ + 20)) and \
	   ((not gymgi.berührt( plattform4 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform4.positionY) or (gymgi.positionX + 10 >= plattform4.positionX + plattform4.breite) or (gymgi.positionZ <= plattform4.positionZ - 20) or (gymgi.positionZ >= plattform4.positionZ + 20)) and \
	   ((not gymgi.berührt( plattform5 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform5.positionY) or (gymgi.positionX + 10 >= plattform5.positionX + plattform5.breite) or (gymgi.positionZ <= plattform5.positionZ - 20) or (gymgi.positionZ >= plattform5.positionZ + 20)) and \
	   ((not gymgi.berührt( plattform6 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform6.positionY) or (gymgi.positionX + 10 >= plattform6.positionX + plattform6.breite) or (gymgi.positionZ <= plattform6.positionZ - 20) or (gymgi.positionZ >= plattform6.positionZ + 20)) and \
	   ((not gymgi.berührt( plattform7 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform7.positionY) or (gymgi.positionX + 10 >= plattform7.positionX + plattform7.breite) or (gymgi.positionZ <= plattform7.positionZ - 20) or (gymgi.positionZ >= plattform7.positionZ + 20)) and \
	   ((not gymgi.berührt( plattform8 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform8.positionY) or (gymgi.positionX + 10 >= plattform8.positionX + plattform8.breite) or (gymgi.positionZ <= plattform8.positionZ - 20) or (gymgi.positionZ >= plattform8.positionZ + 20)):
	   
        
        # Wahr zurückgeben
        return( True )

    # ...sonst
    else:

        # Falsch zurückgeben
        return( False )


#---------------------------------------------------------------------------------------
# Funktion zum Prüfen, ob Gymgi nach links laufen darf (oder ob dort ein Hindernis ist)
#---------------------------------------------------------------------------------------

def darfNachLinks( gymgi ):

    # Wenn möglich nach links zu gehen...
    if ((not gymgi.berührt( plattform1 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform1.positionY) or (gymgi.positionX - 10 + gymgi.breite <= plattform1.positionX) or (gymgi.positionZ <= plattform1.positionZ - 20) or (gymgi.positionZ >= plattform1.positionZ + 20)) and \
       ((not gymgi.berührt( plattform2 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform2.positionY) or (gymgi.positionX - 10 + gymgi.breite <= plattform2.positionX) or (gymgi.positionZ <= plattform2.positionZ - 20) or (gymgi.positionZ >= plattform2.positionZ + 20)) and \
       ((not gymgi.berührt( plattform3 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform3.positionY) or (gymgi.positionX - 10 + gymgi.breite <= plattform3.positionX) or (gymgi.positionZ <= plattform3.positionZ - 20) or (gymgi.positionZ >= plattform3.positionZ + 20)) and \
       ((not gymgi.berührt( plattform4 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform4.positionY) or (gymgi.positionX - 10 + gymgi.breite <= plattform4.positionX) or (gymgi.positionZ <= plattform4.positionZ - 20) or (gymgi.positionZ >= plattform4.positionZ + 20)) and \
       ((not gymgi.berührt( plattform5 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform5.positionY) or (gymgi.positionX - 10 + gymgi.breite <= plattform5.positionX) or (gymgi.positionZ <= plattform5.positionZ - 20) or (gymgi.positionZ >= plattform5.positionZ + 20)) and \
       ((not gymgi.berührt( plattform6 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform6.positionY) or (gymgi.positionX - 10 + gymgi.breite <= plattform6.positionX) or (gymgi.positionZ <= plattform6.positionZ - 20) or (gymgi.positionZ >= plattform6.positionZ + 20)) and \
       ((not gymgi.berührt( plattform7 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform7.positionY) or (gymgi.positionX - 10 + gymgi.breite <= plattform7.positionX) or (gymgi.positionZ <= plattform7.positionZ - 20) or (gymgi.positionZ >= plattform7.positionZ + 20)) and \
       ((not gymgi.berührt( plattform8 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform8.positionY) or (gymgi.positionX - 10 + gymgi.breite <= plattform8.positionX) or (gymgi.positionZ <= plattform8.positionZ - 20) or (gymgi.positionZ >= plattform8.positionZ + 20)):

        # Wahr zurückgeben
        return( True )

    # ...sonst
    else:

        # Falsch zurückgeben
        return( False )


#---------------------------------------------------------------------------------------
# Funktion zum Prüfen, ob Gymgi nach hinten laufen darf (oder ob dort ein Hindernis ist)
#---------------------------------------------------------------------------------------

def darfNachHinten( gymgi ):

    # Wenn möglich nach hinten zu gehen...
    if  ((not gymgi.berührt( plattform1 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform1.positionY) or (gymgi.positionZ >= plattform1.positionZ + 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform1.positionX) or (gymgi.positionX + 10 >= plattform1.positionX + plattform1.breite)) and \
		((not gymgi.berührt( plattform2 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform2.positionY) or (gymgi.positionZ >= plattform2.positionZ + 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform2.positionX) or (gymgi.positionX + 10 >= plattform2.positionX + plattform2.breite)) and \
		((not gymgi.berührt( plattform3 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform3.positionY) or (gymgi.positionZ >= plattform3.positionZ + 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform3.positionX) or (gymgi.positionX + 10 >= plattform3.positionX + plattform3.breite)) and \
		((not gymgi.berührt( plattform4 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform4.positionY) or (gymgi.positionZ >= plattform4.positionZ + 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform4.positionX) or (gymgi.positionX + 10 >= plattform4.positionX + plattform4.breite)) and \
		((not gymgi.berührt( plattform5 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform5.positionY) or (gymgi.positionZ >= plattform5.positionZ + 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform5.positionX) or (gymgi.positionX + 10 >= plattform5.positionX + plattform5.breite)) and \
		((not gymgi.berührt( plattform6 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform6.positionY) or (gymgi.positionZ >= plattform6.positionZ + 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform6.positionX) or (gymgi.positionX + 10 >= plattform6.positionX + plattform6.breite)) and \
		((not gymgi.berührt( plattform7 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform7.positionY) or (gymgi.positionZ >= plattform7.positionZ + 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform7.positionX) or (gymgi.positionX + 10 >= plattform7.positionX + plattform7.breite)) and \
        ((not gymgi.berührt( plattform8 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform8.positionY) or (gymgi.positionZ >= plattform8.positionZ + 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform8.positionX) or (gymgi.positionX + 10 >= plattform8.positionX + plattform8.breite)):
        
        # Wahr zurückgeben
        return( True )

    # ...sonst
    else:

        # Falsch zurückgeben
        return( False )


#---------------------------------------------------------------------------------------
# Funktion zum Prüfen, ob Gymgi nach vorne laufen darf (oder ob dort ein Hindernis ist)
#---------------------------------------------------------------------------------------

def darfNachVorne( gymgi ):

    # Wenn möglich nach vorne zu gehen...
    if  ((not gymgi.berührt( plattform1 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform1.positionY) or (gymgi.positionZ <= plattform1.positionZ - 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform1.positionX) or (gymgi.positionX + 10 >= plattform1.positionX + plattform1.breite)) and \
		((not gymgi.berührt( plattform2 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform2.positionY) or (gymgi.positionZ <= plattform2.positionZ - 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform2.positionX) or (gymgi.positionX + 10 >= plattform2.positionX + plattform2.breite)) and \
		((not gymgi.berührt( plattform3 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform3.positionY) or (gymgi.positionZ <= plattform3.positionZ - 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform3.positionX) or (gymgi.positionX + 10 >= plattform3.positionX + plattform3.breite)) and \
		((not gymgi.berührt( plattform4 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform4.positionY) or (gymgi.positionZ <= plattform4.positionZ - 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform4.positionX) or (gymgi.positionX + 10 >= plattform4.positionX + plattform4.breite)) and \
		((not gymgi.berührt( plattform5 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform5.positionY) or (gymgi.positionZ <= plattform5.positionZ - 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform5.positionX) or (gymgi.positionX + 10 >= plattform5.positionX + plattform5.breite)) and \
		((not gymgi.berührt( plattform6 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform6.positionY) or (gymgi.positionZ <= plattform6.positionZ - 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform6.positionX) or (gymgi.positionX + 10 >= plattform6.positionX + plattform6.breite)) and \
		((not gymgi.berührt( plattform7 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform7.positionY) or (gymgi.positionZ <= plattform7.positionZ - 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform7.positionX) or (gymgi.positionX + 10 >= plattform7.positionX + plattform7.breite)) and \
        ((not gymgi.berührt( plattform8 )) or (gymgi.positionY + gymgi.höhe - 1 <= plattform8.positionY) or (gymgi.positionZ <= plattform8.positionZ - 20) or (gymgi.positionX + gymgi.breite - 10 <= plattform8.positionX) or (gymgi.positionX + 10 >= plattform8.positionX + plattform8.breite)):
        
        # Wahr zurückgeben
        return( True )

    # ...sonst
    else:

        # Falsch zurückgeben
        return( False )


#---------------------------------------------------------------------------------------
# Funktion zum Prüfen, ob Gymgi springen darf (oder ob dort ein Hindernis ist)
#---------------------------------------------------------------------------------------

def darfSpringen( gymgi ):

    # Wenn nicht möglich zu springen...
    if (gymgi.berührt( plattform1 ) and (gymgi.positionY + gymgi.höhe - 1 > plattform1.positionY) and (gymgi.positionX + 10 < plattform1.positionX + plattform1.breite) and (gymgi.positionX + gymgi.breite - 10 > plattform1.positionX) and (gymgi.positionZ > plattform1.positionZ - 20) and (gymgi.positionZ < plattform1.positionZ + 20)) or \
       (gymgi.berührt( plattform2 ) and (gymgi.positionY + gymgi.höhe - 1 > plattform2.positionY) and (gymgi.positionX + 10 < plattform2.positionX + plattform2.breite) and (gymgi.positionX + gymgi.breite - 10 > plattform2.positionX) and (gymgi.positionZ > plattform2.positionZ - 20) and (gymgi.positionZ < plattform2.positionZ + 20)) or \
	   (gymgi.berührt( plattform3 ) and (gymgi.positionY + gymgi.höhe - 1 > plattform3.positionY) and (gymgi.positionX + 10 < plattform3.positionX + plattform3.breite) and (gymgi.positionX + gymgi.breite - 10 > plattform3.positionX) and (gymgi.positionZ > plattform3.positionZ - 20) and (gymgi.positionZ < plattform3.positionZ + 20)) or \
	   (gymgi.berührt( plattform4 ) and (gymgi.positionY + gymgi.höhe - 1 > plattform4.positionY) and (gymgi.positionX + 10 < plattform4.positionX + plattform4.breite) and (gymgi.positionX + gymgi.breite - 10 > plattform4.positionX) and (gymgi.positionZ > plattform4.positionZ - 20) and (gymgi.positionZ < plattform4.positionZ + 20)) or \
	   (gymgi.berührt( plattform5 ) and (gymgi.positionY + gymgi.höhe - 1 > plattform5.positionY) and (gymgi.positionX + 10 < plattform5.positionX + plattform5.breite) and (gymgi.positionX + gymgi.breite - 10 > plattform5.positionX) and (gymgi.positionZ > plattform5.positionZ - 20) and (gymgi.positionZ < plattform5.positionZ + 20)) or \
	   (gymgi.berührt( plattform6 ) and (gymgi.positionY + gymgi.höhe - 1 > plattform6.positionY) and (gymgi.positionX + 10 < plattform6.positionX + plattform6.breite) and (gymgi.positionX + gymgi.breite - 10 > plattform6.positionX) and (gymgi.positionZ > plattform6.positionZ - 20) and (gymgi.positionZ < plattform6.positionZ + 20)) or \
	   (gymgi.berührt( plattform7 ) and (gymgi.positionY + gymgi.höhe - 1 > plattform7.positionY) and (gymgi.positionX + 10 < plattform7.positionX + plattform7.breite) and (gymgi.positionX + gymgi.breite - 10 > plattform7.positionX) and (gymgi.positionZ > plattform7.positionZ - 20) and (gymgi.positionZ < plattform7.positionZ + 20)) or \
	   (gymgi.berührt( plattform8 ) and (gymgi.positionY + gymgi.höhe - 1 > plattform8.positionY) and (gymgi.positionX + 10 < plattform8.positionX + plattform8.breite) and (gymgi.positionX + gymgi.breite - 10 > plattform8.positionX) and (gymgi.positionZ > plattform8.positionZ - 20) and (gymgi.positionZ < plattform8.positionZ + 20)):
        
        # Falsch zurückgeben
        return( False )

    # ...sonst
    else:

        # Wahr zurückgeben
        return( True )





#---------------------------------------------------------------------------------------
# HAUPTPROGRAMM
#---------------------------------------------------------------------------------------

# Spielfeld erstellen
spielfeld = Spielfeld3D()

# Hintergrund erstellen
hintergrund = Spielobjekt3D()
hintergrund.bildname = "HintergrundBerge.gif"
hintergrund.breite = 800
hintergrund.höhe = 600
hintergrund.positionX = 0
hintergrund.positionY = 0
spielfeld.hinzufügen( hintergrund )

# Plattform erstellen
plattform1 = Spielobjekt3D()
plattform1.bildname = "Stein.gif"
plattform1.breite = 250
plattform1.höhe = 40
plattform1.positionX = 300
plattform1.positionY = 520
plattform1.positionZ = 350
spielfeld.hinzufügen( plattform1 )

# Zweite Plattform erstellen
plattform2 = Spielobjekt3D()
plattform2.bildname = "Stein.gif"
plattform2.breite = 100
plattform2.höhe = 40
plattform2.positionX = 375
plattform2.positionY = 450
plattform2.positionZ = 350
plattform2.richtungX = 1
spielfeld.hinzufügen( plattform2 )

# Plattform3 erstellen
plattform3 = Spielobjekt3D()
plattform3.bildname = "Stein.gif"
plattform3.breite = 100
plattform3.höhe = 40
plattform3.positionX = 430
plattform3.positionY = 380
plattform3.positionZ = 350
plattform3.richtungX = 1
spielfeld.hinzufügen( plattform3 )

# Zweite Plattform erstellen
plattform4 = Spielobjekt3D()
plattform4.bildname = "Stein.gif"
plattform4.breite = 100
plattform4.höhe = 40
plattform4.positionX = 480
plattform4.positionY = 350
plattform4.positionZ = 350
plattform4.richtungX = 1
spielfeld.hinzufügen( plattform4 )

# Zweite Plattform erstellen
plattform5 = Spielobjekt3D()
plattform5.bildname = "Stein.gif"
plattform5.breite = 100
plattform5.höhe = 40
plattform5.positionX = 520
plattform5.positionY = 320
plattform5.positionZ = 350
plattform5.richtungX = 1
spielfeld.hinzufügen( plattform5 )

# Zweite Plattform erstellen
plattform6 = Spielobjekt3D()
plattform6.bildname = "Stein.gif"
plattform6.breite = 100
plattform6.höhe = 40
plattform6.positionX = 550
plattform6.positionY = 300
plattform6.positionZ = 350
plattform6.richtungX = 1
spielfeld.hinzufügen( plattform6 )

# Zweite Plattform erstellen
plattform7 = Spielobjekt3D()
plattform7.bildname = "Stein.gif"
plattform7.breite = 100
plattform7.höhe = 40
plattform7.positionX = 570
plattform7.positionY = 270
plattform7.positionZ = 350
plattform7.richtungX = 1
spielfeld.hinzufügen( plattform7 )

# Zweite Plattform erstellen
plattform8 = Spielobjekt3D()
plattform8.bildname = "Stein.gif"
plattform8.breite = 100
plattform8.höhe = 40
plattform8.positionX = 650
plattform8.positionY = 250
plattform8.positionZ = 350
plattform8.richtungX = 1
spielfeld.hinzufügen( plattform8 )

# Tür erstellen
tür = Spielobjekt3D()
tür.bildname = "Ausgangstür.gif"
tür.breite = 50
tür.höhe = 90
tür.text = "--> nächstes Level"
tür.positionX = 500
tür.positionY = 400
tür.positionZ = 390
spielfeld.hinzufügen( tür )

# Gegner erstellen
gegner1 = Spielobjekt3D()
gegner1.bildname = "Kokosnuss1.gif"
gegner1.höhe = 60
gegner1.breite = 60
gegner1.positionX = 700
gegner1.positionY = 151
gegner1.positionZ = 200
gegner1.richtungX = -1
spielfeld.hinzufügen( gegner1 )

# Gymgi erstellen
gymgi = Spielobjekt3D()
gymgi.bildname = "GymgiStehen.gif"
gymgi.breite = 40
gymgi.höhe = 100
gymgi.positionX = 10
gymgi.positionY = 491
gymgi.positionZ = 10
gymgi.richtungX = 1
gymgi.sprungZähler = 0
gymgi.istSchrittGelaufen = False
spielfeld.hinzufügen( gymgi )

# Schriftrolle erstellen
schriftrolle = Spielobjekt3D()
schriftrolle.bildname = "Schriftrolle.gif"
schriftrolle.breite = 260
schriftrolle.höhe = 80
schriftrolle.positionX = -10
schriftrolle.positionY = 2
spielfeld.hinzufügen( schriftrolle )

# Variablen für Leben und Punkte erstellen
leben = 5
punkte = 0

# Lebenanzeige erstellen
lebenAnzeige = Spielobjekt3D()
lebenAnzeige.text = "Leben: " + str( leben )
lebenAnzeige.positionX = 25
lebenAnzeige.positionY = 35
spielfeld.hinzufügen( lebenAnzeige )

# Punkteanzeige erstellen
punkteAnzeige = Spielobjekt3D()
punkteAnzeige.text = "Punkte: " + str( punkte )
punkteAnzeige.positionX = 100
punkteAnzeige.positionY = 35
spielfeld.hinzufügen( punkteAnzeige )

# Hauptschleife (solange Spieler noch Leben hat)
while leben > 0 and not gymgi.berührt( tür ):

    # Zu Beginn eines Schleifendurchgangs ist Gymgi noch kein Schritt gelaufen
    gymgi.istSchrittGelaufen = False
        
    # Wenn nach rechts gedrückt, bewege Gymgi nach rechts
    if spielfeld.rechtsGedrückt and darfNachRechts( gymgi ):
        gymgi.positionX = gymgi.positionX + 10

        # Richtung merken
        gymgi.richtungX = 1

        # Wenn Gymgi Schritt 1, dann Schritt 2
        if gymgi.bildname == "GymgiSchritt1.gif":
            gymgi.bildname = "GymgiSchritt2.gif"

        # Wenn Gymgi Schritt 2, dann Schritt 1
        elif gymgi.bildname == "GymgiSchritt2.gif":
            gymgi.bildname = "GymgiSchritt1.gif"

        # sonst
        else:
            gymgi.bildname = "GymgiSchritt1.gif"

        # Merken, dass Schritt gelaufen
        gymgi.istSchrittGelaufen = True
        
    # sonst wenn nach links gedrückt, bewege Gymgi nach links
    elif spielfeld.linksGedrückt and darfNachLinks( gymgi ):
        gymgi.positionX = gymgi.positionX - 10

        # Richtung merken
        gymgi.richtungX = -1

        # Wenn Gymgi Schritt 1, dann Schritt 2
        if gymgi.bildname == "GymgiSchrittLinks1.gif":
            gymgi.bildname = "GymgiSchrittLinks2.gif"

        # Wenn Gymgi Schritt 2, dann Schritt 1
        elif gymgi.bildname == "GymgiSchrittLinks2.gif":
            gymgi.bildname = "GymgiSchrittLinks1.gif"

        # sonst
        else:
            gymgi.bildname = "GymgiSchrittLinks1.gif"

        # Merken, dass Schritt gelaufen
        gymgi.istSchrittGelaufen = True
        
    # Wenn nach oben gedrückt, bewege Gymgi nach hinten
    if spielfeld.obenGedrückt and darfNachHinten( gymgi ):
        
        # Gymgis Position nach hinten begrenzen
        if gymgi.positionZ + 10 <= 400:
            gymgi.positionZ = gymgi.positionZ + 10

        # Wenn Gymgi noch keinen Schritt gelaufen ist in diesem Schleifendurchgang
        if not gymgi.istSchrittGelaufen:

            if gymgi.richtungX == 1:
                
                # Wenn Gymgi Schritt 1, dann Schritt 2
                if gymgi.bildname == "GymgiSchritt1.gif":
                    gymgi.bildname = "GymgiSchritt2.gif"

                # Wenn Gymgi Schritt 2, dann Schritt 1
                elif gymgi.bildname == "GymgiSchritt2.gif":
                    gymgi.bildname = "GymgiSchritt1.gif"

                # sonst
                else:
                    gymgi.bildname = "GymgiSchritt1.gif"
                    
            elif gymgi.richtungX == -1:
                
                # Wenn Gymgi Schritt 1, dann Schritt 2
                if gymgi.bildname == "GymgiSchrittLinks1.gif":
                    gymgi.bildname = "GymgiSchrittLinks2.gif"

                # Wenn Gymgi Schritt 2, dann Schritt 1
                elif gymgi.bildname == "GymgiSchrittLinks2.gif":
                    gymgi.bildname = "GymgiSchrittLinks1.gif"

                # sonst
                else:
                    gymgi.bildname = "GymgiSchrittLinks1.gif"

    # sonst wenn nach unten gedrückt, bewege Gymgi nach vorne
    elif spielfeld.untenGedrückt and darfNachVorne( gymgi ):

        # Gymgis Position nach vorne begrenzen
        if gymgi.positionZ - 10 >= 0:
            gymgi.positionZ = gymgi.positionZ - 10

        # Wenn Gymgi noch keinen Schritt gelaufen ist in diesem Schleifendurchgang
        if not gymgi.istSchrittGelaufen:

            if gymgi.richtungX == 1:
                
                # Wenn Gymgi Schritt 1, dann Schritt 2
                if gymgi.bildname == "GymgiSchritt1.gif":
                    gymgi.bildname = "GymgiSchritt2.gif"

                # Wenn Gymgi Schritt 2, dann Schritt 1
                elif gymgi.bildname == "GymgiSchritt2.gif":
                    gymgi.bildname = "GymgiSchritt1.gif"

                # sonst
                else:
                    gymgi.bildname = "GymgiSchritt1.gif"
                    
            elif gymgi.richtungX == -1:
                
                # Wenn Gymgi Schritt 1, dann Schritt 2
                if gymgi.bildname == "GymgiSchrittLinks1.gif":
                    gymgi.bildname = "GymgiSchrittLinks2.gif"

                # Wenn Gymgi Schritt 2, dann Schritt 1
                elif gymgi.bildname == "GymgiSchrittLinks2.gif":
                    gymgi.bildname = "GymgiSchrittLinks1.gif"

                # sonst
                else:
                    gymgi.bildname = "GymgiSchrittLinks1.gif"

    # Wenn Leertaste gedrückt und noch nicht maximale Sprunghöhe erreicht, lasse Gymgi springen
    if spielfeld.tasteGedrückt == " " and gymgi.sprungZähler < 8:
        gymgi.positionY = gymgi.positionY - 20

        # Sprungzähler hochzählen
        gymgi.sprungZähler = gymgi.sprungZähler + 1

        # Entsprechend der Richtung, springen Bild anzeigen
        if gymgi.richtungX > 0:
            gymgi.bildname = "GymgiSpringen.gif"
        else:
            gymgi.bildname = "GymgiSpringenLinks.gif"

    # sonst wenn Leertaste gedrückt und sonst nichts anderes gedrückt wird
    elif spielfeld.tasteGedrückt == " " and not spielfeld.linksGedrückt and not spielfeld.rechtsGedrückt and not spielfeld.obenGedrückt and not spielfeld.untenGedrückt:
        
        # Entsprechend der Richtung, stehen Bild anzeigen
        if gymgi.richtungX > 0:
            gymgi.bildname = "GymgiStehen.gif"
        else:
            gymgi.bildname = "GymgiStehenLinks.gif"

    # Wenn während des Sprungs irgendwo mit dem Kopf angeeckt
    if spielfeld.tasteGedrückt == " " and not darfSpringen( gymgi ):
        gymgi.sprungZähler = 8

    # Wenn nicht Leertaste gedrückt und noch in der Luft, Sprungzähler auf Maximum setzen
    if not spielfeld.tasteGedrückt == " " and gymgi.sprungZähler > 0:
        gymgi.sprungZähler = 8

    # Wenn nichts gedrückt
    if not spielfeld.linksGedrückt and not spielfeld.rechtsGedrückt and not spielfeld.obenGedrückt and not spielfeld.untenGedrückt and not spielfeld.tasteGedrückt == " ":

        # Entsprechend der Richtung, stehen Bild anzeigen
        if gymgi.richtungX > 0:
            gymgi.bildname = "GymgiStehen.gif"
        else:
            gymgi.bildname = "GymgiStehenLinks.gif"

    # Schwerkraft (wenn Gymgi nicht auf einer Plattform steht)
    if not schwerkraftBerechnen( gymgi ):
        gymgi.sprungZähler = 0

    # ...sonst wenn Gymgi irgendwo heruntergefallen ist (Sprungzähler auf 8 setzen - wie wenn maximale Sprunghöhe erreicht)
    elif not spielfeld.tasteGedrückt == " ":
        gymgi.sprungZähler = 8


    #
    # Gegner berechnen
    #
    
    if not gegner1.text == "100 Punkte":

        # Gegner 1 bewegen und animieren
        gegner1.positionX = gegner1.positionX + 5 * gegner1.richtungX
        if( gegner1.bildname == "kokosnuss1.gif" ):
            gegner1.bildname = "kokosnuss2.gif"
        else:
            gegner1.bildname = "kokosnuss1.gif"

        # Schwerkraft für Gegner 1 berechnen
        schwerkraftBerechnen( gegner1 )

    else:

        # Gegner 1 getroffen => fällt nach unten!
        gegner1.positionY = gegner1.positionY + 10

    # Auf Gegner draufspringen
    if gymgi.berührt( gegner1 ) and gymgi.positionY + gymgi.höhe <= gegner1.positionY + 20:
        gegner1.text = "100 Punkte"
        gegner1.positionY = gegner1.positionY + 10
        gymgi.positionY = gymgi.positionY - 20
        punkte = punkte + 100

    # Ein Leben verlieren
    if gymgi.positionY > spielfeld.höhe or \
       gymgi.berührt( gegner1 ):

        # Gymgi unsichtbar machen
        gymgi.unsichtbar = True

        # Spielfeld aktualisieren
        spielfeld.zeichnen()

        # Etwas warten
        spielfeld.warten( 20 )

        # Gymgi wieder sichtbar machen
        gymgi.unsichtbar = False

        # Leben runterzählen
        leben = leben - 1

        # Gymgi auf Anfang zurücksetzen
        gymgi.bildname = "GymgiStehen.gif"
        gymgi.positionX = 10
        gymgi.positionY = 401
        gymgi.positionZ = 10
        gymgi.richtungX = 1

        # ALLE Gegner auf Anfang zurücksetzen
        gegner1.positionX = 700
        gegner1.positionY = 71
        gegner1.positionZ = 100
        gegner1.text = ""
        gegner1.richtungX = -1

    # Lebenanzeige aktualisieren
    lebenAnzeige.text = "Leben: " + str( leben )

    # Punkteanzeige aktualisieren
    punkteAnzeige.text = "Punkte: " + str( punkte )

    # Spielfeld zeichnen
    spielfeld.zeichnen()

    # Etwas warten
    spielfeld.warten( 30 )


#
# Level geschafft
#

# Gymgi unsichtbar machen
gymgi.unsichtbar = True

# Spielfeld nochmal zeichnen
spielfeld.zeichnen()
