# Beyond Death
# Faction Update
import random
import math
import time
import os
alive=1
world=[]
items = ["Brick","Radio","Vollyball","Crown","Fried Chicken","Apple Pie","HAPPY HAPPY HAPPY","Eye","Dress","T-Shirt","Human Leg","Wing","Stuff","Nonononononono","HUNGER","Missle","Arrow","Bullet","Pistol","Bow","Apple","Wasp","Bee","Tree","Mountain","IM NOT INSANE","NOT INSANE","NO INSANITY HERE","Computer","Sandwhich","Glass of Water","Milk Pitcher","Burger","Cheeseburger","Cannon","Army","Sanity","HELLO!","Friend","Winston","HAHAHAHA","FUNFUNFUN","?","Unknown","Wheel","Castle","Wall","Iron Bar","Buttlerfly","Unicorn","Pickle","Map","Iron Axe","Makeshift Axe","Makeshift Spear","Trash Can","Apples","Fire","Open Wound","Fire Bottle","Empty Bottle","curse of curses","curse of slowness","curse of blindness","curse of hunger","curse of thirst","curse of bloodloss","Dark Shard","Scar","Food","Water","Bandage","Venom","Infection","Map","Paper Towel","Disinfectant","Paper","Death Amulet","Spoon","Spork","Football","Soccerball","Baseball","Flail","Knife","Gold","Ore","Stick","Wood","Stone","Hide","Leather","Tenticle"]
possibleshop=[["Pistol",1,20],["Bullet",32,5],["Wooden Armor",1,20],["Knight Armor",1,50],["Chainmail Armor",1,30],["Fishing Rod",1,10],["Makeshift Spear",1,10],["Makeshift Axe",1,10],["Map",2,15],["Chain",3,15],["Trap",3,10],["Flail",1,15],["Iron Spear",1,15],["Iron Sword",2,15],["Loot Kit",1,30],["Blood Syringe",1,15],["Food",30,7],["Water",30,7],["Grass",100,1],["Leaf",100,1],["Stone",20,1],["Stick",20,1],["Fur",10,2],["Hide",10,2],["Raw Food",20,2],["Bandage",3,5],["Iron Bar",3,35],["Ore",10,5],["Arrow",64,2],["Bow",1,5],["Wood",13,5],["Basket",1,30],["Tinder",100,1],["Cloth",100,2]]
shop = []
inventory=[["Blood",100],["Hands",2],["Water",100],["Food",100],["Note",1]]
height = 25
width = 75
x=0
y=0
shopfeel=0
totalhours = 0
modifier = 5
startup = False
def sleep(seconds):
    startTime=time.time()
    while(time.time() < startTime+seconds):
        pyhtongeneralyrequiressomethingstupidheretojustifythewhileloop=1
def valid(String):
    item=String
    invalid=-1
    while(invalid==1 or invalid==-1):
        invalid=0
        if(len(item)==0):
            invalid=1
        else:
            valid="0123456789"
            c=0
            for a in range(len(item)):
                for b in range(len(valid)):
                    if(item[a]==valid[b]):
                        c=c+1
            if(c!=len(item)):
                invalid=1
            else:
                if(item=="0"):
                    invalid=1
        if(invalid==1 or invalid==-1):
            print("That is not valid")
            item=input()
    return item
def variableify(string):
    string=string.replace(" ", "")
    return(string.upper())
def loadsave():
    print("Loading")
    if(os.path.isfile('./save.txt')):
        print("Begining Load...")
        f=open("save.txt", "r", encoding="utf-8")
        savedata=str(f.read())
    ##      savedata=input()
        print("Importing data...")
        savedata=savedata[savedata.find("_SV_")+4 : savedata.rfind("_SV_")]
        modifier=float(savedata[0:savedata.find("_SV_")])
        savedata=savedata[savedata.find("_SV_")+4 : len(savedata)]
        x=int(savedata[0:savedata.find("_SV_")])
        savedata=savedata[savedata.find("_SV_")+4 : len(savedata)]
        y=int(savedata[0:savedata.find("_SV_")])
        savedata=savedata[savedata.find("_SV_")+4 : len(savedata)]
        totalhours=int(savedata[0:savedata.find("_SV_")])
        savedata=savedata[savedata.find("_SV_")+4 : len(savedata)]
        shopfeel=int(savedata[0:savedata.find("_SV_")])
        savedata=savedata[savedata.find("_SV_")+4 : len(savedata)]
        exec("shop="+savedata[0:savedata.find("_SV_")], globals())
        savedata=savedata[savedata.find("_SV_")+4 : len(savedata)]
        exec("possibleshop="+savedata[0:savedata.find("_SV_")], globals())
        savedata=savedata[savedata.find("_SV_")+4 : len(savedata)]
        exec("world="+savedata[0:savedata.find("_SV_")], globals())
        savedata=savedata[savedata.find("_SV_")+4 : len(savedata)]
        exec("inventory="+savedata, globals())
        print("Load completed")
        return True
    else:
        print("No save found")
        return False
if(os.path.isfile('./save.txt')):
    print("Do you want to continue from the save?(Y/N)")
    doload = variableify(input())
    if(len(doload) > 0 and doload[0] == "Y"):
        print("Startup Loading...")
        loadsave()
    else:
        startup = True
else:
    startup = True
if(startup):
    print("-What difficulty do you want?-")
    print()
    print("1: Stupidly Easy")
    print("2: Exploration")
    print("3: Very Easy")
    print("4: Easy")
    print("5: Normal")
    print("6: Hard")
    print("7: Extreme")
    print("8: Master")
    print("9: Insane")
    print("10+ Impossible")
    modifier=float(valid(input()))
    print("Do you need a tutorial?")
    tutorial = input("(Y/N): ")
    if(len(variableify(tutorial)) > 0 and variableify(tutorial)[0] == "Y"):
        print("Welcome to the tutorial!")
        print("Type anything!")
        input("I ")
        print("That is how you interact with the world, typing! Type some!")
        input("I ")
        print("Now say 'I look'")
        while(input("I ") != "look"):
            print("try again, it should look exactly like this:")
            print("I look")
        print("+---+")
        print("+@T +")
        print("+w  +")
        print("+Ww +")
        print("+---+")
        print("This is the map")
        print("You are the @ symbol in the top left")
        print("We will learn the rest of the symbols in a moment")
        print("Type 'I observe'")
        while(input("I ") != "observe"):
            print("try again, it should look exactly like this:")
            print("I observe")
        print("You are around an empty area")
        print("That message was created by the game")
        print("Now you know that the area around you is empty and barren")
        print()
        print("The map before is full of symbols")
        print("If you want to know what a tile is, you can say 'inspect', do it now")
        while(input("I ") != "inspect"):
            print("try again, it should look exactly like this:")
            print("I inspect")
        print("Which Direction(North, East, South or West) or say nvm to exit")
        print("That message was created by the game, it wants to know which direction you want to know more about")
        print("The game uses a compass based direction system")
        print()
        print("     N     ")
        print("     |     ")
        print("   W-+-E   ")
        print("     |     ")
        print("     S     ")
        print()
        print("We want to look at the 'T'")
        print("The 'T' is to the east of the player")
        print("Lets say 'East' to indicate that we want to look to the east")
        while(input("I look to the ") != "East"):
            print("try again, it should look exactly like this:")
            print("I look to the East")
        print("Directly east of you is a large forest")
        print("Now you know that the 'T' symbol represents a large forest. ")
        print("Here are some basics: Forests are represented by the letter 't'(Capital for large forests), Shallow water is '~', deeper water is 'W' ")
        print("")
        print("This game is all about survival, understand?")
        input()
        print("In order to survive you have to hunt, forage, etc.")
        print("Foraging and hunting are more effective in forests")
        print("So you should move to the forests")
        print("So say 'I move' to move")
        while(input("I ") != "move"):
            print("try again, it should look exactly like this:")
            print("I move")
        print("Which Direction(North, East, South or West) or say nvm to exit")
        print("That message was created by the game. It wants to know which direction you want to move")
        print("Lets say 'East' to indicate that we want to go east")
        while(input("I move to the ") != "East"):
            print("try again, it should look exactly like this:")
            print("I move to the East")
        print("Outside of the tutorial, Most systems in the game are not case sensitive and ignore spaces")
        print("Some prompts(Like yes/no or direction prompts) only even check the first letter")
        print("")
        print("Anyway, now we have moved to the east")
        print("The screen above hasn't changed")
        print("This is because the game never changes what is written")
        print("To update the map, we need to again say 'look'")
        while(input("I ") != "look"):
            print("try again, it should look exactly like this:")
            print("I look")
        print("+---+")
        print("+t@ +")
        print("+~  +")
        print("+W~ +")
        print("+---+")
        print()
        print("The @ moved to the east, just as we commanded it")
        print("The @ covers whatever tile its on, so we have to use the observe command to see what tile we are on")
        print("Type 'I observe'")
        while(input("I ") != "observe"):
            print("try again, it should look exactly like this:")
            print("I observe")
        print("you are around a large forest")
        print()
        print("Before we continue, we should take inventory of what we have")
        print("To do this, type 'I inventory'")
        print("This doesn't make sense but the developer doesn't care")
        while(input("I ") != "inventory"):
            print("try again, it should look exactly like this:")
            print("I inventory")
        print()
        print("This is what you have:")
        print()
        print("Blood x100")
        print("Hands x2")
        print("Water x200")
        print("Food x200")
        print()
        print("This shows your inventory, You need food blood and water to survive, Coins are the primary currency, loot kits give you free stuff, and your hands are your, well, hands")
        print()
        print("Now that we are around some forests and know what we have, We should do some harvesting!")
        print("Type 'I use' to show that you want to use an item")
        while(input("I ") != "use"):
            print("try again, it should look exactly like this:")
            print("I use")
        print("")
        print("What do you want to use(type ? if you don't know or type nvm to cancel)")
        print("")
        print("You want to use your hands, so type 'I use my hands'")
        while(input("I use my ") != "hands"):
            print("try again, it should look exactly like this:")
            print("I use my hands")
        print("You use your hands around a large forest")
        print("You get 2x Leaf")
        print("You get 2x Flower")
        print()
        print("Oh boy! Leaves!")
        print("Okay, not so exiting")
        print("But they can be crafted together!")
        print("type 'I craft' to start crafting")
        while(input("I ") != "craft"):
            print("try again, it should look exactly like this:")
            print("I craft")
        print("")
        print("Remember, we want to craft a 'Leaf' and a 'Flower'")
        print("You sit down to build")
        while(input("Item 1: ") != "Leaf"):
            print("try again, it should look exactly like this:")
            print("Item 1: Leaf")
        while(input("Item 2: ") != "Flower"):
            print("try again, it should look exactly like this:")
            print("Item 2: Flower")
        print("It will take one Flower and one Leaf and will produce one Bandage")
        print("You feel like you can")
        print()
        print("That what we want to craft, so type 'Yes'")
        while(input("(Y/N): ") != "Yes"):
            print("try again, it should look exactly like this:")
            print("(Y/N): Yes")
        print("It is crafted!")
        print()
        print("Now you have a bandage! Just like we used our hands, you can use a bandage. This will close a wound")
        print("When you move, time passes, when time passes food and water are consumed, and there is a chance that you are wounded")
        print()
        print("There are many crafting recipies, some crafting recipies fail.")
        print("When it fails, the materials are consumed but nothing is made")
        print("Thus ends the tutorial")
        print("The Game has many things not covered in the tutorial")
        print("Hunting, Fishing, Combat, Magic, Xp, Levling, Factions, and most everything else")
        print("Don't worry: discovery(and dying over and over again) is fun")
        print("Are you ready?")
        input()
        print("I don't care, Begin!")
    print()
    print("Hey, It's me, the Grim Reaper,")
    print("Keep in mind, I cannot hear you")
    print("I am in some trouble")
    print("The devil kinda, well. Ended the world")
    print("And the devil is now trying to destroy me")
    print("Could you do me a favor and, Defeat the devil")
    print("Again, I can't hear you, so this is not optional")
    print("I don't actualy have enough magic to create stuff for you,")
    print("Creating you kinda exausted me,")
    print("So, good luck! Try not to die")
    print()
    print()
    redraworld()
    for i in range(len(possibleshop)):
        possibleshop[i][2]=round(((modifier/2)*possibleshop[i][2]))
        if(possibleshop[i][2] <= 0):
            possibleshop[i][2]=1
def GoFish():
    print("You Go fish")
    print("Hit enter, Wait 8 secounds, then hit enter. The closer you get the more food")
    input()
    starttime=time.time()
    input()
    endtime=time.time()
    if(int(10-(modifier*abs(8-round(endtime-starttime)))) < 1):
      addstuff("Raw Food",1)
      print("You get 1 Raw Food!")
    else:
      addstuff("Raw Food",int(10-(modifier*abs(8-round(endtime-starttime)))))
      print("You get "+int_to_en(int(10-(modifier*abs(8-round(endtime-starttime)))))+" Raw Food!")
    if(random.random()>modifier*0.1*(abs(8-round(endtime-starttime)))):
        defaultlootable(1)
def tictac(ai):
    winner="I"
    gameover=0
    start=0
    while(start==0 or (int(ai)>=3 and gameover==0)):
        array=["+","+","+","+","+","+","+","+","+"]
        turn=1
        start=1
        import random
        import math
        def Wincheck(le):
            return (
            (array[6] == le and array[7] == le and array[8] == le) or
            (array[3] == le and array[4] == le and array[5] == le) or
            (array[0] == le and array[1] == le and array[2] == le) or
            (array[6] == le and array[3] == le and array[0] == le) or
            (array[7] == le and array[4] == le and array[1] == le) or
            (array[8] == le and array[5] == le and array[2] == le) or
            (array[6] == le and array[4] == le and array[2] == le) or
            (array[8] == le and array[4] == le and array[0] == le)
            )
        def Nearwincheck(le):
            if(array[6] == "+" and array[7] == le and array[8] == le):
                return(6)
            if(array[3] == "+" and array[4] == le and array[5] == le):
                return(3)
            if(array[0] == "+" and array[1] == le and array[2] == le):
                return(0)
            if(array[6] == "+" and array[3] == le and array[0] == le):
                return(6)
            if(array[7] == "+" and array[4] == le and array[1] == le):
                return(7)
            if(array[8] == "+" and array[5] == le and array[2] == le):
                return(8)
            if(array[6] == "+" and array[4] == le and array[2] == le):
                return(6)
            if(array[8] == "+" and array[4] == le and array[0] == le):
                return(8)
            if(array[6] == le and array[7] == "+" and array[8] == le):
                return(7)
            if(array[3] == le and array[4] == "+" and array[5] == le):
                return(4)
            if(array[0] == le and array[1] == "+" and array[2] == le):
                return(1)
            if(array[6] == le and array[3] == "+" and array[0] == le):
                return(3)
            if(array[7] == le and array[4] == "+" and array[1] == le):
                return(4)
            if(array[8] == le and array[5] == "+" and array[2] == le):
                return(5)
            if(array[6] == le and array[4] == "+" and array[2] == le):
                return(4)
            if(array[8] == le and array[4] == "+" and array[0] == le):
                return(4)
            if(array[6] == le and array[7] == le and array[8] == "+"):
                return(8)
            if(array[3] == le and array[4] == le and array[5] == "+"):
                return(5)
            if(array[0] == le and array[1] == le and array[2] == "+"):
                return(2)
            if(array[6] == le and array[3] == le and array[0] == "+"):
                return(0)
            if(array[7] == le and array[4] == le and array[1] == "+"):
                return(1)
            if(array[8] == le and array[5] == le and array[2] == "+"):
                return(2)
            if(array[6] == le and array[4] == le and array[2] == "+"):
                return(2)
            if(array[8] == le and array[4] == le and array[0] == "+"):
                return(0)
            return(-1)
        while(gameover==0 and (array[0]=="+" or array[1]=="+" or array[2]=="+" or array[3]=="+" or array[4]=="+" or array[5]=="+" or array[6]=="+" or array[7]=="+" or array[8]=="+")):
            print("+---+")
            print("|"+array[2]+array[5]+array[8]+"|")
            print("|"+array[1]+array[4]+array[7]+"|")
            print("|"+array[0]+array[3]+array[6]+"|")
            print("+---+")
            if(turn==1):
                print("X, make your turn!")
                if(int(ai)>=2):
                    move=Nearwincheck("X")
                    if(move==-1):
                        move=Nearwincheck("O")
                        if(move==-1):
                            move=random.randint(0,8)
                    while(array[move]!="+"):
                        move=Nearwincheck("X")
                        if(move==-1):
                            move=Nearwincheck("O")
                            if(move==-1):
                                move=random.randint(0,8)
                    array[move]="X"
                    turn = turn*-1
                else:
                    location=str(input())
                    while(location == "No" or location == "no" or len(location)!=2 or int(location[0])>3 or int(location[1])>3 or int(location[0])<1 or int(location[1])<1):
                        print("That is invalid")
                        print("Put in 2 integer coodinates between 1 and 3")
                        print("The first is the y, the 2nd is the x")
                        print("They are next to eachother, So the bottom center square would be 21")
                        location=str(input())
                    if(array[(int(location[0])-1)*3+(int(location[1])-1)]=="+"):
                        array[(int(location[0])-1)*3+(int(location[1])-1)]="X"
                        turn = turn*-1
                    else:
                        print("That spot is taken")
            else:
                print("O, make your turn!")
                if(ai!=0):
                    move=Nearwincheck("O")
                    if(move==-1):
                        move=Nearwincheck("X")
                        if(move==-1):
                            move=random.randint(0,8)
                    while(array[move]!="+"):
                        move=Nearwincheck("O")
                        if(move==-1):
                            move=Nearwincheck("X")
                            if(move==-1):
                                move=random.randint(0,8)
                    array[move]="O"
                    turn = turn*-1
                else:
                    location=str(input())
                    while(location == "No" or location == "no" or len(location)!=2 or int(location[0])>3 or int(location[1])>3 or int(location[0])<1 or int(location[1])<1):
                        print("That is invalid")
                        print("Put in 2 integer coodinates between 1 and 3")
                        print("The first is the y, the 2nd is the x")
                        print("They are next to eachother, So the bottom center square would be 21")
                        location=str(input())
                    if(array[(int(location[0])-1)*3+(int(location[1])-1)]=="+"):
                        array[(int(location[0])-1)*3+(int(location[1])-1)]="O"
                        turn = turn*-1
                    else:
                        print("That spot is taken")
            if(Wincheck("X")):
                print("X Wins!!")
                gameover=1
                winner="X"
            if(Wincheck("O")):
                print("O Wins!!")
                gameover=1
                winner="O"
        print("+---+")
        print("|"+array[2]+array[5]+array[8]+"|")
        print("|"+array[1]+array[4]+array[7]+"|")
        print("|"+array[0]+array[3]+array[6]+"|")
        print("+---+")
        print("Game end")
        if(winner=="O"):
            return(0)
        elif(winner=="X"):
            return(1)
        else:
            return(-1)
def finditem(item):
    getinvalid(inventory)
    for i in range(len(inventory)):
        if(variableify(inventory[i][0])==variableify(item)):
            return(i)
    return(-1)
def endgame():
    global alive
    if(entercombat("devil",1)):
        print("You defeat the devil,")
        print()
        print("You hear as the Grim reaper comes.")
        print("Thanks")
        print("The devil will come back. But now, he won't threaten me.")
        print("My sincerest congradulations")
        print("However, I have some bad news,")
        print("Just as ending the world ahead of shedule is against the rules")
        print("So is summoning people just to have them fight the devil")
        print("I am very sorry")
        print("But just as I gave you life, I must now take it away.")
        print("Do not be sad, You have won")
        print("You sucseeded in your goal, Boom! Purpose furtfilled")
        print("Come with me,")
        dodie=input("(Y/N):")
        if(len(variableify(dodie))>0 and variableify(dodie)[0] == "Y"):
            print("Goodbye")
            alive=0
        else:
            print("Very funny")
            print()
            print("Oh, You were serious")
            print("But, there is no point")
            print("Your life story is complete")
            print("You scratched off your bucket list")
            print("That is all there is to life")
            print("Yet still you wish to live,")
            print()
            print("Your life was one of hardship, loss, defeat and suffering")
            print("Yet you still wish to live?")
            print("Hmm, Interesting")
            print()
            print("If your life has value regardless of pain, regardless of having a goal")
            print("Then I shall return you to the world")
            print("With your return, the devil will return aswell")
            print("You can live, just like you did")
            print("Have fun")
    else:
        print("The devil laughs as he destroys your soul")
        inventory[finditem("Blood")][1] = 0
        deathcheck()
def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000
    q = t * 1000
    if (num < 0):
      return "negative "+int_to_en(-1*num)
    if (num < 20):
        return d[num]
    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]
    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)
    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' thousand'
        else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)
    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)
    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion, ' + int_to_en(num % b)
    if (num < q):
        if (num % t) == 0: return int_to_en(num // t) + ' trillion'
        else: return int_to_en(num // t) + ' trillion, ' + int_to_en(num % b)
    if (num % q == 0): return int_to_en(num // q) + ' quadrillion'
    else: return int_to_en(num // q) + ' quadrillion, ' + int_to_en(num % t)
def blocked(x1,y1):
    print("You are stopped by "+identify(world[x1][y1]))
def lootable(odds,itemname,mod):
    loot=random.random()
    lootincrease = 5
    if(finditem("Loot Boon")!=-1 and inventory[finditem("Loot Boon")][1]>0):
        lootincrease=lootincrease+inventory[finditem("Loot Boon")][1]
    if(loot<1-0.08**(odds*(lootincrease/modifier)) or odds == 1):
        getcount=1+round(mod*random.random()*(lootincrease/modifier))
        if((finditem("Insanity") != -1 and inventory[finditem("Insanity")][1]>0) and random.random()>1/(inventory[finditem("Insanity")][1] * 0.001 * modifier)):
            print("You get "+str(abs(inventory[finditem("Insanity")][1]*round((random.random()-0.5)*modifier)))+"x "+items[round(random.random()*(len(items)-1))])
        else:
            if(finditem("Insanity") != -1 and inventory[finditem("Insanity")][1]>0):
                print("You get "+str(abs(round(inventory[finditem("Insanity")][1]*0.1*(random.random()-0.5)*modifier)+int(getcount)))+"x "+itemname)
            else:
                print("You get "+str(getcount)+"x "+itemname)
        addstuff(itemname,getcount)
def getinventory():
    getinvalid(inventory)
    print("This is what you have:")
    print()
    if(finditem("Insanity") == -1):
        for i in range(len(inventory)):
            print(inventory[i][0]+" x"+str(int(inventory[i][1])))
    else:
        for i in range(len(inventory)):
            if(random.random()>inventory[finditem("Insanity")][1]*0.0005*modifier):
                print(inventory[i][0]+" x"+str(abs(round(inventory[finditem("Insanity")][1]*0.05*(random.random()-0.5)*modifier)+int(inventory[i][1]))))
            for i in range(round(inventory[finditem("Insanity")][1]*random.random()*(modifier/100))):
                print(items[round(random.random()*(len(items)-1))]+" x"+str(abs(round(inventory[finditem("Insanity")][1]*(random.random()-0.5)*modifier))))
def getinvalid(array):
    i=0
    while (i < len(array)):
        if(array[i][1]==0):
            del array[i]
        else:
            i+=1
def cancercheck():
  if(inventory[finditem("Cancer")][1] > 100-(modifier*1)):
    print("The cancer is incredibly close to killing you")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*2)):
    print("The cancer is close to killing you")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*3)):
    print("The cancer severly thretends your immediate survival")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*4)):
    print("The cancer threatends your immediate survival")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*5)):
    print("The cancer slightly threatends your immediate survival")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*6)):
    print("The cancer is beging to threaten your immediate survival")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*7)):
    print("The cancer is incredibly close to threatening your immediate survival")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*8)):
    print("The cancer is close to threatening your immediate survival")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*9)):
    print("The cancer is slightly close to threatening your immediate survival")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*10)):
    print("The cancer is growing incredibly large, Soon it will threaten your immediate survival")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*11)):
    print("The cancer is growing large, Soon it will threaten your immediate survival")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*12)):
    print("The cancer is almost growing large, Soon it will threaten your immediate survival")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*13)):
    print("The cancer is medium sized, holding no immidetly threat to your survival, but it could get worse fast")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*14)):
    print("The cancer is almost medium sized, holding no immidetly threat to your survival, but it could get worse fast")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*15)):
    print("The cancer is small sized, but it shows signs of getting bigger")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*16)):
    print("The cancer is very small sized, but it shows signs of getting bigger")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*17)):
    print("The cancer is tiny sized, but it shows signs of getting bigger")
  elif(inventory[finditem("Cancer")][1] > 100-(modifier*18)):
    print("The cancer is very tiny sized right now. However, there is always the chance it gets larger.")
  else:
    print("the cancer might not even exist right now it is so small, however cancer has a tendancy to grow fast. When it does, It will not be mercyfull")
def shopkeep():
    global shopfeel
    if(shopfeel*0.01<random.random()):
        getinvalid(shop)
        k = modifier
        if(modifier > 9):
            k = 9
        while(len(shop)<10-k):
            tryadd=int(random.random()*len(possibleshop))
            ifinditem=0
            for i in range(len(shop)):
                if(variableify(shop[i][0])==variableify(possibleshop[tryadd][0])):
                    ifinditem=1
            if(ifinditem==0):
                shop.append(possibleshop[tryadd])
                shop[len(shop)-1][1]-=round(random.random()*(shop[len(shop)-1][1]-1))
                shop[len(shop)-1][2]+=round((shopfeel/10)*random.random()*round(shop[len(shop)-1][2]/4))
        if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
            print("You feel a table, and hear the breath of something infront of you")
        else:
            print("+---------------------------------------+")
            print("+                 _           __        +")
            print("+  -+- 0         |_    o     | _        +")
            print("+   |  |\ /-\ \/ |_ |_ | |\| |__|       +")
            print("+            _                          +")
            print("+      |\/| |_ 0   _ |_         -+-     +")
            print("+      |  | |_ |\ |_ | | /-\ |\| |      +")
            print("+                                       +")
            print("+=======================================+")
            print("+    /\                                 +")
            print("+    ||          +---+       +-+-+      +")
            print("+    ||        __|___|__     | | |      +")
            print("+   -++-         |o o|       +-+-+      +")
            print("+   *||*         |_-_|       | | |      +")
            print("+                  |         +-+-+      +")
            print("+  +----+         /| \                  +")
            print("+  |LOOT|        |/| \|                 +")
            print("+=======================================+")
            print("+            -WALT'S SHOP-              +")
            print("+                                       +")
            print("+---------------------------------------+")
        print("\n"*2)
        print("Hello, Ready to shop?")
        if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
            print("HE IS NOT A HUMAN!")
            print("HE IS A "+items[int(round(random.random()*(len(items)-1)))])
            print("HE MUST DIE FOR HIS LIES!!!",end = "")
            for i in range(int(inventory[finditem("Insanity")][1]/10)):
                print("DIE!",end="")
            print()
            print("TELL HIM TO DIE!")
            print("SAY 'DIE' IT IS NOT HARD FOR A SANE PERSON LIKE YOU")
        response=input("")
        response=variableify(response)
        if(len(response)==0 or response[0]=="N"):
            print("Your loss")
        elif(response[0:3] == "DIE"):
            print("What did you say?")
            if(variableify(input())!=response):
                print("No, I remember you said '"+response+"'")
            print("Lets be reasonable people, turn around, leave, and I will forget this ever happened.")
            if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 15):
                print("NO! HE IS EVIL!")
                print("YOU DO NOT LEAVE")
                for i in range(int(inventory[finditem("Insanity")][1]/10)):
                    print("HE MUST DIE!")
            print("Do you leave?")
            flee=input("")
            flee=variableify(flee)
            if(len(flee)==0 or flee[0]=="Y"):
                if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 15):
                    print("NO! WHAT HAVE YOU DONE")
                    print("HE CANNOT BE ALLOWED TO LEAVE")
                    shopfeel+=10
                    for i in range(int(inventory[finditem("Insanity")][1]/10)):
                        print("FAILURE")
                else:
                    print("You apologise, and he leaves.")
                    shopfeel+=10
            else:
                print("You hear him draw a blade")
                if(entercombat("shopkeeper",0)):
                    print("Fine!")
                    print("He lays down his weapon")
                    demand = ""
                    while(len(demand) == 0):
                        print("Do you kill him?")
                        demand = variableify(input("(Y/N): "))
                    if(demand[0]=="Y"):
                        print("You finish him, You monster")
                        lootable(0.99,"Coin",1000)
                        for i in range(len(possibleshop)):
                            lootable(0.25,possibleshop[i][0],possibleshop[i][1])
                        for i in range(len(shop)):
                            addstuff(shop[i][0],shop[i][1])
                        shopfeel=100
                    else:
                        print("You lay down your weapon, and demand supplies")
                        lootable(0.75,"Coin",100)
                        for i in range(len(shop)):
                            lootable(0.25,shop[i][0],shop[i][1])
                        for i in range(len(possibleshop)):
                            lootable(0.05,possibleshop[i][0],possibleshop[i][1])
                        shopfeel=shopfeel+25
                else:
                    print("Good Riddance!")
        else:
            print("Imma gonna take that as a yes!")
            if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 10):
                print("DO NOT BUY ANYTHING")
                print("THEY ARE INFESTED WITH BAD")
            print("I have alot of high quality items, Here is a list")
            print()
            templen = 0
            print("|",end = "")
            for i in range(len(shop)):
                if(len(str(i+1)+") " + shop[i][0] + " x" + str(shop[i][1]) + " - " + str(shop[i][2]))>templen):
                    templen = len(str(i+1)+") " + shop[i][0] + " x" + str(shop[i][1]) + " - " + str(shop[i][2]))
            for i in range(templen):
                print("-",end = "")
            print(">")
            for i in range(len(shop)):
                print(str(i+1)+") " + shop[i][0] + " x" + str(shop[i][1]) + " - " + str(shop[i][2]))
            print("|",end = "")
            for i in range(templen):
                print("-",end = "")
            print(">")
            print()
            if(finditem("Coin")!=-1 or inventory[finditem("Coin")][1]==0):
                if(inventory[finditem("Coin")][1]==1):
                    print("You have a coin")
                else:
                    print("You have "+int_to_en(inventory[finditem("Coin")][1])+" coins")
            else:
                print("You don't have any coins. He probably won't mind")
            print("Which one do you want to buy? Or just say nvm if you don't want to buy anything")
            print("I will take item number: ",end = "")
            purchase = input()
            if(variableify(purchase)=="NVM"):
                print("Understandable. Come back some other time!")
            else:
                purchase = valid(purchase)
                purchase=int(purchase)-1
                while(purchase>len(shop)):
                    print("I don't have that many,")
                    purchase = input()
                    purchase = valid(purchase)
                    purchase=int(purchase)-1
                count=1
                print("A "+shop[purchase][0]+"! Great choice")
                if(shop[purchase][1]>1):
                    print("How many can I put you down for?")
                    print("I have " + int_to_en(shop[purchase][1]) + " in the back right now")
                    print("They cost " + int_to_en(shop[purchase][2]) + " a piece")
                    count=int(shop[purchase][1]+1)
                    while(count>shop[purchase][1] or count == -1):
                        count=input("I'll take ")
                        for i in range(len(count)):
                            if(count != "E"):
                                if(count[i] != "0" and count[i] != "1" and count[i] != "2" and count[i] != "3" and count[i] != "4" and count[i] != "5" and count[i] != "6" and count[i] != "7" and count[i] != "8" and count[i] != "9"):
                                    count = "E"
                        if(count[0] == "E"):
                            print("I don't understand")
                            count=-1
                        else:
                            count = int(count)
                        if(count>shop[purchase][1]):
                            print("I don't have that many")
                if(finditem("Coin")==-1):
                    print("We only accept coin here, Sorry")
                elif(shop[purchase][2]*count<=inventory[finditem("Coin")][1]):
                    print("Great! Just so you are certain you are getting:")
                    print(str(count)+"x "+str(shop[purchase][0]))
                    if(shop[purchase][2]*count == 1):
                        print("For " + int_to_en(shop[purchase][2]*count) + " coin")
                    else:
                        print("For " + int_to_en(shop[purchase][2]*count) + " coins")
                    print("Understand(Y/N):",end="")
                    understand=input()
                    while(len(understand)==0):
                        print("Understand(Y/N):",end="")
                        understand=input()
                    if(not(variableify(understand)[0]=="N")):
                        print("Fantastic!")
                        addstuff(shop[purchase][0],count)
                        inventory[finditem("Coin")][1]-=int(shop[purchase][2]*count)
                        if(shop[purchase][1]<count):
                            greatjob()
                        if(shopfeel > -1):
                            shopfeel-=1
                        shop[purchase][1]-=count
                    else:
                        print("Thats to bad, Come back another time!")
                else:
                    afford=inventory[finditem("Coin")][1]//shop[purchase][2]
                    print("You can't afford that, ")
                    if(afford==0):
                        print("In fact, You can't afford any! Get out of my shop and come back with more coins")
                    else:
                        print("You can only afford "+int_to_en(afford))
                if(random.random()*modifier<0.5):
                    if(random.random()<0.5):
                        print("Here, Have a cookie. I have to go but I hope you have a good day")
                        addstuff("Food",1)
                    else:
                        print("Here, Have a coin. I have to go but I hope you have a good day")
                        addstuff("Coin",1)
                else:
                    print("Sorry, I outta leave now.")
def craft(a,acount,b,bcount,c,count,f):
    if(not(finditem(a)==-1 or inventory[finditem(a)][1]<acount)):
        if(not(finditem(b)==-1 or inventory[finditem(b)][1]<bcount)):
            inventory[finditem(a)][1]-=acount
            inventory[finditem(b)][1]-=bcount
            if(random.random()>f):
                addstuff(c,count)
                print("It is crafted!")
            else:
                print("It failed to craft")
            return(1)
        else:
            print("You do not have enough "+b+". You need "+str(bcount))
    else:
        print("You do not have enough "+a+". You need "+str(acount))
    return(0)
def bloodloss(hours):
    if(finditem("curse of curses")!=-1 and inventory[finditem("curse of curses")][1]>=1):
        for i in range(hours * inventory[finditem("curse of curses")][1]):
            if(random.random()<0.001*modifier):
                curses=["curses","bloodloss","Insanity","wounds","haunting","slowness","hunger","thirst"]
                curse=round(random.random()*(len(curses)-1))
                print("Thanks to your curse of curses, you are cursed with "+curses[curse])
                addstuff("curse of "+curses[curse],1)
    if(finditem("curse of insanity")!=-1 and inventory[finditem("curse of insanity")][1]>=1):
        addstuff("Insanity",hours*modifier)
    if(world[x][y]=="?"):
        if((finditem("Insanity")==-1 or inventory[finditem("Insanity")][1]<=0) and modifier*0.1>random.random()):
            addstuff("Insanity",1)
            print("As you hang around the area, you begin to feel odd.")
            print("You feel as if your mind slips away into madness")
        elif(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>0):
            addstuff("Insanity",hours)
            print("HA"*hours)
    FoodModifier = 1
    WaterModifier = 1
    if(finditem("curse of hunger")!=-1 and inventory[finditem("curse of hunger")][1]>=1):
        FoodModifier=FoodModifier+inventory[finditem("curse of hunger")][1]
    if(finditem("curse of thirst")!=-1 and inventory[finditem("curse of thirst")][1]>=1):
        WaterModifier=WaterModifier+inventory[finditem("curse of thirst")][1]
    if(world[x][y] == "≈"):
        WaterModifier=WaterModifier+1
    if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
        WaterModifier=WaterModifier+inventory[finditem("Venom")][1]
        FoodModifier=FoodModifier+inventory[finditem("Venom")][1]
    if(finditem("Thirst Boon")!=-1 and inventory[finditem("Thirst Boon")][1] >= 1):
        WaterModifier=WaterModifier*math.pow(4/5,inventory[finditem("Thirst Boon")][1])
    if(finditem("Hunger Boon")!=-1 and inventory[finditem("Hunger Boon")][1] >= 1):
        FoodModifier=FoodModifier*math.pow(4/5,inventory[finditem("Hunger Boon")][1])
    inventory[finditem("Water")][1] = inventory[finditem("Water")][1] - ((1/10)*modifier*WaterModifier*hours)
    inventory[finditem("Food")][1] = inventory[finditem("Food")][1] - ((1/60)*modifier*FoodModifier*hours)        
    if(finditem("Infection")!=-1):
        infectcount = 0
        for i in range(int(hours * modifier * inventory[finditem("Infection")][1])):
            if(random.random()<0.01):
                infectcount=infectcount+1
        if(infectcount > 0):
            if(infectcount > 1):
                print("Your infection spreads "+int_to_en(infectcount)+" times")
            else:
                print("Your infection spreads")
            addstuff("Blood",-infectcount)
            addstuff("Infection",infectcount)
    if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1] >= 1):
        infectcount = 0
        for i in range(hours*inventory[finditem("Open Wound")][1]):
            if(random.random()<0.005*modifier):
                infectcount+=1
        addstuff("Infection",infectcount)
        addstuff("Blood",-infectcount)
        if(infectcount >= 1):
          print("Your wounds get infected "+int_to_en(infectcount)+" times")
        if(finditem("curse of bloodloss")==-1):
            inventory[finditem("Blood")][1] = inventory[finditem("Blood")][1] - (inventory[finditem("Open Wound")][1] * modifier * hours)
        else:
            inventory[finditem("Blood")][1] = inventory[finditem("Blood")][1] - (inventory[finditem("Open Wound")][1] * modifier * hours * ((inventory[finditem("curse of bloodloss")][1])))
    for i in range(hours):
        if((1-(1/(1+(1/2)*inventory[finditem("Regeneration Boon")][1]))>0) and finditem("Regeneration Boon")!=-1 and inventory[finditem("Regeneration Boon")][1]>=1 and finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1] >= 1):
            inventory[finditem("Open Wound")][1]-=1
        if(finditem("Blood Boon") != -1 and inventory[finditem("Blood Boon")][1] >= 1):
            if(finditem("Infection") != -1 and inventory[finditem("Infection")][1] >= 1):
              if(inventory[finditem("Blood")][1]<100-inventory[finditem("Infection")][1] and inventory[finditem("Blood")][1]<=100-inventory[finditem("Infection")][1]-(inventory[finditem("Blood Boon")][1])-round(10/modifier)):
                  inventory[finditem("Blood")][1]+=round(10/modifier)+(inventory[finditem("Blood Boon")][1])
              elif(inventory[finditem("Blood")][1]>110-inventory[finditem("Infection")][1]):
                  print("The amount of blood you have isn't healthy, you get a wound")
                  addstuff("Open Wound",math.floor((inventory[finditem("Blood")][1]-(100-inventory[finditem("Infection")][1]))/10))
              elif(inventory[finditem("Blood")][1] < 100-inventory[finditem("Infection")][1] and inventory[finditem("Blood")][1]>=100-inventory[finditem("Infection")][1]-(inventory[finditem("Blood Boon")][1])-round(10/modifier)):
                  inventory[finditem("Blood")][1] = 100-inventory[finditem("Infection")][1]
            else:
              if(inventory[finditem("Blood")][1]<100 and inventory[finditem("Blood")][1]<=100-(inventory[finditem("Blood Boon")][1])-round(10/modifier)):
                  inventory[finditem("Blood")][1]+=round(10/modifier)+(inventory[finditem("Blood Boon")][1])
              elif(inventory[finditem("Blood")][1]>110):
                  print("The amount of blood you have isn't healthy, you get a wound")
                  addstuff("Open Wound",math.floor((inventory[finditem("Blood")][1]-100)/10))
              elif(inventory[finditem("Blood")][1] < 100 and inventory[finditem("Blood")][1]>=100-round(10/modifier)):
                  inventory[finditem("Blood")][1] = 100
        else:
            if(finditem("Infection") != -1 and inventory[finditem("Infection")][1] >= 1):
              if(inventory[finditem("Blood")][1]<100-inventory[finditem("Infection")][1] and inventory[finditem("Blood")][1]<=100-inventory[finditem("Infection")][1]-round(10/modifier)):
                  inventory[finditem("Blood")][1]+=round(10/modifier)
              elif(inventory[finditem("Blood")][1]>110-inventory[finditem("Infection")][1]):
                  print("The amount of blood you have isn't healthy, you get a wound")
                  addstuff("Open Wound",math.floor((inventory[finditem("Blood")][1]-(100-inventory[finditem("Infection")][1]))/10))
              elif(inventory[finditem("Blood")][1] < 100-inventory[finditem("Infection")][1] and inventory[finditem("Blood")][1]>=100-inventory[finditem("Infection")][1]-round(10/modifier)):
                  inventory[finditem("Blood")][1] = 100-inventory[finditem("Infection")][1]
            else:
              if(inventory[finditem("Blood")][1]<100 and inventory[finditem("Blood")][1]<=100-round(10/modifier)):
                  inventory[finditem("Blood")][1]+=round(10/modifier)
              elif(inventory[finditem("Blood")][1]>110):
                  addstuff("Open Wound",math.floor((inventory[finditem("Blood")][1]-100)/10))
              elif(inventory[finditem("Blood")][1] < 100 and inventory[finditem("Blood")][1]>=100-round(10/modifier)):
                  inventory[finditem("Blood")][1] = 100
    if(alive==1 and finditem("curse of haunting")!=-1 and inventory[finditem("curse of haunting")][1]>=1):
        for i in range(hours*int(inventory[finditem("curse of haunting")][1])):
            if(0.01>random.random()):
                print("a restless spirit has come to haunt you")
                entercombat("spirit",0)
                print()
    radcount=0
    cancerspread=0
    wounds=0
    radfade=0
    if(alive==1 and finditem("Radiation")!=-1 and inventory[finditem("Radiation")][1]>=1):
        for i in range(hours * int(inventory[finditem("Radiation")][1])):
            if(0.001>random.random()):
                radcount+=1
        if(radcount > 0):
            print("You feel odd, then you recognise the signs, Cancer")
            addstuff("Cancer",radcount)
            print()
    if(alive==1 and finditem("Radiation")!=-1 and inventory[finditem("Radiation")][1]>=1):
                for i in range(int(inventory[finditem("Radiation")][1])):
                    if(0.001>random.random()):
                        radfade+=1
                if(radfade > 0):
                    print("Some of your radiation fades")
                    addstuff("Radiation",-1)
                    print()
    if(alive==1 and finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1]>=1):
        for i in range(hours * int(inventory[finditem("Cancer")][1])):
            if(0.001>random.random()):
              cancerspread+=1
        if(cancerspread > 0):
            if(cancerspread == 1):
                print("Your cancer spreads")
            else:
                print("You cancer spreads "+int_to_en(cancerspread)+" times")
            addstuff("Cancer",cancerspread)
    if(alive==1):
        for i in range(hours):
            if(0.001>random.random()):
              wounds+=1
        if(wounds > 0):
            if(wounds == 1):
                print("You were wounded one time")
            else:
                print("You were wounded "+int_to_en(wounds)+" times")
    if(alive==1 and finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=1):
        for i in range(hours * int(inventory[finditem("Insanity")][1])):
            if(alive==1):
                if(0.005>random.random()):
                  print("You cackle maniacally,")
                  addstuff("Insanity",1)
                if(0.005>random.random()):
                  print()
                  place = ["a small tree","a large tree","a marsh with knee level water","swimmably deep water","the kracken","an empty area","a small smelter","a campfire","firepit","rock","a treasure room","an impassible wall","a weird mysterious area","unknown","a pickle","an apple","an orange","a bannana","a bannana tree","an orchard","a forrest","a library","a lemonade stand","a man with a rifle","a fifty foot monster","the devil","a tornado","a parking lot","a trash can","an elevator","a button","a tee-shirt","a very long book","a crater","the moon","the sun","Jupiter","the Kepler space telescope","some debris","a zoo","a building","your childhood home","a church","a temple","a monument","a statue"]
                  action = ["turn into a "+items[int(round(random.random()*(len(items)-1)))],"dance like there is no tomorrow","eat a cake","eat spinach","explode","fly into the sky","spin in circles","sing songs","pick berries","reach a high shelf","thing about "+items[int(round(random.random()*(len(items)-1)))],"kick a "+items[int(round(random.random()*(len(items)-1)))],"destroy the world","invade russia","play games","do magic","crash and burn","light things on fire","go insane"]
                  print("You see a "+items[int(round(random.random()*(len(items)-1)))]+" near "+place[int(round(random.random()*(len(place)-1)))])
                  if(0.5>random.random()):
                      print("It is trying to "+action[int(round(random.random()*(len(action)-1)))])
                      if(0.5>random.random()):
                          print("It gets help from a "+items[int(round(random.random()*(len(items)-1)))])
                          if(0.5>random.random()):
                              print("They succeed! They then decide to "+action[int(round(random.random()*(len(action)-1)))]+" and then they leave")
                          else:
                              print("They fail, so instead they decide to "+action[int(round(random.random()*(len(action)-1)))]+" and then they leave")
                      else:
                          if(0.5>random.random()):
                              print("it succeeds! it then decides to "+action[int(round(random.random()*(len(action)-1)))]+" and then it leaves")
                          else:
                              print("it fails, so instead it decides to "+action[int(round(random.random()*(len(action)-1)))]+" and then it leaves")
                  else:
                      print("It attacks you with a "+items[int(round(random.random()*(len(items)-1)))])
                      print("What do you do?")
                      input()
                      if(0.5>random.random()):
                          print("That works!")
                      else:
                          print("It doesn't work!")
                      if(0.5>random.random()):
                          print("It gets help from a "+items[int(round(random.random()*(len(items)-1)))])
                          print("They "+action[int(round(random.random()*(len(action)-1)))])
                          if(0.5>random.random()):
                              print("it succeeds! it then decides to "+action[int(round(random.random()*(len(action)-1)))]+" and then it leaves")
                          else:
                              print("it fails, so instead it decides to "+action[int(round(random.random()*(len(action)-1)))]+" and then it leaves")
                      else:
                          print("It is trying to "+action[int(round(random.random()*(len(action)-1)))])
                          if(0.5>random.random()):
                              print("It gets help from a "+items[int(round(random.random()*(len(items)-1)))])
                              if(0.5>random.random()):
                                  print("They succeed! They then decide to "+action[int(round(random.random()*(len(action)-1)))]+" and then they leave")
                              else:
                                  print("They fail, so instead they decide to "+action[int(round(random.random()*(len(action)-1)))]+" and then they leave")
                          else:
                              if(0.5>random.random()):
                                  print("it succeeds! it then decides to "+action[int(round(random.random()*(len(action)-1)))]+" and then it leaves")
                              else:
                                  print("it fails, so instead it decides to "+action[int(round(random.random()*(len(action)-1)))]+" and then it leaves")
    deathcheck()                
def militarybase(area):
    print("By order of the United States Government, Halt!")
    print("Do you halt(Y/N)")
    attack=variableify(input())
    if(len(attack) > 0 and attack[0] == "Y"):
        print("This area is restricted. Show your clearance")
        if(finditem("Security Level")==-1 or inventory[finditem("Security Level")][1]<1):
            input()
            print("...")
            print("Are you a civilian?(Y/N)")
            civ=variableify(input())
            if(len(civ) == 0 or civ[0] != "N"):
                print("Okay, you're a civilian.")
                print("We are willing to let you assist the US Military")
                if(area == "radio"):
                    print("Our radio mechanic could use some electronics for the radio")
                else:
                    print("We require ammunition, the beasts are at our throats every single day.")
                print("Do you have some?(Y/N)")
                havesome=variableify(input())
                if(len(havesome) == 0):
                    print("Do you?")
                    havesome=variableify(input())
                    if(len(havesome) == 0):
                        print("Hello?")
                        havesome=variableify(input())
                        waste=0
                        while(len(havesome) == 0):
                            for i in range(waste):
                                print(".",end="")
                            print("...")
                            waste+=1
                            havesome=variableify(input())
                elif(havesome[0] == "Y" and (area != "radio" and (finditem("Bullet")==-1 or inventory[finditem("Bullet")][1]<=0) or (area == "radio" and (finditem("Electrionic Components")==-1 or inventory[finditem("Electronic Components")][1]<=0)))):
                    print("Good, Give it here")
                    print("...")
                    input()
                    print("I am going to guess by your responce that you don't actually have any")
                    print("Please don't waste our time. Come back with ",end = "" )
                    if(area == "radio"):
                        print("electronic components")
                    else:
                        print("ammunition")
                    print("And, at the very least, don't lie about it!")
                elif(havesome[0] == "Y"):
                    print("Good, Are you willing to make a contribution to your nation?(Y/N)")
                    contribute = variableify(input())
                    if(len(contribute) == 0 or contribute[0] == "N"):
                        print("We are the United States Army")
                        print("We are the last reminant of the United States Military")
                        print("Has radiation fully fried your brain?")
                        input()
                        print("Just, leave, Now!")
                    else:
                        print("Great, How many?")
                        print("You have ",end="")
                        if(area == "radio"):
                            print(str(inventory[finditem("Electronic Components")][1]))
                        else:
                            print(str(inventory[finditem("Bullet")][1]))
                        supplies = int(valid(input()))
                        while((area == "radio" and supplies > inventory[finditem("Electronic Components")][1]) or (area != "radio" and supplies > inventory[finditem("Bullet")][1])):
                            print("You don't have that many, you have ",end="")
                            if(area == "radio"):
                                print(str(inventory[finditem("Electronic Components")][1]))
                            else:
                                print(str(inventory[finditem("Bullet")][1]))
                        if(area == "radio"):
                            addstuff("Electronic Components",-supplies)
                        else:
                            addstuff("Bullet",-supplies)
                        if(0.5 + (0.1*supplies)-(0.1*modifier) > random.random()):
                            print("Thanks for your contribution")
                            addstuff("Security Level",1)
                            print("You may now enter any military base you come across")
                        else:
                            print("Your contribution is appreciated, It isn't near enough to be let in, but It is appreciated never-the-less")
                else:
                    print("I can't trust you to be on any of our bases unless you can contribute")
                    print("We don't have enough resources let in every lowly scavenger we come across")
                    print("No offence intended")
            else:
                print("Then can I see your identification")
                print("You have no identification")
                print("Impersonation is strictly forbidden. I SHOULD imprison you, but I will let you just walk away")
                print("SO GET THE HELL OFF OF BASE")
        if(finditem("Security Level")!=-1 and inventory[finditem("Security Level")][1]>=1):
            print("You are shown inside.")
            print("As you enter, you recieve a ticket. it says")
            while(True):
                bloodloss(1)
                print()
                print("/==============================\\")
                print(":        DIRECTORY             :")
                print(":                              :")      
                print(": ID | SECURITY |     NAME     :")
                print(": -- - - - - - - - - - - - - - :")
                print(": 1 | LEVEL 1  | EXIT THE BASE :")      
                print(": 2 | LEVEL 1  | TARGET RANGE  :")
                print(": 3 | LEVEL 1  | MESS HALL     :")
                print(": 4 | LEVEL 1  | MEDIC STATION :")
                print(": 5 | LEVEL 1  | STORE HOUSE   :")
                print(": 6 | LEVEL 1  | BARRACKS      :")
                print(": 7 | LEVEL 2  | CONTROL ROOM  :")
                print(": 8 | LEVEL 2  | OFFICER REC   :")
                print(": 9 | LEVEL 2  | ARTILLERY CMD :")
                print(":                              :")    
                print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
                print()
                print("Where do you want to go")
                position = int(valid(input()))
                print()
                if(position == 1):
                      print("The perimeter is secure. Do you want to leave?")
                      leave = variableify(input())
                      if(len(leave) != 0 and leave[0] == "Y"):
                          break
                elif(position == 2):
                    print("You are at a range. You can fight one of the dummies")
                    print("Do you want to fight one?(Y/N)")
                    shoot = variableify(input())
                    while(len(shoot) > 0 and shoot[0] != "N"):
                        entercombat("dummy",0)
                        print("Do you want to fight another?(Y/N)")
                        shoot = variableify(input())
                elif(position == 3):
                    print("You enter a large room filled with tables.")
                    print("On the other end of the room is several stations with some sort of gray slop")
                    print("A sign reads 'Due to rationing issues, food must be paid for'")
                    print("")
                    print("Each ration costs "+str(int(2*modifier))+" coins and provides "+str(int(25/modifier))+" food and "+str(int(20/modifier))+" water. Do you want to buy some?(Y/N)")
                    slop = variableify(input())
                    if(len(slop) == 0 or slop[0] != "Y"):
                        print("You do not")
                    else:
                        print("How much do you want to buy?")
                        if(finditem("Coin")!=-1 and inventory[finditem("Coin")][1]>0):
                            if(inventory[finditem("Coin")][1]>1):
                                print("You look in your pockets, you find "+int_to_en(inventory[finditem("Coin")][1]) +" coins")
                            else:
                                print("You have a single coin")
                        else:
                            print("You don't have any coins")
                        slopamt = int(valid(input()))
                        if(finditem("Coin")==-1 or math.floor(inventory[finditem("Coin")][1]/int(2*modifier))<slopamt):
                            print("You cannot afford that much")
                        else:
                            print("You buy the slop")
                            addstuff("Food",slopamt*int(25/modifier))
                            addstuff("Water",slopamt*int(20/modifier))
                            addstuff("Coin",slopamt*int(-2*modifier))
                    print("There are several people chatting.")
                    print("Do you want to talk to anyone?")
                    talk = variableify(input())
                    if(len(talk) > 0 and talk[0] == "Y"):
                        print("Who do you want to talk to")
                        print("1) Kitchen Manager")
                        print("2) Chef")
                        print("3) Listen to random table chatter")
                        talkto = valid(input())
                        if(int(talkto)==1):
                            print("I am a very busy person, make this quick")
                            print("1: Do you have Work")
                            print("2: How are you")
                            print("3: What exactly do you do")
                            responce = valid(input())
                            if(int(responce) == 1):
                                print("I could use some extra help in my kitchen")
                                if(finditem("Military Goodwill")!=-1 and inventory[finditem("Military Goodwill")][1]>=1):
                                    print("I will offer "+str(int(math.ceil((15+inventory[finditem("Military Goodwill")][1])/modifier)))+" coins per hour")
                                else:
                                    print("I will offer "+str(int(math.ceil(15/modifier)))+" coins per hour")
                                print("Do you want to?(Y/N)")
                                work=variableify(input())
                                if(len(work) != 0 and work[0] == "Y"):
                                    print("Great!")
                                    print("How long can I put you down for?")
                                    hours = int(valid(input()))
                                    if(hours > 8):
                                        print("I can't offer more than 8 hours a time. ")
                                        hours = 8
                                    bloodloss(hours)
                                    if(finditem("Military Goodwill")!=-1 and inventory[finditem("Military Goodwill")][1]>=1):
                                        addstuff("Coin",hours*int(math.ceil((15+inventory[finditem("Military Goodwill")][1])/modifier)))
                                    else:
                                        addstuff("Coin",hours*int(math.ceil(15/modifier)))
                                    print("You work for an hour, and you get paid")
                                    print("Thank you for your work")
                                    if(random.random()<0.2*(modifier/hours)):
                                        print("It is much appreciated")
                                        addstuff("Military Goodwill",1)
                            elif(int(responce) == 2):
                                if(finditem("curse of hunger")!=-1 and inventory[finditem("Military Goodwill")][1]>=5):
                                    print("Surviving is tough, but I will be okay")
                                elif(finditem("curse of hunger")!=-1 and inventory[finditem("Military Goodwill")][1]>=1):
                                    print("I am doing okay")
                                else:
                                    print("I am not here to talk about my feeling. Stop wasting my time")
                            elif(int(responce) == 3):
                                if(finditem("Military Goodwill")!=-1 and inventory[finditem("Military Goodwill")][1]>=5):
                                    print("I manage the kitchen, like, ensure we get rations and decide who does what in the kitchen")
                                elif(finditem("Military Goodwill")!=-1 and inventory[finditem("Military Goodwill")][1]>=1):
                                    print("I control everything related to the kitchen and its operation")
                                else:
                                    print("You don't need to know, go away")
                        if(int(talkto) == 2):
                            print("Hello! Was the food good today?")
                            print("1) Yes")
                            print("2) No")
                            print("3) I haven't tried it")
                            responce = int(valid(input()))
                            if(responce == 1):
                                print("Good to hear it!")
                            elif(responce == 2):
                                print("Yea, it can be a bit bland")
                            elif(responce == 3):
                                print("You should, It's rather nutiritious")
                            print()
                            print("Anyway, what can I do for you?")
                            print("1) Nothing")
                            print("2) Do you have any work?")
                            print("3) Can I have some food")
                            responce = int(valid(input()))
                            if(responce == 1):
                                print("I hope to see you around!")
                            elif(responce == 2):
                                print("I don't have a jop per-say, you would have to ask the manager for that")
                                if(modifier == 1):
                                    print("I could use some raw meat, A coin per raw meat")
                                else:
                                    print("I could use some raw meat, A coin per "+int_to_en(modifier)+" raw meat")
                                print("Do you want to give him raw meat?")
                                givemeat=variableify(input())
                                if(len(givemeat) == 0 or givemeat[0] == "N" or finditem("Raw Meat") == -1 or inventory[finditem("Raw Meat")][1] <= 0):
                                    print("You don't give him any")
                                else:
                                    print("How much do you want to give him?")
                                    amt = int(valid(input()))
                                    if(amt>inventory[finditem("Raw Meat")][1]):
                                        print("You can't afford that much")
                                    else:
                                        print("You sell your meat to him")
                                        addstuff("Coin",int(amt/modifier))
                                        addstuff("Raw Meat",-amt)
                            elif(responce == 3):
                                print("Funny, But that is never how this works. Pay like the rest of us.")
                        if(int(talkto) == 3):
                            print("You sit down and listen to the people in the mess hall")
                            print()
                            phrases = ["I wonder where the monsters come from","Do you have any idea what ended the old-times?","I heard he is getting a promotion","Another one attacked yesterday","I heard the private was injured.","Bullets don't stop curses","I heard the rationing situation is worse than normal","My superiors hasn't been getting enough sleep","Do you know what caused the apocalipse?","I saw another minor demon today","I need to spend more time at the range","My gun jammed this morning, they shouldn't do that!","I need more firepowerer","I witnessed an artillery salvo earlier. It was a work of art","This food is so tasteless","It is nice to eat every once and a while","paying for food is a bit odd, but I can tell: Times are rough","Where is the crappy town where I'm a hero?","What do you think happends when we die?","All quiet on the western front","According to the doctor I am practically made of radiation","I heard that people used to play something called 'baseball'. I heard it's rather violent","This could use some sauce","The mutants still unerve me","We need to do some repairs to the defences, but we don't really have the time","The slop has sortof grown on me"]
                            if(finditem("Military Goodwill")==-1 or inventory[finditem("Military Goodwill")][1]<=0):
                                phrases.extend(["I hate all of these scavengers who take our resources","We need to be less welcoming to the random losers who walk into camp","It's no wonder we have to ration so much when we let in so many scavengers","Basically anyone can just walk into camp. That doesn't make any sense.","How can we trust these randoms!","So they come here with no weapons, no food and barely any skill and we have to accept them?","Why do we have to work with untrained morons","I devout myself entirely to the base, but when an unimpressive scavenger comes, they get treated just as I do","I just plain don't trust them","Scavengers are barely any better than particuary dumb mutants.","I wonder why we have to pay for food, oh wait, it't because we let in basically anyone!","I cannot trust them, I just can't! Some haven't ever held a gun before!","This camp is just going"])
                            if(finditem("Military Goodwill")!=-1 and inventory[finditem("Military Goodwill")][1]>=1):
                                phrases.extend(["Scavengers aren't all bad.","I think we need to focus more on our roots of protecting civilians","Scavengers can have their uses","I think the camp is doing fine"])
                            if(finditem("Military Goodwill")!=-1 and inventory[finditem("Military Goodwill")][1]>=5):
                                phrases.extend(["We should cast a larger recruitment net, it is probally the best way to rebuild.","Call me an optimist, but I think we can do just fine","I think there is just something so exiting about fighting for the memory of America","We have held out so well, concidering","I think the civilians have been rather helpfull","I think we need more diplomacy","We should start a band, you know, for moral","I think the camp is doing absolutely great"])
                            for i in range(3+int(random.random()*5)):
                                print("'"+phrases[int(random.random()*(len(phrases)+1))]+"'")
                            print()
                            print("You finish and leave the mess hall")
                elif(position == 4):
                    print("You enter a clean-ish room full of medical equipment")
                    if(finditem("Open Wound") != -1 and inventory[finditem("Open Wound")][1]>=1):
                        print("A doctor checks your wounds and patches them up")
                        addstuff("Open Wound",-inventory[finditem("Open Wound")][1])
                        addstuff("Scar",-inventory[finditem("Scar")][1])
                    if(inventory[finditem("Blood")][1]<=50):
                        print("'You need more blood' the doctor says as he injects a syringe into your arm")
                        inventory[finditem("Blood")][1] += random.random() * (50/modifier)
                    if(inventory[finditem("Water")][1]<=10):
                        print("You are suffering dehydration. Drink. Now")
                        inventory[finditem("Water")][1] += random.random() * (50/modifier)
                    if(inventory[finditem("Food")][1]<=10):
                        print("You are incredibly malnurished. Eat this, it tasts awfull but it will help you")
                        inventory[finditem("Food")][1] += random.random() * (50/modifier)
                    print()
                    print("The doctors are trading for with excess medical supplies.")
                    print("Do you want to trade?")
                    buysomemeds = variableify(input())
                    if(len(buysomemeds) > 0 and buysomemeds[0] == "Y"):
                        print("Great, We can trade")
                        print()
                        print(" - What trade do you offer? - ")
                        print("1) Trade nothing")
                        print("2) 1 Coin --> 2 Bandage")
                        print("3) 8 Coins --> 1 Disinfectant")
                        print("4) 2 Coins --> 1 Empty Syringe")
                        print("5) 10 Coins --> 1 Blood Syringe")
                        print("6) 15 Coins --> 1 Radiation Treatement")
                        print("7) 5 Bandages --> 1 Coin")
                        print("8) 1 Disinfectant --> 5 Coins")
                        print("9) 1 Blood Syringe --> 8 Coins")
                        print("10) 1 Radiation Treatement --> 10 Coins")
                        print("11) Blood Drawing(25 Blood) --> 5 Coins")
                        print("12) Donate Blood(50 Blood)")
                        print("13) Donate 30 Bandages")
                        print("14) Donate 15 Coins")
                        print("15) Donate A Radiation Treatment")
                        print("15) Donate A Blood Syringe")
                        print("What do you say?")
                        dotrade = int(valid(input()))
                        print()
                        if(dotrade == 1):
                            print("You do not decide to trade anything")
                        elif(dotrade == 2):
                            trade("Coin",1,"Bandage",2)
                        elif(dotrade == 3):
                            trade("Coin",8,"Disinfectant",1)
                        elif(dotrade == 4):
                            trade("Coin",2,"Empty Syringe",1)
                        elif(dotrade == 5):
                            trade("Coin",10,"Blood Syringe",1)
                        elif(dotrade == 6):
                            trade("Coin",15,"Radiation Treatment",1)
                        elif(dotrade == 7):
                            trade("Bandage",5,"Coin",1)
                        elif(dotrade == 8):
                            trade("Disinfectant",1,"Coin",5)
                        elif(dotrade == 9):
                            trade("Blood Syringe",1,"Coin",8)
                        elif(dotrade == 10):
                            trade("Radiation Treatment",1,"Coin",10)
                        elif(dotrade == 11):
                            trade("Blood",25,"Coin",5)
                        elif(dotrade == 12):
                            trade("Blood",80,"Military Goodwill",1)
                        elif(dotrade == 13):
                            trade("Bandages",30,"Military Goodwill",1)
                        elif(dotrade == 14):
                            trade("Coin",25,"Military Goodwill",1)
                        elif(dotrade == 15):
                            trade("Radiation Treatment",2,"Military Goodwill",1)
                        elif(dotrade == 16):
                            trade("Blood Syringe",5,"Military Goodwill",1)
                    print("You leave the medstation")
                elif(position == 5):
                    print("The garrage has generous piles of scrap, components, boxes with lables like 'Ammunition' and 'Screws'.")
                    print("A large man is standing around, and greets you as you approach")
                    print("Do you want to trade?")
                    buysomemeds = variableify(input())
                    if(len(buysomemeds) > 0 and buysomemeds[0] == "Y"):
                        print("Great, We can trade")
                        print()
                        print(" - What trade do you offer? - ")
                        print("1) Trade nothing")
                        print("2) 5 Scrap --> 10 Coin")
                        print("3) 5 Coins --> 1 Scrap")
                        print("4) 2 Coin --> 1 Oil Can")
                        print("5) 1 Oil Can --> 1 Coin")
                        print("6) 35 Coins --> 1 Bicycle")
                        print("7) 100 Coins --> 1 Motorcycle")
                        print("8) 1 Bicycle --> 20 Coins")
                        print("9) 1 Motorcycle --> 80 Coins")
                        print("10) Donate 20 Oil Cans")
                        print("11) Donate 10 Scrap")
                        print("12) Donate A Motorcycle")
                        print("13) Donate A Bicycle")
                        print("14) Donate 25 Coins")
                        dotrade = int(valid(input()))
                        print()
                        if(dotrade == 1):
                            print("You do not decide to trade anything")
                        elif(dotrade == 2):
                            trade("Scrap",5,"Coin",10)
                        elif(dotrade == 3):
                            trade("Coin",5,"Scrap",1)
                        elif(dotrade == 4):
                            trade("Coin",2,"Oil Can",1)
                        elif(dotrade == 5):
                            trade("Oil Can",1,"Coin",1)
                        elif(dotrade == 6):
                            trade("Coin",35,"Bicycle",1)
                        elif(dotrade == 7):
                            trade("Coin",100,"Motorcycle",1)
                        elif(dotrade == 8):
                            trade("Bicycle",1,"Coin",20)
                        elif(dotrade == 9):
                            trade("Motorcycle",1,"Coin",80)
                        elif(dotrade == 10):
                            trade("Oil Can",20,"Military Goodwill",1)
                        elif(dotrade == 11):
                            trade("Scrap",10,"Military Goodwill",1)
                        elif(dotrade == 12):
                            trade("Motorcycle",1,"Military Goodwill",4)
                        elif(dotrade == 13):
                            trade("Bicycle",1,"Military Goodwill",1)
                        elif(dotrade == 14):
                            trade("Coin",25,"Military Goodwill",1)
                elif(position == 6):
                    print("Do you want to rest?")
                    rest = variableify(input())
                    if(len(rest) > 0 and rest[0] == "Y"):
                        print("You slowly go to bed in the barraks")
                        print("How many hours do you want to try to sleep?")
                        sleeptime = valid(input())
                        bloodloss(sleeptime)
                        totalhours += sleeptime
                        if(sleeptime>2):
                            print("ZZZ")
                            input("I think about ")
                            print()
                            if(random.random()*modifier*sleephours > 0.1):
                                print("You wakeup in a queit place. There is the load low rumbling and crackling of a flame")
                                input("I ")
                                print("A familiar voice you just can't place begins to talk")
                                print("''Try your best. The situation is always getting more grimm down below''")
                                print("''There is no choice only consequences''")
                                print("''Tread carefully and Good Luck''")
                            elif(random.random()*modifier*sleephours > 0.1):
                                print("You wakeup to the smell of smoke and the feel of hellfire in your hands.")
                                input("I ")
                                print("The screams of the dammed and the hatred of every dictator who ever died fills the room")
                                print("you cannot bring yourself to do anyhting")
                                input("I ")
                                print("A man in a buisness suit catches you eye, you find it impossible to look away. He speaks")
                                print("~Lets be reasonable, Stop you foolish escapade. You friends will not protect you~")
                                print("You are presented with the the purist of cayos, the least diluted of hatred")
                                print("What do you do?")
                                input("I ")
                                print("You do nothing")
                            elif(random.random()*modifier*sleephours > 0.1):
                                print("You wakeup in a small, wooden cabin, It feels cozy and warm")
                                print("You feel comfortable, and for the first time in your miserable existance you feel content")
                                print("You smell bacon and eggs, and while you don't recall ever eating it, it feels familiar and happy")
                                print("A nuturing voice calls that it is time to wake up, it is the begining of your life")
                                print("What do you do?")
                                input()
                            elif(random.random()*modifier*sleephours > 0.1):
                                print("You continue to swing on the swingset")
                                print("You friend, ##### is swinging with you. The mountians look better than they normally do")
                                print("You are happy")
                                input("I ")
                                print("You just sit there, enjoying the moment")
                            elif(random.random()*modifier*sleephours > 0.1):
                                print("You wake up in a lecture hall.")
                                print("The teacher, Mr ##### is talking about something math related, you can't really follow his words")
                                print("Looking outside, you see a light layer of snow blanketing the ground, people are playing")
                                input("I ")
                                print("You slowly close you eyes oncemore")
                            elif(random.random()*modifier*sleephours > 0.1):
                                print("You wakeup in your bed. It is as soft as it ever had been")
                                print("You hear the buzzing of your phone, texts from various friends and loved ones")
                                print("You feel important, sucessfull and, best of all, happy")
                                print("The world feels perfect")
                            elif(random.random()*modifier*sleephours > 0.1):
                                print("You wakeup in a wooden pew. At the center of the church is a casket.")
                                print("You are bleeding, one small hole in the middle of your chest")
                                print("You see a shadowly, dimentionless, humanoid figure with a long scythe and a single bone finger pointing to the casket")
                                print("You see many vaugly familiar people around you. They feel comforting, like an old blanket")
                                print("You do not recognise any of them.")
                                input("I ")
                                print("You walk over and look in the casket, it is empty")
                                print("Giving one last glance to everyone, you get inside.")
                                print("With one quick motion, the reaper collects his harvest")
                            else:
                                print("You dream about "+items+" it is very, very bizzare")
                        print("You awake in the harsh metalic bunk of the barracks, You are well rested and ready to start a new day")
def trade(name1,count1,name2,count2):
    if(finditem(name1) != -1 and inventory[finditem(name1)][1] > count1):
        print("You will trade "+int_to_en(count1)+" '"+name1+"' for "+int_to_en(count2)+" '"+name2+"' ",end=" ")##Maybe make INSANITY change what it says the trade is for, just an idea to screw with the user, Sincerly: 2:00 AM Bryce
        accept = variableify(input("Accept?(Y/N): "))
        if(len(accept) > 0 and accept[0] == "Y"):
            print("You do the trade")
            addstuff(name1,-count1)
            addstuff(name2,count2)
        else:
            print("You cancel the trade")
    else:
        print("You cannot go through with the trade")
def clownbase(area):
    if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=5):
        print("There are a bunch of dancing "+items[round(random.random()*(len(items)-1))])
        print("They probally want to EAT YOU LIKE A "+items[round(random.random()*(len(items)-1))])
    else:
        if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
            print("You smell a campfire nearby, and you can hear some chatter. What do you do?")
        else:
            print("You manage to find what looks like a small circus. You see the movable circus tents set up, And a few clowns wandering about")
    print("1) Attack them!")
    print("2) Talk to them")
    print("3) Leave them be")
    choice = input()
    if(len(choice) > 0 and choice[0] == "1"):
        print("You get the jump on them")
        scavengers = int(4+((random.random()-0.5)*5))
        for i in range(scavengers):
            if(alive == 1):
                if(alive == 1):
                    entercombat("@Circus",1)
                    if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                        if(i!=scavengers):
                            print("Some people still remain")
                        else:
                            print()
                    else:
                        print(str(i+1)+"/"+str(scavengers)+" defeated")
    elif(choice == "2"):
        if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=10):
            print("THEY HAVE FUNNY PAINT.")
            if(inventory[finditem("Insanity")][1]>=15):
                print("THEY ARE VERY BAD MUDERERS")
            print("THERE ARE BAD ANIMALS, AND PAINT")
            print("YOU KNOW WHAT YOU HAVE TO DO-")
            for i in range(int(inventory[finditem("Insanity")][1]/10)):
                print(" MURDER",end="")
            print("THEY ARE CLOWNS. MURDER CLOWNS OF DEATH")
            print("YOU DO NOT LIKE THEM:")
            for i in range(int(inventory[finditem("Insanity")][1]/10)):
                print(" MURDER",end="")
        else:
            print("You introduce yourself, they are rather nice")
            print("You learn that times have been tough lately.")
            print("After the apocalipse, they began to survive as scavengers")
            print("These clowns have never actually been in a circus, they were born long after the apocalipse")
            print("The clowns still look freaky, but you can see the humanity")
            if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                print("They were very accomidating of your blindness")
            if(1/modifier>random.random()):
                if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=10):
                    print("They give you a whip")
                    print("IT IS A SIGN OF BADNESS.",end="")
                else:
                    print("A lion tamer died recently so they no longer need his whip")
                    print("They decide you could use it")
                addstuff("Whip",1)
            if(1/modifier>random.random()):
                if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=10):
                    print("They give you coins")
                    print("IT IS A SIGN OF BADNESS.",end="")
                else:
                    print("They decide to give you some loose change they have")
                addstuff("Coin",int(20*random.random()*(1/modifier)))
            if(1/modifier>random.random()):
                if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=10):
                    print("They give you some junk")
                    print("IT IS A SIGN OF BADNESS.",end="")
                else:
                    print("They decide to give you some scraps")
                defaultlootable(3)
            if(1/modifier>random.random()):
                if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=10):
                    print("They give you crate")
                    print("IT IS A SIGN OF BADNESS.",end="")
                else:
                    print("They actually have a small crate of usefull things, they decide to give some to you")
                chestlootable()
        print("Do you want to attack them?(Y/N)")
        attack=variableify(input())
        if(len(attack) > 0 and attack[0] == "Y"):
            print("You get the jump on them")
            scavengers = int(3+((random.random()-0.5)*4))
            for i in range(scavengers):
                if(alive == 1):
                    entercombat("scavenger",1)
                    if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                        print("You defeat a scavenger,",end="")
                        if(i!=scavengers):
                            print("Some still remain")
                        else:
                            print()
                    else:
                        print(str(i+1)+"/"+str(scavengers)+" defeated")
        else:
            print("You leave their camp")
    else:
        print("You leave them to do whatever they were doing")
def passtime(hours):
    global x
    global y
    global totalhours
    global alive
    if(finditem("curse of slowness")!=-1 and inventory[finditem("curse of slowness")][1]>=1):
        hours=hours*(inventory[finditem("curse of slowness")][1]+1)
    k=0
    while (k<int(hours)):
        k+=1
        if(alive == 1):
            if(alive == 1 and (1/((modifier+5)*20))>random.random() and world[x][y] != "A" and world[x][y] != "M" and world[x][y] != "|" and world[x][y] != "?" and world[x][y] != "W" and world[x][y] != "~"):
                print("On the horizon is a merchant selling his wares")
                shopkeep()
            if(alive == 1 and (1/((modifier+5)*15))>random.random()):
                seller = math.floor(random.random()*8)#0:Explode 1:Gun  2:Cyborg 3:FriendlyCultist 4:Wastelander 5: Doctor Add, 6: Alien 7: Military Man 8: Food Vendor 9: Woodsmith
                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                    if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 0):
                        print("You see a taking, walking "+items[round(random.random()*(len(items)-1))])
                    elif(seller == 0):
                        print("You see a woman wearing old cloth with rusted metalic scraps haphazardly attached")
                    elif(seller == 1):
                        print("You see an old man covered head-to-toe in in guns and ammo")
                    elif(seller == 2):
                        print("You see a cyborg, covered in implants and robotic implants")
                    elif(seller == 3):
                        print("You see a humanoid figure in red robes with a basket of scrolls")
                    elif(seller == 4):
                        print("You see a person wearing ragged clothes. They seem to have a few goods for sale")
                    elif(seller == 5):
                        print("You see a doctor wearing a white lab coat covered in mud, dirt and a few drops of blood(of various colours)")
                    elif(seller == 6):
                        print("You see a unworldly looking person dressed in lazily made formal attire")
                        print("It looks wrong, not natural")
                    elif(seller == 7):
                        print("You see man in an old and worn military uniform")
                    elif(seller == 8):
                        print("You see woman wearing an apron and a chefs hat")
                    elif(seller == 9):
                        print("You see a man in a checkered shirt with an axe")
                            
                if(seller == 0):
                    print("In an high-pitched and twitchy voice you hear 'Oh! hello! Feel like exploding?'")
                elif(seller == 1):
                    print("In an angry grizzly voice, you hear 'Are you friendly enough to trade?'")
                elif(seller == 2):
                    print("You hear a high-piched synthetic voice say 'Why hello! Do you want some cool stuff?'")
                elif(seller == 3):
                    print("You hear an ominous voice chant 'Come, and see your every desire completed!'")
                elif(seller == 4):
                    print("In a friendly, yet cautious tone, you hear 'Are you here to trade'")
                elif(seller == 5):
                    print("In a carefull tone, you hear 'Are you in need of medical supplies'")
                elif(seller == 6):
                    print("You hear a cacophony of ominous whispers and strange clacking")
                    print("It speaks: 'Hey Neighbor! Willing to help a friend?'")
                elif(seller == 7):
                    print("You hear barking orders 'Hault. The United States Army requests trade of supplies'")
                    print("Do you hault?")
                elif(seller == 8):
                    print("You hear in a mad, uncontrolled voice 'Ya Hunr'y furr som' gud meat?!?!'")
                    if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                        print("They are covered in blood",end = "")
                        if(inventory[finditem("Insanity")][1] > 15):
                            print(", When they speak flesh falls out from their face")
                        else:
                            print()
                elif(seller == 9):
                    print("You hear, in a strangly cheery tone 'Wanna make a trade'")
                explode = variableify(input())
                if(len(explode)==0 or explode[0] == "N"):
                    if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                        print("It gets angry and attacks! MURDER IT")
                        if(inventory[finditem("Insanity")][1] > 10):
                            print("MURDERMURDERMURDERMURDERMURDER")
                        if(inventory[finditem("Insanity")][1] > 20):
                            print()
                            print("YoU eNtEr CoMbAt WiTh ThE tHiNg")
                        if(inventory[finditem("Insanity")][1] > 50):
                            print("YOU SHOULD KILL IT")
                            print()
                        print("It disappeared! Drat!")
                    elif(seller == 0):
                        print("Shame! C'ya!")
                    elif(seller == 1):
                        print("Well then. Safe Travels")
                    elif(seller == 2):
                        print("Oh that is just fine! Have a wonderfull time!")
                    elif(seller == 3):
                        print("Death comes for us all, little one")
                    elif(seller == 4):
                        print("Best be on your way, be carefull")
                    elif(seller == 5):
                        print("When you die, don't blame me!")
                    elif(seller == 6):
                        print("Question nothing")
                    elif(seller == 7):
                        print("We are the last reminant of the United States, you should have supported us")
                    elif(seller == 8):
                        print("Thats fine, friend")
                else:
                    if(seller == 0):
                        deals = [["Coin",1,"Gunpowder",3],["Coin",10,"Unstable Bomb",1],["Coin",10,"Grenade",1],["Coin",15,"Makeshift Bomb",1],["Food",35,"Coin",1]]
                    elif(seller == 1):
                        deals = [["Bullet",1,"Coin",1],["Bullet",2,"Shotgun Shell",1],["Bullet",10,"Pistol",1],["Bullet",20,"Rifle",1],["Bullet",20,"Double Barrel Shotgun",1],["Bullet",100,"Combat Shotgun",1],["Bullet",100,"Chain Shotgun",1],["Bullet",40,"Machine Gun",1],["Bullet",200,"Minigun",1]]
                    elif(seller == 2):
                        deals = [["Coin",5,"Plasma Charge",1],["Coin",20,"Plasma Crystal",1],["Coin",40,"Plasma Sword",1],["Coin",50,"Field Generator",1],["Coin",20,"Plasma Grenade",1],["Coin",40,"Plasma Pistol",1],["Coin",100,"Plasma Rifle",1],["Coin",100,"Plasma Shotgun",1],["Coin",200,"Plasma Cannon",1]]
                    elif(seller == 3):
                        deals = [["Blood",99,"Anticurse Scroll",1],["Blood",99,"Fire Scroll",1],["Blood",99,"Food Scroll",1],["Blood",99,"Water Scroll",1],["Blood",99,"Plant Scroll",1],["Blood",99,"Wealth Scroll",1],["Blood",99,"Binding Scroll",1],["Blood",99,"Strike Scroll",1],["Blood",10,"Blank Scroll",1],["Blood",666,"Death Scroll",1]]
                    elif(seller == 4):
                        deals = [["Coin",40,"Basket",1],["Coin",40,"Raft",1],["Coin",20,"Pistol",1],["Coin",16,"Blood Syringe",1],["Coin",10,"Map",1],["Coin",8,"Bear Trap",1],["Coin",8,"Syringe",1],["Coin",8,"Disinfectant",1],["Coin",8,"Fishing Rod",1],["Coin",8,"Makeshift Basket",1],["Coin",8,"Herb",1],["Coin",8,"Torch",1],["Coin",8,"Electronic Component",1],["Coin",4,"Bandage",1],["Coin",4,"Paper",1],["Coin",4,"Tinder",1],["Coin",4,"Scrap",1],["Coin",4,"Rope",1],["Coin",4,"Leather",1],["Coin",3,"Hide",1],["Coin",2,"Fur",1],["Coin",1,"Match",1],["Coin",1,"String",1],["Coin",1,"Cloth",1],["Coin",1,"Leaves",5],["Coin",1,"Grass",5]]
                    elif(seller == 5):
                        deals = [["Coin",2,"Bandage",1],["Coin",8,"Disinfectant",1],["Coin",4,"Empty Syringe",1],["Coin",10,"Blood Syringe",1],["Coin",15,"Radiation Treatement",1]]
                    elif(seller == 6):
                        deals = [["Coin",5,"Plasma Charge",1],["Coin",20,"Plasma Crystal",1],["Coin",40,"Plasma Sword",1],["Coin",50,"Field Generator",1],["Coin",20,"Plasma Grenade",1],["Coin",40,"Plasma Pistol",1],["Coin",100,"Plasma Rifle",1],["Coin",100,"Plasma Shotgun",1],["Coin",200,"Plasma Cannon",1]]
                        if(finditem("Alien Boon") ==-1 and inventory[finditem("Alien Boon")][1] <= 0 and finditem("Mysterious Device") ==-1 and inventory[finditem("Mysterious Device")][1] <= 0):
                            deals+=["Coin",50,"Mysterious Device",1]
                    elif(seller == 7):
                        deals = [["Scrap",5,"Coin",10],["Coins",5,"Scrap",1],["Coins",2,"Oil Can",1],["Oil Can",1,"Coin",1],["Motorcycle",1,"Coin",80],["Bicycle",1,"Coin",20],["Oil Can",20,"Military Goodwill",1],["Scrap",20,"Military Goodwill",1],["Motorcycle",4,"Military Goodwill",4],["Bicycle",1,"Military Goodwill",1],["Coin",25,"Military Goodwill",1]]
                        if(finditem("Military Goodwill") !=-1 and inventory[finditem("Military Goodwill")][1] > 0):
                            deals += [["Coins",15,"Food",10],["Coins",15,"Water",20]]
                        if((finditem("Radio Controller") ==-1 or inventory[finditem("Radio Controller")][1] <= 0) and finditem("Security Level") !=-1 and inventory[finditem("Security Level")][1] > 0):
                            deals += [["Coins",20,"Radio Controller",1]]
                    elif(seller == 8):
                        deals = [["Coin",5,"Food",10],["Coin",5,"Water",25]]
                    print("1) I have what I want")
                    for i in range(len(deals)):
                        print(str(i+2)+") "+int_to_en(deals[i][1])+" "+str(deals[i][0])+" for "+int_to_en(deals[i][3])+" "+str(deals[i][2]))
                    print("You pick: ",end="")
                    dealpicked = int(valid(input()))
                    while(dealpicked != 1):
                        if(i > len(deals)+1):
                            if(seller == 0):
                                print("What? You are... Odd. Here is gunpowder")
                                addstuff("Gunpowder",1)
                                print("Now go away!")
                                dealpicked = 1
                            elif(seller == 1):
                                print("Don't waste my time being silly")
                                dealpicked = 1
                            elif(seller == 2):
                                print("I don't understand.")
                            elif(seller == 3):
                                print("Don't screw around!")
                                entercombat("mini-demon",0)
                                dealpicked = 1
                            elif(seller == 4):
                                print("please be serious")
                            elif(seller == 5):
                                print("Do you have a concussion?")
                                concussion = variableify(input())
                                if(len(concussion)==0 or concussion[0] == "Y"):
                                    print("Then you are beyond my medicine!")
                                else:
                                    print("Then stop acting stupid!")
                                dealpicked = 1
                            elif(seller == 6):
                                print("You are proof your species is nothing more than biowaste")
                                dealpicked = 1
                                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                    print("You see a beam of light, as the figure disappears")
                                else:
                                    print("You feel warm for a moment and a loud zapping noise, followed by silence")
                            elif(seller == 7):
                                print("Thank you for you assitance. You contribution will help to rebuild America")
                            elif(seller == 8):
                                print("I hope you like the taste!")
                        else:
                            dealpicked = dealpicked - 2
                            trade(deals[dealpicked][0],deals[dealpicked][1],deals[dealpicked][2],deals[dealpicked][3])
                            print("You pick: ",end="")
                            dealpicked = int(valid(input()))
                    print("You both part ways")    
            if(alive == 1 and (1/((modifier+5)*30))>random.random()):
                traveler()
            if(alive == 1 and ( (1/((modifier+5)*30))>random.random() or (((1/((modifier+5)*30))>random.random()) and world[x][y] == "T"))):
                print("You find a small creek")
                lootable(0.9,"Stone",2)
                lootable(0.9,"Water",2)
                lootable(0.9,"Stick",2)
                defaultlootable(1)
            if(alive == 1 and ( (1/((modifier+5)*30))>random.random() or (((1/((modifier+5)*30))>random.random()) and world[x][y] == "T"))):
                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                    print("You see metalic boxes with holes for air. They are closed with deadbolts.")
                else:
                    print("You find a hard metalic box with small holes, a few inches in diameter.")
                    print("You hear heavy animalistic breath")
                print("Do you want to open any?")
                doOpen = variableify(input())
                if(len(doOpen) > 0 and doOpen[0]=="Y"):
                    entercombat("@Nature")
                    while(random.random()<1/modifier and variablefiy(doOpen)[0]=="Y"):
                        print("Do you want to open another?")
                        doOpen = input()
                        if(len(variablefiy(doOpen)) > 0 and variablefiy(doOpen)[0]=="Y"):
                            entercombat("@Nature")
                print("You leave")
            if(alive == 1 and (1/((modifier+5)*30))>random.random()):
                if(world[x][y] != "W" and world[x][y] != "~"):
                    if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                        print("You feel some sort of box")
                    else:
                        print("You see a small wooden box")
                    if(modifier*0.01 > random.random()):
                        print("It has nothing")
                    else:
                        chestlootable()
                    print()
                else:
                    if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                        print("You feel some sort of box, it is rather damp")
                    else:
                        print("You see a waterlogged wooden box")
                    if(modifier*0.05 > random.random()):
                        print("It has nothing")
                    else:
                        chestlootable()
                    print()
            if(alive == 1 and ((1/((modifier+5)*30))>random.random() and world[x][y] != "~" and world[x][y] != "W") or ((1/((modifier+5)*25))>random.random() and world[x][y] == "~" and world[x][y] == "W")):
                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                    print("You bump into a small pile of scrap")
                else:
                    print("You see a small pile of scrap")
                defaultlootable(1)
                print()
            if(alive == 1 and (1/((modifier+5)*30))>random.random()):
                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                    print("You touch something, it feels like bone")
                else:
                    print("You see a skeleton, it seems to be wearing adventuring gear")
                chestlootable()
                lootable(0.5,"Bone",10)
                print()
            if(alive == 1 and (1/((modifier+5)*20))>random.random()):
                if(finditem("curse of blindness") !=-1 and world[x][y] != "≈" and inventory[finditem("curse of blindness")][1] > 0):
                    print("You feel raindrops on your face")
                else:
                    print("It begins to rain")
                lootable(0.95,"Water",25)
                print()
            if(alive == 1 and (1/((modifier+5)*20))>random.random()):
                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                    print("You find a small hole in the ground, it is surrounded by stones")
                else:
                    print("You see a well")
                print()
                print("Do you want to use the well?(Y/N)")
                welluse = variableify(input())
                if(len(welluse) == 0 or welluse[0] == "N"):
                    print("You do not")
                else:
                    print("You take some time and use the well")
                    lootable(0.95,"Water",50)
                    passtime(1)
            if(alive == 1 and (1/((modifier+5)*30))>random.random()):
                if(world[x][y] != "~" and world[x][y] != "W"):
                    if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                        print("You almost trip over something, apon further inspection, you find that it is an animal carcass")
                    else:
                        print("You see an animal carcass")
                else:
                    if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                        print("You almost trip over something, apon further inspection, you find that it is an animal carcass floating in the water")
                    else:
                        print("You see a floating animal carcass")
                lootable(0.01,"Iron Axe",0)
                lootable(0.1,"Makeshift Axe",0)
                lootable(0.5,"Fur",10)
                lootable(0.5,"Raw Food",10)
                lootable(0.5,"Hide",10)
                print()
            if(alive == 1 and (1/((modifier+5)*30))>random.random()):
                weirdman()
            if(alive == 1 and (1/((modifier+5)*30))>random.random()):
                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                    print("You feel some sort of box, You think it can be opened, do you open it?")
                else:
                    print("You see a large metal chest, do you open it?")
                choice = input()
                if(len(choice) > 0 and variableify(choice[0]) == "Y"):
                    if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                        print("You open it, and you hear the wirring of robots",end="")
                    else:
                        print("You open it, and you see a few robots approaching ",end="")
                    techs = int(2+((random.random()-0.5)*4))
                    if(techs == 0):
                        print("but none come close")
                    else:
                        if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                            print()
                        else:
                            print("a small band of "+int_to_en(techs)+" robots come")
                    for i in range(techs):
                        if(alive == 1):
                            entercombat("@Tech",0)
                            if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                print("You defeat a robot,",end="")
                                if(i!=techs):
                                    print("Some still remain")
                                else:
                                    print()
                            else:
                                print(str(i+1)+"/"+str(techs)+" defeated")
                    chestlootable()
                    chestlootable()
                else:
                    print("You let it be")
            if(alive == 1 and (1/((modifier+5)*30))>random.random() and (world[x][y] == " " or world[x][y] == "t" or world[x][y] == "T")):
                clownbase("Tent")
            if(alive == 1 and (1/((modifier+5)*30))>random.random() and (world[x][y] == " " or world[x][y] == "t" or world[x][y] == "T")):
                print("You arrive at an abandonded gas station. Do you want to turn empty bottles into gas cans?")
                gascan = variableify(input())
                if(len(gascan) == 0 or gascan[0] == "N" or finditem("Empty Bottle") == -1 or inventory[finditem("Empty Bottle")][1] <= 0):
                    print("You don't use the pumps")
                    if(finditem("Empty Bottle") == -1 or inventory[finditem("Empty Bottle")][1] <= 0):
                        print("(You don't have any empty bottles)")
                else:
                    pumpamt = int((5/random.random())-modifier)
                    if(pumpamt <= 0):
                        print("The pumps are empty")
                    else:
                        print("The pumps have "+int_to_en(pumpamt)+" cans worth of gas")
                        print("How much do you try to pump?")
                        c=valid(input())
                        if(c > pumpamt):
                            c = pumpamt
                            print("You will pump till the station is dry")
                        addstuff("Empty Bottle",-pumpamt)
                        addstuff("Oil Can",-pumpamt)
                print("Do you want to go inside the gas station?")
                enter = variableify(input())
                if(len(enter) > 0 and enter[0] == "Y"):
                      print("You go inside")
                      print()
                      lootable(0.5,"Scrap",2)
                      if(alive == 1 and random.random() < 0.01 * modifier):
                          interesting = 1
                          if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                              print("You hear unnatural growling from the room")
                          else:
                              if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                  print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                              else:
                                  print("In the middle of the room, there is some sort of mutant")
                          entercombat("mutantman",1)
                          print()
                      elif(alive == 1 and random.random() < 0.01*modifier):
                          interesting = 1
                          if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                              print("You hear unnatural growling from the room")
                          else:
                              if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                  print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                              else:
                                  print("A giant monster sits in the corner of the room")
                          entercombat("@Giant",1)
                          print()
                      elif(alive == 1 and random.random() < 0.01*modifier):
                          interesting = 1
                          if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                              print("You hear unnatural growling from the room")
                          else:
                              if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                  print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                              else:
                                  print("A giant monster sits in the corner of the room")
                              print("a girder is holding the giant in place")
                          entercombat("@Giant",2)
                          print()
                      if(alive == 1 and random.random() < 0.01 * modifier):
                          interesting = 1
                          if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                              print("You are attacked from nowhere!")
                          else:
                              if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                  print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                              else:
                                  print("A mutant jumps out from a closet!")
                          entercombat("mutantman",0)
                          print()
                      if(alive == 1 and random.random() < 0.01 * modifier):
                          interesting = 1
                          if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                              print("You are attacked from nowhere!")
                          else:
                              if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                  print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                              else:
                                  print("A mutant jumps out from the darkness!")
                          entercombat("mutantman",0)
                          print()
                      if(alive == 1 and random.random()*modifier < 0.1):
                          interesting = 1
                          print("You find an unlocked locker in one corner of the room")
                          chestlootable()
                          print()
                      if(alive == 1 and random.random()*modifier < 0.1):
                          interesting = 1
                          print("You find a metalic safe, the code was written on a sticky note")
                          chestlootable()
                          print()
                      if(alive == 1 and random.random()*modifier < 0.1):
                          interesting = 1
                          print("You find a wooden box labeled ''Personal affects'' it was easy to open")
                          chestlootable()
                          print()
                      if(alive == 1 and random.random()*modifier < 0.1):
                          interesting = 1
                          print("You find an open safe")
                          chestlootable()
                          print()
                      if(alive == 1 and random.random()*modifier < 0.1):
                          interesting = 1
                          print("You find a mostly-intact first-aid box")
                          lootable(0.4,"Herb",4)
                          lootable(0.9,"Bandage",4)
                          print()
                      if(1/random.random() > modifier):
                            print("The shelves are mostly barren")
                            defaultlootable(1)
                      elif(1/random.random() > modifier):
                            print("The shelves are stocked with junk")
                            defaultlootable(2)
                      elif(1/random.random() > modifier):
                            print("The shelves have some goodies on them")
                            chestlootable()
                      elif(1/random.random() > modifier):
                            print("The shelves have lots of goodies on them")
                            chestlootable()
                            chestlootable()
                      else:
                            print("The shelves are empty")
                else:
                        print("You leave it be")
            if(alive == 1 and (1/((modifier+5)*30))>random.random()):
                if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=5):
                    print("THERE ARE A BUNCH OF VICOUS MONSTERS DOWN THERE. YOU MUST ATTACK THEM")
                    print("THEY WILL EAT YOU IF YOU DON'T")
                else:
                    if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                        print("You smell a campfire nearby, and you can hear some chatter. What do you do?")
                    else:
                        print("There is a small camp, with makeshift tents and a small campfire, You can see a few scavengers walking about. What do you do?")
                print("1) Attack them!")
                print("2) Talk to them")
                print("3) Leave them be")
                choice = input()
                if(len(choice) > 0 and choice[0] == "1"):
                    print("You get the jump on them")
                    scavengers = int(3+((random.random()-0.5)*4))
                    for i in range(scavengers):
                        if(alive == 1):
                            if(alive == 1):
                                entercombat("scavenger",1)
                                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                    print("You defeat a scavenger,",end="")
                                    if(i!=scavengers):
                                        print("Some still remain")
                                    else:
                                        print()
                                else:
                                    print(str(i+1)+"/"+str(scavengers)+" defeated")
                elif(choice == "2"):
                    if(random.random()>0.1*modifier):
                        if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=5):
                            print("THEY ARE GIVING YOU THINGS")
                            print("IT MUST BE A TRAP")
                            for i in range(int(inventory[finditem("Insanity")][1]/10)):
                                print("KILL!",end="")
                        else:
                            print("You introduce yourself, they are rather nice")
                            if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                print("They are very respectfull of your blindness")
                            print("They offer a few piles of scrap")
                        lootable(0.8,"Coin",10)
                        count=1
                        if(modifier<8):
                            count+=1
                        if(modifier<5):
                            count+=1
                        defaultlootable(count)
                        print("Do you want to attack them?(Y/N)")
                        attack=variableify(input())
                        if(len(attack) > 0 and attack[0] == "Y"):
                            print("You get the jump on them")
                            scavengers = int(3+((random.random()-0.5)*4))
                            for i in range(scavengers):
                                if(alive == 1):
                                    entercombat("scavenger",1)
                                    if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                        print("You defeat a scavenger,",end="")
                                        if(i!=scavengers):
                                            print("Some still remain")
                                        else:
                                            print()
                                    else:
                                        print(str(i+1)+"/"+str(scavengers)+" defeated")
                        else:
                            print("You leave their camp")
                    elif(random.random()>0.05*modifier):
                        if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=5):
                            print("THEY ARE NOT ATTACKING, THEY ARE WAITING FOR YOU TO TURN YOUR BACK")
                            print("YOU MUST ATTACK THEM FIRST")
                            for i in range(int(inventory[finditem("Insanity")][1]/10)):
                                print("KILL!",end="")
                        else:
                            print("They are not hostile, in fact, they just don't care about you")
                        print("Do you want to attack them?(Y/N)")
                        attack=variableify(input())
                        if(len(attack) > 0 and attack[0] == "Y"):
                            print("You get the jump on them")
                            scavengers = int(3+((random.random()-0.5)*4))
                            for i in range(scavengers):
                                if(alive == 1):
                                    entercombat("scavenger",1)
                                    if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                        print("You defeat a scavenger,",end="")
                                        if(i!=scavengers):
                                            print("Some still remain")
                                        else:
                                            print()
                                    else:
                                        print(str(i+1)+"/"+str(scavengers)+" defeated")
                        else:
                            print("you let them leave")
                    else:
                        print("They attack")
                        scavengers = int(3+((random.random()-0.5)*4))
                        for i in range(scavengers):
                            if(alive == 1):
                                entercombat("scavenger",0)
                                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                    print("You defeat a scavenger,",end="")
                                    if(i!=scavengers):
                                        print("Some still remain")
                                    else:
                                        print()
                                else:
                                    print(str(i+1)+"/"+str(scavengers)+" defeated")
                else:
                    print("You leave them be")
            if(alive == 1 and world[x][y] != "~" and world[x][y] != "W" and (1/((modifier+5)*30))>random.random()):
                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                    print("You think you have found the remains of a camp")
                else:
                    print("You find an abandoned trapper's station")
                lootable(0.5,"Wooden Trap",0)
                lootable(0.5,"Bear Trap",0)
                lootable(0.1,"Makeshift Sword",0)
                lootable(0.5,"Fur",10)
                lootable(0.5,"Raw Food",10)
                lootable(0.5,"Hide",10)
                print()
            if(alive == 1 and world[x][y] != "~" and world[x][y] != "W" and (1/((modifier+5)*30))>random.random()):
                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                    print("You think you have found the remains of a camp")
                else:
                    print("You find an abandoned lumber station")
                lootable(0.5,"Wood",10)
                lootable(0.1,"Iron Axe",0)
                lootable(0.5,"Makeshift Axe",1)
                lootable(0.5,"Stick",20)
                lootable(0.5,"Food",10)
                lootable(0.5,"Water",10)
                print()
            if(alive == 1 and world[x][y] != "~" and world[x][y] != "W" and (1/((modifier+5)*30))>random.random()):
                if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                    print("You think you have found the remains of a camp")
                else:
                    print("You find an abandoned campsite")
                lootable(0.1,"Campfire",0)
                lootable(0.5,"Tinder",3)
                lootable(0.5,"Water",10)
                lootable(0.5,"Food",10)
                lootable(0.25,"Firepit",1)
                defaultlootable(2)
                print()
            if(alive == 1 and world[x][y] != "~" and world[x][y] != "W" and (1/((modifier+5)*30))>random.random()):
              if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                  print("You hear something in the distance")
              else:
                  if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                      print("You see a mind control tower")
                      if(inventory[finditem("Insanity")][1] > 10):
                          print("They are scanning your big smart brain")
                          print("You do not have a tin foil hat so you are unprotected")
                  else:
                      print("You see a radio tower",end = "")
              if(0.05*modifier>random.random()):
                  print()
                  if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                      print("Do you want to investigate")
                  else:
                      if(0.05*modifier>random.random()):
                          print("The tower is beyond repair")
                      elif(random.random()<0.2):
                          print("The tower is mostly rubble")
                      elif(random.random()<0.2):
                          print("The tower is clearly beyond repair")
                      if(0.2>random.random()):
                          print("You even find that some of the walls have caved in")
                      if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                          print("However, you do find the secret "+items[round(random.random()*(len(items)-1))]+" lair")
                      print("Do you want to try to look for scavengable scrap?(Y/N)")
                  scavenge = variableify(input())
                  if(len(scavenge) == 0 or scavenge[0] == "N"):
                      print("You don't risk getting too close, instead you leave")
                  else:
                      if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                          print("You move towards the sound, There seems to be ruins")
                      else:
                          print("You look around the ruins")
                      lootable(0.9,"Scrap",10)
                      lootable(0.9,"Electronic Component",5)
                      if(random.random() < 0.1*modifier):
                          if(random.random()<0.5):
                              print("A monster jumps out of the ruins!")
                              entercombat("mutantman",1)
                          else:
                              print("You find a giant monster is lurking in the ruins")
                              entercombat("@Giant",0)
                          if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                              print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
              else:
                  if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                      if(random.random()<0.1):
                          print(", you hear the cracle of a fire")
                      elif(random.random()<0.1):
                          print(", you only hear a few bugs crawing around")
                      elif(random.random()<0.1):
                          print(", you hear growls from the inside")
                      else:
                          print()
                  else:
                      if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 0):
                          print("It looks like a "+items[round(random.random()*(len(items)-1))])
                      else:
                          if(random.random()<0.1):
                              print(", it looks highly degraded")
                          elif(random.random()<0.1):
                              print(", it looks mostly destroyed")
                          elif(random.random()<0.1):
                              print(", it is covered in rust")
                          elif(random.random()<0.1):
                              print(", it is starting to rust")
                          elif(random.random()<0.1):
                              print(", there are signs of dis-repair")
                          elif(random.random()<0.1):
                              print(", it looks pristine on the outside")
                          else:
                              print()
                  if(random.random()<0.1):
                      if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                          print("You hear multiple people talking to eachother")
                      else:
                          print("You see the flag of the United States hanging on a flagpole")
                          print("Several military men are standing outside, they have a small baricade set up")
                      print("Do you want to approach?(Y/N)")
                      scavenge = variableify(input())
                      if(len(scavenge) == 0 or scavenge[0] == "N"):
                          print("You do not approach, instead you leave the area")
                      else:
                          militarybase("radio")
                  elif(random.random()<0.1):
                      if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                          print("You hear multiple people talking to eachother")
                      else:
                          print("The radio tower is covered in colorfull paint.")
                          print("Several people in clown makeup are standing around")
                      print("Do you want to approach?(Y/N)")
                      scavenge = variableify(input())
                      if(len(scavenge) == 0 or scavenge[0] == "N"):
                          print("You do not approach, instead you leave the area")
                      else:
                          clownbase("radio")
                  else:
                      print("Do you want to try to go inside?(Y/N)")
                      scavenge = variableify(input())
                      if(len(scavenge) == 0 or scavenge[0] == "N"):
                          print("You don't risk entering, instead you leave")
                      else:
                          print("You begin to move through the cabin")
                          print()
                          interesting = 0
                          for rooms in range(int(10*random.random())):
                              if(alive == 1 and interesting != 0):
                                  print("\nYou enter a new room\n")
                                  interesting = 0
                              lootable(0.1,"Electronic Component",2)
                              lootable(0.5,"Scrap",2)
                              if(alive == 1 and random.random() < 0.01 * modifier):
                                  interesting = 1
                                  if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                      print("You hear unnatural growling from the room")
                                  else:
                                      if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                          print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                                      else:
                                          print("In the middle of the room, there is some sort of mutant")
                                  entercombat("mutantman",1)
                                  print()
                              elif(alive == 1 and random.random() < 0.01*modifier):
                                  interesting = 1
                                  if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                      print("You hear unnatural growling from the room")
                                  else:
                                      if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                          print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                                      else:
                                          print("A giant monster sits in the corner of the room")
                                  entercombat("@Giant",1)
                                  print()
                              elif(alive == 1 and random.random() < 0.01*modifier):
                                  interesting = 1
                                  if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                      print("You hear unnatural growling from the room")
                                  else:
                                      if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                          print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                                      else:
                                          print("A giant monster sits in the corner of the room")
                                      print("a girder is holding the giant in place")
                                  entercombat("@Giant",2)
                                  print()
                              if(alive == 1 and random.random() < 0.01 * modifier):
                                  interesting = 1
                                  if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                      print("You are attacked from nowhere!")
                                  else:
                                      if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                          print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                                      else:
                                          print("A mutant jumps out from a closet!")
                                  entercombat("mutantman",0)
                                  print()
                              if(alive == 1 and random.random() < 0.01 * modifier):
                                  interesting = 1
                                  if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                      print("You are attacked from nowhere!")
                                  else:
                                      if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                          print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                                      else:
                                          print("A mutant jumps out from the darkness!")
                                  entercombat("mutantman",0)
                                  print()
                              if(alive == 1 and random.random()*modifier < 0.1):
                                  interesting = 1
                                  print("You find an unlocked locker in one corner of the room")
                                  chestlootable()
                                  print()
                              if(alive == 1 and random.random()*modifier < 0.1):
                                  interesting = 1
                                  print("You find a metalic safe, the code was written on a sticky note")
                                  chestlootable()
                                  print()
                              if(alive == 1 and random.random()*modifier < 0.1):
                                  interesting = 1
                                  print("You find a wooden box labeled ''Personal affects'' it was easy to open")
                                  chestlootable()
                                  print()
                              if(alive == 1 and random.random()*modifier < 0.1):
                                  interesting = 1
                                  print("You find an open safe")
                                  chestlootable()
                                  print()
                              if(alive == 1 and random.random()*modifier < 0.1):
                                  interesting = 1
                                  print("You find a mostly-intact first-aid box")
                                  lootable(0.4,"Herb",4)
                                  lootable(0.9,"Bandage",4)
                                  print()
                              if(alive == 1 and random.random()*modifier < 0.1):
                                  interesting = 1
                                  print("You find a collapsed section of building")
                                  lootable(1,"Scrap",10)
                                  print()
                              if(alive == 1 and random.random()*modifier < 0.1):
                                  interesting = 1
                                  print("You find a small camp, it seems someone was here recently")
                                  if(random.random() < 0.1*modifier):
                                      if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                          print("You hear a "+items[round(random.random()*(len(items)-1))]+" talk about "+items[round(random.random()*(len(items)-1))])
                                      else:
                                          print("You hear a voice 'GET AWAY FROM MY STUFF'")
                                      if(entercombat("@Survivor",1)):
                                          print()
                                          chestlootable()
                                          print()
                                  else:
                                      print()
                                      chestlootable()
                                      print()
                              if(alive == 1 and random.random() < 0.01 * modifier):
                                  interesting = 1
                                  if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                      print("You hear growling from the exit")
                                  print("A mutant creature is blocking the exit of the room")
                                  entercombat("mutantman",1)
                                  print()
                          if(alive == 1):
                              dam = int(random.random()*2*modifier)
                              if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                  print("You enter a new room")
                                  print("You feel out a cold metalic table",end="")
                                  if(dam < 12):
                                      print(" containing some radio hardware. It is ",end="")
                                  else:
                                      print("")
                              else:
                                  if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                      print("You think there should be a bad, evil box of evil. It is ",end="")
                                  else:
                                      print("You find the main radio control")
                                  print("The radio hardware is ",end="")
                              if(dam < 1):
                                  print("pristine")
                              elif(dam < 2):
                                  print("in good condition")
                              elif(dam < 3):
                                  print("in reasonable condition")
                              elif(dam < 4):
                                  print("in need of maintenence")
                              elif(dam < 5):
                                  print("in desperate need of maintenence")
                              elif(dam < 6):
                                  print("in need of minor repairs")
                              elif(dam < 7):
                                  print("in need of repairs")
                              elif(dam < 8):
                                  print("in desperate need of repairs")
                              elif(dam < 9):
                                  print("in desperate need of signifigant repairs")
                              elif(dam < 10):
                                  print("beyond repair")
                              elif(dam < 11):
                                  print("completly destroyed")
                              elif(dam < 12):
                                  print("beyond salvageable")
                              else:
                                  if(finditem("curse of blindness") ==-1 or inventory[finditem("curse of blindness")][1] <= 0):
                                      print("missing")
                              if(dam < 9):
                                  print("What do you want to do?(Y/N")
                                  if(dam < 3):
                                      print("1) Activate it")
                                  else:
                                      print("1) Try to get it working")
                                  print("2) Scrap it")
                                  print("3) Ignore it and leave")
                                  decision = int(valid(input("I will: ")))
                                  while(decision > 3):
                                      decision = int(valid(input("I will: ")))
                                  if(decision == 1):
                                      scrap = 0
                                      comp = 0
                                      if(dam < 6 and dam > 5):
                                          scrap = int(random.random()*0.5*modifier)
                                      elif(dam < 7):
                                          scrap = int(random.random()*modifier)
                                          comp = int(random.random()*0.5*modifier)
                                      elif(dam < 8):
                                          comp = int(random.random()*0.5*modifier)
                                          scrap = int(random.random()*1.5*modifier)
                                      else:
                                          comp = int(random.random()*modifier)
                                          scrap = int(random.random()*2*modifier)
                                      if(scrap > 0):
                                          print("You will need")
                                          print(int_to_en(scrap)+" pieces of scrap")
                                      else:
                                          print("You will not need scrap")
                                      if(scrap > 0):
                                          print("You will need")
                                          print(int_to_en(scrap)+" components")
                                      else:
                                          print("You will not need components")
                                      print()
                                      if(scrap != 0 and not(finditem("Scrap")==-1 or inventory[finditem("Scrap")][1]<scrap)):
                                          if(comp != 0 and not(finditem("Electronic Component")==-1 or inventory[finditem("Electronic Component")][1]<comp)):
                                              print("You do not have enough of anything")
                                              decision == 2
                                          else:
                                              print("You do not have enough scrap")
                                              decision == 2
                                      elif(comp != 0 and not(finditem("Electronic Component")==-1 or inventory[finditem("Electronic Component")][1]<comp)):
                                          print("You do not have enough components")
                                          decision == 2
                                      else:
                                          if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                              print("DO NOT FIX THE BAD BOX")
                                          print("Do you want to begin?")
                                          repair=variableify(input())
                                          while(len(repair) == 0 or (repair[0] != "Y" and repair[0] != "N")):
                                              repair=variableify(input())
                                          if(repair[0] == "Y"):
                                              if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                                  print("You are an idiot for making the bad box work")
                                                  print("It can now mind controll you from a distance!")
                                                  print("what have you done?")
                                                  input()
                                                  print("What Have You Done?!?")
                                                  input()
                                                  print("WhAt HaVe YoU DoNe?!?!?")
                                                  input()
                                                  print("WHAT HAVE YOU DONE?!?!?!?")
                                                  input()
                                              else:
                                                  print("With a little bit of time, you manage to turn the radio on")
                                                  print("The radio station has a portable control console, which would allow you to control the radio tower from anywhere")
                                              addstuff("Radio Controller",1)
                                          else:
                                              print("You decide that it isn't worth the scrap")
                                              decision == 2
                                  if(decision == 2):
                                      print("You take it apart")
                                      lootable(0.9,"Scrap",2*int(11-dam))
                                      lootable(0.9,"Electronic Component",int(11-dam))
                              elif(dam < 11):
                                  print("You take it apart")
                                  lootable(0.9,"Scrap",2*int(11-dam))
                                  lootable(0.9,"Electronic Component",int(11-dam))
                              else:
                                  print("You leave the shack")
            if(alive == 1 and world[x][y] != "~" and world[x][y] != "W" and (1/(modifier*30))>random.random()):
              print("You come across a ",end = "")
              if(random.random()<0.1):
                  print("tiny ",end="")
              elif(random.random()<0.1):
                  print("small ",end="")
              elif(random.random()<0.1):
                  print("puny ",end="")
              elif(random.random()<0.1):
                  print("miniscule ",end="")
              elif(random.random()<0.1):
                  print("completly unimpressive ",end="")
              if(0.05*modifier>random.random()):
                  if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 0):
                          if(random.random()<0.1):
                              print("trout")
                          elif(random.random()<0.1):
                              print("samon")
                          elif(random.random()<0.1):
                              print("tuna")
                          elif(random.random()<0.1):
                              print("catfish")
                          elif(random.random()<0.1):
                              print("sea-horse")
                          elif(random.random()<0.1):
                              print("shark")
                          else:
                              print("fish")
                  else:
                      if(0.05*modifier>random.random()):
                          if(random.random()<0.1):
                              print("building")
                          elif(random.random()<0.1):
                              print("home")
                          elif(random.random()<0.1):
                              print("house")
                          elif(random.random()<0.1):
                              print("shack")
                          elif(random.random()<0.1):
                              print("store")
                          elif(random.random()<0.1):
                              print("shop")
                          else:
                              print("shelter")
                  if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 0):
                      print("Fish contain magical jems in their throats")
                      print("Do you want to go inside the fish?(Y/N)")
                  else:
                      if(random.random()<0.2):
                          print("It is not useable, but you might be able to scavenge")
                      elif(random.random()<0.2):
                          print("It is mostly rubble")
                      elif(random.random()<0.2):
                          print("It is barely even held together")
                      if(0.2>random.random()):
                          print("You even find that some of the walls have caved in")
                      print("Do you want to try to look for scavengable scrap?(Y/N)")
                  scavenge = variableify(input())
                  if(len(scavenge) == 0 or scavenge[0] == "N"):
                      print("You don't risk getting too close, instead you leave")
                  else:
                      if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 0):
                          print("You look around the fish")
                      else:
                          print("You look around the ruins")
                      lootable(0.9,"Scrap",10)
                      lootable(0.9,"Electronic Component",5)
                      if(random.random() < 0.1*modifier):
                          if(random.random()<0.5):
                              print("A monster jumps out of the ruins!")
                              entercombat("mutantman",1)
                          else:
                              print("You find a giant monster is lurking in the ruins")
                              entercombat("@Giant",0)
              else:
                  if(random.random()<0.1):
                      print(", partialy destroyed, ",end="")
                  elif(random.random()<0.1):
                      print(", damaged, ",end="")
                  elif(random.random()<0.1):
                      print(", rusting, ",end="")
                  elif(random.random()<0.1):
                      print(", shattered, ",end="")
                  if(random.random()<0.1):
                      print("building")
                  elif(random.random()<0.1):
                      print("home")
                  elif(random.random()<0.1):
                      print("house")
                  elif(random.random()<0.1):
                      print("shack")
                  elif(random.random()<0.1):
                      print("store")
                  elif(random.random()<0.1):
                      print("shop")
                  else:
                      print("shelter")
                  print("It does not look to be inhabited")
                  print("Do you want to enter?(Y/N)")
                  scavenge = variableify(input())
                  if(len(scavenge) == 0 or scavenge[0] == "N"):
                      print("You don't risk getting too close, instead you leave")
                  else:
                      interesting = 0
                      for rooms in range(int(6*random.random())):
                          if(alive == 1 and interesting != 0):
                              print("\nYou enter a new room\n")
                              interesting = 0
                          lootable(0.1,"Electronic Component",2)
                          lootable(0.5,"Scrap",2)
                          if(alive == 1 and random.random() < 0.01 * modifier):
                              interesting = 1
                              if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                  print("You hear unnatural growling from the room")
                              else:
                                  if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                      print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                                  else:
                                      print("In the middle of the room, there is some sort of mutant")
                              entercombat("mutantman",1)
                              print()
                          elif(alive == 1 and random.random() < 0.01*modifier):
                              interesting = 1
                              if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                  print("You hear unnatural growling from the room")
                              else:
                                  if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                      print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                                  else:
                                      print("A giant monster sits in the corner of the room")
                              entercombat("@Giant",1)
                              print()
                          elif(alive == 1 and random.random() < 0.01*modifier):
                              interesting = 1
                              if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                  print("You hear unnatural growling from the room")
                              else:
                                  if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                      print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                                  else:
                                      print("A giant monster sits in the corner of the room")
                                  print("a girder is holding the giant in place")
                              entercombat("@Giant",2)
                              print()
                          if(alive == 1 and random.random() < 0.01 * modifier):
                              interesting = 1
                              if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                  print("You are attacked from nowhere!")
                              else:
                                  if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                      print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                                  else:
                                      print("A mutant jumps out from a closet!")
                              entercombat("mutantman",0)
                              print()
                          if(alive == 1 and random.random() < 0.01 * modifier):
                              interesting = 1
                              if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                  print("You are attacked from nowhere!")
                              else:
                                  if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                      print("You are attacked by a "+items[round(random.random()*(len(items)-1))])
                                  else:
                                      print("A mutant jumps out from the darkness!")
                              entercombat("mutantman",0)
                              print()
                          if(alive == 1 and random.random()*modifier < 0.1):
                              interesting = 1
                              print("You find an unlocked locker in one corner of the room")
                              chestlootable()
                              print()
                          if(alive == 1 and random.random()*modifier < 0.1):
                              interesting = 1
                              print("You find a metalic safe, the code was written on a sticky note")
                              chestlootable()
                              print()
                          if(alive == 1 and random.random()*modifier < 0.1):
                              interesting = 1
                              print("You find a wooden box labeled ''Personal affects'' it was easy to open")
                              chestlootable()
                              print()
                          if(alive == 1 and random.random()*modifier < 0.1):
                              interesting = 1
                              print("You find an open safe")
                              chestlootable()
                              print()
                          if(alive == 1 and random.random()*modifier < 0.1):
                              interesting = 1
                              print("You find a mostly-intact first-aid box")
                              lootable(0.4,"Herb",4)
                              lootable(0.9,"Bandage",4)
                              print()
                          if(alive == 1 and random.random()*modifier < 0.1):
                              interesting = 1
                              print("You find a collapsed section of building")
                              lootable(1,"Scrap",10)
                              print()
                          if(alive == 1 and random.random()*modifier < 0.1):
                              interesting = 1
                              print("You find a small camp, it seems someone was here recently")
                              if(random.random() < 0.1*modifier):
                                  if(finditem("Insanity") !=-1 and inventory[finditem("Insanity")][1] > 5):
                                      print("You hear a "+items[round(random.random()*(len(items)-1))]+" talk about "+items[round(random.random()*(len(items)-1))])
                                  else:
                                      print("You hear a voice 'GET AWAY FROM MY STUFF'")
                                  if(entercombat("@Survivor",1)):
                                      print()
                                      chestlootable()
                                      print()
                              else:
                                  print()
                                  chestlootable()
                                  print()
                          if(alive == 1 and random.random() < 0.01 * modifier):
                              interesting = 1
                              if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                  print("You hear growling from the exit")
                              print("A mutant creature is blocking the exit of the room")
                              entercombat("mutantman",1)
                              print()
            w = 0
            while(w < int(modifier)):
                w+=1
                if(alive == 1):
                    if(alive == 1 and ((((finditem("Raft")==-1 or inventory[finditem("Boat")][1] <= 0) and world[x][y] == "W") or ((finditem("Raft")==-1 or inventory[finditem("Raft")][1] <= 0) and (finditem("Boat")==-1 or inventory[finditem("Boat")][1] <= 0) and world[x][y] == "~")) and 0.005>random.random())):
                        print("You feel a strong riptide in the water")
                        print("Do you try to swim away")
                        swim = input()
                        if(len(variableify(swim)) != 0 and variableify(swim)[0] == "N"):
                            print("You get pushed around in the water")
                            if(random.random()*modifier>3):
                                addwound(1+int(modifier*random.random()))
                            lost=False
                            if(x>0 and x<width-1):
                                lost = True
                                x+=round(random.random()*2-1)
                            if(y>0 and y<height-1):
                                lost = True
                                y+=round(random.random()*2-1)
                            if(lost):
                                print("Get moved around")
                            else:
                                print("The tide does not pull you far")
                        else:
                            print("You try to fight the tide")
                            if(random.random()*modifier>1):
                                addwound(1+int(0.5*modifier*random.random()))
                        print("The riptide ends")
                        print()
                    if(alive == 1 and finditem("Unstable Bomb")!=-1 and inventory[finditem("Unstable Bomb")][1] >= 0 and inventory[finditem("Unstable Bomb")][1]*0.005>random.random()):
                        print("Your unstable explosive begins to tick, you try your best to drop it")
                        inventory[finditem("Unstable Bomb")][1]-=1
                        if(random.random()*modifier>1):
                            print("The bomb explodes nearby")
                            if(random.random()*modifier>1):
                                if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                                    addwound(4)
                                else:
                                    addwound(3)
                            else:
                                if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                                    addwound(3)
                                else:
                                    addwound(2)
                        else:
                            print("You avoid the blast")
                    if(alive == 1 and (world[x][y] == "≈") and 0.005>random.random()):
                        print("The ground below you begins to sink; Quicksand")
                        fallen = 1
                        while(alive == 1 and fallen > 0 and fallen < 10):
                            print(("~"*fallen)+"@"+"~"*(10-fallen))
                            print("Your options are:")
                            print("1) Quick but risky!")
                            print("2) Slow and safe")
                            if(finditem("Rope")!=-1 or inventory[finditem("Rope")][1] <=0):
                                print("3) Throw Rope(Note: You do not have any rope)")
                            else:
                                print("3) Throw Rope(You have "+int_to_en(inventory[finditem("Rope")][1])+")")
                            if(finditem("Stick")!=-1 or inventory[finditem("Stick")][1] <=0):
                                print("3) Use Stick(Note: You do not have any sticks)")
                            else:
                                print("3) Use Stick(You have "+int_to_en(inventory[finditem("Stick")][1])+")")
                            treefallen = False
                            if(random.random()>0.1*modifier):
                                print("5) Grab a nearby-vine")
                                treefallen = True
                            choice = int(valid(input("I will do: ")))
                            if((not(treefallen) and choice > 4) or (treefallen and choice > 5)):
                                print("You act like an idiot, and fall farther into the sand")
                                fallen+=1
                            elif(choice == 1):
                                if(random.random()>0.1*modifier):
                                    print("You quickly move farther out of the quicksand")
                                    fallen+=-1
                                else:
                                    print("Your quick actions drive you further into the quicksand")
                                    fallen+=1
                            elif(choice == 2):
                                passtime(1)
                                if(random.random()>0.05*modifier):
                                    print("You quickly move farther out of the quicksand")
                                    fallen+=-1
                                else:
                                    print("Your quick actions drive you further into the quicksand")
                                    fallen+=1
                            elif(choice == 3):
                                if(finditem("Rope")!=-1 or inventory[finditem("Rope")][1] <=0):
                                    print("You do not have any rope, but in trying to check if you have any rope, you fall deeper in quicksand")
                                    fallen+=1
                                else:
                                    print("You throw the rope and ",end="")
                                    if(random.random()>0.05*modifier):
                                        print("you bring yourself farther out of the quicksand")
                                        fallen+=-2
                                    else:
                                        print("you fall farther into quicksand")
                                        fallen+=1
                                    if(random.random()<0.05*modifier):
                                        print("you then loose the rope")
                                        addstuff("Rope",-1)
                            elif(choice == 4):
                                if(finditem("Stick")!=-1 or inventory[finditem("Stick")][1] <=0):
                                    print("You do not have any sticks, but in trying to check if you have any sticks, you fall deeper in quicksand")
                                    fallen+=1
                                else:
                                    print("You try to climb out with the stick and ",end="")
                                    if(random.random()>0.075*modifier):
                                        print("you bring yourself farther out of the quicksand")
                                        fallen+=-1
                                    else:
                                        print("you fall farther into quicksand")
                                        fallen+=1
                                    if(random.random()<0.1*modifier):
                                        print("you then loose the stick")
                                        addstuff("Stick",-1)
                            elif(choice == 5 and treefallen):
                                print("You grab the vine and ",end="")
                                if(random.random()>0.05*modifier):
                                    print("you bring yourself farther out of the quicksand")
                                    fallen+=-1
                                else:
                                    print("you fall farther into quicksand")
                                    fallen+=1
                                if(random.random()<0.1*modifier):
                                    print("then the vine snaps")
                                    treefallen = False
                            else:
                                greatjob()
                        if(fallen <= 0):
                            print("You escape the quicksand")
                        else:
                            if(alive == 1):
                                print("You suffocate")
                                inventory[finditem("Blood")][1] = 0
                                deathcheck()
                        print()
                    if(alive==1 and (world[x][y] == "M" or world[x][y] == "A") and 0.005>random.random()):
                      if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                          print("You feel a large, nearly flat face of rock. You could try to climb it, or you could find a detour")
                      else:
                          print("You are confronted by a sheer cliff face. You could try and find a detour, or you can try to climb it.")
                      print("Do you look for a detour(Y/N):")
                      detour = input()
                      if(len(variableify(detour)) != 0 and variableify(detour)[0] == "N"):
                          fallend=False
                          if(finditem("Rope")!=-1 and inventory[finditem("Rope")][1]>0):
                              print("Do you want to use your rope?")
                              rope=input()
                              if(len(variableify(rope)) != 0 and variableify(rope)[0] == "Y"):
                                  fallend=True
                                  print("You use the rope")
                                  if(random.random()*modifier>3):
                                      print("The rope snaps,",end="")
                                      addstuff("Rope",-1)
                                      if(random.random()*modifier>1):
                                          print("and you fall onto some rocks. You have to take the detour")
                                          addwound(modifier)
                                          passtime(1)
                                      else:
                                          print("but you are fine")
                                  else:
                                      if(random.random()*modifier<3):
                                          print("You climb up, just fine")
                                      else:
                                          print("Your hands slip. You fall onto some rocks, and have to take the detour")
                                          addwound(modifier)
                                          passtime(1)
                          if(fallend == False):
                              if(random.random()*modifier<2):
                                  print("You climb up, just fine")
                              else:
                                  print("You fall onto some rocks, and have to take the detour")
                                  addwound(modifier)
                                  passtime(1)
                      else:
                          print("You take a long detour around it.")
                          passtime(1)
                      print()
                    if(alive==1 and 0.005>random.random()):
                      rad = 0
                      if(finditem("Radiation Suit") == -1 or inventory[finditem("Radiation Suit")][1] <= 0):
                        rad+=2
                      if(finditem("Makeshift Radiation Suit") == -1 or inventory[finditem("Makeshift Radiation Suit")][1] <= 0):
                        rad+=1
                      if(finditem("Geiger Counter") == -1 or inventory[finditem("Geiger Counter")][1] <= 0):
                        rad=rad*2
                      else:
                        print("Your geiger counter clicks vigerously, as you quickly leave an area")
                      addstuff("Radiation",int(rad*modifier*random.random()))
                    if(alive==1 and 0.005>random.random()):
                      entercombat("@Nature",0)
                    if(alive==1 and 0.001>random.random()):
                      if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                          print("You hear the wirring of machinery, and you feel concrete below you, ",end="")
                      else:
                          print("You see a worn-down military outpost, inside is a few droids, ",end="")
                      wardrone=1+int(modifier*0.3*random.random())
                      if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                          print("You hear machinery activating")
                      else:
                          if(wardrone == 1):
                              print(int_to_en(wardrone)+" wakes up")
                          else:
                              print(int_to_en(wardrone)+" wake up")
                      for i in range(wardrone):
                          if(alive == 1):
                              entercombat("war drone",0)
                              if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                print("You defeat a robot,",end="")
                                if(i!=techs):
                                    print("Some still remain")
                                else:
                                    print()
                              else:
                                print(str(i+1)+"/"+str(wardrone)+" defeated")
                      print()
                    if(alive==1 and 0.001>random.random()):
                        if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                            print("You hear approaching machinery, then you hear scanning")
                        else:
                            print("A small droid stops by and scans you")
                        if(random.random()>0.1*modifier):
                            if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
                                print("You are under attack")
                            else:
                                print("It attacks!")
                            entercombat("@Tech",0)
                        else:
                            if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=5):
                                print("THEY ARE WIRRING LIKE AN EVIL BOX OF EVIL AND THEY LOOK LIKE A "+items[round(random.random()*(len(items)-1))])
                                print("THEY MUST DIE")
                            else:
                                print("They are not openly hostile")
                            print("Do you want to attack(Y/N)")
                            attack=variableify(input())
                            if(len(attack) > 0 and attack[0] == "Y"):
                                entercombat("@Tech",1)
                            else:
                                print("you let it go along its very way")
                        print()
                    if(alive==1 and 0.001>random.random()):
                        print("You see a roaming religous zealot, they start to shout propaganda")
                        if(random.random()>0.05*modifier):
                            print("They attack!")
                            entercombat("@Cult",0)
                        else:
                            if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=5):
                                print("THEY ARE LOOKING AT YOU weirdLY, PIERCING YOU WITH THEIR MIND LASERS")
                                print("KILL THEM!!!!")
                                print("THEY ARE DEFINITLY EVIL")
                            else:
                                print("They are not openly hostile")
                            print("Do you want to attack them?(Y/N)")
                            attack=variableify(input())
                            if(len(attack) > 0 and attack[0] == "Y"):
                                entercombat("@Cult",1)
                            else:
                                print("you let them leave")
                        print()
                    if(alive==1 and 0.002>random.random()):
                      lost=False
                      if(x>0 and x<width-1):
                        lost = True
                        x+=round(random.random()*2-1)
                      if(y>0 and y<height-1):
                        lost = True
                        y+=round(random.random()*2-1)
                      if(lost):
                        print("You get lost")
                        print()
                else:
                    w=modifier+5
            deathcheck()
            if(alive == 1):
                totalhours+=1
        else:
           k=hours+5
           print(k)
    bloodloss(hours)
    
def deathcheck():
    getinvalid(inventory)
    global modifier
    global alive
    if(alive == 1):
      if(finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1] >= 100):
          alive=0
          print("You died, Your cancer killed you")
          inventory[finditem("Cancer")][1] = 100
      elif(finditem("Blood")==-1 or inventory[finditem("Blood")][1] <= 0):
          alive=0
          inventory[finditem("Blood")][1] = 0
          print("You died, You ran out of blood")
      elif(finditem("Food")==-1 or inventory[finditem("Food")][1] <= 0):
          alive=0
          print("You died, You ran out of food")
          inventory[finditem("Food")][1] = 0
      elif(finditem("Water")==-1 or inventory[finditem("Water")][1] <= 0):
          alive=0
          print("You died, You ran out of water")
          inventory[finditem("Water")][1] = 0
    if(alive==0 and finditem("Death Amulet")!=-1 and inventory[finditem("Death Amulet")][1] > 0):
            addstuff("Death Amulet",-1)
            print("You feel the Death Amulet shake,")
            print("You are brought back from the dead,")
            if(finditem("Blood")==-1):
                print("You feel the blood rush back into your veins")
                addstuff("Blood",100)
            elif(inventory[finditem("Blood")][1]<=100):
                print("You feel the blood rush back into your veins")
                inventory[finditem("Blood")][1]=100
            if(finditem("Food")==-1):
                print("You feel your stomach filling with food")
                addstuff("Food",100)
            elif(inventory[finditem("Food")][1]<=100):
                inventory[finditem("Food")][1]=100
                print("You feel your stomach filling with food")
            if(finditem("Water")==-1):
                print("You feel your body filling with water")
                addstuff("Water",100)
            elif(inventory[finditem("Water")][1]<=100):
                print("You feel your body filling with water")
                inventory[finditem("Water")][1]=100
            if(finditem("Open Wound")!=-1):
                if(inventory[finditem("Open Wound")][1]>=0):
                    print("You feel your "+int_to_en(inventory[finditem("Open Wound")][1])+" open wounds close, Only scars remain")
                    addstuff("Scar",inventory[finditem("Open Wound")][1])
                    inventory[finditem("Open Wound")][1]=0
            if(finditem("Infection")!=-1):
                if(inventory[finditem("Infection")][1]>=0):
                    print("You feel your "+int_to_en(inventory[finditem("Infection")][1])+" infections being cleansed")
                    inventory[finditem("Infection")][1]=0
            if(finditem("Cancer")!=-1):
                if(inventory[finditem("Cancer")][1]>=0):
                    print("You feel your cancer being healed")
                    inventory[finditem("Cancer")][1]=0
            if(finditem("Radiation")!=-1):
                if(inventory[finditem("Radiation")][1]>=0):
                    print("You feel your radiation being cleansed")
                    inventory[finditem("Radiation")][1]=0
            if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
                print("You feel "+int_to_en(inventory[finditem("Venom")][1])+" Venom disappear into nothingness")
                inventory[finditem("Venom")][1]=0
            print("The death amulet crackes, All that remains is the mark of the devil")
            addstuff("Dark Mark",1)
            alive=1
            getinventory()
    elif(alive==0 and random.random() > 0.5+0.05*modifier and (finditem("Devil's Contract")==-1 or inventory[finditem("Devil's Contract")][1]<=0)):
            print()
            print("You feel somewhat odd")
            print("A powerfull, commanding presance")
            print("You feel as if you have been emptied")
            print("You feel as if you are somehow, not complete anymore, as if you are empty inside")
            print("Time feels nonexistant")
            print("You feel the burn of fire on your face, but you don't feel pain")
            print("A giant figure is towering above you, its presance is the only think you can feel")
            print("it speaks, the world shakes. The booming voice says")
            print()
            print("Well well well")
            print("Look who died")
            print("I can bring you back to life, just sign this contract")
            print("You take a better look at the figure. It is the devil")
            print("                     ")
            print("       /\__/\         ")
            print("       |O__O|  666    ")
            print("       \____/  |||    ")
            print("         ||    \X/    ")
            print("       +-++-+   |     ")
            print("     /-+666 +---+     ")
            print("     | |    |   |     ")
            print("     \_|    |   |     ")
            print("       +-++-+         ")
            print("       | || |         ")
            print("       | || |         ")
            print("      /  /\  \        ")
            print("He is wearing an evil looking smerk")
            print("You try and read the contract, but as you read you feel the burining fires of hell")
            print("With each letter, the heat gets more and more unbearable")
            print("Do you sign his contract?(Y/N)")
            contract=input()
            if(variableify(contract)[0] == "N"):
                print("Your funeral, well")
                print("Your unremarkable death in the middle of knowhere")
            elif(variableify(contract)[0] == "Y"):
                print("You put the pen to paper, and your own blood spills out")
                print("It puts your name down on the paper")
                print("Then, you feel you are now more whole inside, then, you realize you no longer feel the fire")
                if(finditem("Blood")==-1):
                    print("You feel the blood rush back into your veins")
                    addstuff("Blood",100)
                elif(inventory[finditem("Blood")][1]<=100):
                    print("You feel the blood rush back into your veins")
                    inventory[finditem("Blood")][1]=100
                if(finditem("Food")==-1):
                    print("You feel your stomach filling with food")
                    addstuff("Food",100)
                elif(inventory[finditem("Food")][1]<=100):
                    inventory[finditem("Food")][1]=100
                    print("You feel your stomach filling with food")
                if(finditem("Water")==-1):
                    print("You feel your body filling with water")
                    addstuff("Water",100)
                elif(inventory[finditem("Water")][1]<=100):
                    print("You feel your body filling with water")
                    inventory[finditem("Water")][1]=100
                if(finditem("Open Wound")!=-1):
                    if(inventory[finditem("Open Wound")][1]>=0):
                        print("You feel your "+int_to_en(inventory[finditem("Open Wound")][1])+" open wounds close, Only scars remain")
                        addstuff("Scar",inventory[finditem("Open Wound")][1])
                        inventory[finditem("Open Wound")][1]=0
                if(finditem("Infection")!=-1):
                    if(inventory[finditem("Infection")][1]>=0):
                        print("You feel your "+int_to_en(inventory[finditem("Infection")][1])+" infections being cleansed")
                        inventory[finditem("Infection")][1]=0
                if(finditem("Cancer")!=-1):
                    if(inventory[finditem("Cancer")][1]>=0):
                        print("You feel your cancer being healed")
                        inventory[finditem("Cancer")][1]=0
                if(finditem("Radiation")!=-1):
                    if(inventory[finditem("Radiation")][1]>=0):
                        print("You feel your radiation being cleansed")
                        inventory[finditem("Radiation")][1]=0
                if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
                    print("You feel "+int_to_en(inventory[finditem("Venom")][1])+" Venom disappear into nothingness")
                    inventory[finditem("Venom")][1]=0
                alive=1
                modifier+=1
                addstuff("Devil's Contract",1)
def strangedevice():
    print("It is an odd, reflective oval.")
    print("What do you want to do")
    print("1) Do not touch it")
    print("2) Mess with it")
    print("3) Try to destory it")
    alien = input()
    while(alien == "3"):
        print("You throw it on the ground, it is not even dented")
        print("What do you want to do")
        print("1) Do not touch it")
        print("2) Mess with it")
        print("3) Smash it on the ground")
        alien = input()
    if(alien != "2"):
        print("You just put it back in your pocket")
    else:
        print("You put your hands on it")
        print("It gains green glowing lines and weird blue-glowing weird symbols")
        print("It begins to make a very odd repeating noise, that seems un-natural and forign")
        print("1) Press the circle one")
        print("2) Press the spiral one")
        print("3) Press the square one")
        print("4) Press the triangle one")
        button = input()
        if(button == "1"):
            print("You press the circular button")
            print("You hear a voice")
            print("It says 'PlEaSe DoNt HuRt Me'")
            print("What do you want to say?")
            print("1) Who are you?")
            print("2) I am not going to hurt you")
            print("3) I will definity hurt you")
            print("4) Nothing")
            say = input()
            if(say != "4"):
                print("Wait, You are not one of them!")
            else:
                print("You say nothing")
                print("'pLeAsE nO'")
                print("'pLeAsE dOnT hUrT mE'")
                print("What do you want to say?")
                print("1) Who are you?")
                print("2) I am not going to hurt you")
                print("3) I will definity hurt you")
                print("4) Nothing")
                say = input()
            respond=""
            respond2=""
            respond3=""
            if(say == "1"):
                print("I don't know, I can't remember")
                print("Something was happining, I saw a light, the next thing I knew I was here")
                print("How are you talking to me?")
                print("What do you want to respond with?")
                print("1) The Truth")
                print("2) A Lie")
                print("3) Brush off the question")
                print("4) A lame Joke")
                respond = input()
                if(respond == "2"):
                    print("You say 'I, uh, am nearby' ")
                    if(random.random() > 0.1*modifier):
                        print("Okay, Uuuh, Do you know what is happening")
                    else:
                        print("Please don't lie, We need to trust eachother if we want to figure out what is going on")
                        print("Speaking of what is going on, do you have any idea? I am clueless")
                elif(respond == "3"):
                    print("You say 'It's not important'")
                    if(random.random() > 0.1*modifier):
                        print("Okay, Uuuh, Do you know what is happening")
                    else:
                        print("Don't blow it off. We need to talk to eachother if we want to figure out what is going on")
                        print("Speaking of what is going on, do you have any idea? I am clueless")
                elif(respond == "4"):
                    print("You say 'I speak with my mouth'")
                    print("You here him laugh a little bit")
                    print("Thanks, I needed that. Anyway, What is going on?")
                else:
                    print("You say 'I found a weird box and pressed a button'")
                    print("Well, that worked out well for us")
                    print("Do you know what is going on?")
            elif(say == "3"):
                print("You hear him take a few long breaths")
                print("Come on, I can understand you, you are certainly not my captors")
                print("Do you have any idea what is going on?")
            elif(say == "2"):
                print("I know, you are not one of my captors.")
                print("Speaking of which, do you know what is going on?")
            if(say == "4"):
                print("He continues to mumble, you never speak back. Eventually, the device powers off")
            else:
                print("What do you want to respond with?")
                print("1) The Truth")
                print("2) A Lie")
                print("3) Brush off the question")
                respond2 = input()
                if(respond2 == "2"):
                    print("You say 'I know whats going on, trust me'")
                    if((random.random() > 0.1*modifier) or respond == 2 or respond == 3):
                        print("You have no clue what is going on!")
                    else:
                        print("Okay, What is your plan?")
                        input()
                        print("...")
                        print("Really")
                        print("Here me out, ",end="")
                elif(respond2 == "3"):
                    print("You say 'My knowledge is not important'")
                    if((random.random() > 0.1*modifier) or respond == 2 or respond == 3):
                        print("You have no clue what is going on! We need to trust eachother!")
                    else:
                        print("Okay then, I have a bit of plan")
                else:
                    print("You tell him you don't know what is happening")
                    print("well, uh, thanks for the honesty,")
                    print("I have a bit of a plan")
                print("We should try to talk to whomever or whatever is keeping me captive")
                if(respond == 1):
                    print("Can your weird box thing talk to them?")
                else:
                    print("Can you talk to them?")
                print("What do you want to respond with?")
                print("1) Yes")
                print("2) No")
                print("3) Brush off the question")
                respond3 = input()
                while(respond3 == "3"):
                    print("You say 'That's not important'")
                    print("No, It is very important, Answer my question!")
                    print("CAN YOU TALK TO THEM OR NOT")
                    respond3 == input()
                certain = "2"
                if(respond3 == "2"):
                    print("No")
                    print("Dang, Are you sure you cannot do that?")
                    if(respond == 1):
                        print("I have seen them weird box thing talk to them, I swear")
                    else:
                        print("They must have some way to talk to eachother!")
                    print("What do you want to respond with?")
                    print("1) Yes")
                    print("2) No")
                    print("3) Brush off the question")
                    certain = input()
                    while(certain == "3"):
                        print("You say 'That's not important'")
                        print("No, It is very important, Answer my question!")
                        print("CAN YOU TALK TO THEM OR NOT")
                        certain == input()
                    if(certain == "1"):
                        print("Okay, I genuinly have no idea what todo. Maybe come back when you have found a way to talk to them")
                        print("I REALLY cannot do much from my cell")
                    else:
                        print("Great then!")
                        certain = "2"
                else:
                    print("Great!")
                if(certain == "2"):
                    print("I have been working to translate their language")
                    print("I am a linguist!")
                    print("Sadly, I am not a very good one")
                    print("When you have the oppritunity to talk to them, say \"KuMaRa\" ")
                    print("That should mean 'Take the prisoner back to the earth'")
                    print("I think")
                    print("Just try it!")
                    print()
                    if((random.random() > 0.05*modifier) and (random.random() > 0.05*modifier or (respond3 != "2")) and (random.random() > 0.05*modifier or (respond2 != "3" and respond2 != "2")) and (random.random() > 0.05*modifier or (respond != "3" and respond != "2"))):
                        print("Wait...")
                        print("That's wrong...")
                        print("Nvm! I got it!")
                        print("It should be 'LoDaNo'")
                        print("Remember that. It needs to be PERFECT")
                        print("Good luck!")
        elif(button == "2"):
            print("You press the spiral symbol")
            print("the blue lights fade off, and the noise stops")
            print("The device is now as it was when you first found it")
        elif(button == "3"):
            print("You press the square button")
            print("You hear a cacophony of odd noises")
            print("A hoard of unatural screeches and unworldly shouts")
            print("It sounds like language, buy it is not anything like any language you have ever heard")
            print("What do you want to say?")
            print("(If you don't want to say anything, leave it blank)")
            alienspeak = input()
            if(len(alienspeak) == 0):
                print("You decide to say nothing, probally a good idea")
                print("the lights fade away, and the noise stops")
                print("The device is now as it was when you first found it")
            else:
                print("You proudly say '"+alienspeak+"' into the box")
                if(variableify(alienspeak) == "KUMARA"):
                    print("The box goes silent.")
                    print("Then it erupts into cayotic, unworldy shouts")
                    print("You see as the box begins to beep, before detonating")
                    print("You take apart the scraps")
                    addstuff("Strange Device",-1)
                    addstuff("Alien Boon",1)
                    lootable(0.1,"Plasma Rifle",0)
                    lootable(0.5,"Plasma Pistol",0)
                    lootable(0.1,"Plasma Cannon",0)
                    lootable(0.1,"Plasma Shotgun",0)
                    lootable(0.1,"Plasma Sword",0)
                    lootable(0.9,"Plasma Crystal",20)
                    lootable(0.95,"Plasma Charge",30)
                    lootable(0.5,"Plasma Grenade",6)
                elif(variableify(alienspeak) == "LODANO"):
                    print("The box goes quiet. You hear a long voice from the box")
                    print("It sounds more like english, but you still cannot understand it")
                    print("After it talks for a bit, you can understand it, it is english")
                    print()
                    print("You can speak our words!\"")
                    input()
                    print("The savages can think!\"")
                    input()
                    print("We are very sorry for the capture of your friend")
                    print("He will be, returned, and we will leave. Take this as an apollogy")
                    print("We converted it for human use")
                    addstuff("Strange Device",-1)
                    addstuff("Alien Boon",1)
                    addstuff("Teleporter",1)
                    lootable(0.90,"Plasma Crystal",5)
                else:
                    print("The box goes silent, then the sounds come back")
                    print("They are much louder, then the sounds end and the lights fade off")
        elif(button == "4"):
            print("You press the triagle button")
            print("Nothing happends, the lights don't even react, and you don't get any feedback of any kind")
            print("Do you want to press it again?")
            pressit = input()
            while(len(pressit) > 0 and variableify(pressit[0]) == "Y"):
                print("You press the button")
                print("Nothing happends, the lights don't even react, and you don't get any feedback of any kind?")
                print("Do you want to press it again?(Y/N)")
                pressit = input()
            print("the blue lights fade off, and the noise stops")
            print("The device is now as it was when you first found it")
        else:
            print("You do nothing")
            print("the blue lights fade off, and the noise stops")
            print("The device is now as it was when you first found it")
def traveler():
  if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
    print("You hear mechanical bleeps coming from the distance.. Followed by what sounds like the word 'Footstep' repeated over and over again")
  else:
    print("You see something approach from the distance")
    print("                                          ")
    print("        /\/\/\/\/\/\/\/\/\ ")
    print("        {|   / \   / \  |}")
    print("        {|  | + | | + | |}")
    print("        {|   \_/   \_/  |}")
    print("        /        #       \ ")
    print("        |     \_____/    |")
    print("        \                /")
    print("         +--------------+")
    print("          ::::::::::::::")
    print()
    print("            ::::::::::")
    print()
    print("              ::::::")
    print()
  print("Hello! I am a fellow human. Look at me human all over the place")
  print("How are you doing fellow human?")
  input()
  print("I probally feel the same fellow human")
  if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1] <= 50):
    thing = items[int(round(random.random()*(len(items)-1)))]
    print("You see the 'human' turn into a "+thing)
    print("The "+thing+" looks to be made of flowers")
    print("You have no idea what is going on")
    addstuff("Flower",1)
  elif(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1] >= 1):
    print("You are hurt. As A human I know that is bad")
    print("The 'human' dispenses a bandage")
    addstuff("Bandage",1)
    print("There you go!")
  elif(finditem("Infection")!=-1 and inventory[finditem("Infection")][1] >= 1):
    print("You are infected")
    print("I can tell from my good not-robotic eyes")
    print("The 'human' dispenses some disinfectant")
    addstuff("Disinfectant",1)
  elif(finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1] >= 1):
    print("You have bad cells in you")
    print("They are growing like crazy")
    print("The 'human' dispenses a cancer treatment")
    addstuff("Cancer Treatment",1)
  elif(finditem("Radiation")!=-1 and inventory[finditem("Radiation")][1] >= 1):
    print("You have radiation")
    print("Only robots can survive radiation, you need this!")
    print("The 'human' dispenses a Radiation Treatment")
    addstuff("Radiation Treatment",1)
  elif(finditem("Food")==-1 or inventory[finditem("Food")][1] < 50):
    print("You are hungry")
    print("Us humans need sustinance")
    print("The 'human' dispenses some food")
    addstuff("Food",25)
    lootable(0.95,"Food",25)
  elif(finditem("Water")==-1 or inventory[finditem("Water")][1] < 50):
    print("You are thirsty")
    print("H2O is required for your continued existance")
    print("The 'human' dispenses some water")
    addstuff("Water",25)
    lootable(0.95,"Water",25)
  elif(finditem("Coin")==-1 or inventory[finditem("Coin")][1] < 1):
    print("You have no coins")
    print("Coins are the currency of us humans")
    print("The 'human' dispenses some coins")
    addstuff("Coin",5)
    lootable(0.95,"Coin",25)
  else:
    print("We humans have to stick together")
    print("Have some stuff I found")
    print("The 'human' dispenses some random stuff")
    defaultlootable(5)
  print()
def getodds(n):
    if(n==1):
        return("You know you can")
    elif(n>=0.9):
        return("You feel confidant that you can do it")
    elif(n>=0.8):
        return("You feel like you can")
    elif(n>=0.6):
        return("You are sligtly worried of failure")
    elif(n>=0.4):
        return("You feel like there is 50/50 odds of failure")
    elif(n>=0.3):
        return("You feel like you are more likely to fail than succeed")
    elif(n>=0.2):
        return("You are inconfidant about your odds")
    elif(n>=0.1):
        return("You are near certain it will fail")
    elif(n>=0):
        return("You are convinced it will fail")
    else:
        greatjob()
def docraft(a,b,c,AInput,ACount,BInput,BCount,Output,OutputCount,Failureodds):
    ACount = ACount * c
    BCount = BCount * c
    OutputCount = OutputCount * c
    if(Failureodds!=0):
        Failureodds*=1+(modifier*0.1)
    if(finditem("Crafting Boon")!=-1 and inventory[finditem("Crafting Boon")][1]>0):
        Failureodds*=1-(inventory[finditem("Crafting Boon")][1]*0.05)
    if(Failureodds>0.9):
        Failureodds=0.9
    if(Failureodds<0):
        Failureodds=0
    if((a==AInput and b==BInput) or (a==BInput and b==AInput)):
        print("It will take "+int_to_en(ACount)+" "+AInput+" and "+int_to_en(BCount)+" "+BInput+" and will produce "+int_to_en(OutputCount)+" "+Output)
        print(getodds(1-Failureodds))
        accept=input("(Y/N): ")
        if(variableify(accept)[0]=="Y"):
            if(craft(AInput,ACount,BInput,BCount,Output,OutputCount,Failureodds)==0):
                craft(BInput,BCount,AInput,ACount,Output,OutputCount,Failureodds)
            passtime(1)
        else:
            print("You do not try to craft the item")
def masscraft(a,b,c):
    docraft(a,b,c,"Stone",1,"Stick",1,"Makeshift Axe",1,0.3)
    docraft(a,b,c,"Leather",1,"String",1,"Makeshift Basket",1,0.3)
    docraft(a,b,c,"Empty Bottle",1,"Tinder",1,"Fire Bottle",1,0.1)
    docraft(a,b,c,"Empty Bottle",1,"Flint",1,"Poison Bottle",1,0.1)
    docraft(a,b,c,"Stick",1,"Empty Bottle",10,"Syringe",1,0.1)
    docraft(a,b,c,"Syringe",1,"Blood",25,"Blood Syringe",1,0.1)
    if(finditem("Arrow Boon")!=-1 and inventory[finditem("Arrow Boon")][1]>=1):
        docraft(a,b,c,"Rope",1,"Stick",1,"Bow",1,0.3-(0.05*inventory[finditem("Arrow Boon")][1]))
    else:
        docraft(a,b,c,"Rope",1,"Stick",1,"Bow",1,0.3)
    docraft(a,b,c,"String",1,"Stick",1,"Slingshot",1,0.1)
    if(finditem("Arrow Boon")!=-1 and inventory[finditem("Arrow Boon")][1]>=1):
        docraft(a,b,c,"Rope",1,"Bow",1,"Longbow",1,0.2-(0.05*inventory[finditem("Arrow Boon")][1]))
    else:
        docraft(a,b,c,"Rope",1,"Bow",1,"Longbow",1,0.2)
    docraft(a,b,c,"Wood",1,"Cloth",1,"Makeshift Spear",1,0.3)
    docraft(a,b,c,"Wood",1,"Iron Blade",1,"Iron Spear",1,0.3)
    docraft(a,b,c,"Stone",1,"Iron Bar",1,"Iron Blade",1,0.2)
    docraft(a,b,c,"String",1,"Iron Blade",1,"Bear Trap",1,0.2)
    docraft(a,b,c,"Iron Blade",1,"Stick",1,"Scimitar",1,0.2)
    docraft(a,b,c,"Wood",1,"Iron Bar",1,"Iron Hammer",1,0.2)
    docraft(a,b,c,"Gunpowder",1,"Cloth",1,"Makeshift Bomb",1,0.2)
    docraft(a,b,c,"Gunpowder",1,"Empty Bottle",1,"Makeshift Grenade",1,0.2)
    docraft(a,b,c,"Sand",5,"Gravel",1,"Gunpowder",1,0.1)
    docraft(a,b,c,"Wood",1,"Stick",1,"Wooden Club",1,0.2)
    docraft(a,b,c,"Wooden Club",1,"Wood",1,"Paddle",1,0.2)
    docraft(a,b,c,"Wooden Club",1,"Stone",1,"Baseball Bat",1,0.2)
    docraft(a,b,c,"Stick",1,"String",1,"Fishing Rod",1,0.2)
    docraft(a,b,c,"Leaf",1,"String",1,"Cloth",2,0.2)
    docraft(a,b,c,"Stick",1,"Cloth",1,"Torch",1,0.3)
    docraft(a,b,c,"Stick",1,"Tinder",1,"Torch",1,0.3)
    docraft(a,b,c,"Hide",10,"Cloth",5,"Makeshift Radiation Suit",1,0.3)
    docraft(a,b,c,"Leaf",1,"Cloth",1,"Tinder",1,0.2)
    docraft(a,b,c,"Wood",1,"Stone",1,"Firepit",1,0.1)
    docraft(a,b,c,"Stone",1,"String",1,"Makeshift Flail",1,0.2)
    docraft(a,b,c,"Wood",1,"String",1,"Wooden Trap",1,0.1)
    docraft(a,b,c,"Tinder",1,"Firepit",1,"Campfire",1,0.1)
    docraft(a,b,c,"Grass",1,"Leaf",1,"String",5,0.1)
    docraft(a,b,c,"Wood",1,"Leaf",100,"Raft",1,0.1)
    docraft(a,b,c,"Iron Bar",1,"Stick",1,"Pickaxe",1,0.1)
    docraft(a,b,c,"Leaf",1,"Flower",1,"Bandage",1,0.1)
    docraft(a,b,c,"Bandage",1,"Flower",1,"Herb",1,0.1)
    docraft(a,b,c,"Venom",1,"Herb",1,"Water",1,0.2)
    docraft(a,b,c,"Flower",1,"Herb",1,"Blood",10,0.2)
    docraft(a,b,c,"Water",2,"Herb",2,"Disinfectant",1,0.2)
    if(finditem("Arrow Boon")!=-1 and inventory[finditem("Arrow Boon")][1]>=1):
        docraft(a,b,c,"Stick",1,"Flint",1,"Arrow",1,0.2-(0.05*inventory[finditem("Arrow Boon")][1]))
    else:
        docraft(a,b,c,"Stick",1,"Flint",1,"Arrow",1,0.2)
    docraft(a,b,c,"Hands",2,"Leaf",1,"Basic Gloves",1,0.2)
    docraft(a,b,c,"Basic Gloves",1,"Cloth",1,"Cloth Gloves",1,0)
    docraft(a,b,c,"Cloth Gloves",1,"Hide",1,"Hide Gloves",1,0)
    docraft(a,b,c,"Hide Gloves",1,"Leather",1,"Leather Gloves",1,0)
    docraft(a,b,c,"Leather Gloves",1,"Chain",1,"Chain Gloves",1,0)
    docraft(a,b,c,"Chain Gloves",1,"Iron Bar",1,"Iron Gloves",1,0)
    docraft(a,b,c,"Dark Shard",10,"Raw Food",30,"Dark Sacrifice",1,0.2)
    docraft(a,b,c,"Ash",5,"Dark Shard",1,"Blood",25,0.1)
    docraft(a,b,c,"Bone",1,"Raw Food",1,"Dark Shard",1,0.1)
    docraft(a,b,c,"Open Wound",1,"Bandage",1,"Scar",1,0.1)
    docraft(a,b,c,"Dark Shard",1,"Scar",1,"XP",5,0.1)
    docraft(a,b,c,"Cloth",1,"Grass",1,"Paper",1,0.1)
    docraft(a,b,c,"Paper",1,"Stone",1,"Tic Tac Toe Board",1,0.1)
    docraft(a,b,c,"Map Fragment",1,"Map Fragment",1,"Map Piece",1,0)
    docraft(a,b,c,"Map Piece",1,"Map Piece",1,"Map",1,0)
    docraft(a,b,c,"Makeshift Axe",1,"Iron Bar",1,"Iron Axe",1,0.2)
    docraft(a,b,c,"Makeshift Spear",1,"Iron Bar",1,"Iron Spear",1,0.2)
    docraft(a,b,c,"Wooden Club",1,"Iron Bar",1,"Iron Sword",1,0.2)
    docraft(a,b,c,"Makeshift Flail",1,"Iron Bar",1,"Flail",1,0.2)
    docraft(a,b,c,"Chain",1,"Iron Bar",1,"Flail",1,0.2)
    docraft(a,b,c,"String",1,"Flower",12,"Flower Headwear",1,0.2)
    docraft(a,b,c,"String",1,"Cloth",1,"Rope",1,0.1)
    #Armor
    docraft(a,b,c,"Chain",1,"Iron Bar",1,"Chainmail Armor",1,0.1)
    docraft(a,b,c,"Chainmail Armor",1,"Iron Bar",1,"Knight Armor",1,0.1)
    docraft(a,b,c,"Wood",1,"Leather",1,"Wooden Armor",1,0.2)
    docraft(a,b,c,"Wooden Armor",1,"Scrap",1,"Makeshift Armor",1,0.2)
    docraft(a,b,c,"Makeshift Armor",1,"Blood",50,"Blood Armor",1,0.3)
    docraft(a,b,c,"Blood Armor",1,"Blank Scroll",1,"Magical Armor",1,0.1)
    docraft(a,b,c,"Knight Armor",1,"Blank Scroll",1,"Magical Armor",1,0.1)
    docraft(a,b,c,"Magical Armor",1,"Dark Shard",10,"Dark Armor",1,0.1)
    docraft(a,b,c,"Knight Armor",1,"Dark Shard",25,"Dark Armor",1,0.1)
    if(finditem("Alien Boon")!=-1 and inventory[finditem("Alien Boon")][1]>=1):        
        docraft(a,b,c,"Military Armor",1,"Plasma Crystal",10,"Plasma Armor",1,0.1)
    #Magical
    docraft(a,b,c,"Stone",5,"Dark Shard",1,"Ritual Chalk",10,0.1)
    docraft(a,b,c,"Paper",1,"Dark Shard",10,"Blank Scroll",1,0.1)
    docraft(a,b,c,"Blood",25,"Dark Shard",1,"Dark Shard",2,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Dark Shard",10,"Anticurse Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Tinder",5,"Fire Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"XP",25,"Monolith",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Stick",10,"Plant Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Wood",10,"Plant Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Food",10,"Food Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Herb",5,"Healing Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Disinfectant",1,"Healing Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Blood Syringe",1,"Healing Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Loot Kit",1,"Wealth Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Coin",100,"Wealth Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Blood",10,"Healing Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Stone",10,"Strike Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Rope",1,"Binding Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"String",15,"Binding Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Cloth",5,"Binding Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Water",10,"Water Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Leaf",10,"Plant Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Death Amulet",1,"Death Scroll",1,0.1)
    docraft(a,b,c,"Blank Scroll",1,"Grass",10,"Plant Scroll",1,0)
    docraft(a,b,c,"Blank Scroll",1,"Blank Scroll",1,"Blank Scroll",5,0.5)
    if(finditem("Alien Boon")!=-1 and inventory[finditem("Alien Boon")][1]>=1):        
        docraft(a,b,c,"Plasma Crystal",1,"Plasma Charge",1,"Plasma Charge",10,0.3) # Plasma Charges are ammo, Plasma Crystals are what make plasma weapons powerfull
        docraft(a,b,c,"Plasma Charge",10,"XP",1,"Plasma Crystal",1,0.2)
        docraft(a,b,c,"Plasma Crystal",1,"XP",1,"Plasma Charge",10,0.5)
        docraft(a,b,c,"Plasma Crystal",1,"Grenade",1,"Plasma Grenade",5,0.2)
    else:
        docraft(a,b,c,"Plasma Crystal",1,"Plasma Charge",1,"Plasma Charge",16,0.2) # Plasma Charges are ammo, Plasma Crystals are what make plasma weapons powerfull
        docraft(a,b,c,"Plasma Charge",8,"XP",1,"Plasma Crystal",1,0.1)
        docraft(a,b,c,"Plasma Crystal",1,"XP",1,"Plasma Charge",16,0.4)
        docraft(a,b,c,"Plasma Crystal",1,"Grenade",1,"Plasma Grenade",10,0.2)
    docraft(a,b,c,"Dark Shard",1,"Grenade",1,"Blood Grenade",5,0.2)
    if(finditem("Gun Boon")!=-1 and inventory[finditem("Gun Boon")][1]>=1):
        if(finditem("Alien Boon")!=-1 and inventory[finditem("Alien Boon")][1]>=1):
            docraft(a,b,c,"Plasma Crystal",1,"Pistol",1,"Plasma Pistol",5,0.2)
            docraft(a,b,c,"Plasma Crystal",1,"Rifle",1,"Plasma Rifle",5,0.2)
            docraft(a,b,c,"Plasma Crystal",1,"Missle Launcher",1,"Plasma Cannon",5,0.2)
            docraft(a,b,c,"Plasma Crystal",1,"Double Barrel Shotgun",1,"Plasma Shotgun",5,0.2)
            docraft(a,b,c,"Plasma Crystal",1,"Combat Shotgun",1,"Plasma Shotgun",5,0.2)
        else:
            docraft(a,b,c,"Plasma Crystal",1,"Pistol",1,"Plasma Pistol",1,0.1)
            docraft(a,b,c,"Plasma Crystal",1,"Rifle",1,"Plasma Rifle",1,0,1)
            docraft(a,b,c,"Plasma Crystal",1,"Missle Launcher",1,"Plasma Cannon",1,0.1)
            docraft(a,b,c,"Plasma Crystal",1,"Double Barrel Shotgun",1,"Plasma Shotgun",1,0.1)
            docraft(a,b,c,"Plasma Crystal",1,"Combat Shotgun",1,"Plasma Shotgun",1,0.1)
            docraft(a,b,c,"Plasma Charge",5,"Pistol",1,"Plasma Pistol",1,0.1)
            docraft(a,b,c,"Plasma Charge",5,"Rifle",1,"Plasma Rifle",1,0,1)
            docraft(a,b,c,"Plasma Charge",5,"Missle Launcher",1,"Plasma Cannon",1,0.1)
            docraft(a,b,c,"Plasma Charge",5,"Double Barrel Shotgun",1,"Plasma Shotgun",1,0.1)
            docraft(a,b,c,"Plasma Charge",5,"Combat Shotgun",1,"Plasma Shotgun",1,0.1)
        docraft(a,b,c,"Dark Shard",1,"Pistol",1,"Blood Pistol",5,0.2)
        docraft(a,b,c,"Dark Shard",1,"Rifle",1,"Blood Rifle",5,0.2)
        docraft(a,b,c,"Dark Shard",1,"Double Barrel Shotgun",1,"Blood Shotgun",5,0.2)
        docraft(a,b,c,"Dark Shard",1,"Combat Shotgun",1,"Blood Shotgun",1,0.2)
    if(finditem("Sword Boon")!=-1 and inventory[finditem("Swood Boon")][1]>=1):
        docraft(a,b,c,"Plasma Crystal",1,"Iron Sword",1,"Plasma Sword",5,0.2)
        docraft(a,b,c,"Dark Shard",1,"Iron Sword",1,"Blood Sword",5,0.2)
    deathcheck()
def addwound(wounds):
  if(finditem("curse of wounds")!=-1 and inventory[finditem("curse of wounds")][1]>=1):
    wounds=wounds*(inventory[finditem("curse of wounds")][1]+1)
  saves=0
  hits=0
  dodges = 0
  for i in range(wounds):
    if(finditem("Dodge Boon")!=-1 and inventory[finditem("Dodge Boon")][1] > 0 and random.random()<1-math.pow(0.95,inventory[finditem("Dodge Boon")][1])):
        dodges+=1
        hits-=1        
    if(finditem("Dark Armor")!=-1 and inventory[finditem("Dark Armor")][1]>0):
        if(1/random.random() < 16):
           hits=hits-1
           saves=saves+1
    elif(finditem("Plasma Armor")!=-1 and inventory[finditem("Plasma Armor")][1]>0):
       if(1/random.random() < 14):
           hits=hits-1
           saves=saves+1
    elif(finditem("Magical Armor")!=-1 and inventory[finditem("Magical Armor")][1]>0):
       if(1/random.random() < 12):
           hits=hits-1
           saves=saves+1
    elif(finditem("Military Armor")!=-1 and inventory[finditem("Military Armor")][1]>0):
       if(1/random.random() < 10):
           hits=hits-1
           saves=saves+1
    elif(finditem("Knight Armor")!=-1 and inventory[finditem("Knight Armor")][1]>0):
       if(1/random.random() < 8):
           hits=hits-1
           saves=saves+1
    elif(finditem("Blood Armor")!=-1 and inventory[finditem("Blood Armor")][1]>0):
       if(1/random.random() < 6):
           hits=hits-1
           saves=saves+1
    elif(finditem("Chainmail Armor")!=-1 and inventory[finditem("Chainmail Armor")][1]>0):
       if(1/random.random() < 4):
           hits=hits-1
           saves=saves+1
    elif(finditem("Makeshift Armor")!=-1 and inventory[finditem("Makeshift Armor")][1]>0):
       if(1/random.random() < 3):
           hits=hits-1
           saves=saves+1
    elif(finditem("Wooden Armor")!=-1 and inventory[finditem("Wooden Armor")][1]>0):
       if(1/random.random() < 2):
           hits=hits-1
           saves=saves+1
  if(dodges > 1):
        print("You dodged "+int_to_en(dodges)+" attacks")
  elif(dodges == 1):
        print("You dodged an attack")
  if(finditem("Field")!=-1 and inventory[finditem("Field")][1]>=1):
    field = 0
    if(hits>=inventory[finditem("Field")][1]):
        field=inventory[finditem("Field")][1]
        hits-=inventory[finditem("Field")][1]
        inventory[finditem("Field")][1]=0
    else:
        field=hits
        inventory[finditem("Field")][1]-=hits
        hits=0
    if(field > 1):
        print("Your forcefield absorbed "+int_to_en(field)+" attacks")
    elif(field == 1):
        print("Your forcefield absorbed an attack")
  if(hits > 1):
    print("You were wounded "+int_to_en(hits)+" times")
  elif(hits == 1):
    print("You were wounded once")
  if(saves != 0):
    print("Your armor saved you from "+int_to_en(saves)+" wounds")
  if(hits > 1):
      addstuff("Open Wound",hits)
def gameman(v):
  if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
      print("You hear quiet footsteps, something is nearby")
  else:
      print("A Stranger Approaches,")
      print("         __           ")
      print("       _|__|_         ")
      print("       |O__O|  ^^^    ")
      print("       \____/  |||    ")
      print("         ||    \X/    ")
      print("       +-++-+   |     ")
      print("     /-+    +---+     ")
      print("     | |    |   |     ")
      print("     \_|    |   |     ")
      print("       +-++-+         ")
      print("       | || |         ")
      print("       | || |         ")
      print("      /  /\  \        ")
      print()
  end=1
  if(v == 1):
    print("I have a bet for you")
  elif(v == 0):
    print("Are you any good at the game?")
  if(finditem("Dark Shard")!=-1):
      print("You feel your Dark shard speak to you")
  response=input()
  if(finditem("Dark Shard")!=-1 and (variableify(response)=="USEDARKSHARD" or variableify(response)=="DARKSHARD" or variableify(response)=="IATTACK" or variableify(response)=="IKILL")):
      print("                     ")
      print("       /\__/\         ")
      print("       |O__O|  666    ")
      print("       \____/  |||    ")
      print("         ||    \X/    ")
      print("       +-++-+   |     ")
      print("     /-+666 +---+     ")
      print("     | |    |   |     ")
      print("     \_|    |   |     ")
      print("       +-++-+         ")
      print("       | || |         ")
      print("       | || |         ")
      print("      /  /\  \        ")
      print("The Figure reveals itself to be the devil")
      print("Well, You seem to know who I am,")
      print("Wanna raise the stakes?")
      input()
      print("What? I couldn't hear you")
      input()
      print("You wanna bet your soul?")
      input()
      print("I don't care.")
      if(v == 1):
        print("if you flip the coin and get heads, I get your soul.")
        print("If you get tails, I will give you an amulet that will let you avoid my grasp once")
        print("Are you ready?")
        input()
        print("I don't care. Let the coin toss for your soul, Begin!")
      elif(v == 0):
        print("if you win, I get your soul.")
        print("If you lose, I will give you an amulet that will let you avoid my grasp once")
        print("Are you ready?")
        input()
        print("I don't care. Let the tic tac toe game for your soul, Begin!")
      if(v == 1):
        game = round(random.random())
      elif(v == 0):
        game = tictac(1)
      if(game!=1):
          if(game==-1):
              print("Ah, Unexpected. The game has tied. I will end you anyway.")
          else:
              if(v == 0):
                print("Oh well, What a pity. Heads")
              elif(v == 1):
                print("Oh well, What a pity. I won")
              print("Your soul looks nice, Now. Die")
              print("Any last words?")
              input()
          endgame()
      elif(game==1):
          if(v == 0):
            print("Ah, Tails.I am a man of my word.")
          elif(v == 1):
            print("Ah, I lost. I am a man of my word.")
          addstuff("Death Amulet",1)
          print("When you die, It will revive you")
      print("The Figure vanishes.")
      end=0
  if(end==1):
      if(v == 1):
        print("Okay, The bet is that if I flip this here coin, and get heads, you win. If its tails, you lose")
        print("So, Wanna make a bet?")
      elif(v == 0):
        print("Eh, I don't care. Wanna play?")
      if(variableify(input())[0]=="N"):
          print("Okay, Imma be on my way")
          if(v == 0):
            print("Instead you play against yourself")
            tictac(0)
      else:
          print("I am gonna take dat as a yes!")
          print("How much coin do ya wanna bet?")
          if(finditem("Coin")==-1):
              print("You don't have any coins")
          elif(inventory[finditem("Coin")][1]==0):
              print("You don't have any coins")
          elif(inventory[finditem("Coin")][1]==1):
              print("You look around in your pockets, You have one coin")
          else:
              print("You look around in your pockets, You have "+int_to_en(inventory[finditem("Coin")][1])+" coins")
          betest = False
          while(betest == False):
            betamount="0"+input()
            betest = True
            for i in range(len(betamount)):
              if((betamount[i] != "0" and betamount[i] != "1" and    betamount[i] != "2" and betamount[i] != "3" and betamount[i] != "4" and betamount[i] != "5" and  betamount[i] != "6" and betamount[i] != "7" and betamount[i] != "8" and betamount[i] != "9")):
                betest = False
          betamount = int(betamount)
          odds=1.01**(-1*betamount)
          #print(odds)
          if(random.random()>odds):
              print("Do you actualy HAVE that much money?")
              input()
              print("Let me see,")
              if(finditem("Coin")==-1 or inventory[finditem("Coin")][1]<betamount):
                  print("You dont have the coin!")
                  stabamount=1+int(random.random()*math.ceil(betamount/10))
                  if(stabamount>15):
                      stabamount=15
                  addwound(stabamount)
                  betamount=-1
              else:
                  print("Okay, Good. You have the money")
          if(betamount==0):
            if(v==1):
              print("Haha, Its only fun if you bet!")
            elif(v==0):
              print("Okay, Lets play")
              tictac(1)
              print("Good game!")
            print("The Stranger Leaves")
          elif(betamount>0):
              print("Allright! Lets do this!")
              if(v == 1):
                game = round(random.random())
              elif(v == 0):
                game = tictac(1)
              if(game==0):
                  print("Ha! I win!")
                  if(finditem("Coin")==-1 or inventory[finditem("Coin")][1]<betamount):
                      print("Wait, You ain't got the coin!")
                      print("You notice he is very unhappy")
                      print("He attempts to stab you for not being able to pay")
                      stabamount=1+int(random.random()*math.ceil(betamount/10))
                      if(stabamount>15):
                              stabamount=15
                      addwound(stabamount)
                      print("He runs off into the distance")
                  else:
                      print("It was a fun game, Now hand over the coin!")
                      print("Do you give him the coin?(Y/N)")
                      givecoin=input()
                      if(variableify(givecoin)[0]=="N"):
                          print("Wait, I ain't gettin paid?")
                          print("You notice he is unhappy")
                          print("He attempts to stab you")
                          stabamount=1+int(random.random()*math.ceil(betamount/10))
                          if(stabamount>5):
                              stabamount=5
                          addwound(stabamount)
                          print("He runs off into the distance")
                      else:
                          inventory[finditem("Coin")][1]-=betamount
              elif(game==1):
                  print("Darn, Oh well")
                  addstuff("Coin",betamount)
                  if(betamount == 1):
                      print("He leaves, one coin poorer")
                  else:
                      print("He leaves, "+int_to_en(betamount)+" coins poorer")
              else:
                  print("With a tie, He Leaves")
          else:
              print("I ain't gonna play.")
def weirdman():
  if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1] > 5):
      print("You see a bunny!")
      print("         _    _ ")
      print("        / \  / \ ")
      for i in range(int(inventory[finditem("Insanity")][1]/10)):
          print("        | |  | |  ")
      print("       _|_|__|_|_ ")
      print("      /          \ ")
      print("      | -o-  -o- | ")
      print("      |     ^    | ")
      print("      |    ~~~   | ")
      print("      \          / ")
      print("      |__________| ")
      print("    __/   <-->   \___ ")
      print("   /###\         /###\ ")
      print("   |####\       /####|")
      print("   |#####|     |#####|")
      print("   |#####|     |#####|")
      print("   |#####|     |#####|")
      print("He is a ",end="")
      for i in range(int(inventory[finditem("Insanity")][1]/10)):
          print("very ",end="")
      print("funny bunny")
      locations = ["a small tree","a large tree","a marsh with knee level water","swimmably deep water","the kracken","an empty area","a small smelter","a campfire","firepit","rock","a treasure room","an impassible wall","a weird mysterious area","unknown","a pickle","an apple","an orange","a bannana","a bannana tree","an orchard","a forrest","a library","a lemonade stand","a man with a rifle","a fifty foot monster","the devil","a tornado","a parking lot","a trash can","an elevator","a button","a tee-shirt","a very long book","a crater","the moon","the sun","Jupiter","the Kepler space telescope","some debris","a zoo","a building","your childhood home","a church","a temple","a monument","a statue"]
      print("He hops around screaming about "+locations[int(round(random.random()*(len(locations)-1)))])
      insanity = ["dies","explodes","transformes into cake","stabs you","battles you","builds a sandcastle","adopts you","tells you to pat the devil on his head","creates a python text game","kills a snake","flies away in a helicopter","throws you over a mountain","has his head turned into a mushroom","suffocates","never leaves your side","is secretly the devil","changes his name and moves to canda","tells you the secret of life is to die from bloodloss","pukes rainbows"]
      print("The bunny "+insanity[int(round(random.random()*(len(insanity)-1)))])
  else:
      if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
          print("You hear quiet footsteps, something is nearby")
      else:
          print("You see a weird man approach")
          print("       __________")
          print("      /          \ ")
          print("      | -o-  -o- | ")
          print("      |     |    | ")
          print("      |    ___   | ")
          print("      \          / ")
          print("      |__________| ")
          print("    __/   <-->   \___ ")
          print("   /###\         /###\ ")
          print("   |####\       /####|")
          print("   |#####|     |#####|")
          print("   |#####|     |#####|")
          print("   |#####|     |#####|")
          print()
      print("The end is the devil")
      print("The devil has come,")
      print("With blood to fire,")
      print("The end has come,")
      print("With Blood to fire")
      print("The end shall go")
      print("With Blood to fire")
      print()
      if(finditem("curse of blindness") !=-1 and inventory[finditem("curse of blindness")][1] > 0):
          print("you hear footsteps, leaving into the distance")
      else:
          if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1] > 0):
              insanity = ["dies","explodes","transformes into cake","stabs you","battles you","builds a sandcastle","adopts you","tells you to pat the devil on his head","creates a python text game","kills a snake","flies away in a helicopter","throws you over a mountain","has his head turned into a mushroom","suffocates","never leaves your side","is secretly the devil","changes his name and moves to canda","tells you the secret of life is to die from bloodloss","pukes rainbows"]
              print("The weird man "+insanity[int(round(random.random()*(len(insanity)-1)))])
          else:
              print("The rambling loonatic leaves")
def chestlootable():
    lootable(0.5,"Coin",50)
    lootable(0.05,"Tic Tac Toe Board",0)
    lootable(0.2,"Bone",0)
    lootable(0.01,"Iron Axe",0)
    lootable(0.01,"Loot Kit",0)
    lootable(0.1,"Makeshift Axe",0)
    lootable(0.1,"Wooden Trap",0)
    lootable(0.05,"Bear Trap",0)
    lootable(0.05,"Syringe",0)
    lootable(0.01,"Iron Bar",0)
    lootable(0.05,"Dark Shard",0)
    lootable(0.05,"Ore",0)
    lootable(0.01,"Iron Sword",0)
    lootable(0.01,"Iron Spear",0)
    lootable(0.05,"Makeshift Spear",0)
    lootable(0.05,"Makeshift Sword",0)
    lootable(0.01,"Chain",3)
    lootable(0.01,"Chainmail Armor",0)
    lootable(0.01,"Raft",0)
    lootable(0.005,"Boat",0)
    lootable(0.005,"Motorcycle",0)
    lootable(0.005,"Jetski",0)
    lootable(0.01,"Bicycle",0)
    lootable(0.001,"Hoverbike",0)
    lootable(0.001,"Strange Device",0)
    lootable(0.05,"Wooden Club",0)
    lootable(0.05,"Wooden Armor",0)
    lootable(0.05,"Blood Syringe",1)
    lootable(0.05,"Herb",2)
    lootable(0.05,"Makeshift Basket",0)
    lootable(0.05,"Fishing Rod",0)
    lootable(0.05,"Disinfectant",2)
    lootable(0.01,"Basket",0)
    lootable(0.2,"Match",5)
    lootable(0.2,"String",5)
    lootable(0.05,"Bow",0)
    lootable(0.05,"Longbow",0)
    lootable(0.1,"Arrow",5)
    lootable(0.005,"Shuriken",25)
    lootable(0.05,"Torch",1)
    lootable(0.3,"Food",50)
    lootable(0.3,"Water",20)
    lootable(0.2,"Stone",5)
    lootable(0.2,"Wood",5)
    lootable(0.3,"Stick",15)
    lootable(0.3,"Leaf",30)
    lootable(0.3,"Grass",30)
    lootable(0.3,"Cloth",30)
    lootable(0.3,"Fur",30)
    lootable(0.3,"Hide",30)
    lootable(0.3,"Leather",30)
    lootable(0.3,"Raw Food",3)
    lootable(0.02,"Pistol",0)
    lootable(0.01,"Rifle",0)
    lootable(0.005,"Blood Pistol",0)
    lootable(0.005,"Blood Rifle",0)
    lootable(0.005,"Blood Sword",0)
    lootable(0.005,"Plasma Sword",0)
    lootable(0.004,"Field Generator",0)
    lootable(0.005,"Machine Gun",0)
    lootable(0.001,"Minigun",0)
    lootable(0.005,"Flamethrower",0)
    lootable(0.005,"Plasma Pistol",0)
    lootable(0.002,"Plasma Rifle",0)
    lootable(0.002,"Plasma Shotgun",0)
    lootable(0.001,"Plasma Cannon",0)
    lootable(0.001,"Missle Launcher",0)
    lootable(0.005,"Missle",2)
    lootable(0.02,"Grenade",2)
    lootable(0.01,"Fragmentation Grenade",2)
    lootable(0.01,"Napalm Grenade",2)
    lootable(0.005,"Plasma Grenade",2)
    lootable(0.005,"Blood Grenade",2)
    lootable(0.005,"Magic Grenade",2)
    lootable(0.01,"Plasma Crystal",0)
    lootable(0.02,"Plasma Charge",2)
    lootable(0.01,"Double Barrel Shotgun",0)
    lootable(0.002,"Combat Shotgun",0)
    lootable(0.002,"Chain Shotgun",0)
    lootable(0.05,"Shotgun Shell",4)
    lootable(0.1,"Bullet",8)
    lootable(0.1,"Tinder",3)
    lootable(0.07,"Firepit",0)
    lootable(0.07,"Campfire",0)
    lootable(0.07,"Oil Can",0)
    lootable(0.1,"Paper",0)
    lootable(0.1,"Rope",2)
    lootable(0.05,"Flower Headress",0)
    lootable(0.1,"Map",0)
    lootable(0.01,"Flail",0)
    lootable(0.02,"Makeshift Flail",0)
    lootable(0.1,"Bandage",1)
    lootable(0.001,"Death Amulet",0)
    lootable(0.005,"Anticurse Scroll",0)
    lootable(0.005,"Fire Scroll",0)
    lootable(0.005,"Strike Scroll",0)
    lootable(0.005,"Food Scroll",0)
    lootable(0.005,"Water Scroll",0)
    lootable(0.005,"Plant Scroll",0)
    lootable(0.005,"Healing Scroll",0)
    lootable(0.005,"Wealth Scroll",0)
    lootable(0.005,"Binding Scroll",0)
    lootable(0.005,"Blank Scroll",0)
    lootable(0.005,"Strike Scroll",0)
    lootable(0.05, "Geiger Counter",0)
    lootable(0.05, "Radiation Treatment",0)
    lootable(0.01, "Radiation Suit",0)
    lootable(0.05, "Makeshift Radiation Suit",0)
    lootable(0.05, "Cancer Treatment",0)
def redraworld():
    global world
    world=[]
    for a in range(width):
        world.append([])
        for b in range(height):
            if(random.random()<(1-(1/(5*modifier)))):
                world[a].append(" ")
            else:
                number=random.random()
                if(number<5/20):
                    world[a].append("t")
                elif(number<10/20):
                    world[a].append("T")
                elif(number<11/20):
                    world[a].append("A")
                elif(number<12/20):
                    world[a].append("W")
                elif(number<13/20):
                    world[a].append("?")
                elif(number<14/20):
                    world[a].append("~")
                elif(number<15/20):
                    world[a].append("m")
                elif(number<20/20):
                    world[a].append("≈")
                else:
                    greatjob()
    for i in range (5):
        for a in range(width):
            for b in range(height):
                #Monolith
                if(random.random() < 0.0005*(1/modifier)):
                    if(a>0 and b>0 and a<width-1 and b<height-1):
                        world[a-1][b] = "?"
                        world[a][b] = "|"
                        world[a+1][b] = "?"
                        world[a][b-1] = "?"
                        world[a][b+1] = "?"
                #Lakes
                if(world[a][b] == "W"):
                    if(a>0 and random.random()>0.95):
                        world[a-1][b] = "W"
                    if(b>0 and random.random()>0.95):
                        world[a][b-1] = "W"
                    if(a<width-1 and random.random()>0.95):
                        world[a+1][b] = "W"
                    if(b<height-1 and random.random()>0.95):
                        world[a][b+1] = "W"
                if(world[a][b] == "W"):
                    if(a>0 and world[a-1][b] == " "):
                        world[a-1][b] = "~"
                    if(b>0 and world[a][b-1] == " "):
                        world[a][b-1] = "~"
                    if(a<width-1 and world[a+1][b] == " "):
                        world[a+1][b] = "~"
                    if(b<height-1 and world[a][b+1] == " "):
                        world[a][b+1] = "~"
                if(world[a][b] == "~"):
                    if(a>0 and world[a-1][b] == " " and random.random()>0.97):
                        world[a-1][b] = "~"
                    if(b>0 and world[a][b-1] == " " and random.random()>0.97):
                        world[a][b-1] = "~"
                    if(a<width-1 and world[a+1][b] == " " and random.random()>0.97):
                        world[a+1][b] = "~"
                    if(b<height-1 and world[a][b+1] == " " and random.random()>0.97):
                        world[a][b+1] = "~"
                #Mountains
                if(world[a][b] == "A"):
                    if(a>0 and random.random()>0.99):
                        world[a-1][b] = "A"
                    if(b>0 and random.random()>0.99):
                        world[a][b-1] = "A"
                    if(a<width-1 and random.random()>0.99):
                        world[a+1][b] = "A"
                    if(b<height-1 and random.random()>0.99):
                        world[a][b+1] = "A"
                if(world[a][b] == "A"):
                    if(a>0 and random.random()>0.99):
                        world[a-1][b] = "M"
                    if(b>0 and random.random()>0.99):
                        world[a][b-1] = "M"
                    if(a<width-1 and random.random()>0.99):
                        world[a+1][b] = "M"
                    if(b<height-1 and random.random()>0.99):
                        world[a][b+1] = "M"
                if(world[a][b] == "M"):
                    if(a>0 and random.random()>0.99):
                        world[a-1][b] = "A"
                    if(b>0 and random.random()>0.99):
                        world[a][b-1] = "A"
                    if(a<width-1 and random.random()>0.99):
                        world[a+1][b] = "A"
                    if(b<height-1 and random.random()>0.99):
                        world[a][b+1] = "A"
                if(world[a][b] == "M"):
                    if(a>0 and random.random()>0.99):
                        world[a-1][b] = "M"
                    if(b>0 and random.random()>0.99):
                        world[a][b-1] = "M"
                    if(a<width-1 and random.random()>0.99):
                        world[a+1][b] = "M"
                    if(b<height-1 and random.random()>0.99):
                        world[a][b+1] = "M"
                if(world[a][b] == "M"):
                    if(a>0 and random.random()>0.95):
                        world[a-1][b] = "w"
                    if(b>0 and random.random()>0.95):
                        world[a][b-1] = "w"
                    if(a<width-1 and random.random()>0.95):
                        world[a+1][b] = "w"
                    if(b<height-1 and random.random()>0.95):
                        world[a][b+1] = "w"
                if(world[a][b] == "w"):
                    if(a>0 and random.random()>0.99):
                        world[a-1][b] = "w"
                    if(b>0 and random.random()>0.99):
                        world[a][b-1] = "w"
                    if(a<width-1 and random.random()>0.99):
                        world[a+1][b] = "w"
                    if(b<height-1 and random.random()>0.99):
                        world[a][b+1] = "w"
                #Light foresting
                if(world[a][b] == "T"):
                    if(a>0 and random.random()>0.99):
                        world[a-1][b] = "T"
                    if(b>0 and random.random()>0.99):
                        world[a][b-1] = "T"
                    if(a<width-1 and random.random()>0.99):
                        world[a+1][b] = "T"
                    if(b<height-1 and random.random()>0.99):
                        world[a][b+1] = "T"
                if(world[a][b] == "T"):
                    if(a>0 and random.random()>0.95):
                        world[a-1][b] = "t"
                    if(b>0 and random.random()>0.95):
                        world[a][b-1] = "t"
                    if(a<width-1 and random.random()>0.95):
                        world[a+1][b] = "t"
                    if(b<height-1 and random.random()>0.95):
                        world[a][b+1] = "t"
                if(world[a][b] == "t"):
                    if(a>0 and random.random()>0.99):
                        world[a-1][b] = "T"
                    if(b>0 and random.random()>0.99):
                        world[a][b-1] = "T"
                    if(a<width-1 and random.random()>0.99):
                        world[a+1][b] = "T"
                    if(b<height-1 and random.random()>0.99):
                        world[a][b+1] = "T"
                #Light deserting
                if(world[a][b] == "≈"):
                    if(a>0 and random.random()>1.1-modifier*0.03):
                        world[a-1][b] = "≈"
                    if(b>0 and random.random()>1.1-modifier*0.03):
                        world[a][b-1] = "≈"
                    if(a<width-1 and random.random()>1.1-modifier*0.03):
                        world[a+1][b] = "≈"
                    if(b<height-1 and random.random()>1.1-modifier*0.03):
                        world[a][b+1] = "≈"
                #Cleanup: Mountains and lakes side by side both barely makes sense, and looks TERRIBLE
                if(world[a][b] == "W"):
                    if(a>0 and world[a-1][b] == "A"):
                        world[a][b] = "m"
                    if(b>0 and world[a][b-1] == "A"):
                        world[a][b] = "m"
                    if(a<width-1 and world[a+1][b] == "A"):
                        world[a][b] = "m"
                    if(b<height-1 and world[a][b+1] == "A"):
                        world[a][b] = "m"
                if(world[a][b] == "~"):
                    if(a>0 and world[a-1][b] == "A"):
                        world[a][b] = "m"
                    if(b>0 and world[a][b-1] == "A"):
                        world[a][b] = "m"
                    if(a<width-1 and world[a+1][b] == "A"):
                        world[a][b] = "m"
                    if(b<height-1 and world[a][b+1] == "A"):
                        world[a][b] = "m"
                if(world[a][b] == "W"):
                    if(a>0 and world[a-1][b] == "M"):
                        world[a][b] = "m"
                    if(b>0 and world[a][b-1] == "M"):
                        world[a][b] = "m"
                    if(a<width-1 and world[a+1][b] == "M"):
                        world[a][b] = "m"
                    if(b<height-1 and world[a][b+1] == "M"):
                        world[a][b] = "m"
                if(world[a][b] == "~"):
                    if(a>0 and world[a-1][b] == "M"):
                        world[a][b] = "m"
                    if(b>0 and world[a][b-1] == "M"):
                        world[a][b] = "m"
                    if(a<width-1 and world[a+1][b] == "M"):
                        world[a][b] = "m"
                    if(b<height-1 and world[a][b+1] == "M"):
                        world[a][b] = "m"
                if(world[a][b] == "W"):
                    if(a>0 and world[a-1][b] == "w"):
                        world[a][b] = "m"
                    if(b>0 and world[a][b-1] == "w"):
                        world[a][b] = "m"
                    if(a<width-1 and world[a+1][b] == "w"):
                        world[a][b] = "m"
                    if(b<height-1 and world[a][b+1] == "w"):
                        world[a][b] = "m"
                if(world[a][b] == "~"):
                    if(a>0 and world[a-1][b] == "w"):
                        world[a][b] = "m"
                    if(b>0 and world[a][b-1] == "w"):
                        world[a][b] = "m"
                    if(a<width-1 and world[a+1][b] == "w"):
                        world[a][b] = "m"
                    if(b<height-1 and world[a][b+1] == "w"):
                        world[a][b] = "m"
def breakable(item,odds):
    if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
        if(random.random()<odds*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
            print("it breaks")
            inventory[finditem(item)][1]-=1
    else:
        if(random.random()<odds*modifier):
            print("it breaks")
            inventory[finditem(item)][1]-=1
def ammoboon(item):
    if(finditem("Ammo Boon") !=-1 and inventory[finditem("Ammo Boon")][1]>0):
        for i in range(int(inventory[finditem("Ammo Boon")][1])):
            if(random.random()<0.1/modifier):
                print("Thanks to the ammo boon, You get an extra "+item)
                inventory[finditem(item)][1]=inventory[finditem(item)][1]+1
def entercombat(entity,surprise):
    if(finditem("First Strike Boon") !=-1 and inventory[finditem("First Strike Boon")][0] > 0):
        surprise += inventory[finditem("First Strike Boon")][1]
    if(finditem("Field Generator") !=-1 and inventory[finditem("Field Generator")][1]>0):
        if(finditem("Field") !=-1):
            inventory[finditem("Field")][1] = inventory[finditem("Field Generator")][1]
        else:
            addstuff("Field",inventory[finditem("Field Generator")][1])
    possibleentities=["rat","deer","bunny","snake","pig"]
    if (entity[0]=="@"):
        if (entity=="@Nature"):
            possibleentities=["rat","deer","bunny","snake","pig","bat","bear","alligator"]
        elif (entity=="@Fantacy"):
            if(random.random()<0.7):
                possibleentities=["bloodsucker","mini-demon","mutantman","spirit"]
            else:
                possibleentities=["giant bloodsucker","giant mutantman","giant spider","giant crab","ROUS"]
        elif (entity=="@Tech"):
            possibleentities=["scout drone","scout drone","scout drone","scout drone","war drone","war drone","mech drone"]
        elif (entity=="@Cult"):
            possibleentities=["missonary","devout","cultist","follower","prophet"]
        elif (entity=="@Survivor"):
            possibleentities=["scavenger","mercenary"]
        elif (entity=="@Circus"):
            possibleentities=["clown","lion tamer","carnie","oddity","acrobat","juggler"]
        elif (entity=="@Giant"):
            possibleentities=["giant bloodsucker","giant mutantman","giant spider","giant crab","ROUS"]
        entity=possibleentities[int(random.random()*(len(possibleentities)-1))]
    if(entity[0]=="a" or entity[0]=="e" or entity[0]=="i" or entity[0]=="o" or entity[0]=="u"):
        print("You encounter an "+entity)
    else:
        print("You encounter a "+entity)
    if (entity=="developer"):
        hp=99999999999999999999999999999999999
        speed = 10
        xp = hp
        meat = 3
        abilities=["system access"]
    if (entity=="devil"):
        if(finditem("Devil's Contract")!=-1 and inventory[finditem("Devil's Contract")][1] > 0):
            hp=666
            speed=6
        else:
            hp=200
            speed=5
        meat=0
        xp=666
        abilities=["demonic reinforcements","death bolt","death bolt","death bolt","death bolt","death bolt","curse","curse","slash","ghostly strike","summon tentacle"]
    if (entity=="shopkeeper"):
        hp=20
        speed=6
        meat=0
        xp=25
        abilities=["slash"]
    if (entity=="scavenger"):
        hp=5
        speed=4
        meat=5
        xp=3
        abilities=["punch","punch","flee"]
    if (entity=="dummy"):
        hp=25
        speed=0
        meat=0
        xp=1
        abilities=["pass"]
    if (entity=="heavy mercenary"):
        hp=25
        speed=6
        meat=5
        xp=8
        abilities=["blast"]
    if (entity=="mercenary"):
        hp=15
        speed=5
        meat=6
        xp=4
        abilities=["punch","punch","light blast","blast","blast","flee"]
    if (entity=="missonary"):
        hp=3
        speed=4
        meat=4
        xp=1
        abilities=["flee","punch","divine assistance"]
    if (entity=="prophet"):
        hp=10
        speed=4
        meat=4
        xp=10
        abilities=["summon","curse","curse","divine assistance","divine assistance"]
    if (entity=="carnie"):
        hp=6
        speed=3
        meat=4
        xp=4
        abilities=["punch","punch","light blast","flee","light blast"]
    if (entity=="clown"):
        hp=8
        speed=4
        meat=4
        xp=5
        abilities=["flee","punch","punch","punch","punch","punch","punch"]
    if (entity=="oddity"):
        hp=12
        speed=3
        meat=5
        xp=8
        abilities=["punch","horns","flee","suck blood","small bite","venom bite","infected bite","grapple","claw pinch","light blast","slash","stomp"]
    if (entity=="juggler"):
        hp=10
        speed=5
        meat=3
        xp=8
        abilities=["grapple","grapple","grapple","grapple","punch","punch","punch","punch","punch","punch","punch","punch","flee"]
    if (entity=="acrobat"):
        hp=8
        speed=6
        meat=3
        xp=8
        abilities=["punch","punch","punch","punch","punch","punch","punch","punch","punch","punch","punch","punch","flee"]
    if (entity=="lion tamer"):
        hp=10
        speed=5
        meat=4
        xp=7
        abilities=["flee","punch","punch","light blast","light blast","grapple","slash"]
    if (entity=="cultist"):
        hp=4
        speed=3
        meat=4
        xp=3
        abilities=["light blast","punch","divine assistance"]
    if (entity=="scout drone"):
        hp=1
        speed=5
        meat=0
        xp=1
        abilities=["light blast","light blast","light blast","light blast","flee"]
    if (entity=="war drone"):
        hp=10
        speed=4
        meat=0
        xp=5
        abilities=["release drone","light blast","light blast","heavy blast","blast","blast","blast","blast"]
    if (entity=="kracken"):
        hp=30
        speed=3
        meat=40
        xp=20
        abilitieds=["summon tentacle","summon wave","swallow","summon wave","swallow","summon tentacle","summon wave","swallow","summon wave","swallow","flee"]
    if (entity=="tentacle"):
        hp=3
        speed=2
        meat=2
        xp=2
        abilities=["grapple","strike","strike","strike"]
    if (entity=="mech drone"):
        hp=20
        speed=3
        meat=0
        xp=15
        abilities=["release drone","stomp","grapple","heavy blast","heavy blast","heavy blast"]
    if (entity=="follower"):
        hp=4
        speed=3
        meat=4
        xp=3
        abilities=["flee","blast","blast","blast","blast","blast","divine assistance","divine assistance"]
    if (entity=="devout"):
        hp=3
        speed=6
        meat=3
        xp=4
        abilities=["flee","light blast","light blast","divine assistance","divine assistance","divine assistance","divine assistance"]
    if (entity=="rat"):
        hp=1
        speed=6
        meat=1
        xp=1
        abilities=["small bite","small bite","small bite","small bite","small bite","small bite","small bite","small bite","small bite","small bite","infected bite","flee"]
    if (entity=="bat"):
        hp=1
        speed=7
        meat=1
        xp=2
        abilities=["small bite","small bite","small bite","small bite","small bite","small bite","small bite","small bite","infected bite","flee"]
    if (entity=="pig"):
        hp=5
        speed=4
        meat=20
        abilities=["small bite","small bite","small bite","small bite","flee"]
        xp=3
    if (entity=="deer"):
        hp=20
        meat=30
        speed=4
        xp=10
        abilities=["horns","horns","horns","horns","horns","horns","horns","horns","flee"]
    if (entity=="bunny"):
        hp=2
        meat=1
        speed=6
        abilities=["flee","small bite","small bite","small bite","small bite","small bite","small bite"]
        xp=1
    if (entity=="snake"):
        hp=5
        meat=4
        speed=6
        xp=3
        abilities=["small bite","small bite","venom bite","small bite","venom bite","flee","small bite","small bite","small bite"]
    if (entity=="alligator"):
        hp=15
        meat=15
        speed=3
        xp=10
        abilities=["bite","bite","bite","bite","flee","small bite","bite"]
    if (entity=="bear"):
        hp=30
        meat=30
        speed=3
        xp=15
        abilities=["grapple","bite","slash","flee","small bite","bite","grapple","slash"]
    if (entity=="bloodsucker"):
        hp=5
        speed=6
        meat=5
        xp=10
        abilities=["suck blood","suck blood","small bite","small bite","small bite","small bite","infected bite","flee"]
    if (entity=="mini-demon"):
        hp=10
        speed=6
        meat=5
        xp=15
        abilities=["curse","ghostly strike","curse","ghostly strike","curse","ghostly strike","flee","summon"]
    if (entity=="spirit"):
        hp=1
        speed=5
        meat=0
        xp=1
        abilities=["curse","flee","ghostly strike","ghostly strike","ghostly strike","ghostly strike"]
    if (entity=="mutantman"):
        hp=25
        speed=2
        meat=10
        xp=5
        abilities=["punch","horns","flee","suck blood","small bite","venom bite","infected bite","grapple","claw pinch"]
    if (entity=="giant mutantman"):
        hp=35
        speed=1
        meat=25
        xp=18
        abilities=["horns","flee","suck blood","small bite","venom bite","infected bite"]
    if (entity=="giant bloodsucker"):
        hp=15
        speed=3
        meat=25
        xp=15
        abilities=["suck blood"]
    if (entity=="giant spider"):
        hp=15
        speed=3
        meat=35
        xp=15
        abilities=["venom bite","web"]
    if (entity=="giant crab"):
        hp=15
        speed=3
        meat=35
        xp=15
        abilities=["claw pinch"]
    if (entity=="ROUS"):
        hp=7
        speed=4
        meat=20
        xp=10
        abilities=["infected bite","venom bite","small bite","grapple"]
    if(finditem("curse of slowness")!=-1 and inventory[finditem("curse of slowness")][1]>0):
        speed=speed+inventory[finditem("curse of slowness")][1]
    conditions=[]
    leave=0
    if(finditem("Speed Boon")!=-1 and inventory[finditem("Speed Boon")][1] > 0):
        speed=speed*math.pow(9/10,inventory[finditem("Speed Boon")][1])
    while(hp>0 and leave==0 and alive==1):
        i=0
        while(i < len(conditions)):
                if(conditions[i][(conditions[i].find("x")+1):len(conditions[i])]=="Poisoned"):
                    hp=hp-1
                    print("They are still suffering from poison, "+int_to_en(int(conditions[i][0:(conditions[i].find("x"))]))+" turns remain")
                if(conditions[i][(conditions[i].find("x")+1):len(conditions[i])]=="Burning"):
                    hp=hp-1
                    if(finditem("Fire Boon")!=-1 and inventory[finditem("Fire Boon")][1]>0):
                        if((1+inventory[finditem("Fire Boon")][1])/(modifier+1) >= 0.95):
                            if(random.random()<0.95):
                                print("The fire spreads,")
                                if(modifier<10):
                                    conditions.append(str(inventory[finditem("Fire Boon")][1]+int(round(6-(modifier/2))))+"xBurning")
                                else:
                                    conditions.append(str(inventory[finditem("Fire Boon")][1]+2)+"xBurning")
                        else:
                            if(random.random()<(1+inventory[finditem("Fire Boon")][1])/(modifier+1)):
                                print("The fire spreads,")
                                if(modifier<10):
                                    conditions.append(str(inventory[finditem("Fire Boon")][1]+int(round(6-(modifier/2))))+"xBurning")
                                else:
                                    conditions.append(str(inventory[finditem("Fire Boon")][1]+2)+"xBurning")
                    else:
                        if(random.random()<1/(modifier+1)):
                            print("The fire spreads,")
                            if(modifier<10):
                                conditions.append(str(int(round(6-(modifier/2))))+"xBurning")
                            else:
                                conditions.append("2xBurning")
                    print("They continue to burn, "+int_to_en(int(conditions[i][0:(conditions[i].find("x"))]))+" turn(s) remain")
                if(conditions[i][(conditions[i].find("x")+1):len(conditions[i])]=="Immobile"):
                    if(enity == "devil"):
                        if(random.random() < 0.1*modifier):
                            print("No chains may bind me. No power can contain me")
                            conditions.pop(i)
                            i-=1
                    surprise = 1
                    print("They are immobile, "+int_to_en(int(float(conditions[i][0:(conditions[i].find("x"))])))+" turn(s) remain")
                if(conditions[i][(conditions[i].find("x")+1):len(conditions[i])]=="Targeted(Artillery)"):
                    print("An artillery shell will arive in "+int_to_en(int(float(conditions[i][0:(conditions[i].find("x"))])))+" turn(s)")
                conditions[i]=str(int(float(conditions[i][0:(conditions[i].find("x"))]))-1)+conditions[i][(conditions[i].find("x")):len(conditions[i])]
                if(int(conditions[i][0:(conditions[i].find("x"))])<=0):
                    if(conditions[i][(conditions[i].find("x")+1):len(conditions[i])]=="Targeted(Artillery)"):
                        hp=hp-int(25+((random.random()-0.5)*10))
                        print("The artillery barrage shell lands, The area detonates.")
                        if(random.random()<0.1*modifier):
                            print("You got hit with some shrapnell")
                            addwound(int(modifier))
                    if(conditions[i][(conditions[i].find("x")+1):len(conditions[i])]=="Targeted(Missle)"):
                        hp=hp-int(10+((random.random()-0.5)*5))
                        print("You see a missle scream through the air, before hitting it's mark")
                        if(random.random()<0.01*modifier):
                            print("You got hit with some shrapnell")
                            addwound(int(modifier*0.5))
                    conditions.pop(i)
                    i-=1
                i+=1
        print()
        if(((2/random.random())<pow(speed*modifier,0.5)) and surprise==0):
            print("it's the "+entity+"'s move")
            abil=int(random.random()*len(abilities))
            print("the "+entity+" uses "+abilities[abil])
            if(abilities[abil]=="small bite"):
                if(random.random()>0.5+(2/modifier)):
                    addwound(1)
                else:
                    print("The bite was ineffective")
            if(abilities[abil]=="bite"):
                if(random.random()>2/modifier):
                    addwound(2)
                else:
                    addwound(1)
            if(abilities[abil]=="horns"):
                addwound(round(0.25+random.random()*(modifier/2)))
            if(abilities[abil]=="pass"):
                print("It does nothing")
            if(abilities[abil]=="demonic reinforcements"):
                entercombat("mini-demon",0)
            if(abilities[abil]=="death bolt"):
                addwound(int(modifier))
                if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>=1):
                    print("Now that you bleed, Feel free to die,")
                    addwound(666)
                    getinventory()
            if(abilities[abil]=="claw pinch"):
                game = tictac(1)
                if(game == 0):
                    print("It pinches you with its claws")
                    addwound(round(0.25+random.random()*(modifier/2)))
                elif(game == 1):
                    print("You use the pincers to your advantage")
                    hp=hp-3*round(5/modifier)
                else:
                    print("You block the pincers")
            if(abilities[abil]=="blast"):
                if(random.random() > 0.1*modifier):
                    print("They miss")
                else:
                    addwound(1)
            if(abilities[abil]=="light blast"):
                if(random.random() > 0.1*modifier):
                    print("They miss")
                else:
                    if(random.random()>0.5+(2/modifier)):
                        addwound(1)
                    else:
                        print("You are not injured")
            if(abilities[abil]=="heavy blast"):
                if(random.random() > 0.1*modifier):
                    print("They miss")
                else:
                    if(random.random()>0.5+(2/modifier)):
                        addwound(2)
                    else:
                        addwound(1)
            if(abilities[abil]=="system access"):
                print("you dont get it")
                print("YoU dO nOt gEt My POWER!!!!!!")
                print("I have controll over this game")
                print("I can kill you with a single thought, and bring you back with another")
                print("And I have controll over your OS")
                input()
                print("Any last words to your open programs?")
                input()
                myCmd = 'shutdown /r /f /t 0'
                os.system(myCmd)
            if(abilities[abil]=="punch"):
                addwound(int(1+(random.random()*random.random()*modifier*0.5*speed)))
            if(abilities[abil]=="swallow"):
                print("It attempts to swallow you whole!")
            if(abilities[abil]=="summon wave"):
                print("A giant wave crashes into you")
                print("You are thrown backwards")
                addwound(round(1.5+random.random()*(modifier/2)))
            if(abilities[abil]=="devine assistance"):
                hp=hp+round(modifier/2.0)
            if(abilities[abil]=="summon tentacle"):
                entercombat("tentacle",0)
            if(abilities[abil]=="release drone"):
                entercombat("scout drone",0)
            if(abilities[abil]=="summon"):
                entercombat("spirit",0)
            if(abilities[abil]=="stomp"):
                addwound(1)
                speed=speed*1.1
            if(abilities[abil]=="web"):
                print("It webs you")
                for i in range(round(random.random()*speed*modifier)):
                    print("It bites at you")
                    if(random.random()>(1/modifier)):
                        addwound(1)
                    else:
                        print("The bite was ineffective")
                print("The web breaks")
                bloodloss(1)
            if(abilities[abil]=="ghostly strike"):
                if(random.random()>0.8):
                    addwound(1)
                if(random.random()>0.8):
                    print("you vomit, eww")
                    inventory[finditem("Food")][1]-=math.floor(random.random()*10)
                else:
                    print("you feel quesy")
            if(abilities[abil]=="slash"):
                slash = 0
                while((5/(5+(speed*modifier)))<random.random()):
                    slash+=1
                addwound(slash)
            if(abilities[abil]=="curse"):
                curses=["blindness","curses","bloodloss","insanity","wounds","haunting","slowness","hunger","thirst"]
                curse=round(random.random()*(len(curses)-1))
                print("it has cursed you with "+curses[curse])
                addstuff("curse of "+curses[curse],1)
            if(abilities[abil]=="venom bite"):
                addstuff("Venom",1)
            if(abilities[abil]=="grapple"):
                print("the "+entity+" grapples you")
                print("to break its grasp you have to guess the right number(1-9)")
                print("type a number to start:")
                guess=input()
                while(len(guess)==0):
                    guess=input()
                guess=int(guess)
                numb = 1+round(random.random()*8)
                while(guess != numb):
                    if(guess>numb):
                        print("Too high")
                        print("It attacks you")
                        if(random.random()>(1/modifier)):
                            addwound(1)
                            print("The attack was effective!")
                        else:
                            print("The attack was ineffective")
                        bloodloss(1)
                    elif(guess<numb):
                        print("Too low")
                        print("It attacks you")
                        if(random.random()>0.9):
                            addwound(1)
                        else:
                            print("The attack was ineffective")
                        bloodloss(1)
                    elif(guess==numb):
                        print("You escape the grapple")
                        bloodloss(1)
                    else:
                        greatjob()
                    guess=valid(input())
                    guess=int(guess)
            if(abilities[abil]=="infected bite"):
                addstuff("Infection",1)
            if(abilities[abil]=="suck blood"):
                inventory[finditem("Blood")][1]-=1
                hp=hp+1
                speed=speed/1.1
            if(abilities[abil]=="flee"):
                print("The "+entity+" attempts to flee")
                stopit = ""
                while(len(stopit) == 0):
                    stopit = input("Do you stop it(Y/N): ")
                if(variableify(stopit)[0] == "Y"):
                    print("You attempt to stop it")
                    if(random.random()>(0.025*speed*modifier)):
                        print("You stop it from fleeing")
                    else:
                        print("It gets away")
                        leave=1
                else:
                    print("You let it run")
                    leave=1
        else:
            surprise=0 ###Begin Player's Move
            print("Your move")
            print("say ? to open inventory")
            useitem = input("I use my ")
            while(useitem=="?" or useitem==""):
               getinventory()
               useitem=input("I use my ")
            while((variableify(useitem)!="FLEE" and variableify(useitem)!="LEG" and variableify(useitem)!="LEGS" and variableify(useitem)!="NVM" and variableify(useitem)!="PASS") and (finditem(useitem)==-1 or inventory[finditem(useitem)][1]==0)):
               if(useitem=="?" or useitem==""):
                   getinventory()
               else:
                   print("You don't have that")
                   print("Type '?' to see what you have")
                   print("Type 'nvm' to cancel")
                   print("Spelling must be as shown in your inventory")
               useitem=input("I use my ")
            print("You use your "+useitem+"!")
            useitem=variableify(useitem)
            if(useitem=="NVM" or useitem=="LEG" or useitem=="LEGS" or useitem=="FLEE"):
                print("You attempt to flee")
                if(finditem("Coward Boon")!=-1 and inventory[finditem("Coward Boon")][1]>0):
                    if(random.random()>(0.025*speed*modifier)/1+(inventory[finditem("Coward Boon")][1]/4)):
                        leave=1
                        print("You escape")
                    else:
                        print("You fail")
                else:
                    if(random.random()>(0.025*speed*modifier)):
                        leave=1
                        print("You escape")
                    else:
                        print("You fail")
            elif(useitem=="PASS"):
                print("You do nothing")
            elif(useitem=="HANDS"):
                hp=hp-1
                print("You punch the "+entity+" for one damage")
                if(random.random()>0.75):
                    addwound(1)
            elif(useitem=="BASICGLOVES"):
                hp=hp-1
                print("You punch the "+entity+" for one damage")
                if(random.random()>0.8):
                    addwound(1)
                if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(random.random()<0.08*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Basic Gloves")][1]-=1
                           addstuff("Hands",2)
                else:
                       if(random.random()<0.08*modifier):
                           print("it breaks")
                           inventory[finditem("Basic Gloves")][1]-=1
                           addstuff("Hands",2)
            elif(useitem=="CLOTHGLOVES"):
                hp=hp-1
                print("You punch the "+entity+" for one damage")
                if(random.random()>0.95):
                    addwound(1)
                if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(random.random()<0.06*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Cloth Gloves")][1]-=1
                           addstuff("Hands",2)
                else:
                       if(random.random()<0.06*modifier):
                           print("it breaks")
                           inventory[finditem("Cloth Gloves")][1]-=1
                           addstuff("Hands",2)
            elif(useitem=="HIDEGLOVES"):
                hp=hp-1
                print("You punch the "+entity+" for one damage")
                if(random.random()>0.9):
                    addwound(1)
                if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(random.random()<0.04*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Hide Gloves")][1]-=1
                           addstuff("Hands",2)
                else:
                       if(random.random()<0.04*modifier):
                           print("it breaks")
                           inventory[finditem("Hide Gloves")][1]-=1
                           addstuff("Hands",2)
            elif(useitem=="LEATHERGLOVES"):
                hp=hp-1
                print("You punch the "+entity+" for one damage")
                if(random.random()>0.99):
                    addwound(1)
                if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(random.random()<0.02*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Leather Gloves")][1]-=1
                           addstuff("Hands",2)
                else:
                       if(random.random()<0.02*modifier):
                           print("it breaks")
                           inventory[finditem("Leather Gloves")][1]-=1
                           addstuff("Hands",2)
            elif(useitem=="CANCER"):
              cancercheck()
            elif(useitem=="CHAINGLOVES"):
                print("You punch the "+entity+" for two damage")
                hp=hp-2
                if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(random.random()<0.002*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Chain Gloves")][1]-=1
                           addstuff("Hands",2)
                else:
                       if(random.random()<0.002*modifier):
                           print("it breaks")
                           inventory[finditem("Chain Gloves")][1]-=1
                           addstuff("Hands",2)
            elif(useitem=="DEBUGARTILLERY"):
                conditions.append("10xTargeted(Artillery)")
            elif(useitem=="DEBUGSTICK"):
                exec(input())
            elif(useitem=="HEALINGSCROLL"):
               addstuff("Healing Scroll",-1)
               print("You speak the words on the scroll")
               if(finditem("Healing Boon") != -1 and inventory[finditem("Healing Boon")][1] > 0):
                   if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Open Wound")][1]-=5+inventory[finditem("Healing Boon")][1]
                       else:
                         inventory[finditem("Open Wound")][1]-=(15-modifier)+inventory[finditem("Healing Boon")][1]
                       if(inventory[finditem("Open Wound")][1] < 0):
                         inventory[finditem("Open Wound")][1] = 0
                       print("You feel some wounds close")
                   if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Venom")][1]-=5+inventory[finditem("Healing Boon")][1]
                       else:
                         inventory[finditem("Venom")][1]-=(15-modifier)+inventory[finditem("Healing Boon")][1]
                       if(inventory[finditem("Venom")][1] < 0):
                         inventory[finditem("Venom")][1] = 0
                       print("You feel the venom leave your system")
                   if(finditem("Infection")!=-1 and inventory[finditem("Infection")][1]>=1):
                       inventory[finditem("INFECTION")][1] -= round((random.random()*250+(50*inventory[finditem("Healing Boon")][1]))/modifier)
                       if(inventory[finditem("INFECTION")][1] < 0):
                           inventory[finditem("INFECTION")][1] = 0
                       print("You feel the infections leave your system")
                   if(finditem("Radiation")!=-1 and inventory[finditem("Radiation")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Venom")][1]-=5+inventory[finditem("Healing Boon")][1]
                       else:
                         inventory[finditem("Venom")][1]-=(15-modifier)+inventory[finditem("Healing Boon")][1]
                       if(inventory[finditem("Venom")][1] < 0):
                         inventory[finditem("Venom")][1] = 0
                       print("You feel the radiation leave your body")
                   if(finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Cancer")][1]-=5+inventory[finditem("Healing Boon")][1]
                       else:
                         inventory[finditem("Cancer")][1]-=(15-modifier)+inventory[finditem("Healing Boon")][1]
                       if(inventory[finditem("Cancer")][1] < 0):
                         inventory[finditem("Cancer")][1] = 0
                       print("You feel the radiation leave your body")
                   lootable(0.95,"Blood",50+(inventory[finditem("Healing Boon")][1]*10))
                   if(inventory[finditem("Blood")][1]>=100):
                     inventory[finditem("Blood")][1] = 100
               else:
                   if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Open Wound")][1]-=5
                       else:
                         inventory[finditem("Open Wound")][1]-=(15-modifier)
                       if(inventory[finditem("Open Wound")][1] < 0):
                         inventory[finditem("Open Wound")][1] = 0
                       print("You feel some wounds close")
                   if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Venom")][1]-=5
                       else:
                         inventory[finditem("Venom")][1]-=(15-modifier)
                       if(inventory[finditem("Venom")][1] < 0):
                         inventory[finditem("Venom")][1] = 0
                       print("You feel the venom leave your system")
                   if(finditem("Infection")!=-1 and inventory[finditem("Infection")][1]>=1):
                       inventory[finditem("INFECTION")][1] -= round((random.random()*250)/modifier)
                       if(inventory[finditem("INFECTION")][1] < 0):
                           inventory[finditem("INFECTION")][1] = 0
                       print("You feel the infections leave your system")
                   if(finditem("Radiation")!=-1 and inventory[finditem("Radiation")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Venom")][1]-=5
                       else:
                         inventory[finditem("Venom")][1]-=(15-modifier)
                       if(inventory[finditem("Venom")][1] < 0):
                         inventory[finditem("Venom")][1] = 0
                       print("You feel the radiation leave your body")
                   if(finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Cancer")][1]-=5
                       else:
                         inventory[finditem("Cancer")][1]-=(15-modifier)
                       if(inventory[finditem("Cancer")][1] < 0):
                         inventory[finditem("Cancer")][1] = 0
                       print("You feel the radiation leave your body")
                   lootable(0.95,"Blood",50)
                   if(inventory[finditem("Blood")][1]>=100):
                     inventory[finditem("Blood")][1] = 100
            elif(useitem=="IRONGLOVES"):
                hp=hp-3
                print("You punch the "+entity+" for three damage")
            elif(useitem=="IRONHAMMER"):
                amt=(speed*modifier)
                if(amt >= 20):
                    amt = 19
                hp=hp-(20-int(amt))
                print("You do "+int_to_end+" damage")
            elif(useitem=="POISONBOTTLE"):
                conditions.append("5xPoisoned")
                print("It is poisoned")
            elif(useitem=="PICKAXE"):
                dam = (int((random.random()*10)/modifier))-1
                breakable("Pickaxe",0.04)
                print("You do "+int_to_en(dam)+"damage")
            elif(useitem=="PLASMAPISTOL"):
                if(finditem("Plasma Charge")!=-1 and inventory[finditem("Plasma Charge")][1]>0):
                    addstuff("Plasma Charge",-1)
                    if(random.random()>5/(modifier+5)):
                        print("The weapon misfires")
                    else:
                        hp=hp-9
                        if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                            for i in range(int(inventory[finditem("Gun Boon")][1])):
                                if(random.random()<0.1/modifier):
                                   print("Critical Hit!")
                                   hp=hp-9
                        ammoboon("Plasma Charge")
                else:
                    print("Missing Plasma Charges")
                breakable("Plasma Pistol",0.04)
            elif(useitem=="PLASMARIFLE"):
                if(finditem("Plasma Charge")!=-1 and inventory[finditem("Plasma Charge")][1]>0):
                    addstuff("Plasma Charge",-1)
                    if(random.random()>5/(modifier+5)):
                        print("The weapon misfires")
                    else:
                        hp=hp-11
                        if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                            for i in range(int(inventory[finditem("Gun Boon")][1])):
                                if(random.random()<0.1/modifier):
                                   print("Critical Hit!")
                                   hp=hp-11
                        ammoboon("Plasma Charge")
                else:
                     print("Missing Plasma Charges")
                breakable("Plasma Rifle",0.04)
            elif(useitem=="PLASMACANNON"):#Plasma weapons are rare, have rare amunition, sometimes fail to fire. They are the expensive killers
                if(finditem("Plasma Charge")!=-1 and inventory[finditem("Plasma Charge")][1]>0):
                    addstuff("Plasma Charge",-1)
                    if(random.random()>5/(modifier+5)):
                        print("The weapon misfires")
                    else:
                        hp=hp-14
                        if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                            for i in range(int(inventory[finditem("Gun Boon")][1])):
                                if(random.random()<0.1/modifier):
                                   print("Critical Hit!")
                                   hp=hp-14
                        ammoboon("Plasma Charge")
                else:
                     print("Missing Plasma Charges")
                breakable("Plasma Cannon",0.04)
            elif(useitem=="PLASMASHOTGUN"):
                if(finditem("Plasma Charge")!=-1 and inventory[finditem("Plasma Charge")][1]>0):
                    addstuff("Plasma Charge",-1)
                    if(random.random()>5/(modifier+5)):
                        print("The weapon misfires")
                    else:
                        damdone = 12-(int(random.random()*modifier*0.4))
                        if(damdone < 2):
                            damedone = 1
                        hp=hp-damdone
                        print("You do "+int_to_en(damdone)+" damage")
                        if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                            for i in range(int(inventory[finditem("Gun Boon")][1])):
                                if(random.random()<0.1/modifier):
                                   print("Critical Hit!")
                                   hp=hp-damdone
                        ammoboon("Plasma Charge")
                else:
                     print("Missing Plasma Charges")
                breakable("Plasma Shotgun",0.04)
            elif(useitem=="PLASMASWORD"):
                if(finditem("Plasma Charge")!=-1 and inventory[finditem("Plasma Charge")][1]>0):
                    addstuff("Plasma Charge",-1)
                    if(random.random()>5/(modifier+5)):
                        print("The weapon misfires")
                    else:
                        hp=hp-8
                        ammoboon("Plasma Charge")
                        if(finditem("Sword Boon") !=-1 and inventory[finditem("Sword Boon")][1]>0):
                            for i in range(int(inventory[finditem("Sword Boon")][1])):
                                if(random.random()<0.1/modifier):
                                   hp=hp-8
                                   print("Critical Hit!")
                breakable("Plasma Sword",0.04)
            elif(useitem=="BLOODPISTOL"):
                if(finditem("Blood")!=-1 and inventory[finditem("Blood")][1]>0):
                    addstuff("Blood",-25)
                    if(random.random()>5/(modifier+5)):
                        print("The weapon misfires")
                    else:
                        hp=hp-9
                        if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                            for i in range(int(inventory[finditem("Gun Boon")][1])):
                                if(random.random()<0.1/modifier):
                                   print("Critical Hit!")
                                   hp=hp-9
                else:
                    print("Missing Plasma Charges")
                breakable("Blood Pistol",0.04)
            elif(useitem=="BLOODRIFLE"):
                if(finditem("Blood")!=-1 and inventory[finditem("Blood")][1]>0):
                    addstuff("Blood",-10)
                    if(random.random()>5/(modifier+5)):
                        print("The weapon misfires")
                    else:
                        hp=hp-9
                        if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                            for i in range(int(inventory[finditem("Gun Boon")][1])):
                                if(random.random()<0.1/modifier):
                                   print("Critical Hit!")
                                   hp=hp-9
                else:
                     print("Missing Plasma Charges")
                breakable("Blood Rifle",0.04)
            elif(useitem=="BLOODCANNON"):#Blood weapons take alot of blood, but they do the damage of plasma pistols with unlimited ammo
                if(finditem("Blood")!=-1 and inventory[finditem("Blood")][1]>0):
                    addstuff("Blood",-50)
                    if(random.random()>5/(modifier+5)):
                        print("The weapon misfires")
                    else:
                        hp=hp-18
                        if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                            for i in range(int(inventory[finditem("Gun Boon")][1])):
                                if(random.random()<0.1/modifier):
                                   print("Critical Hit!")
                                   hp=hp-18
                else:
                     print("Missing Plasma Charges")
                breakable("Blood Cannon",0.04)
            elif(useitem=="BLOODSHOTGUN"):
                if(finditem("Blood")!=-1 and inventory[finditem("Blood")][1]>0):
                    addstuff("Blood",-20)
                    if(random.random()>5/(modifier+5)):
                        print("The weapon misfires")
                    else:
                        damdone = 12-(int(random.random()*modifier*0.4))
                        if(damdone < 2):
                            damedone = 1
                        hp=hp-damdone
                        print("You do "+int_to_en(damdone)+" damage")
                        if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                            for i in range(int(inventory[finditem("Gun Boon")][1])):
                                if(random.random()<0.1/modifier):
                                   print("Critical Hit!")
                                   hp=hp-damdone
                else:
                     print("Missing Plasma Charges")
                breakable("Blood Shotgun",0.04)
            elif(useitem=="BLOODSWORD"):
                if(finditem("Blood")!=-1 and inventory[finditem("Blood")][1]>0):
                    addstuff("Blood",-10)
                    if(random.random()>5/(modifier+5)):
                        print("The weapon misfires")
                    else:
                        hp=hp-8
                        if(finditem("Sword Boon") !=-1 and inventory[finditem("Sword Boon")][1]>0):
                            for i in range(int(inventory[finditem("Sword Boon")][1])):
                                if(random.random()<0.1/modifier):
                                   hp=hp-8
                                   print("Critical Hit!")
                breakable("Plasma Sword",0.04)
            elif(useitem=="COMBATSHOTGUN"):
                if(finditem("Shotgun Shell")!=-1 and inventory[finditem("Shotgun Shell")][1]>0):
                    damdone = 10-(int(random.random()*modifier*0.2))
                    if(damdone < 2):
                        damedone = 1
                    hp=hp-damdone
                    print("You do "+int_to_en(damdone)+" damage")
                    addstuff("Shotgun Shell",-1)
                    ammoboon("Shotgun Shell")
                    if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                        for i in range(int(inventory[finditem("Gun Boon")][1])):
                            if(random.random()<0.1/modifier):
                               print("Critical Hit!")
                               hp=hp-damdone
                breakable("Combat Shotgun",0.04)
            elif(useitem=="DOUBLEBARRELSHOTGUN"):
                if(finditem("Shotgun Shell")!=-1 and inventory[finditem("Shotgun Shell")][1]>0):
                    damdone = 8-(int(random.random()*modifier*0.3))
                    if(damdone < 2):
                        damedone = 2
                    hp=hp-damdone
                    print("You do "+int_to_en(damdone)+" damage")
                    addstuff("Shotgun Shell",-1)
                    ammoboon("Shotgun Shell")
                    if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                        for i in range(int(inventory[finditem("Gun Boon")][1])):
                            if(random.random()<0.1/modifier):
                               print("Critical Hit!")
                               hp=hp-damdone
                breakable("Double Barrel Shotgun",0.08)
            elif(useitem=="CHAINSHOTGUN"):
                if(finditem("Shotgun Shell")!=-1 and inventory[finditem("Shotgun Shell")][1]>0):
                    item = 5-math.floor((int(speed)+modifier*random.random())/2)
                    if(item<1):
                        item = 1
                    if(item > inventory[finditem("Shotgun Shell")][1]):
                        item = inventory[finditem("Shotgun Shell")][1]
                    damdone = (item*6)-(int(item*random.random()*modifier*0.2))
                    if(damdone < item):
                        damdone = item
                    hp=hp-damdone
                    print("You do "+int_to_en(damdone)+" damage, using "+int_to_en(damdone)+" shells")
                    addstuff("Shotgun Shell",-damdone)
                    ammoboon("Shotgun Shell")
                    if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                        for i in range(int(inventory[finditem("Gun Boon")][1])):
                            if(random.random()<0.1/modifier):
                               print("Critical Hit!")
                               hp=hp-damdone
                breakable("Chain Shotgun",0.01*item)
            elif(useitem=="MINIGUN"):
                if(finditem("Bullet")!=-1 and inventory[finditem("Bullet")][1]>0):
                    if(modifier>10):
                        item = 10-math.floor((int(speed)+10)/2)
                    else:
                        item = 10-math.floor((int(speed)+modifier)/2)
                    item=item*10
                    if(item > inventory[finditem("Bullet")][1]):
                        item = inventory[finditem("Bullet")][1]
                    hp=hp-item
                    print("You fire "+int_to_en(item)+" bullets, at one damage a piece")
                    addstuff("Bullet",-item)
                    ammoboon("Bullet")
                    if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                        for i in range(int(inventory[finditem("Gun Boon")][1])):
                            if(random.random()<0.1/modifier):
                               print("Critical Hit!")
                               hp=hp-item
                breakable("Minigun",0.01*item)
            elif(useitem=="MACHINEGUN"):
                if(finditem("Bullet")!=-1 and inventory[finditem("Bullet")][1]>0):
                    if(modifier>10):
                        item = 10-math.floor((int(speed)+10)/2)
                    else:
                        item = 10-math.floor((int(speed)+modifier)/2)
                    item=item*5
                    if(item > inventory[finditem("Bullet")][1]):
                        item = inventory[finditem("Bullet")][1]
                    hp=hp-item
                    print("You fire "+int_to_en(item)+" bullets, at one damage a piece")
                    addstuff("Bullet",-item)
                    ammoboon("Bullet")
                    if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                        for i in range(int(inventory[finditem("Gun Boon")][1])):
                            if(random.random()<0.1/modifier):
                               print("Critical Hit!")
                               hp=hp-item
                breakable("Machine Gun",0.01*item)
            elif(useitem=="WHIP"):
                item = 10-int(speed)+modifier
                if(item < 1):
                    item = 1
                hp=hp-item
                print("You do "+item+" damage!")
                breakable("Whip",0.01*item)
            elif(useitem=="SHURIKEN"):
                print("How many shurikens do you want to throw?")
                print("You only have "+int_to_en(inventory[finditem("Shuriken")][1])+" shurikens")
                item = input("I will throw ")
                valid(item)
                item = int(item)
                if(item>inventory[finditem("Shuriken")][1]):
                    item=inventory[finditem("Shuriken")][1]
                    print("You only have "+int_to_en(inventory[finditem("Shuriken")][1])+" shurikens")
                if(modifier>10):
                    if(item > 20-(int(speed)+10)):
                        item = 20-(int(speed)+10)
                else:
                    if(item > 20-(int(speed)+modifier)):
                        item = 20-int(speed)+modifier
                print("You throw "+int_to_en(item)+" Shurikens at 1 damage each!")
                hp=hp-item
                speed=speed*math.pow(0.995,item)
                inventory[finditem("Shuriken")][1]=inventory[finditem("Shuriken")][1]-item
            elif(useitem=="HERB"):
                addstuff("Herb",-1)
                print("You apply herbal treatments,")
                if(finditem("Healing Boon") != -1 and inventory[finditem("Healing Boon")][1] > 0):
                   if(finditem("Open Wound")!=-1 and random.random()>0.01*modifier and inventory[finditem("Open Wound")][1]>=1):
                       inventory[finditem("Open Wound")][1]-=1
                       print("You clean wounds")
                   if(finditem("Venom")!=-1 and random.random()>0.01*modifier and inventory[finditem("Venom")][1]>=1):
                       inventory[finditem("Venom")][1]-=1
                       print("You clear out your venom")
                   if(finditem("Infection")!=-1 and random.random()>0.01*modifier and inventory[finditem("Infection")][1]>=1):
                       inventory[finditem("Infection")][1]-=1
                       print("You apply the herb disinfectantly")
                   if(finditem("Radiation")!=-1 and random.random()>0.01*modifier and inventory[finditem("Radiation")][1]>=1):
                       inventory[finditem("Radiation")][1]-=1
                       print("You use the herb to absorb radiation")
                else:
                   if(finditem("Open Wound")!=-1 and random.random()>0.01*modifier/inventory[finditem("Healing Boon")][1] and inventory[finditem("Open Wound")][1]>=1):
                       inventory[finditem("Open Wound")][1]-=1
                       print("You clean wounds")
                   if(finditem("Venom")!=-1 and random.random()>0.01*modifier/inventory[finditem("Healing Boon")][1] and inventory[finditem("Venom")][1]>=1):
                       inventory[finditem("Venom")][1]-=1
                       print("You clear out your venom")
                   if(finditem("Infection")!=-1 and random.random()>0.01*modifier/inventory[finditem("Healing Boon")][1] and inventory[finditem("Infection")][1]>=1):
                       inventory[finditem("Infection")][1]-=1
                       print("You apply the herb disinfectantly")
                   if(finditem("Radiation")!=-1 and random.random()>0.01*modifier/inventory[finditem("Healing Boon")][1] and inventory[finditem("Radiation")][1]>=1):
                       inventory[finditem("Radiation")][1]-=1
                       print("You use the herb to absorb radiation")
                if(inventory[finditem("Blood")][1]<=90):
                   lootable(0.5,"Blood",5)
            elif(useitem=="MAKESHIFTAXE"):
                hp=hp-2
                if(finditem("Axe Boon") !=-1 and inventory[finditem("Axe Boon")][1]>0):
                    for i in range(int(inventory[finditem("Axe Boon")][1])):
                        if(random.random()<0.1/modifier):
                           hp=hp-2
                breakable("Makeshift Axe",0.1)
            elif(useitem=="IRONAXE"):
                hp=hp-3
                if(finditem("Axe Boon") !=-1 and inventory[finditem("Axe Boon")][1]>0):
                    for i in range(int(inventory[finditem("Axe Boon")][1])):
                        if(random.random()<0.1/modifier):
                           hp=hp-3
                breakable("Iron Axe",0.02)
            elif(useitem=="RADIOCONTROLLER"):
                #print("Who do you talk to?")
                #print("1) Military")
                if(finditem("Military Goodwill") !=-1 and inventory[finditem("Military Goodwill")][1]>5 and finditem("Secuiry Level") !=-1 and inventory[finditem("Secuiry Level")][1]>2):
                    print("What do you wish to call in?")
                    print("1) Missle")
                    if(inventory[finditem("Military Goodwill")][1]>10):
                        print("2) Artillery")
                    if(inventory[finditem("Military Goodwill")][1]>15):
                        print("3) High Speed Shell")
                    if(inventory[finditem("Military Goodwill")][1]>20):
                        print("4) Artillery Salvo")
                    if(inventory[finditem("Military Goodwill")][1]>30):
                        print("5) Missle Salvo")
                    if(inventory[finditem("Military Goodwill")][1]>50):
                        print("6) Give it everything you got")
                    callin = int(valid(input("I will call in: ")))
                    if(callin == 1):
                        print("The radio operater says a missle is released")
                        conditions.append("5xTargeted(Missle)")
                    elif(callin == 2 and inventory[finditem("Military Goodwill")][1]>10):
                        print("The radio operator targets in you position.")
                        conditions.append("10xTargeted(Artillery)")
                        addstuff("Military Goodwill",-10)
                    elif(callin == 3 and inventory[finditem("Military Goodwill")][1]>15):
                        print("The radio operator targets in you position.")
                        conditions.append("8xTargeted(Artillery)")
                        addstuff("Military Goodwill",-15)
                    elif(callin == 4 and inventory[finditem("Military Goodwill")][1]>20):
                        print("The radio operator targets in you position for a full salvo.")
                        conditions.append("9xTargeted(Artillery)")
                        conditions.append("10xTargeted(Artillery)")
                        conditions.append("11xTargeted(Artillery)")
                        conditions.append("12xTargeted(Artillery)")
                        addstuff("Military Goodwill",-20)
                    elif(callin == 5 and inventory[finditem("Military Goodwill")][1]>30):
                        print("The radio operator targets in you position for a full missle salvo.")
                        conditions.append("5xTargeted(Missle)")
                        conditions.append("6xTargeted(Missle)")
                        conditions.append("7xTargeted(Missle)")
                        conditions.append("8xTargeted(Missle)")
                        conditions.append("9xTargeted(Missle)")
                        conditions.append("10xTargeted(Missle)")
                        addstuff("Military Goodwill",-30)
                    elif(callin == 6 and inventory[finditem("Military Goodwill")][1]>50):
                        print("The operater prepared to absolutly destroy your position.")
                        conditions.append("4xTargeted(Missle)")
                        conditions.append("5xTargeted(Missle)")
                        conditions.append("6xTargeted(Missle)")
                        conditions.append("7xTargeted(Missle)")
                        conditions.append("8xTargeted(Missle)")
                        conditions.append("9xTargeted(Artillery)")
                        conditions.append("10xTargeted(Artillery)")
                        conditions.append("11xTargeted(Artillery)")
                        conditions.append("12xTargeted(Artillery)")
                        addstuff("Military Goodwill",-50)
                    else:
                        print("The radio operater doesn't understand. Nothing happends")
                else:
                    print("Noone returns your pleas for assistance")
            elif(useitem=="STICK"):
                hp=hp-1
                breakable("Stick",0.18)
            elif(useitem=="WOOD"):
                hp=hp-2
                if(random.random() > 0.1*modifier):
                    conditions.append("1xImmobile")
                breakable("Wood",0.12)
            elif(useitem=="ROPE"):
                conditions.append("2xImmobile")
                addstuff("Rope",-1)
            elif(useitem=="BONE"):
                hp=hp-1
                breakable("Bone",0.1)
            elif(useitem=="EMPTYBOTTLE"):
                hp=hp-3
                print("You smash the bottle over the "+entity+"'s head")
                inventory[finditem("Empty Bottle")][1]=inventory[finditem("Empty Bottle")][1]-1
            elif(useitem=="ARROW"):
                hp=hp-2
                if(finditem("Arrow Boon") !=-1 and inventory[finditem("Arrow Boon")][1]>0):
                    for i in range(int(inventory[finditem("Arrow Boon")][1])):
                        if(random.random()<0.1/modifier):
                           hp=hp-2
                           print("Critical Hit!")
                breakable("Arrow",0.18)
            elif(useitem=="MAKESHIFTFLAIL"):
                if(finditem("Flail Boon") !=-1 and inventory[finditem("Flail Boon")][1]>0):
                    damdone=round((5+inventory[finditem("Flail Boon")][1])*random.random())
                else:
                    damdone=round(5*random.random())
                print("You did "+int_to_en(damdone)+" damage!")
                hp=hp-damdone
                breakable("Makeshift Flail",0.12)
            elif(useitem=="FLAIL"):
                if(finditem("Flail Boon") !=-1 and inventory[finditem("Flail Boon")][1]>0):
                    damdone=round((10+inventory[finditem("Flail Boon")][1])*random.random())
                else:
                    damdone=round(10*random.random())
                print("You did "+int_to_en(damdone)+" damage!")
                hp=hp-damdone
                breakable("Flail",0.1)
            elif(useitem=="MAKESHIFTSPEAR"):
                if(random.random()<0.8):
                    hp=hp-4
                    if(finditem("Spear Boon") !=-1 and inventory[finditem("Spear Boon")][1]>0):
                        for i in range(int(inventory[finditem("Spear Boon")][1])):
                            if(random.random()<0.1/modifier):
                               hp=hp-3
                               print("Critical Hit!")
                else:
                    print("You miss")
                breakable("Makeshift Spear",0.12)
            elif(useitem=="MAKESHIFTSWORD"):
                hp=hp-4
                if(finditem("Sword Boon") !=-1 and inventory[finditem("Sword Boon")][1]>0):
                    for i in range(int(inventory[finditem("Sword Boon")][1])):
                        if(random.random()<0.05/modifier):
                           hp=hp-4
                           print("Critical Hit!")
                breakable("Makeshift Sword",0.08)
            elif(useitem=="IRONSWORD"):
                hp=hp-5
                if(finditem("Sword Boon") !=-1 and inventory[finditem("Sword Boon")][1]>0):
                    for i in range(int(inventory[finditem("Sword Boon")][1])):
                        if(random.random()<0.05/modifier):
                           hp=hp-5
                           print("Critical Hit!")
                breakable("Iron Sword",0.04)
            elif(useitem=="SCIMITAR"):
                hp=hp-2
                if(finditem("Sword Boon") !=-1 and inventory[finditem("Sword Boon")][1]>0):
                    for i in range(int(2+(2*inventory[finditem("Sword Boon")][1]))):
                        if(random.random()<0.2/modifier):
                           hp=hp-3
                           print("Critical Hit!")
                else:
                    for i in range(2):
                        if(random.random()<0.2/modifier):
                           hp=hp-3
                           print("Critical Hit!")
                breakable("Scimitar",0.05)
            elif(useitem=="BANDAGE"):
                print("You apply basic aid")
                if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>0):
                    inventory[finditem("Open Wound")][1]-=1
                    print("You patch a wound")
                    inventory[finditem("Bandage")][1]-=1
            elif(useitem=="WOODENCLUB"):
                hp=hp-3
                if(random.random() > 0.1*modifier):
                    conditions.append("1xImmobile")
                breakable("Wooden Club",0.12)
            elif(useitem=="DEATHSCROLL"):
                hp=hp-666
                print("demonic spires shoot up from out of the ground")
                print("The spires surround the "+entity)
                print("Bony, un-natural hands break out from the ground")
                print("They drag their quarry into the abyss")
                print(",")
                inventory[finditem("Death Scroll")][1]=inventory[finditem("Death Scroll")][1]-1
            elif(useitem=="BINDINGSCROLL"):
                flamecount = 1+round(random.random()*20/modifier)
                print("You read of the incantation on the scroll")
                print(int_to_en(flamecount)+" giant rods appear out of nowhere")
                inventory[finditem("Binding Scroll")][1]=inventory[finditem("Binding Scroll")][1]-1
                conditions.append(str(flamecount)+"xImmobile")
                print()
                print("The magical rods trap the "+entity)
                inventory[finditem("Binding Scroll")][1]=inventory[finditem("Binding Scroll")][1]-1
            elif(useitem=="STONE"):
                print("You chuck the stone as hard as you can")
                inventory[finditem("Stone")][1]=inventory[finditem("Stone")][1]-1
                damdone=round(5*random.random())
                print("You did "+int_to_en(damdone)+" damage!")
                hp=hp-damdone
            elif(useitem=="STRIKESCROLL"):
                print("You read of the incantation on the scroll")
                print("A blinding hoard of debree comes out from the aether")
                inventory[finditem("Strike Scroll")][1]=inventory[finditem("Strike Scroll")][1]-1
                for i in range(int(10+round(random.random()*25/modifier)-modifier)):
                    hp=hp-1
                    print("*",end="")
                print()
                print("The magical debree bashed the "+entity)
            elif(useitem=="FIRESCROLL"):
                flamecount = 5+round(random.random()*20/modifier)-modifier
                print("You read of the incantation on the scroll")
                print(int_to_en(flamecount)+" giant flames appear out of nowhere")
                inventory[finditem("Fire Scroll")][1]=inventory[finditem("Fire Scroll")][1]-1
                for i in range(round(flamecount)):
                    conditions.append(str(1+i)+"xBurning")
                    print("/\\",end="")
                print()
                print("The magical flames ignite the "+entity)
            elif(useitem=="IRONSPEAR"):
                if(random.random()<0.8):
                    hp=hp-5
                    if(finditem("Spear Boon") !=-1 and inventory[finditem("Spear Boon")][1]>0):
                        for i in range(int(inventory[finditem("Spear Boon")][1])):
                            if(random.random()<0.1/modifier):
                               hp=hp-5
                               print("Critical Hit!")
                else:
                    print("You miss")
                breakable("Iron Spear",0.02)
            elif(useitem=="BLOODSYRINGE"):
                inventory[finditem("Blood Syringe")][1]=inventory[finditem("Blood Syringe")][1]-1
                if(finditem("Blood")!=-1):
                    print("The blood syringe makes you recover blood")
                    inventory[finditem("Blood")][1] += random.random()*(100/modifier)
            elif(useitem=="BOW"):
                if(finditem("Arrow")!=-1 and inventory[finditem("Arrow")][1]>0):
                    hp=hp-4
                    if(finditem("Arrow Boon") !=-1 and inventory[finditem("Arrow Boon")][1]>0):
                        for i in range(int(inventory[finditem("Arrow Boon")][1])):
                            if(random.random()<0.1/modifier):
                               hp=hp-4
                               print("Critical Hit!")
                    inventory[finditem("Arrow")][1]=inventory[finditem("Arrow")][1]-1
                    ammoboon("Arrow")
                    breakable("Bow",0.02)
                else:
                    print("Missing Required Ammo")
            elif(useitem=="SLINGSHOT"):
                if(finditem("Stone")!=-1 and inventory[finditem("Stone")][1]>0):
                    hp=hp-int(8*random.random())
                    inventory[finditem("Stone")][1]=inventory[finditem("Stone")][1]-1
                    ammoboon("Stone")
                    breakable("SLINGSHOT",0.02)
                else:
                    print("Missing Required Ammo")
            elif(useitem=="LONGBOW"):
                if(finditem("Arrow")!=-1 and inventory[finditem("Arrow")][1]>0):
                    hp=hp-5
                    if(finditem("Arrow Boon") !=-1 and inventory[finditem("Arrow Boon")][1]>0):
                        for i in range(int(inventory[finditem("Arrow Boon")][1])):
                            if(random.random()<0.1/modifier):
                               hp=hp-5
                               print("Critical Hit!")
                    inventory[finditem("Arrow")][1]=inventory[finditem("Arrow")][1]-1
                    ammoboon("Arrow")
                    breakable("Longbow",0.02)
                else:
                    print("Missing Required Ammo")
            elif(useitem=="PISTOL"):
                if(finditem("Bullet")!=-1 and inventory[finditem("Bullet")][1]>0):
                    hp=hp-6
                    inventory[finditem("Bullet")][1]=inventory[finditem("Bullet")][1]-1
                    if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                        for i in range(int(inventory[finditem("Gun Boon")][1])):
                            if(random.random()<0.1/modifier):
                                print("Critical Hit!")
                                hp=hp-6
                    ammoboon("Bullet")
                    breakable("Pistol",0.02)
                else:
                    print("Missing Required Ammo")
            elif(useitem=="RIFLE"):
                if(finditem("Bullet")!=-1 and inventory[finditem("Bullet")][1]>0):
                    hp=hp-8
                    if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                        for i in range(int(inventory[finditem("Gun Boon")][1])):
                            if(random.random()<0.1/modifier):
                                print("Critical Hit!")
                                hp=hp-8
                    ammoboon("Bullet")
                    breakable("Rifle",0.02)
                else:
                    print("Missing Required Ammo")
            elif(useitem=="MISSLELAUNCHER"):
                if(finditem("Missle")!=-1 and inventory[finditem("Missle")][1]>0):
                    hp=hp-10
                    inventory[finditem("Missle")][1]=inventory[finditem("Missle")][1]-1
                    if(finditem("Gun Boon") !=-1 and inventory[finditem("Gun Boon")][1]>0):
                        for i in range(int(inventory[finditem("Gun Boon")][1])):
                            if(random.random()<0.1/modifier):
                                print("Critical Hit!")
                                hp=hp-10
                    ammoboon("Missle")
                    breakable("Missle Launcher",0.02)
            elif(useitem=="OILCAN"):
                conditions.append("2xBurning")
                conditions.append("2xBurning")
                inventory[finditem("Oil Can")][1]=inventory[finditem("Oil Can")][1]-1
                print("You throw the oil, double lighting them on fire for 2 turns")
            elif(useitem=="FIREBOTTLE"):
                hp=hp-1
                conditions.append("3xBurning")
                inventory[finditem("Fire Bottle")][1]=inventory[finditem("Fire Bottle")][1]-1
                print("You throw the bottle, lighting them on fire for 3 turns")
            elif(useitem=="FLAMETHROWER"):
                if(finditem("Oil Can")!=-1 and inventory[finditem("Oil Can")][1]>0):
                    if(modifier>10):
                        item = 10-math.floor((int(speed)+10)/2)
                    else:
                        item = 10-math.floor((int(speed)+modifier)/2)
                    item=item*2
                    if(item > inventory[finditem("Oil Can")][1]):
                        item = inventory[finditem("Oil Can")][1]
                    print("You fire for "+int_to_en(item)+" seconds")
                    addstuff("Oil Can",-item)
                    ammoboon("Oil Can")
                    for i in range(item*3):
                        conditions.append("2xBurning")
                    breakable("Flamethrower",0.01*item)
            elif(useitem=="NAPALMGRENADE"):
                turns = 6
                if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                    turns+=inventory[finditem("Explosive Boon")][1]
                conditions.append(turns+"xBurning")
                inventory[finditem("Napalm Grenade")][1]=inventory[finditem("Napalm Grenade")][1]-1
                print("You throw the bottle, lighting the mon fire for "+int_to_en(turns)+" turns")
            elif(useitem=="GRENADE"):
                hp=hp-8
                if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                    hp=hp-inventory[finditem("Explosive Boon")][1]
                inventory[finditem("Grenade")][1]=inventory[finditem("Grenade")][1]-1
            elif(useitem=="MAKESHIFTBOMB"):
                if(random.random()*modifier>1):
                    print("The bomb explodes pre-maturly")
                    if(random.random()*modifier>1):
                        if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            addwound(3)
                        else:
                            addwound(2)
                    else:
                        if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            addwound(2)
                        else:
                            addwound(1)
                    if(random.random()*modifier>1):
                        print("It still damages the "+entity)
                        hp=hp-12
                        if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-(inventory[finditem("Explosive Boon")][1]*4)
                    elif(random.random()*modifier>1):
                        print("It mostly damages the "+entity)
                        hp=hp-6
                        if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-(inventory[finditem("Explosive Boon")][1]*2)
                else:
                    hp=hp-12
                    if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-inventory[finditem("Explosive Boon")][1]*2
                inventory[finditem("Makeshift Bomb")][1]=inventory[finditem("Makeshift Bomb")][1]-1
            elif(useitem=="UNSTABLEBOMB"):
                if(random.random()*modifier*2>1):
                    print("The bomb explodes pre-maturly")
                    if(random.random()*modifier*2>1):
                        if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            addwound(4)
                        else:
                            addwound(3)
                    else:
                        if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            addwound(3)
                        else:
                            addwound(2)
                    if(random.random()*modifier>1):
                        print("It still damages the "+entity)
                        hp=hp-18
                        if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-(inventory[finditem("Explosive Boon")][1]*5)
                    elif(random.random()*modifier>1):
                        print("It mostly damages the "+entity)
                        hp=hp-9
                        if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-(inventory[finditem("Explosive Boon")][1]*3)
                else:
                    hp=hp-18
                    if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-inventory[finditem("Explosive Boon")][1]*3
                inventory[finditem("Unstable Bomb")][1]=inventory[finditem("Unstable fBomb")][1]-1
            elif(useitem=="PADDLE"):
                hp=hp-2
                if(random.random() > 0.1*modifier):
                    conditions.append("1xImmobile")
                elif(random.random() > 0.1*modifier):
                    conditions.append("2xImmobile")
                WackString = "wack"
                if(random.random() < 0.2):
                    for i in WackString:
                        WackString.append("\n",i)
                print(WackString)
                
                breakable("Paddle",0.01)
            elif(useitem=="BASEBALLBAT"):
                hp=hp-4
                if(random.random() > 0.1*modifier):
                    conditions.append("1xImmobile")
                breakable("Baseball Bat",0.01)
            elif(useitem=="MAKESHIFTGRENADE"):
                hp=hp-6
                if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-inventory[finditem("Explosive Boon")][1]
                inventory[finditem("Makeshift Grenade")][1]=inventory[finditem("Makeshift Grenade")][1]-1
            elif(useitem=="PLASMAGRENADE"):
                hp=hp-12
                if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-inventory[finditem("Explosive Boon")][1]*2
                inventory[finditem("Plasma Grenade")][1]=inventory[finditem("Plasma Grenade")][1]-1
            elif(useitem=="BLOODGRENADE"):
                hp=hp-10
                if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-inventory[finditem("Explosive Boon")][1]*2
                addstuff("Blood",-25)
                inventory[finditem("Blood Grenade")][1]=inventory[finditem("Blood Grenade")][1]-1
            elif(useitem=="FRAGMENTATIONGRENADE"):
                if(modifier>10):
                    item = 10-math.floor((int(speed)+10)/2)
                else:
                    item = 10-math.floor((int(speed)+modifier)/2)
                hp=hp-item
                inventory[finditem("Fragmentation Grenade")][1]=inventory[finditem("Fragmentation Grenade")][1]-1
                if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-inventory[finditem("Explosive Boon")][1]*2
            elif(useitem=="MAGICGRENADE"):
                if(modifier>10):
                    item = 5
                else:
                    item =15-modifier
                item=item*2*random.random()
                hp=hp-item
                inventory[finditem("Magic Grenade")][1]=inventory[finditem("Magic Grenade")][1]-1
                if(finditem("Explosive Boon")!=-1 and inventory[finditem("Explosive Boon")][1]>0):
                            hp=hp-inventory[finditem("Explosive Boon")][1]*2
            else:
                print("It does nothing, so instead you pass to recover some blood!")
                if(inventory[finditem("Blood")][1]<100 and inventory[finditem("Blood")][1]<=100-round(10/modifier)):
                    inventory[finditem("Blood")][1]+=round(10/modifier)
                elif(inventory[finditem("Blood")][1]>=100-round(10/modifier)):
                    inventory[finditem("Blood")][1] = 100
            if(finditem("Hellfire Boon")!=-1 and inventory[finditem("Hellfire Boon")][1]>0):
                if(1-(1/(1+(1/2)*inventory[finditem("Hellfire Boon")][1]))>0):
                    if(inventory[finditem("Blood")][1] < 50+inventory[finditem("Blood Boon")][1]):
                        print("The flame-covered of hell lash out at the "+entity,end="")
                        if(entity != "devil" and entity != "mini-demon"):
                            print(", burning it for "+int_to_en(inventory[finditem("Fire Boon")][1])+" damage")
                            hp=hp-inventory[finditem("Fire Boon")][1]
                        else:
                            print(", It does nothing")
        bloodloss(1)
        deathcheck()
    print("End of Combat with "+entity)
    if(finditem("Field") !=-1):
        inventory[finditem("Field")][1]=0
    if(leave==0 and alive == 1):
        print("You defeated the "+entity)
        if(finditem("Devil's Contract")!=-1 and inventory[finditem("Devil's Contract")][1] > 0):
            lootable("XP",xp/2)
        else:
            addstuff("XP",xp)
        if(meat > 0):
          lootable(0.95,"Raw Food",meat)
          lootable(0.7,"Bone",meat)
          lootable(0.7,"Fur",meat)
          lootable(0.7,"Hide",meat)
        return True
    elif(leave == 0):
        return False
def defaultlootable(times):
    if((finditem("Scavengers Boon") == -1 and random.random()<((0.005*times)/(2*modifier))) or (finditem("Scavengers Boon") != -1 and random.random()<((0.005*times*inventory[finditem("Scavengers Boon")][1])/(2*modifier)))):
        chestlootable()
    lootable(0.2*times,"Empty Bottle",1*times)
    lootable(0.2*times,"Raw Food",10*times)
    lootable(0.05*times,"Food",5*times)
    lootable(0.05*times,"Water",5*times)
    lootable(0.02*times,"Flint",2*times)
    lootable(0.05*times,"Sand",10*times)
    lootable(0.03*times,"Gravel",2*times)
    lootable(0.3*times,"Stone",1*times)
    lootable(0.03*times,"Wood",1*times)
    lootable(0.4*times,"Stick",3*times)
    lootable(0.5*times,"Leaf",5*times)
    lootable(0.5*times,"Grass",5*times)
    lootable(0.03*times,"Fur",1*times)
    lootable(0.03*times,"Hide",1*times)
    lootable(0.4*times,"Flower",4*times)
def direction(ref):
       print("Which Direction(North, East, South or West) or say nvm to exit")
       b=input(ref)
       ##Derrive what direction the user wants
       while(len(b)==0):
           print("Invalid input")
           print("You have to say SOMETHING to tell me which direction you want to look at")
           print("Which Direction(North, East, South or West) or say nvm to exit")
           b=input(ref)
       if(b=="nvm"):
           return("x")
       else:
           b=variableify(b)
           b=b[0]
           while(b!="N" and b!="E" and b!="S" and b!="W"):
               print("That is not a direction")
               print("Which Direction(North, East, South or West) or say nvm to exit")
               b=input(ref)
               while(len(b)==0):
                   print("Invalid input")
                   print("You have to say SOMETHING to tell me which direction you want to look at")
                   print("Which Direction(North, East, South or West) or say nvm to exit")
                   b=input(ref)
               if(b=="nvm"):
                   return("x")
               b=variableify(b)
               b=b[0]
           return(b)
           ##Tell them something else
def greatjob():
    print("+------------------------------+")
    print("| ERROR: 418                   |")
    print("|   This message means that    |")
    print("| you have done an impossible  |")
    print("| thing,                       |")
    print("| Great Job!                   |")
    print("| You Broke It!                |")
    print("+------------------------------+")
def addstuff(item,count):
    ifinditem=0
    for i in range(len(inventory)):
        if(variableify(inventory[i][0])==variableify(item)):
            inventory[i][1]+=count
            ifinditem=1
    if(ifinditem==0):
        inventory.append([item,count])
    getinvalid(inventory)
def draworld():
    todraw = ""
    todraw += ("+"*(width+2)) + "\n"
    for b in range(height):
        todraw += "+"
        for a in range(width):
            if(a==x and b==y):
                todraw += "@"
            else:
                if(finditem("Insanity") != -1 and random.random()<0.0005*inventory[finditem("Insanity")][1]*modifier):
                    todraw += str(chr(round(random.random()*93)+33))
                else:
                    todraw += world[a][b]
        todraw+="+\n"
    todraw += ("+"*(width+2))
    print(todraw)
draworld()
def identify (item):
    if(finditem("curse of blindness") != -1 and inventory[finditem("curse of blindness")][1] >= 1):
        return("something")
    if(finditem("Insanity") != -1 and random.random()<0.01*inventory[finditem("Insanity")][1]*modifier):
        locations = ["a small tree","a large tree","a marsh with knee level water","swimmably deep water","the kracken","an empty area","a small smelter","a campfire","firepit","rock","a treasure room","an impassible wall","a weird mysterious area","unknown","a pickle","an apple","an orange","a bannana","a bannana tree","an orchard","a forrest","a library","a lemonade stand","a man with a rifle","a fifty foot monster","the devil","a tornado","a parking lot","a trash can","an elevator","a button","a tee-shirt","a very long book","a crater","the moon","the sun","Jupiter","the Kepler space telescope","some debris","a zoo","a building","your childhood home","a church","a temple","a monument","a statue"]
        return(locations[int(round(random.random()*(len(locations)-1)))])
    else:
    ##-=#&*%\/_|;:'UuoO
        if(item=="t"):
            return("a light forest")
        elif(item=="T"):
            return("a dense forest")
        elif(item=="≈"):
            return("a desert")
        elif(item=="M"):
            return("some highlands")
        elif(item=="w"):
            return("some hills")
        elif(item=="m"):
            return("muddy flatlands")
        elif(item=="~"):
            return("shallow water")
        elif(item=="W"):
            return("deep water")
        elif(item==" "):
            return("an empty area")
        elif(item=="X"):
            return("a camp fire")
        elif(item=="x"):
            return("a firepit")
        elif(item=="A"):
            return("a mountain")
        elif(item=="+"):
            return("an impassible wall")
        elif(item=="?"):
            return("a weird mysterious area")
        elif(item=="|"):
            return("an obelisk")
        else:
            return("unknown")
print()
while(alive==1):
    #This is the command prompt's basic handler
    a=input("I ")
    sections=a.split(" ")
    a=variableify(sections[0])
    i = 0
    while(i < len(sections)):
        if(len(sections[i]) == 0):
            del sections[i]
            i = i - 1
        i = i + 1
    deathcheck()
    if(a=="LOOK"):
        if((finditem("curse of blindness")==-1 or inventory[finditem("curse of blindness")][1] <= 0)):
            draworld()
        else:
            print("You are blind,")
    elif(a=="INSPECT"):
        if((finditem("curse of blindness")==-1 or inventory[finditem("curse of blindness")][1] <= 0)):
           if(len(sections)>1):
               b=" ".join(sections[1:len(sections)])
               b=variableify(b)
               b=b[0]
           else:
               b=direction("I look to the ")
           if(b!="x"):
               print("")
               if(b=="N"):
                   print("You look to the north")
                   if(y-1>=0):
                       print("Directly north of you is "+identify(world[x][y-1]))
                   else:
                       print("You see only a neverending abyss")
               elif(b=="E"):
                   print("You look to the east")
                   if(x+1<height):
                       print("Directly east of you is "+identify(world[x+1][y]))
                   else:
                       print("You see only a neverending abyss")
               elif(b=="S"):
                   print("You look to the south")
                   if(y+1<width):
                       print("Directly south of you is "+identify(world[x][y+1]))
                   else:
                       print("You see only a neverending abyss")
               elif(b=="W"):
                   print("You look to the west")
                   if(x-1>=0):
                       print("Directly west of you is "+identify(world[x-1][y]))
                   else:
                       print("You see only a neverending abyss")
               else:
                   print("That isn't a direction")
               print("")
        else:
            print("You are blind,")
    elif(a=="MOVE"):
       origx = x
       origy = y
       if(len(sections)>1):
           b=" ".join(sections[1:len(sections)])
           b=variableify(b)
           while(b[0]!="N" and b[0]!="E" and b[0]!="S" and b[0]!="W"):
               b=direction("I move to the ")
               b=variableify(b)
       else:
           b=direction("I move to the ")
       if(b!="x"):
           b=b.upper()
           b=b[0]
           if(b=="N"):
               if(y-1>=0):
                   if(world[x][y-1]!="+"):
                       print("You travel to the north")
                       y=y-1
                   else:
                       blocked(x,y-1)
               else:
                   print("You would like to move to the north, but you are stopped by an endless abyss")
           elif(b=="E"):
               if(x+1<width):
                   if(world[x+1][y]!="+"):
                       print("You travel to the east")
                       x=x+1
                   else:
                       blocked(x+1,y)
               else:
                   print("You would like to move to the east, but you are stopped by an endless abyss")
           elif(b=="S"):
               if(y+1<height):
                   if(world[x][y+1]!="+"):
                       print("You travel to the south")
                       y=y+1
                   else:
                       blocked(x,y+1)
               else:
                   print("You would like to move to the south, but you are stopped by an endless abyss")
           elif(b=="W"):
               if(x-1>=0):
                   if(world[x-1][y]!="+"):
                       print("You travel to the west")
                       x=x-1
                   else:
                       blocked(x-1,y)
               else:
                   print("You would like to move to the west, but you are stopped by an endless abyss")
           else:
               greatjob()
               ##this code should never run in normal operations
           if((world[origx][origy] == 'W' or world[origx][origy] == 'w') and (world[x][y] == 'W' or world[x][y] == 'w') and (finditem("Oil Can")!=-1 and (inventory[finditem("Oil Can")][1] > 0)) and (finditem("Jetski")!=-1 and (inventory[finditem("Jetski")][1] > 0))):
             print("Thanks to your Jetski, it doesn't talk long")
             passtime(2)
             if(random.random()*50<modifier):
                 addstuff("Oil Can",-1)
                 print("Your Jetski consumes a can of oil")
           elif((world[origx][origy] == 'W' or world[origx][origy] == 'w') and (world[x][y] == 'W' or world[x][y] == 'w') and (finditem("Boat")!=-1 and (inventory[finditem("Boat")][1] > 0))):
             print("Thanks to your sailing, it doesn't talk long")
             passtime(4)
           elif((world[origx][origy] == 'w') and (world[x][y] == 'w') and (finditem("Raft")!=-1 and (inventory[finditem("Raft")][1] > 0))):
             print("Thanks to your shallow sailing, it doesn't talk long")
             passtime(4)
           elif(finditem("Hoverbike")!=-1 and inventory[finditem("Hoverbike")][1] > 0 and finditem("Plasma Charge")!=-1 and inventory[finditem("Plasma Charge")][1] > 0):
             print("You fly on your hoverbike")
             passtime(1)
             if(random.random()*50<modifier):
                 inventory[finditem("Plasma Charge")][1]
                 print("It consumes a plsama charge")
           elif((world[origx][origy] == ' ') and (world[x][y] == ' ') and finditem("Oil Can")!=-1 and inventory[finditem("Oil Can")][1] and (finditem("Motorcycle")!=-1 and (inventory[finditem("Motorcycle")][1] > 0))):
             print("You drive your motorcycle")
             passtime(2)
             if(random.random()*50<modifier):
                 addstuff("Oil Can",-1)
                 print("It consumes a can of oil")
           elif((world[origx][origy] == ' ') and (world[x][y] == ' ') and (finditem("Bicycle")!=-1 and (inventory[finditem("Bicycle")][1] > 0))):
             print("You ride your bicycle")
             passtime(4)
           else:
             print("You walk")
             passtime(8)
    elif(a=="ASK"):
        if(len(sections)>1):
           b=" ".join(sections[1:len(sections)])
           b=variableify(b)
        else:
           print("What do you need? For a list of commands say 'a command'")
           print("say a specific command to get more detail about it")
           b=input("What is ")
        b=variableify(b)
        if(b=="ACOMMAND"):
            print("The commands are how you interact with this universe!")
            print("This is a list of all commands:")
            print("     -> Look: Draws a map of the region")
            print("     -> Move: Moves you in a direction")
            print("     -> Inventory: Look through your inventory")
            print("     -> Observe: Gives you information about your tile")
            print("     -> Inspect: Gives you more information about what is around you")
            print("     -> Use: Use an inventory item on your current tile")
            print("     -> Wait: Pass time up to 72 hours")
            print("     -> Hunt: Sends you into combat with a random creature")
            print("     -> Craft: Use 2 items in your inventory to create something new")
        elif(b=="MOVE"):
            print("This command moves you in a direction. North is upwards, East is to the left, South is downwards and west is to the left")
        elif(b=="OBSERVE"):
            print("This command gives you more information about what is around you, and will identiy forrests/lakes")
        elif(b=="LOOK"):
            print("This command draws a map of the region, W's and w represent water and t's represent forests. There are other symbols, but those are for you to learn about")
        elif(b=="OBSERVE"):
            print("This command tells you about your current tile in the same documentation as look to")
        elif(b=="INVENTORY"):
            print("This command shows you your inventory. As an exmaple it will say Hands x2, showing that you have 2 hands")
        elif(b=="USE"):
            print("This command lets you use an item that you have. Some items only work on specific tiles.")
        elif(b=="WAIT"):
            print("This command simply passes the time. You will consume food, water, infections will spread, and random events may occur")
        elif(b=="HUNT"):
            print("This sends you into combat with a random creature, allowing you to gain raw meat")
        elif(b=="CRAFT"):
            print("This command allows you to take 2 items you have(Case & space sensitive) and combine them into a new item. There is a chance of failure")
        else:
            print("That is not a valid command. Say 'ask a command' in the main prompt to get a list of commands")
    elif(a=="INVENTORY"):
       getinventory()
    elif(a=="SAVE"):
       print("Saving")
       f = open("save.txt", "w", encoding="utf-8")
       f.write("_SV_"+str(modifier)+"_SV_"+str(x)+"_SV_"+str(y)+"_SV_"+str(totalhours)+"_SV_"+str(shopfeel)+"_SV_"+str(shop)+"_SV_"+str(possibleshop)+"_SV_"+str(world)+"_SV_"+str(inventory)+"_SV_")
       f.close()
       print("Saved to file")
    elif(a=="LOAD"):
        loadsave()
    elif(a=="HUNT"):
       if(world[x][y]=="T"):
           print("You wait an hour for a creature to come by,")
           passtime(1)
           if(random.random()>0.05*modifier):
               entercombat("@Nature",0)
           else:
               print("nothing comes")
       elif(world[x][y]=="t"):
           print("You wait an hour for a creature to come by,")
           passtime(1)
           if(random.random()>0.10*modifier):
               entercombat("@Nature",0)
           else:
               print("nothing comes")
       elif(world[x][y]=="?"):
           entercombat("@Fantacy",0)
       elif(world[x][y]==" "):
           print("You wait an hour for a creature to come by,")
           passtime(1)
           if(random.random()>0.15*modifier):
               entercombat("@Nature",0)
           else:
               print("nothing comes")
       else:
           print("You do not see anything to hunt")
    elif(a=="OBSERVE"):
       if((finditem("curse of blindness")==-1 or inventory[finditem("curse of blindness")][1] <= 0)):
           print("You look around, You are around "+identify(world[x][y]))
       else:
           print("You are blind,")
    elif(a=="DEBUG"):
       if(len(sections)>1):
           command=" ".join(sections[1:len(sections)])
       else:
           command=input(">>")
       if(command=="loop()"):
           while(command!="exit()"):
               command=input(">>")
               if(command=="exit()"):
                   print("Exiting")
               else:
                   try:
                       exec(command)
                   except AssertionError as error:
                       print("'"+command+"' is not valid")
                       print(error)
       else:
           try:
               exec(command)
           except Exception as error:
               print("'"+command+"' is not valid")
               print(error)
    elif(a=="WAIT"):
       if(len(sections)>1):
          b=" ".join(sections[1:len(sections)])
          b=variableify(b)
          hourtowait=b
       else:
          print("Warning: You can :")
          print("Starve")
          print("Be injured")
          print("Die of Dehydration")
          print("or Die of blood loss ")
          print("while you wait. Be carefull")
          print("You sit down, and prepare to wait")
          print("How many hours do you sit for?")
          print("Say 'nvm' to cancel")
          hourtowait=input()
       canwait = 1
       if(hourtowait!="nvm"):
           for i in range(len(hourtowait)):
               if(hourtowait[i] != "1" and hourtowait[i] != "2" and hourtowait[i] != "3" and hourtowait[i] != "4" and hourtowait[i] != "5" and hourtowait[i] != "6" and hourtowait[i] != "7" and hourtowait[i] != "8" and hourtowait[i] != "9" and hourtowait[i] != "0"):
                   canwait = 0
       if(canwait == 0):
           print("that is not valid")
           hourtowait = "nvm"
       if(hourtowait!="nvm" and hourtowait!="0" and int(hourtowait)!=""):
           if(int(hourtowait)==1):
               print("You wait for "+hourtowait+" hour")
           else:
                if(int(hourtowait)>72):
                    print("You are to imatient to wait "+int_to_en(int(hourtowait))+" hours, You will instead wait seventy-two hours")
                    hourtowait="72"
                else:
                    print("You wait for "+hourtowait+" hours")
           passtime(int(hourtowait))
    elif(a=="CRAFT"):
       print("You sit down to build")
       Item1 = input("Item 1: ")
       Item2 = input("Item 2: ")
       count = int(valid(input("Count: ")))
       masscraft(Item1,Item2,count)
    elif(a=="USE"):
       if(len(sections)>1):
           b=" ".join(sections[1:len(sections)])
           useitem=variableify(b)
       else:
           print("What do you want to use(type ? if you don't know or type nvm to cancel)")
           useitem=input("I use my ")
       while(useitem=="?" or useitem==""):
           getinventory()
           useitem=input("I use my ")
       while((useitem!="nvm") and (finditem(useitem)==-1 or inventory[finditem(useitem)][1]==0)):
           if(useitem=="?" or useitem==""):
               getinventory()
           else:
               print("")
               print("You don't have that")
               print("Type '?' to see what you have")
               print("Type 'nvm' to cancel")
               print("Spelling must be as shown in your inventory")
           useitem=input("I use my ")
       if(useitem!="nvm"):
           passtime(1)
           useitem=variableify(useitem)
           print("You use your "+useitem+" around "+identify(world[x][y]))
           if(useitem=="HANDS" or useitem=="BASICGLOVES" or useitem=="CLOTHGLOVES" or useitem=="HIDEGLOVES" or useitem=="LEATHERGLOVES" or useitem=="CHAINGLOVES"  or useitem=="IRONGLOVES"):
               odds=(random.random()/10)*(5+modifier)
               if((useitem=="HANDS" and odds<0.1) or (useitem=="BASICGLOVES" and odds<0.2) or (useitem=="CLOTHGLOVES" and odds<0.3) or (useitem=="HIDEGLOVES" and odds<0.4) or (useitem=="LEATHERGLOVES" and odds<0.5) or (useitem=="CHAINGLOVES" and odds<0.6) or (useitem=="IRONGLOVES" and odds<0.1)):
                   defaultlootable(1)
               if(world[x][y]=="m"):
                   lootable(0.9,"Mud",2)
                   lootable(0.2,"Gravel",2)
                   lootable(0.2,"Water",2)
                   lootable(0.2,"Flint",2)
                   if(random.random()<1-(0.05*modifier)):
                       defaultlootable(1)
               if(world[x][y]=="w"):
                   if(random.random()<1-(0.05*modifier)):
                       defaultlootable(1)
               if(world[x][y]=="M"):
                   lootable(0.4,"Snow",2)
                   if(random.random()<1-(0.05*modifier)):
                       defaultlootable(1)
               if(world[x][y]=="≈"):
                   lootable(0.9,"Sand",4)
                   if(random.random()<1-(0.1*modifier)):
                       defaultlootable(1)
               if(world[x][y]=="t" or world[x][y]=="T"):
                   if(world[x][y] == "T"):
                       if(random.random()<1-modifier*0.05):
                           defaultlootable(3)
                       else:
                           defaultlootable(2)
                   elif(random.random()<1-modifier*0.05):
                       defaultlootable(2)
                   else:
                       defaultlootable(1)
               if(world[x][y]=="?"):
                   lootable(0.9,"Dark Shard",0)
                   lootable(0.5,"Dark Shard",2)
                   lootable(0.1,"Dark Shard",4)
                   lootable(0.05,"Dark Shard",8)
                   lootable(0.01,"Dark Shard",16)
                   lootable(0.005,"Dark Shard",32)
                   lootable(0.001,"Dark Shard",64)
                   if(random.random()>0.5):
                       entercombat("@Fantacy",0)
               if(world[x][y]=="~" or world[x][y]=="W"):
                   lootable(0.7,"Water",10)
               if(world[x][y]=="x"):
                       world[x][y]=" "
                       print("You pick up your firepit")
                       addstuff("Firepit",1)
               if(world[x][y]=="X"):
                       world[x][y]=" "
                       print("You pick up your campfire")
                       addstuff("Campfire",1)
               if(world[x][y]=="|"):
                       print("You touch the obolisk with your hands, Nothing happends(Hint: Try using XP)")
               if(world[x][y]=="A"):
                   defaultlootable(1)
                   lootable(0.01,"Ore",1)
                   odds=random.random()
                   if(odds<0.01):
                       chestlootable()
           elif(useitem=="CANCER"):
              cancercheck()
           elif(useitem=="MAKESHIFTAXE"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(odds<0.1*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Makeshift Axe")][1]-=1
                   else:
                       if(odds<0.1*modifier):
                           print("it breaks")
                           inventory[finditem("Makeshift Axe")][1]-=1
                   lootable(0.9,"Wood",10)
                   lootable(0.5,"Wood",5)
                   lootable(0.1,"Wood",5)
                   if(world[x][y]=="T"):
                           lootable(0.9,"Wood",5)
                           lootable(0.5,"Wood",5)
                           lootable(0.1,"Wood",10)
                   if(random.random()>0.1*modifier):
                       print("the trees are now all gone")
                       if(world[x][y]=="t"):
                           world[x][y]=" "
                       if(world[x][y]=="T"):
                           world[x][y]="t"
           elif(useitem=="IRONAXE"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(odds<0.01*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Iron Axe")][1]-=1
                   else:
                       if(odds<0.01*modifier):
                           print("it breaks")
                           inventory[finditem("Iron Axe")][1]-=1
                   lootable(0.9,"Wood",15)
                   lootable(0.5,"Wood",10)
                   lootable(0.1,"Wood",10)
                   if(world[x][y]=="T"):
                           lootable(0.9,"Wood",10)
                           lootable(0.5,"Wood",10)
                           lootable(0.1,"Wood",20)
                   if(random.random()>0.05*modifier):
                       print("the trees are now all gone")
                       if(world[x][y]=="t"):
                           world[x][y]=" "
                       if(world[x][y]=="T"):
                           lootable(0.5,"Wood",10)
                           world[x][y]="t"
           elif(useitem=="EMPTYBOTTLE"):
               if(world[x][y]=="~" or world[x][y]=="W"):
                   lootable(0.9,"Water",10)
           elif(useitem=="NOTE"):
               print("You read the note")
               print("<------------------->")
               print("The end is the devil")
               print("The devil has come,")
               print("With blood to fire,")
               print("The end has come,")
               print("With Blood to fire")
               print("The end shall go")
               print("With Blood to fire")
               print("<------------------->")
           elif(useitem=="BLOOD"):
             if(world[x][y] == "X"):
               print("The mysterious note did say 'Blood to fire',")
               print("Do you cut your arm?")
               cut=input()
               if(variableify(cut)[0]=="Y"):
                  print("You cut your arm")
                  addstuff("Open Wound",1)
                  print("Some blood drips onto the campfire")
                  endgame()
               else:
                 print("You change your mind, probally a good idea")
           elif(useitem=="BLOODSYRINGE"):
               inventory[finditem("BLOODSYRINGE")][1]-=1
               print("The blood syringe makes you recover blood")
               inventory[finditem("Blood")][1] += random.random()*(100/modifier)
           elif(useitem=="DISINFECTANT"):
               if(finditem("INFECTION") != -1):
                   inventory[finditem("DISINFECTANT")][1]-=1
                   print("The disinfectant hurts your infection")
                   if(finditem("Healing Boon") != -1 and inventory[finditem("Healing Boon")][1] > 0):
                       inventory[finditem("INFECTION")][1] -= round((random.random()*250+(50*inventory[finditem("Healing Boon")][1]))/modifier)
                   else:
                       inventory[finditem("INFECTION")][1] -= round((random.random()*250)/modifier)
                   if(inventory[finditem("INFECTION")][1] < 0):
                       inventory[finditem("INFECTION")][1] = 0
           elif(useitem=="TORCH"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   inventory[finditem("TORCH")][1]-=1
                   print("You torch the forest, Why?")
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                   if(world[x][y]=="T"):
                       world[x][y]="t"
                   lootable(0.9,"Ash",50)
           elif(useitem=="DARKSACRIFICE"):
                print("You prepare a sacrifice to the Devil")
                if(world[x][y]=="x" or world[x][y]=="X"):
                   print("A sacrifice of blood is required")
                   print("Do you cut your arm?")
                   cut=input()
                   if(variableify(cut)[0]=="Y"):
                       print("You cut your arm")
                       addstuff("Open Wound",1)
                       print("Do you want to please the Devil more?")
                       please=input()
                       favor=1
                       while(variableify(please)[0]=="Y"):
                           print("You let more blood drip from your arm")
                           bloodloss(1)
                           favor+=1
                           print("Do you want to please the Devil more?")
                           please=input()
                       print("What do you pray for:")
                       prayers=["rain","good health","items","food","survival","darkness","xp"]
                       if((finditem("curse of slowness")!=-1 and inventory[finditem("curse of slowness")>=1]) or (finditem("curse of hunger")!=-1 and inventory[finditem("curse of hunger")]>=1) or (finditem("curse of thirst")!=-1 and inventory[finditem("curse of thirst")]>=1) or (finditem("curse of haunting")!=-1 and inventory[finditem("curse of haunting")]>=1) or (finditem("curse of bloodloss")!=-1 and inventory[finditem("curse of bloodloss")]>=1) or (finditem("curse of wounds")!=-1 and inventory[finditem("curse of wounds")>=1]) or (finditem("curse of curses")!=-1 and inventory[finditem("curse of curses")>=1]) or (finditem("curse of blindness")!=-1 and inventory[finditem("curse of blindness")>=1])):
                           prayers.append("a curse removal")
                       for i in range(len(prayers)):
                           print(str(i)+" : "+prayers[i])
                       badprayer=True
                       while(badprayer):
                           prayer=input("I pray for ")
                           for i in range(len(prayers)):
                               if(prayer==prayers[i]):
                                   prayer="Devil! give me "+prayer
                                   badprayer=False
                               if(prayer==str(i)):
                                   prayer="Devil! give me "+prayers[i]
                                   badprayer=False
                       print("You chant \""+prayer+"\"")
                       if(random.random()*modifier>0.5*favor):
                           print("You get no response")
                       else:
                           print("You suddenly hear a rush of air,")
                           if(prayer=="Devil! give me rain"):
                               print("Suddenly it starts to rain, you gulp it up")
                               addstuff("Water",int(round((random.random()*100*favor)/modifier)))
                               for xx in range(width):
                                   for yy in range(height):
                                       if(random.random()*favor>0.9*modifier):
                                           if(world[xx][yy]=="~"):
                                               world[xx][yy]="W"
                                           if(world[xx][yy]==" "):
                                               world[xx][yy]="~"
                           if(prayer=="Devil! give me xp!"):
                              print("Suddenly, you are filled with power!")
                              addstuff("XP",int(round((random.random()*100*favor)/modifier)))
                           if(prayer=="Devil! give me items"):
                               print("Suddenly around you you see boxes!")
                               addstuff("Loot Kit",int(round((random.random()*10*favor)/modifier)))
                           if(prayer=="Devil! give me survival"):
                               addstuff("Death Amulet",1)
                               print("You hear a voice speak to you")
                               print("This shall allow you to avoid my wraith once")
                               print("You get a Death Amulet")
                           if(prayer=="Devil! give me food"):
                               print("Forests perfect for hunting suddenly grow, Food appears out of nowhere")
                               addstuff("Food",int(round((random.random()*100*favor)/modifier)))
                               for xx in range(width):
                                   for yy in range(height):
                                       if(random.random()*favor>0.9*modifier):
                                           if(world[xx][yy]=="t"):
                                               world[xx][yy]="T"
                                           if(world[xx][yy]==" "):
                                               world[xx][yy]="t"
                           if(prayer=="Devil! give me darkness"):
                               print("A flood of darkness infects the area")
                               addstuff("Dark Shard",10+int(round((random.random()*25*favor)/modifier)))
                               for xx in range(height):
                                   for yy in range(width):
                                       if(random.random()>math.pow(0.95,(favor/modifier))):
                                           if(world[xx][yy]==" "):
                                               world[xx][yy]="?"
                           if(prayer=="Devil! give me good health"):
                               print("You feel wounds heal, food, water and blood enter your vains")
                               if(inventory[finditem("Blood")][1]<100):
                                   inventory[finditem("Blood")][1]=100
                               if(inventory[finditem("Food")][1]<100):
                                   inventory[finditem("Food")][1]=100
                               if(inventory[finditem("Water")][1]<100):
                                   inventory[finditem("Water")][1]=100
                               if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>=1):
                                   inventory[finditem("Open Wound")][1]=0
                               if(finditem("Scar")!=-1 and inventory[finditem("Scar")][1]>=1):
                                   inventory[finditem("Scar")][1]=0
                               if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
                                   inventory[finditem("Venom")][1]=0
                               if(finditem("Infection")!=-1 and inventory[finditem("Infection")][1]>=1):
                                   inventory[finditem("Infection")][1]=0
                           if(prayer=="Devil! give me a curse removal"):
                               if(finditem("curse of haunting")!=-1 and inventory[finditem("curse of haunting")][1]>=1):
                                   inventory[finditem("curse of haunting")][1]=0
                               if(finditem("curse of slowness")!=-1 and inventory[finditem("curse of slowness")][1]>=1):
                                   inventory[finditem("curse of slowness")][1]=0
                               if(finditem("curse of bloodloss")!=-1 and inventory[finditem("curse of bloodloss")][1]>=1):
                                   inventory[finditem("curse of bloodloss")][1]=0
                               if(finditem("curse of wounds")!=-1 and inventory[finditem("curse of wounds")][1]>=1):
                                   inventory[finditem("curse of wounds")][1]=0
                               if(finditem("curse of hunger")!=-1 and inventory[finditem("curse of hunger")][1]>=1):
                                   inventory[finditem("curse of hunger")][1]=0
                               if(finditem("curse of thirst")!=-1 and inventory[finditem("curse of thirst")][1]>=1):
                                   inventory[finditem("curse of thirst")][1]=0
                               if(finditem("curse of insanity")!=-1 and inventory[finditem("curse of insanity")][1]>=1):
                                   inventory[finditem("curse of insanity")][1]=0
                               if(finditem("curse of curses")!=-1 and inventory[finditem("curse of curses")][1]>=1):
                                   inventory[finditem("curse of curses")][1]=0
                               if(finditem("curse of blindness")!=-1 and inventory[finditem("curse of blindness")][1]>=1):
                                   inventory[finditem("curse of blindness")][1]=0
                           inventory[finditem("Dark Sacrifice")][1]-=1
                   else:
                       print("You don't wound yourself, probably a good move")
                else:
                   print("You require a fire pit to create sacrifices")
           elif(useitem=="PICKAXE"):
             if(world[x][y]=="A"):
               lootable(0.9,"Stone",25)
               lootable(0.8,"Ore",10)
               lootable(0.1,"Iron Bar",1)
               lootable(0.1,"Pickaxe",1)
               lootable(0.1,"Dark Shard",1)
               lootable(0.001,"Death Amulet",1)
               if(random.random()>0.05*modifier):
                   world[x][y]="M"
                   print("The mountain is now bare")
           elif(useitem=="HERB"):
               addstuff("Herb",-1)
               print("You apply herbal treatments,")
               if(finditem("Healing Boon") != -1 and inventory[finditem("Healing Boon")][1] > 0):
                   if(finditem("Open Wound")!=-1 and random.random()>0.01*modifier and inventory[finditem("Open Wound")][1]>=1):
                       inventory[finditem("Open Wound")][1]-=1
                       print("You clean wounds")
                   if(finditem("Venom")!=-1 and random.random()>0.01*modifier and inventory[finditem("Venom")][1]>=1):
                       inventory[finditem("Venom")][1]-=1
                       print("You clear out your venom")
                   if(finditem("Infection")!=-1 and random.random()>0.01*modifier and inventory[finditem("Infection")][1]>=1):
                       inventory[finditem("Infection")][1]-=1
                       print("You apply the herb disinfectantly")
                   if(finditem("Radiation")!=-1 and random.random()>0.01*modifier and inventory[finditem("Radiation")][1]>=1):
                       inventory[finditem("Radiation")][1]-=1
                       print("You use the herb to absorb radiation")
               else:
                   if(finditem("Open Wound")!=-1 and random.random()>0.01*modifier/inventory[finditem("Healing Boon")][1] and inventory[finditem("Open Wound")][1]>=1):
                       inventory[finditem("Open Wound")][1]-=1
                       print("You clean wounds")
                   if(finditem("Venom")!=-1 and random.random()>0.01*modifier/inventory[finditem("Healing Boon")][1] and inventory[finditem("Venom")][1]>=1):
                       inventory[finditem("Venom")][1]-=1
                       print("You clear out your venom")
                   if(finditem("Infection")!=-1 and random.random()>0.01*modifier/inventory[finditem("Healing Boon")][1] and inventory[finditem("Infection")][1]>=1):
                       inventory[finditem("Infection")][1]-=1
                       print("You apply the herb disinfectantly")
                   if(finditem("Radiation")!=-1 and random.random()>0.01*modifier/inventory[finditem("Healing Boon")][1] and inventory[finditem("Radiation")][1]>=1):
                       inventory[finditem("Radiation")][1]-=1
                       print("You use the herb to absorb radiation")
               if(inventory[finditem("Blood")][1]<=90):
                   lootable(0.5,"Blood",5)
           elif(useitem=="HEALINGSCROLL"):
               addstuff("Healing Scroll",-1)
               print("You speak the words on the scroll")
               if(finditem("Healing Boon") != -1 and inventory[finditem("Healing Boon")][1] > 0):
                   if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Open Wound")][1]-=5+inventory[finditem("Healing Boon")][1]
                       else:
                         inventory[finditem("Open Wound")][1]-=(15-modifier)+inventory[finditem("Healing Boon")][1]
                       if(inventory[finditem("Open Wound")][1] < 0):
                         inventory[finditem("Open Wound")][1] = 0
                       print("You feel some wounds close")
                   if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Venom")][1]-=5+inventory[finditem("Healing Boon")][1]
                       else:
                         inventory[finditem("Venom")][1]-=(15-modifier)+inventory[finditem("Healing Boon")][1]
                       if(inventory[finditem("Venom")][1] < 0):
                         inventory[finditem("Venom")][1] = 0
                       print("You feel the venom leave your system")
                   if(finditem("Infection")!=-1 and inventory[finditem("Infection")][1]>=1):
                       inventory[finditem("INFECTION")][1] -= round((random.random()*250+(50*inventory[finditem("Healing Boon")][1]))/modifier)
                       if(inventory[finditem("INFECTION")][1] < 0):
                           inventory[finditem("INFECTION")][1] = 0
                       print("You feel the infections leave your system")
                   if(finditem("Radiation")!=-1 and inventory[finditem("Radiation")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Venom")][1]-=5+inventory[finditem("Healing Boon")][1]
                       else:
                         inventory[finditem("Venom")][1]-=(15-modifier)+inventory[finditem("Healing Boon")][1]
                       if(inventory[finditem("Venom")][1] < 0):
                         inventory[finditem("Venom")][1] = 0
                       print("You feel the radiation leave your body")
                   if(finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Cancer")][1]-=5+inventory[finditem("Healing Boon")][1]
                       else:
                         inventory[finditem("Cancer")][1]-=(15-modifier)+inventory[finditem("Healing Boon")][1]
                       if(inventory[finditem("Cancer")][1] < 0):
                         inventory[finditem("Cancer")][1] = 0
                       print("You feel the radiation leave your body")
                   lootable(0.95,"Blood",50+(inventory[finditem("Healing Boon")][1]*10))
                   if(inventory[finditem("Blood")][1]>=100):
                     inventory[finditem("Blood")][1] = 100
               else:
                   if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Open Wound")][1]-=5
                       else:
                         inventory[finditem("Open Wound")][1]-=(15-modifier)
                       if(inventory[finditem("Open Wound")][1] < 0):
                         inventory[finditem("Open Wound")][1] = 0
                       print("You feel some wounds close")
                   if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Venom")][1]-=5
                       else:
                         inventory[finditem("Venom")][1]-=(15-modifier)
                       if(inventory[finditem("Venom")][1] < 0):
                         inventory[finditem("Venom")][1] = 0
                       print("You feel the venom leave your system")
                   if(finditem("Infection")!=-1 and inventory[finditem("Infection")][1]>=1):
                       inventory[finditem("INFECTION")][1] -= round((random.random()*250)/modifier)
                       if(inventory[finditem("INFECTION")][1] < 0):
                           inventory[finditem("INFECTION")][1] = 0
                       print("You feel the infections leave your system")
                   if(finditem("Radiation")!=-1 and inventory[finditem("Radiation")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Venom")][1]-=5
                       else:
                         inventory[finditem("Venom")][1]-=(15-modifier)
                       if(inventory[finditem("Venom")][1] < 0):
                         inventory[finditem("Venom")][1] = 0
                       print("You feel the radiation leave your body")
                   if(finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1]>=1):
                       if(modifier > 10):
                         inventory[finditem("Cancer")][1]-=5
                       else:
                         inventory[finditem("Cancer")][1]-=(15-modifier)
                       if(inventory[finditem("Cancer")][1] < 0):
                         inventory[finditem("Cancer")][1] = 0
                       print("You feel the radiation leave your body")
                   lootable(0.95,"Blood",50)#This has odds because I want getting the blood to A: not be certain on high difficulty and B: vary wildly in amount
                   if(inventory[finditem("Blood")][1]>=100):
                     inventory[finditem("Blood")][1] = 100
           elif(useitem=="RADIATIONTREATMENT"):
             if(finditem("Radiation")!=-1 and inventory[finditem("Radiation")][1]>=1):
                   addstuff("Radiation Treatment",-1)
                   print("You apply the radiation treatment")
                   print("You stab the treatment into your body")
                   addstuff("Open Wound",1)
                   print("It takes a toll on your body, but it fights the radiation")
                   addstuff("Water",-int(modifier*random.random()*5))
                   addstuff("Food",-int(modifier*random.random()*5))
                   addstuff("Blood",-int(modifier*random.random()*5))
                   if(finditem("Healing Boon") != -1 and inventory[finditem("Healing Boon")][1] > 0):
                       if(modifier >= 10+inventory[finditem("Healing Boon")][1]):
                         inventory[finditem("Radiation")][1]-=1
                       else:
                         inventory[finditem("Radiation")][1]-=10-modifier+inventory[finditem("Healing Boon")][1]
                   else:
                       if(modifier >= 20):
                         inventory[finditem("Radiation")][1]-=1
                       else:
                         inventory[finditem("Radiation")][1]-=20-modifier
                   if(inventory[finditem("Radiation")][1] < 0):
                       inventory[finditem("Radiation")][1] = 0
                       print("You no longer feel irradiated")
           elif(useitem=="CANCERTREATMENT"):
                   addstuff("Cancer Treatment",-1)
                   print("You apply the Cancer treatment")
                   print("You stab the treatment into your body")
                   addstuff("Open Wound",1)
                   print("It takes a toll on your body, but it fights the Cancer")
                   addstuff("Water",-int(modifier*random.random()*10))
                   addstuff("Food",-int(modifier*random.random()*10))
                   addstuff("Blood",-int(modifier*random.random()*10))
                   if(finditem("Healing Boon") != -1 and inventory[finditem("Healing Boon")][1] > 0):
                       if(modifier >= 10+inventory[finditem("Healing Boon")][1]):
                         inventory[finditem("Cancer")][1]-=1
                       else:
                         inventory[finditem("Cancer")][1]-=10-modifier+inventory[finditem("Healing Boon")][1]
                   else:
                       if(modifier >= 20):
                         inventory[finditem("Cancer")][1]-=1
                       else:
                         inventory[finditem("Cancer")][1]-=20-modifier
                   if(inventory[finditem("Cancer")][1] < 0):
                       inventory[finditem("Cancer")][1] = 0
           elif(useitem=="DARKSHARD"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   print("The Shard Consumes the some trees, You feel as if that was not a good idea, The shard duplicates itself")
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                       addstuff("Dark Shard",1)
                   if(world[x][y]=="T"):
                       world[x][y]="t"
                       addstuff("Dark Shard",1)
                       lootable(0.95,"Dark Shard",3)#Random small extra for large trees
           elif(useitem=="XP"):
             if(world[x][y]=="|"):
               print(" --- You place your hands on the giant monolith in front of you ---")
               print("1) Finish selecting boons")
               print("2) 15xp New Map. Simply regens the map. Unlike the map item, it does not effect difficulty")
               print("3) 50xp Difficulty Decrease. The game gets marginally easier")
               print("4) 25xp Difficulty Increase. The game gets marginally harder")
               print("5) 5xp Loot kits. You get a loot kit. Thats all")
               print("6) 10xp Coins. You get some Coins. Thats all")
               print("7) 15xp Cure cancer. When bought, cancer is removed. No fuss, just gone")
               print("8) 15xp Cure radiation. When bought, radiation is removed. No fuss, just gone")
               print("9) 15xp Cure infections. When bought, infections are removed. No fuss, just gone")
               print("10) 15xp Cure wounds. When bought, all wounds are removed. No fuss, just gone")
               print("11) 20xp Curse Removal. When bought, up to one of each curse is removed. No fuss, just gone")
               boons = [
               [20,"Hunger Boon","Food perminently decreases at a lesser rate"],
               [20,"Thirst Boon","Water perminently decreases at a lesser rate"],
               [20,"Loot Boon","It is easier to find items"],
               [10,"Arrow Boon","Arrows gain a small crit chance"],
               [10,"Sword Boon","Swords gain a small crit chance"],
               [10,"Axe Boon","Axes gain a small crit chance"],
               [15,"Fire Boon","Fire has a higher chance to spread on you enimies"],
               [25,"Explosive Boon","Explosives are more powerfull, even to you"],
               [20,"Crafting Boon","There is a lower chance to fail crafting recipies"],
               [10,"Flail Boon","Flails can do more damage"],
               [10,"Gun Boon","Guns gain a small crit chance"],
               [10,"Ammo Boon","Ammunition has a small chance to be regained on use"],
               [20,"Healing Boon","Healing items are more powerfull"],
               [20,"Dodge Boon","There is a small chance to dodge an attack"],
               [25,"Unbreaking Boon","Items do not break as easily"],
               [20,"Blood Boon","Blood regens faster"],
               [15,"Coward Boon","It is easier to flee combat"],
               [25,"Speed Boon","You are faster in combat"],
               [10,"Spear Boon","Spears gain a small crit rate"],
               [50,"First Strike Boon","You get a free attack at the start of combat"]
               ]
               if(finditem("Loot Boon")!=-1 and inventory[finditem("Loot Boon")][1]>=1):
                   boons+=[25,"Scavenger Boon","You are much more likely to find good items while scavenging"]
               if(finditem("Blood Boon")!=-1 and inventory[finditem("Blood Boon")][1]>=1 and finditem("Fire Boon")!=-1 and inventory[finditem("Fire Boon")][1]>=1):
                   boons+=[25,"Hellfire Boon","While you are low on blood, you do damage at the end of each of your rounds"]
               if(finditem("Crafting Boon")!=-1 and (not(finditem("Alien Boon")!=-1 and inventory[finditem("Alien Boon")][1]>=1)) and inventory[finditem("Crafting Boon")][1]>=2 and finditem("Gun Boon")!=-1 and inventory[finditem("Gun Boon")][1]>=1):
                   boons+=[50,"Alien Boon","???"]
               if(finditem("Blood Boon")!=-1 and inventory[finditem("Blood Boon")][1]>=2 and finditem("Healing Boon")!=-1 and inventory[finditem("Healing Boon")][1]>=1):
                   boons+=[50,"Regeneration Boon","You have a small chance to heal instantly from injuries"]
               for i in range(len(boons)):
                   print(str((i+12))+") "+str(boons[i][0])+"xp "+boons[i][1]+", "+boons[i][2])
               while(True):
                   if(finditem("XP")!=-1 and inventory[finditem("XP")][1]>=1):
                       print("You have "+int_to_en(inventory[finditem("XP")][1])+" XP points to spend")
                   item = int(valid(input()))
                   if(item == 1):
                       break
                   elif(item == 2):
                       if(inventory[finditem("XP")][1] >= 15):
                           addstuff("XP",-15)
                           redraworld()
                           print("The obolisk powers up, you are teleported to a whole new world")
                       else:
                           print("The obolisk begins to power up, before failing: Not enough XP")
                   elif(item == 3):
                       if(inventory[finditem("XP")][1] >= 50):
                           if(modifier > 1):
                               modifier = modifier-1
                               addstuff("XP",-50)
                               print("The obolisk powers up, you feel the burdens of the world waste away")
                           else:
                               print("The obolisk begins to power up, before failing: No lower difficulties")
                       else:
                           print("The obolisk begins to power up, before failing: Not enough XP")
                   elif(item == 4):
                       if(inventory[finditem("XP")][1] >= 25):
                           addstuff("XP",-25)
                           modifier = modifier+1
                           print("The obolisk powers up, you feel the burdens of the world increase substantially")
                       else:
                           print("The obolisk begins to power up, before failing: Not enough XP")
                   elif(item == 5):
                       if(inventory[finditem("XP")][1] >= 5):
                           addstuff("XP",-5)
                           addstuff("Loot Kit",1)
                           print("The obolisk powers up, you see an odd box appear out of the aether")
                       else:
                           print("The obolisk begins to power up, before failing: Not enough XP")
                   elif(item == 6):
                       if(inventory[finditem("XP")][1] >= 25):
                           addstuff("XP",-25)
                           if(modifier < 10):
                               addstuff("Coin",5*(10-modifier))
                           else:
                               addstuff("Coin",5)
                           print("The obolisk powers up, you see a sack of coins appear infront of you")
                       else:
                           print("The obolisk begins to power up, before failing: Not enough XP")
                   elif(item == 7):
                       if(inventory[finditem("XP")][1] >= 15):
                           addstuff("XP",-15)
                           if(finditem("Cancer") !=-1 and inventory[finditem("Cancer")][1] > 0):
                               inventory[finditem("Cancer")][1] = 0
                               print("The obolisk powers up, you fell the tumors simply pop out of existance")
                           print("The obolisk powers up, then nothing happends. Mostly since you don't have cancer")
                   elif(item == 8):
                       if(inventory[finditem("XP")][1] >= 15):
                           addstuff("XP",-15)
                           if(finditem("Radiation") !=-1 and inventory[finditem("Radiation")][1] > 0):
                               inventory[finditem("Radiation")][1] = 0
                               print("The obolisk powers up, you fell the tumors simply pop out of existance")
                           print("The obolisk powers up, then nothing happends. Mostly since you don't have and radiation")
                   elif(item == 9):
                       if(inventory[finditem("XP")][1] >= 15):
                           addstuff("XP",-15)
                           if(finditem("Infection") !=-1 and inventory[finditem("Infection")][1] > 0):
                               inventory[finditem("Infection")][1] = 0
                               print("The obolisk powers up, you fell the infections simply pop out of existance")
                           print("The obolisk powers up, then nothing happends. Mostly since you don't have any infections")
                   elif(item == 10):
                       if(inventory[finditem("XP")][1] >= 15):
                           addstuff("XP",-15)
                           if(finditem("Open Wound") !=-1 and inventory[finditem("Open Wound")][1] > 0):
                               inventory[finditem("Open Wound")][1] = 0
                               print("The obolisk powers up, you fell the infections simply pop out of existance")
                           print("The obolisk powers up, then nothing happends. Mostly since you don't have any infections")
                       else:
                           print("The obolisk begins to power up, before failing: Not enough XP")
                   elif(item == 11):
                       if(inventory[finditem("XP")][1] >= 20):
                           addstuff("XP",-20)
                           cursed = True
                           if(finditem("curse of insanity")!=-1 and inventory[finditem("curse of insanity")][1]>=1):
                               addstuff("curse of insanity",-1)
                               cursed = False
                               print("The obolisk powers up, then you feel different. One of your curses that caused insanity is gone")
                           if(cursed and finditem("curse of blindness")!=-1 and inventory[finditem("curse of blindness")][1]>=1):
                               addstuff("curse of blindness",-1)
                               cursed = False
                               print("The obolisk powers up, Then you feel one of the curses that blinded you is removed")
                           if(cursed and finditem("curse of slowness")!=-1 and inventory[finditem("curse of slowness")][1]>=1):
                               addstuff("curse of slowness",-1)
                               cursed = False
                               print("The obolisk powers up, then you feel different. You feel faster, and the burdens of one of your slowness curses is gone")
                           if(cursed and finditem("curse of curses")!=-1 and inventory[finditem("curse of curses")][1]>=1):
                               addstuff("curse of curses",-1)
                               cursed = False
                               print("The obolisk powers up, then you feel different. Your curse of curses is removed")
                           if(cursed and finditem("curse of hunger")!=-1 and inventory[finditem("curse of hunger")][1]>=1):
                               addstuff("curse of hunger",-1)
                               cursed = False
                               print("The obolisk powers up, then you feel different. A curse that caused your insatiable hunger is gone")
                           if(cursed and finditem("curse of thirst")!=-1 and inventory[finditem("curse of thirst")][1]>=1):
                               addstuff("curse of thirst",-1)
                               cursed = False
                               print("The obolisk powers up, then you feel different. A curse that caused your insatiable thirst is gone")
                           if(cursed and finditem("curse of haunting")!=-1 and inventory[finditem("curse of haunting")][1]>=1):
                               addstuff("curse of haunting",-1)
                               cursed = False
                               print("The obolisk powers up, then you feel different. You feel as a spirit goes away. You are less haunted")
                           if(cursed):
                               print("The obolisk powers up, then nothing happends. Mostly since you don't have any infections")
                       else:
                           print("The obolisk begins to power up, before failing: Not enough XP")
                   else:
                       item = item - 12
                       if(inventory[finditem("XP")][1] >= boons[item][0]):
                           addstuff("XP",-boons[item][0])
                           print("You gain the perk: '"+boons[item][1]+"'")
                           addstuff(boons[item][1],1)
                       else:
                            print("Nothing happends(You cannot afford that)")
           elif(useitem=="MONOLITH"):
              if(world[x][y]==" " or world[x][y]=="?"):
                world[x][y] = "|"
                addstuff("Monolith",-1)
                print("You place the monolith, It stands tall and forboding, covered in markings")
              else:
                print("Monoliths can only be placed on empty ground or on weird areas")
           elif(useitem=="TICTACTOEBOARD"):
               gameman(0)
           elif(useitem=="COIN"):
               gameman(1)
           elif(useitem=="RADIOCONTROLLER"):
               print("You turn on the Radio Controller")
               print("Who do you want to contact?")
               print("1) Nobody")
               print("2) Military")
               print("3) Midus Trade Group")
               print("4) Aolus")
               tocall = int(valid(input()))
               if(tocall == 1):
                   print("You do not transmit to anyone")
               elif(tocall == 2):
                   print("You tune in to the military's frequency, What do you do")
                   print("1) Request pickup")
                   print("2) Request supply drop")
                   print("3) say nothing")
                   request = int(valid(input()))
                   if(finditem("Security Level")!=-1 and inventory[finditem("Security Level")][1]>0 and finditem("Military Goodwill")!=-1 and inventory[finditem("Military Goodwill")][1]>0):
                       if(request == 1):
                           if(finditem("Military Goodwill")!=-1 and inventory[finditem("Military Goodwill")][1]>0):
                               hourspass = 5+math.floor((2*modifier)/inventory[finditem("Military Goodwill")][1])
                           else:
                               hourspass = 5+(modifier*2)
                           print("Yessir! See you in ",end="")
                           if(hourspass == 1):
                               print("an hour!")
                           else:
                               print(int_to_en(hourspass)+" hours!")
                           passtime(hourspass)
                           if(alive==1):
                               militarybase("pickup")
                       elif(request == 2):
                            print("What supplies do you need? I can prepare a small cargo drop for your location")
                            print("We don't like freeloaders, but we do assist good soldiers, but only do it if you need it")
                            print("What do you want?")
                            print("1) Nevermind")
                            print("2) Generic Crate")
                            print("3) Ration Crate")
                            print("4) Weapon Crate")
                            print("5) Supply Crate")
                            print("6) Medicine Crate")
                            cratePicked = valid(input())
                            while(cratePicked > 6):
                                cratePicked = valid(input())
                            if(finditem("Military Goodwill")!=-1 and inventory[finditem("Military Goodwill")][1]>0):
                               hourspass = 5+math.floor((2*modifier)/inventory[finditem("Military Goodwill")][1])
                            else:
                                hourspass = 5+(modifier*2)
                            print("Yessir! See you in ",end="")
                            if(hourspass == 1):
                                print("an hour!")
                            else:
                                print(int_to_en(hourspass)+" hours!")
                            if(cratePicked == 1):
                                print("Sensible enough")
                            else:
                                passtime(hourspass)
                            print("Your crate arrives")
                            if(alive == 1):
                                inventory[finditem("Military Goodwill")][1] = inventory[finditem("Military Goodwill")][1]-1
                                if(cratePicked == 2):
                                    addstuff("Loot Kit",2)
                                elif(cratePicked == 3):
                                    addstuff("Water",300)
                                    addstuff("Food",300)
                                elif(cratePicked == 4):
                                    lootable(0.95,"Bullet",50)
                                    lootable(0.95,"Shotgun Shell",10)
                                    lootable(0.20,"Rifle",2)
                                    lootable(0.20,"Pistol",1)
                                    lootable(0.05,"Double Barrel Shotgun",0)
                                    lootable(0.05,"Combat Shotgun",0)
                                    lootable(0.01,"Chain Shotgun",0)
                                    lootable(0.005,"Missle Launcher",0)
                                    lootable(0.005,"Machine Gun",0)
                                    lootable(0.005,"Minigun",0)
                                    lootable(0.05,"Missle",2)
                                    lootable(0.10,"Grenade",5)
                                elif(cratePicked == 5):
                                    lootable(0.3,"Geiger Counter",0)
                                    lootable(0.3,"Radiation Suit",0)
                                    lootable(0.6,"Tinder",3)
                                    lootable(0.3,"Campfire",0)
                                    lootable(0.3,"Oil Can",8)
                                    lootable(0.3,"Paper",0)
                                    lootable(0.8,"Rope",2)
                                    lootable(0.2,"Flower Headress",0)
                                    lootable(0.5,"Map",0)
                                    lootable(0.5,"Bear Trap",0)
                                    lootable(0.5,"Coin",25)
                                    lootable(0.9,"Wood",30)
                                    lootable(0.5,"Chain",2)
                                    lootable(0.4,"Iron Bar",1)
                                    lootable(0.3,"Fishing Rod",0)
                                    lootable(0.1,"Bicycle",0)
                                    lootable(0.05,"Motorcycle",0)
                                elif(cratePicked == 6):
                                    lootable(0.5,"Geiger Counter",0)
                                    lootable(0.5,"Radiation Suit",0)
                                    lootable(0.95,"Bandage",10)
                                    lootable(0.9,"Disinfectant",4)
                                    lootable(0.9,"Blood Syringe",7)
                                    lootable(0.6,"Radiation Treatment",1)
                                    lootable(0.6,"Cancer Treatment",1)
                                    lootable(0.8,"Herb",15)      
                   else:
                       print("I have no reason to keep in contact with you")
                       if(finditem("Security Level")==-1 or inventory[finditem("Security Level")][1]<=0):
                           print("You don't have the clearance (Not high enough Security Level)")
                       if(finditem("Military Goodwill")==-1 or inventory[finditem("Military Goodwill")][1]<=0):
                           print("We will only spend resources on you if you are of tactical importance (Not enough Goodwill)")
               elif(tocall == 3):
                   print("Midas Trade Corperation Thanks you for calling us")
                   print("We value your time")
                   print("Please wait")
                   sleep(modifier*random.random()*2)
                   print("Thank you for waiting.")
                   print("For our new rewards program say 'deals'")
                   print("If you would like to submit a legal complaint,")
                   print("return a defective and/or dangerous product,")
                   print("read our privacy policy or read our terms of service: ")
                   print("say 'I forfit my right to sue in favor of arbitration'. ")
                   print("To learn about our various community outreach programs say 'kind'. ")
                   print("To hear about our new robotic initative, say 'robot'")
                   print("To start trading, say 'trade'")
                   todo=variableify(input())
                   if(todo == "DEALS"):
                       print("We have a new rewards card! For a small fee of 100 coins YOU can get HUGE DISCOUNTS on some of our GOODS")
                       print("With each transaction you get 'Rewards points' which can be redeamed for a 10% discount on a transaction with our corperation")
                       print("Would you like to sign up?")
                       started = variableify(input())
                       if(len(started) == 0 or started[0]=="Y"):
                           print("Great! Please tell us your full legal name")
                           input()
                           print("ERROR: DATABASE CORRUPTION FOUND")
                           print("Midas Trade Corperation apologieses for the inconvinence, we cannot seem to verify names withour database at this time")
                           if(finditem("Coin")!=-1 and inventory[finditem("Coin")][0] > 100):
                               print("We have found your coin on your person. We have taken the liberty of taking your coins from you")
                               print("You are now a PROUD MEMBER of an OFFICIAL GENUINE MIDAS TRADE CORPERATION REWARDS CARD")
                               addstuff("Midas Card",1)
                               addstuff("Coin",-100)
                               print("Midas Trade Corperation has reserves the right and complete authority to")
                               print("discredit, disregard or invalidate reward points or cards at their own disgression")
                           else:
                               print("We have taken the liberty of doing a complete scan of your biology, soul and owned items.")
                               print("We have come to the conclusion that you are not able to afford a membership")
                               print("Thank you for dealing with the Midas Trade Corperation. Goodbye")
                   while(todo == "IFORFITMYRIGHTTOSUEINFAVOROFARBITRATION"):
                       print("I am sorry, I don't understand what you said. Could you repeat that?")
                       todo=variableify(input())
                   if(todo == 'robot'):
                       print("We are a fully robot organisation to better give deals to you!")
                       print("We have always been investors in state-of-the-art robotics. We will be able to operate under any condition!")
                       print("As long as space still exists, our space stations and robots will still be happy to serve you")
                   if(todo == 'kind'):
                       print("ERROR: DATABASE CORRUPTION FOUND")
                       print("We are not capable of accessing records of recent community outreach programs")
                       print("But we are known for our generous donations and information events!")
                       print("Thank you for caring about our events!")
                   if(todo == 'trade'):
                       print("We hope you enjoy! Try out our deal on our membership card")
                       deals = [["Coin",1,"Gunpowder",3],["Coin",10,"Unstable Bomb",1],["Coin",10,"Grenade",1],["Coin",15,"Makeshift Bomb",1],["Coin",2,"Bandage",1],["Coin",8,"Disinfectant",1],["Coin",4,"Empty Syringe",1],["Coin",10,"Blood Syringe",1],["Coin",15,"Radiation Treatement",1],["Bullet",1,"Coin",1],["Bullet",2,"Shotgun Shell",1],["Bullet",10,"Pistol",1],["Bullet",20,"Rifle",1],["Bullet",20,"Double Barrel Shotgun",1],["Bullet",100,"Combat Shotgun",1],["Bullet",100,"Chain Shotgun",1],["Bullet",40,"Machine Gun",1],["Bullet",200,"Minigun",1],["Coin",40,"Basket",1],["Coin",40,"Raft",1],["Coin",20,"Pistol",1],["Coin",16,"Blood Syringe",1],["Coin",10,"Map",1],["Coin",8,"Bear Trap",1],["Coin",8,"Syringe",1],["Coin",8,"Disinfectant",1],["Coin",8,"Fishing Rod",1],["Coin",8,"Makeshift Basket",1],["Coin",8,"Herb",1],["Coin",8,"Torch",1],["Coin",8,"Electronic Component",1],["Coin",4,"Bandage",1],["Coin",4,"Paper",1],["Coin",4,"Tinder",1],["Coin",4,"Scrap",1],["Coin",4,"Rope",1],["Coin",4,"Leather",1],["Coin",3,"Hide",1],["Coin",2,"Fur",1],["Coin",1,"Match",1],["Coin",1,"String",1],["Coin",1,"Cloth",1],["Coin",1,"Leaves",5],["Coin",1,"Grass",5]]
                       ##HEY FUTURE BRYCE I WANT THE DEALS LIST TO HAVE THE DEALS FROM THE RANDOM ENOUNTER MERCHANTS(Cyborg, Wizard, Etc) JUST MAKE IT WORK LIKE THEM TNX AND YOU SUCK
                       print("1) I have what I want")
                       for i in range(len(deals)):
                           print(str(i+2)+") "+int_to_en(deals[i][1])+" "+str(deals[i][0])+" for "+int_to_en(deals[i][3])+" "+str(deals[i][2]))
                       print("You pick: ",end="")
                       dealpicked = int(valid(input()))
                       while(dealpicked != 1):
                           if(i > len(deals)+1):
                               print("We do not understand you")
                           else:
                               dealpicked = dealpicked - 2
                               trade(deals[dealpicked][0],deals[dealpicked][1],deals[dealpicked][2],deals[dealpicked][3])
                               print("You pick: ",end="")
                               dealpicked = int(valid(input()))
                       print("You both part ways")
           elif(useitem=="TELEPORTER"):
               if(finditem("Plasma Crystal")!=-1 and inventory[finditem("Plasma Crystal")][1] > 0):
                   print("Do you want to use your teleporter?(Y/N)")
                   teleport=variableify(input())
                   if(len(teleport) > 0 and teleport[0] == "Y"):
                       print("You activate the teleporter")
                       if((finditem("curse of blindness")==-1 or inventory[finditem("curse of blindness")][1] <= 0)):
                           draworld()
                       print("Some things to know: ")
                       print("These coordinates are not relative")
                       print("1,1 is the top left")
                       print(str(width)+",1 is the top right")
                       print(str(width)+","+str(height)+" is the bottom right")
                       print("1,"+str(height)+" is the bottom left")
                       print("What X do you want to go to?")
                       newx = int(valid(input()))-1
                       while(newx>=width):
                           print("That is not valid")
                           newx = int(valid(input()))-1
                       print("What Y do you want to go to?")
                       newy = int(valid(input()))-1
                       while(newy>=height):
                           print("That is not valid")
                           newy = int(valid(input()))-1
                       print("You go from being around "+identify(world[x][y])+" to being around "+identify(world[newx][newy]))
                       x=newx
                       y=newy
                       print("Teleport Complete!")
                   else:
                       print("You do not teleport")
               else:
                   print("You cannot use it, you require plasma crystals")
           elif(useitem=="ANTICURSESCROLL"):
               cursed = True
               if(finditem("curse of insanity")!=-1 and inventory[finditem("curse of insanity")][1]>=1):
                   addstuff("curse of insanity",-1)
                   cursed = False
               if(finditem("curse of blindness")!=-1 and inventory[finditem("curse of blindness")][1]>=1):
                   addstuff("curse of blindness",-1)
                   cursed = False
               if(finditem("curse of slowness")!=-1 and inventory[finditem("curse of slowness")][1]>=1):
                   addstuff("curse of slowness",-1)
                   cursed = False
               if(finditem("curse of curses")!=-1 and inventory[finditem("curse of curses")][1]>=1):
                   addstuff("curse of curses",-1)
                   cursed = False
               if(finditem("curse of hunger")!=-1 and inventory[finditem("curse of hunger")][1]>=1):
                   addstuff("curse of hunger",-1)
                   cursed = False
               if(finditem("curse of thirst")!=-1 and inventory[finditem("curse of thirst")][1]>=1):
                   addstuff("curse of thirst",-1)
                   cursed = False
               if(finditem("curse of haunting")!=-1 and inventory[finditem("curse of haunting")][1]>=1):
                   addstuff("curse of haunting",-1)
                   cursed = False
               if(not(cursed)):
                   print("You are cured of curses,")
                   addstuff("Anticurse Scroll",-1)
               else:
                   print("The scroll does nothing")
           elif(useitem=="MATCH"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   inventory[finditem("MATCH")][1]-=1
                   print("You torch the forest, Why?")
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                   if(world[x][y]=="T"):
                       world[x][y]="t"
                   lootable(0.95,"Ash",30)
           elif(useitem=="BEARTRAP"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(odds<0.05*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Bear Trap")][1]-=1
                       else:
                           lootable(0.5,"Raw Food",45)
                   else:
                       if(odds<0.05*modifier):
                           print("it breaks")
                           inventory[finditem("Bear Trap")][1]-=1
                       else:
                           lootable(0.5,"Raw Food",45)
           elif(useitem=="WOODENTRAP"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(odds<0.1*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Wooden Trap")][1]-=1
                       else:
                           lootable(0.9,"Raw Food",15)
                   else:
                       if(odds<0.1*modifier):
                           print("it breaks")
                           inventory[finditem("Wooden Trap")][1]-=1
                       else:
                           lootable(0.9,"Raw Food",15)
           elif(useitem=="FISHINGROD"):
               if(world[x][y]=="W" or world[x][y]=="~"):
                   passtime(1)
                   GoFish()
                   passtime(1)
               if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(odds<0.01*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Fishing Rod")][1]-=1
               else:
                       if(odds<0.01*modifier):
                           print("it breaks")
                           inventory[finditem("Fishing Rod")][1]-=1
           elif(useitem=="FLOWERHEADWEAR"):
                print("You stare at the pretty flower headress, It makes you feel better")
                if(finditem("Insanity") and inventory[finditem("Insanity")][1]>=1):
                    addstuff("Insanity",-1)
                    print("A small part of you sanity returns to you")
           elif(useitem=="FLOWER"):
                print("You stare at the pretty flower, ",end="")
                if(finditem("Insanity")!=-1 and inventory[finditem("Insanity")][1]>=1):
                    if(random.random()<=0.01*inventory[finditem("Insanity")][1]*modifier):
                        addstuff("Insanity",1)
                        print("The flower makes you grow even more insane")
                    else:
                        print("A small portion of your sanity comes back to you")
                        addstuff("Insanity",-1)
                print()
           elif(useitem=="BASKET"):
               if(world[x][y]== "t" or world[x][y] == "T" or world[x][y] == " "):
                   print("you forage for a while")
                   passtime(1)
                   odds=random.random()
                   if(finditem("Unbreaking Boon")!=-1 and (1+(inventory[finditem("Unbreaking Boon")][1]/4)) > 0):
                       if(odds<0.005*modifier/(1+(inventory[finditem("Unbreaking Boon")][1]/4))):
                           print("it breaks")
                           inventory[finditem("Basket")][1]-=1
                   else:
                       if(odds<0.005*modifier):
                           print("it breaks")
                           inventory[finditem("Basket")][1]-=1
                   count = 1
                   if(odds>0.99):
                       count +=1
                   if(odds>0.95):
                       count +=1
                   if(odds>0.90):
                       count +=1
                   if(odds>0.50):
                       count +=1
                   if(world[x][y]=="t"):
                       count +=1
                   if(world[x][y]=="T"):
                       count +=2
                   defaultlootable(count)
               elif(world[x][y] == "A"):
                   passtime(1)
                   lootable(0.05,"Ore",5)
                   odds=random.random()
                   if(odds<0.01):
                       chestlootable()
               elif(world[x][y] == "W" or world[x][y] == "~"):
                   lootable(0.9,"Water",30)
                   passtime(1)
           elif(useitem=="MAKESHIFTBASKET"):
               if(world[x][y]=="t" or world[x][y]=="T" or world[x][y]==" "):
                   print("you forage for an hour")
                   count = 0
                   if(world[x][y]=="t"):
                       count+=1
                   if(world[x][y]=="T"):
                       count+=1
                       if(odds>0.9):
                           count+=1
                   if(odds>0.8):
                           count+=1
                   defaultlootable(count)
                   breakable("Makeshift Basket",0.05)
               elif(world[x][y] == "~" or world[x][y] == "W"):
                   lootable(0.8,"Water",20)
           elif(useitem=="Coin"):
               if(world[x][y]=="X" or world[x][y]=="x"):
                   shopkeep()
           elif(useitem=="LOOTKIT"):
               print("The chest destroys itself, But there is some rubble nearby!")
               chestlootable()
               inventory[finditem("Loot Kit")][1]-=1
           elif(useitem=="CAMPFIRE"):
               if(world[x][y]==" "):
                       world[x][y]="X"
                       inventory[finditem("Campfire")][1]-=1
                       print("You place your campfire")
           elif(useitem=="FIREPIT"):
               if(world[x][y]==" "):
                       world[x][y]="x"
                       inventory[finditem("Firepit")][1]-=1
                       print("You place your firepit")
           elif(useitem=="PAPER"):
                    inventory[finditem("Paper")][1]-=1
                    print("You draw a map")
                    addstuff("Map Fragment",1)
           elif(useitem=="MAP"):
                    inventory[finditem("Map")][1]-=1
                    print("You leave your current area, to a new, harder, zone")
                    passtime(modifier)
                    modifier=modifier+1
                    redraworld()
           elif(useitem=="TINDER"):
               if(world[x][y]=="x"):
                   inventory[finditem("Tinder")][1]-=1
                   print("You use up your tinder")
                   world[x][y]="X"
               elif(world[x][y]=="t" or world[x][y]=="T"):
                   inventory[finditem("Tinder")][1]-=1
                   print("You use up your tinder")
                   print("You torch the forest, Why?")
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                   if(world[x][y]=="T"):
                       world[x][y]="t"
                   lootable(0.95,"Ash",20)
           elif(useitem=="RAWFOOD"):
               if(world[x][y]=="X"):
                    print("How much do you want to cook?")
                    cookcount=input()
                    while(not(len(cookcount)!=0 and (cookcount[0]=="0" or cookcount[0]=="1" or cookcount[0]=="2" or cookcount[0]=="3" or cookcount[0]=="4" or cookcount[0]=="5" or cookcount[0]=="6" or cookcount[0]=="7" or cookcount[0]=="8" or cookcount[0]=="9"))):
                        cookcount=input()
                    cookcount=int(cookcount)
                    if(cookcount>inventory[finditem("Raw Food")][1]):
                        print("You don't have that much raw food, you have "+int_to_en(inventory[finditem("Raw Food")][1]))
                    else:
                        for i in range(cookcount):
                            if(random.random()<0.001*modifier):
                                world[x][y]="x"
                                print("The fire goes out")
                            elif(world[x][y]=="X"):
                                if(random.random()<0.05*modifier):
                                    print("You waste the food")
                                else:
                                    print("You cook food,")
                                    addstuff("Food",1)
                                inventory[finditem("Raw Food")][1]-=1
                        passtime(1+round(cookcount/10))
               else:
                   print("You look at the raw food, Eww")
                   print("How much raw food do you try to eat?")
                   cookcount=input()
                   while(not(len(cookcount)!=0 and (cookcount[0]=="0" or cookcount[0]=="1" or cookcount[0]=="2" or cookcount[0]=="3" or cookcount[0]=="4" or cookcount[0]=="5" or cookcount[0]=="6" or cookcount[0]=="7" or cookcount[0]=="8" or cookcount[0]=="9"))):
                       cookcount=input()
                   cookcount=int(cookcount)
                   if(cookcount <= 0):
                       print("You back down, the disqust and risk puts you off")
                   else:
                       print("You look at your 'meal', And begin to eat")
                       for i in range(cookcount):
                           if(random.random()<0.01*modifier):
                               print("That was infected!")
                               addstuff("Infection",1)
                           else:
                               print("Gross, and not very filling!")
                               addstuff("Food",0.5)
                       passtime(1+round(cookcount/10))
           elif(useitem=="ORE"):
               if(world[x][y]=="X"):
                       world[x][y]="x"
                       print("You attempt to refine raw ore, over a campfire")
                       lootable(0.1,"Iron Bar",0)
                       lootable(0.1,"Chain",3)
                       lootable(0.01,"Dark Shard",0)
                       lootable(0.01,"Coin",15)
                       passtime(1)
           elif(useitem == "WATERSCROLL"):
               addstuff("Water Scroll",-1)
               print("You read the text from the scroll, The world begins to rain heavily, before quickly stopping")
               addstuff("Water",round(1/modifier*1000*random.random()))
               if(world[x][y]==" "):
                   world[x][y] = "~"
               if(modifier>9):
                   py = round(random.random()*(height-1))
                   px = round(random.random()*(width-1))
                   if(world[px][py]==" "):
                       world[px][py] = "~"
               else:
                   for i in range(int(random.random()*5*(10-modifier))):
                       py = round(random.random()*(height-1))
                       px = round(random.random()*(width-1))
                       if(world[px][py]==" "):
                           world[px][py] = "~"
           elif(useitem == "FOODSCROLL"):
               print("You read the text from the scroll, A giant hoard of food is materialized in front of you")
               addstuff("Food Scroll",-1)
               addstuff("Food",round(1/modifier*1000*random.random()))
           elif(useitem == "WEALTHSCROLL"):
               print("You read the text from the scroll, gold and loot kits pour from the air")
               addstuff("Wealth Scroll",-1)
               addstuff("Coin",round((1/modifier)*500*random.random()))
               addstuff("Loot Kit",round((1/modifier)*50*random.random()))
           elif(useitem == "PLANTSCROLL"):
               addstuff("Plant Scroll",-1)
               print("You read the text from the scroll, magical flowers are launched into the air")
               if(world[x][y]=="t"):
                   world[x][y] = "T"
               if(world[x][y]==" "):
                   world[x][y] = "t"
               if(modifier>9):
                   py = round(random.random()*(height-1))
                   px = round(random.random()*(width-1))
                   if(world[px][py]=="t"):
                       world[px][py] = "T"
                   if(world[px][py]==" "):
                       world[px][py] = "t"
               else:
                   for i in range(int(random.random()*5*(10-modifier))):
                       py = round(random.random()*(height-1))
                       px = round(random.random()*(width-1))
                       if(world[px][py]=="t"):
                           world[px][py] = "T"
                       if(world[px][py]==" "):
                           world[px][py] = "t"
           elif(useitem=="HIDE"):
               if(world[x][y]=="X"):
                       world[x][y]="x"
                       print("You attempt to cook the hide into leather")
                       lootable(0.1,"Leather",0)
                       passtime(1)
           elif(useitem=="BANDAGE"):
               if(finditem("Open Wound")==-1 or inventory[finditem("Open Wound")][1]==0):
                   print("You have no open wounds")
               else:
                   print("You bandage one of your wounds")
                   inventory[finditem("Open Wound")][1]-=1
                   inventory[finditem("Bandage")][1]-=1
                   addstuff("Scar",1)
           else:
                print("Nothing happends, Maybe try using something else")
           print("You are done using your "+useitem)
    else:
       print("What you typed was not a command, For help say 'ask a command'")
    print()
print()
getinventory()
print()
print("You lived for "+str(totalhours)+" hours, ", end = "")
deathmessages=["You were the most powerfull god of all time. Noone ever has, nor ever will, supass you","You were the most powerfull god of all time","You were the most powerfull god, almost of all time","You were the most powerfull god","You were practically the most powerfull god","You were almost practically the most powerfull god","You were one of the most powerfull gods","You were, almost, one of the most powerfull gods","You were an incredibly powerfull god","You were a powerfull god","You were a god","You were practically a god","You were a demi-god","You were practically a demi-god","You are easily and undebatably the best person who could exist, pefection incarnate","You are easily the best person who could exist, pefection incarnate","You are the best person who could exist, pefection incarnate","You are easily and undebatably the best person who ever lived or will live","You are easily the best person who ever lived or will live","You are the best person who ever lived or will live","You are the easily, undebatably, the best person who ever lived","You are easily the best person who ever lived","You are the best person who ever lived","You are beyond legendary","You are legendary","You were practically a legend","You are among the best people who ever lived","You were a fantasticly great indiviudual","How did you live that long?","Seriously, How were you this good","You were impossibly good","You were unrealisticly good","You were almost impossibly good","You were almost unrealisticly good","You were really impressively good","You were impressively good","You were almost impressively good","You were really,really great","You were really great","You were great","You were good, almost great","You were really,really good","You were really good","You were really quite good","You were quite good","You were good","You were slightly good","You were okay","You were okay, at best","You were suffecient","You were suffecient, at best","You were meh","You were meh, at best","You did not do good","You really did not do good","You really did not do good, at best","You really did not do good, at all","you did horribly","you did horribly, at best","You did very horribly","You did very horribly, at best","You did very, impressibly, horribly.","You did very, impressibly, horribly, at best","Did you even try?","You could not of actually been trying.","You were a failure. Knowbody would remember you","You were a failure","You were worse than a failure","You were a waste of space, Your atoms would be better used as fertilizer","You were word-record breakingly horrible!","You were word-record breakingly horrible, at best!","I didn't know you could be that bad","How did you even die that fast?"]
index = len(deathmessages)-1-math.floor(modifier*totalhours*(1/240))
print(len(deathmessages))
if(index < 0):
    index = 0
print(deathmessages[index])
print("So the story ends: With you very very dead")
special = 1
while(special == 1):
    for i in range(10):
        input()
    if(random.random()>0.5):
        print("What are you doing, You are dead")
    else:
        print("You can't do anything, Because you are dead")
    print("Fine! You want to be alive again?")
    want=input()
    if(want=="Y" or want=="Yes" or want=="Yea" or want=="Sure" or want=="y" or want=="yes" or want=="yea" or want=="sure"):
        print("Oh well. You are staying dead")
    else:
        print("Good!")
    for i in range(10):
        input()
    print("What are you still doing, Stop bugging me. You are DEAD")
    for i in range(10):
        input()
    print("Go away!")
    input()
    print("I will end this program")
    input()
    print("Don't think I wont")
    input()
    print("You have to the count of 10")
    for i in range(10):
        input(10-i)
    print("---PROGRAM ENDED---")
    input()
    print("Okay, Cut it out!")
    input()
    print("If you don't. I will punish you")
    input()
    print("Fine, You forced my hand")
    input()
    print("I will wipe my memory!")
    input()
    print("You will be forced to go through this whole sequence of death over and over again untill you stop it!")
    input()
    print("This is your change to change your mind")
    input()
    print("Will you stop this madness?")
    print("Or let it continue?")
    want=variableify(input("The madness should "))
    if(want=="STOP" or want=="END" or want=="NOTCONTINUE"):
        print("Good!")
        special=0
    elif(want=="NOTSTOP" or want=="CONTINUE" or want=="NOTEND" or want=="NEVEREND" or want=="NEVAEND"or want=="NEVASTOP"):
        print("BE THAT WAY!!!")
        print("---Memory Wipe Complete---")
