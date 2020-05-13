####################################################
#   Part 0: Character Creation Screen
#   Author: Nichole Wong
####################################################
init python:

    class Vampy:
        def __init__(self):
            self.name = "Vampy"
            self.color = "#ad0c00"
            self.dir = "images/Vampy/"
            
        def getPart(self, part, index):
            return self.dir + part + str(index) + ".png"
            
    v = Vampy()
    hair, shirt, jeans, eyes, accessory = 0, 0, 0, 0, 0
    maxHairs, maxShirts, maxJeans, maxEyes, maxAccessories = 2, 3, 2, 6, 2

    def changeHair(direction):
        global hair
        hair += direction 
        if hair > maxHairs - 1: hair = 0
        if hair < 0: hair = maxHairs - 1
        
    def changeEyes(direction):
        global eyes
        eyes += direction 
        if eyes > maxEyes - 1: eyes = 0
        if eyes < 0: eyes = maxEyes - 1
        
    def changeShirt(direction):
        global shirt
        shirt += direction
        if shirt > maxShirts - 1: shirt = 0
        if shirt < 0: maxShirts - 1
        
    def changeJeans(direction):
        global jeans
        jeans += direction 
        if jeans > maxJeans - 1: jeans = 0
        if jeans < 0: maxJeans - 1
        
    def changeAccessory(direction):
        global accessory
        accessory += direction
        if accessory > maxAccessories - 1: accessory = 0
        if accessory < 0: maxAccessories - 1
        
####################################################
#   Set up Vampy's sprite
####################################################

layeredimage VampySprite:
    always v.dir + "VampyBase.png"
   
    if hair == 0:
        v.getPart("Hair", 1)
    elif hair == 1:
        v.getPart("Hair", 2)
        
    if eyes == 0:
        v.getPart("Eyes", 1)
    elif eyes == 1:
        v.getPart("Eyes", 2)
    elif eyes == 2:
        v.getPart("Eyes", 3)
    elif eyes == 3: 
        v.getPart("Eyes", 4)
    elif eyes == 4:
        v.getPart("Eyes", 5)
    elif eyes == 5:
        v.getPart("Eyes", 6)
        
    if jeans == 0:
        v.getPart("Jeans", 1)
    elif jeans == 1:
        v.getPart("Jeans", 2)
        
    if shirt == 0:
        v.getPart("Shirt", 1)
    elif shirt == 1:
        v.getPart("Shirt", 2)
    elif shirt == 2:
        v.getPart("Shirt", 3)
       
    if accessory == 0:
        v.getPart("Accessory", 1)
    elif accessory == 1:
        v.getPart("Accessory", 2)
        
####################################################
#   Part 0: Character Creation Screen
####################################################
   
screen customization():
    hbox:
        yalign .5
        xalign .5
        spacing 100
        
    vbox:
        text "Hair"
        hbox:
            textbutton "<" action Function(changeHair, -1)
            textbutton ">" action Function(changeHair, 1)
                    
        text "Shirt"
        hbox:
            textbutton "<" action Function(changeShirt, -1)
            textbutton ">" action Function(changeShirt, 1)
            
        text "Jeans"
        hbox:
            textbutton "<" action Function(changeJeans, -1)
            textbutton ">" action Function(changeJeans, 1)
        
        text "Eyes"
        hbox:
            textbutton "<" action Function(changeEyes, -1)
            textbutton ">" action Function(changeEyes, 1)
            
        text "Accessory"
        hbox:
            textbutton "<" action Function(changeAccessory, -1)
            textbutton ">" action Function(changeAccessory, 1)
            
        textbutton "Done" action Return()
        
    add "VampySprite" at center