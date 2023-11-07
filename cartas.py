
def createCard():
    cardName = input("Introduce el nombre de la carta")
    cardClass = input("Introduce la clase de la carta a traves de un numero. Las opciones son: 1.Attack 2.Shield 3.Healing 4.States 5.Minion 6.Mixed")
    cardMana = input("Introduce el coste de mana de la carta")
    if cardClass == 1:
        print("Has creado una carta de ataque")
        cardDamage = input("Introduce el valor del daño de la carta")
    if cardClass== 2: 
        print ("Has creado una carta de escudo")
        cardShield = input("Introduce el valor de escudo de la carta")
    if  cardClass == 3:
        print("Has creado una carta de curacion")
        cardHealing = input("Introduce el valor de curacion de la carta")
    if cardClass == 4:
        print("Has creado una carta de estado")
        cardState = input("Introduce el estado que provoca a traves de un numero: 1.Strength 2.Protect 3.Zap 4.Taunt 5.Sleep 6.Poison")
        if cardState == 1:
            cardStateEnum = "Strength"
        if cardState == 2:
            cardStateEnum = "Protect"
        if cardState == 3:
            cardStateEnum = "Zap"
        if cardState == 4:
            cardStateEnum = "Taunt"
        if cardState == 5:
            cardStateEnum = "Sleep"
        if cardState == 6:
            cardStateEnum = "Poison"
    if cardClass == 5:
        print("Has creado una carta de subdito")
        cardMinionLife = input("Introduce el valor de la vida del minion")
    if cardClass == 6:
        print("Has creado una carta mixta")
        correctClass = False
        while (correctClass!= True):
            class1=input("Introduce el primer tipo de clase de la carta mixta a traves de un numero. \n Las opciones son: 1.Attack 2.Shield 3.Healing 4.States 5.Minion")
            class2=input("Introduce el segundo tipo de clase de la carta mixta a traves de un numero. \n Las opciones son: 1.Attack 2.Shield 3.Healing 4.States 5.Minion")
            try:
               c1 = int(class1)
               c2 = int(class2)
               if c1 != c2 and c1 < 6 and c1 > 0 and c2 < 6 and c2 > 0:
                   correctClass = True
            except:
                print("Vuelve a repetir el input de clases")
            if c1==1:
                print("La primera clase de la carta es de daño")
                confbool1=False
                while(confbool1==False): 
                    cardDamage = input("Introduce el valor del daño de la carta")
                    try:
                        i = int(cardDamage)
                        if i>0:
                            confbool1 = True
                    except:
                        print("Ese valor no es correcto")
            if c1==2:
                print("La primera clase de la carta es de escudo")
                confbool1=False
                while(confbool1==False): 
                    cardShield = input("Introduce el valor del escudo de la carta")
                    try:
                        i = int(cardShield)
                        if i>0:
                            confbool1 = True
                    except:
                        print("Ese valor no es correcto")
            if c1==3:
                print("La primera clase de la carta es de curacion")
                confbool1=False
                while(confbool1==False): 
                    cardHealing = input("Introduce el valor de curacion de la carta")
                    try:
                        i = int(cardHealing)
                        if i>0:
                            confbool1 = True
                    except:
                        print("No es un valor valido")
                print(cardHealing)
            if c1==4:
                print("La primera clase de la carta es de estado")
                while True:
                    cardState = input("Introduce el estado que provoca a traves de un numero: 1.Strength 2.Protect 3.Zap 4.Taunt 5.Sleep 6.Poison") 
                    try:
                        i = int(cardState)
                        if i>0 and i<7:
                            break
                    except: print("No es un valor valido")
                       
                if cardState == 1:
                    cardStateEnum = "Strength"
                if cardState == 2:
                    cardStateEnum = "Protect"
                if cardState == 3:
                    cardStateEnum = "Zap"
                if cardState == 4:
                    cardStateEnum = "Taunt"
                if cardState == 5:
                    cardStateEnum = "Sleep"
                if cardState == 6:
                    cardStateEnum = "Poison"
                print (cardStateEnum)
            if c1==5:
                print("La primera clase de la carta es de minion")
                confbool1=False
                while(confbool1==False): 
                    cardMinionLife = input("Introduce el valor de la vida del minion")
                    try:
                        i = int(cardMinionLife)
                        if i>0:
                            confbool1 = True
                    except:
                        print("Ese valor no es correcto")
            if c2==1:
                print("La segunda clase de la carta es de daño")
                cardDamage = input("Introduce el valor del daño de la carta")

            if c2==2:
                print("La segunda clase de la carta es de escudo")
                cardShield = input("Introduce el valor del escudo de la carta")

            if c2==3:
                print("La segunda clase de la carta es de curacion")
                cardHealing = input("Introduce el valor de curacion de la carta")
            if c2==4:
                print("La segunda clase de la carta es de estado")
            if c2==5:
                print("La segunda clase de la carta es de minion")
                cardMinionLife = input("Introduce el valor de la vida del minion")
           
    
    cardSprite = input("Introduce el id de la carta")
    cardDescription = input("Introduce la descripcion de la carta")
    cardShortPhrase = input("Introduce la frase corta de la carta ")
    cardDeckID = input("Introduce el id de las barajas a las que pertenezca la carta")


    return None

def createDeck():
    return None

def createUser():
    return None

def createCharacter():
    return None


menu = input
menuelection= int(menu)
if menuelection == 1:
    createCard()
if menuelection == 2:
    createDeck()
if menuelection == 3:
    createUser()
if menuelection == 4:
    createCharacter()

