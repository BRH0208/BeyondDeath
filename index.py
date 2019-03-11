#'Survival Game'(Name WIP). By Bryce Hawken with assistance and ideas from his family and friends(who playtested the game). The entire game is WIP. If you wish to contact me with ideas. Then email bryce@hawken.net 
import random
import math
import time
world=[]
possibleshop=[["Pistol",1,20],["Bullet",32,5],["Wooden Armor",1,20],["Knight Armor",1,50],["Chainmail",1,30],["Fishing Rod",1,10],["Makeshift Spear",1,10],["Makeshift Axe",1,10],["Map",2,15],["Chain",3,15],["Sharpened Stone",15,1],["Trap",3,10],["Flail",1,15],["Iron Spear",1,15],["Iron Sword",2,15],["Loot Kit",1,30],["Blood Syringe",1,15],["Food",30,7],["Water",30,7],["Grass",100,1],["Leaf",100,1],["Stone",20,1],["Stick",20,1],["Fur",10,2],["Hide",10,2],["Raw Food",20,2],["Bandage",3,5],["Iron Bar",3,35],["Ore",10,5],["Arrow",64,2],["Bow",1,5],["Wood",13,5],["Basket",1,30],["Tinder",100,1],["Cloth",100,2]]
shop = []
inventory=[["Blood",100],["Hands",2],["Water",100],["Food",100],["Note",1]]
height = 25
width = 50
x=0
y=0
totalhours = 0

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
invalidmodifier=-1
while(invalidmodifier==1 or invalidmodifier==-1):
    if(invalidmodifier==1):
        print("That is not valid")
    invalidmodifier=0
    modifier=input()
    if(len(modifier)==0):
        invalidmodifier=1
    else:
        valid="0123456789"
        c=0
        for a in range(len(modifier)):
            for b in range(len(valid)):
                if(modifier[a]==valid[b]):
                    c=c+1
        if(c!=len(modifier)):
            invalidmodifier=1
        else:
            if(modifier=="0"):
                invalidmodifier=1
modifier=float(modifier)

def variableify(string):
    string=string.replace(" ", "")
    return(string.upper())
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
    print("+~  +")
    print("+w~ +")
    print("+---+")
    print("This is the map")
    print("You are the @ symbol in the top left")
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
    print("Directly east of you is a large tree")
    print("Now you know that the 'T' symbol represents a large tree. ")
    print("Here are some basics: Trees are represented by the letter 't'(Capital for large trees), Shallow water is '~', deeper water is 'w' ")
    print("")
    print("This game is all about survival, understand?")
    input()
    print("In order to survive you have to hunt, forage, etc.")
    print("Foraging and hunting are more effective around trees")
    print("So you should move to the tree")
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
    print("+w~ +")
    print("+---+")
    print()
    print("The @ moved to the east, just as we commanded it")
    print("The @ covers whatever tile its on, so we have to use the observe command to see what tile we are on")
    print("Type 'I observe'")
    while(input("I ") != "observe"):
        print("try again, it should look exactly like this:")
        print("I observe")
    print("you are around a large tree")
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
    print("Water x100")
    print("Food x100")
    print()
    print("This shows your inventory, You need food blood and water to survive, Coins are the primary currency, loot kits give you free stuff, and your hands are your, well, hands")
    print()
    print("Now that we are around a tree and know what we have, We should do some harvesting!")
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
    print("You use your hands around a large tree")
    print("You get 2x Leaf")
    print("You get 2x Cloth")
    print()
    print("Oh boy! Leaves!")
    print("Okay, not so exiting")
    print("But they can be crafted together!")
    print("type 'I craft' to start crafting")
    while(input("I ") != "craft"):
        print("try again, it should look exactly like this:")
        print("I craft")
    print("")
    print("Remember, we want to craft a 'Leaf' and a 'Cloth'")
    print("You sit down to build")
    while(input("Item 1: ") != "Leaf"):
        print("try again, it should look exactly like this:")
        print("Item 1: Leaf")
    while(input("Item 2: ") != "Cloth"):
        print("try again, it should look exactly like this:")
        print("Item 2: Cloth")
    print("It will take one Cloth and one Leaf and will produce one Bandage")
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
    print("The Game has many things not covered in the tutorial(Hunting, Fishing etc)")
    print("Don't worry: discovery(and dying over and over again) is fun")
    print("Are you ready?")
    input()
    print("I don't care, Begin!")
global alive
alive=1
print()
print("Hey, It's me, the Grim Reaper...")
print("Keep in mind, I cannot hear you")
print("I am in some trouble")
print("The devil kinda, well. Ended the world")
print("And the devil is now trying to destroy me")
print("Could you do me a favor and, Defeat the devil")
print("Again, I can't hear you, so this is not optional")
print("... I don't actualy have enough magic to create stuff for you...")
print("Creating you kinda exausted me....")
print("So, good luck! Try not to die")
print()
print()
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
        defaultlootable()
def tictac(ai):
    winner="I"
    gameover=0;
    start=0;
    while(start==0 or (int(ai)>=3 and gameover==0)):
        array=["+","+","+","+","+","+","+","+","+"];
        turn=1;
        start=1;
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
                    location=str(input());
                    while(location == "No" or location == "no" or len(location)!=2 or int(location[0])>3 or int(location[1])>3 or int(location[0])<1 or int(location[1])<1):
                        print("That is invalid")
                        print("Put in 2 integer coodinates between 1 and 3")
                        print("The first is the y, the 2nd is the x")
                        print("They are next to eachother, So the bottom center square would be 21")
                        location=str(input());
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
                    location=str(input());
                    while(location == "No" or location == "no" or len(location)!=2 or int(location[0])>3 or int(location[1])>3 or int(location[0])<1 or int(location[1])<1):
                        print("That is invalid")
                        print("Put in 2 integer coodinates between 1 and 3")
                        print("The first is the y, the 2nd is the x")
                        print("They are next to eachother, So the bottom center square would be 21")
                        location=str(input());
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
        print("You defeat the devil...")
        print()
        print("You hear as the Grim reaper comes.")
        print("Thanks")
        print("The devil will come back. But now, he won't threaten me.")
        print("My sincerest congradulations")
        print("However, I have some bad news...")
        print("Just as ending the world ahead of shedule is against the rules")
        print("So is summoning people just to have them fight the devil")
        print("I am very sorry")
        print("But just as I gave you life, I must now take it away.")
        print("Do not be sad, You have won")
        print("You sucseeded in your goal, Boom! Purpose furtfilled")
        print("Come with me...")
        dodie=input("(Y/N):")
        if(len(variableify(dodie))>0 and variableify(dodie)[0] == "Y"):
            print("Goodbye")
            alive = 0
        else:
            print("Very funny")
            print()
            print("Oh, You were serious")
            print("But, there is no point")
            print("Your life story is complete")
            print("You scratched off your bucket list")
            print("That is all there is to life")
            print("Yet still you wish to live...")
            print()
            print("Your life was one of hardship, loss, defeat and suffering")
            print("Yet you still wish to live?")
            print("Hmm... Interesting")
            print()
            print("If your life has value regardless of pain, regardless of having a goal")
            print("Then I shall return you to the world")
            print("I shall wipe my memory of you defeating the devil")
            print("just as the devil will forget you ever defeating him")
            print("and you can live, just like you did")
            print("Have fun")
    else:
        print("The devil laughs as he destroys your soul")
        alive = 0
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
    if(loot<odds*(5/modifier)):
        getcount=1+round(mod*random.random()*(5/modifier))
        print("You get "+str(getcount)+"x "+itemname)
        addstuff(itemname,getcount)
def getinventory():
    getinvalid(inventory)
    print("This is what you have:")
    print()
    if(finditem("curse of insanity") == -1):
        for i in range(len(inventory)):
            print(inventory[i][0]+" x"+str(int(inventory[i][1])))
    else:
        for i in range(len(inventory)):
            if(random.random()>inventory[finditem("curse of insanity")][1]*0.01*modifier):
                print(inventory[i][0]+" x"+str(abs((inventory[finditem("curse of insanity")][1]*round((random.random()-0.5)*10*modifier))+int(inventory[i][1]))))
            for i in range(round(inventory[finditem("curse of insanity")][1]*random.random()*(modifier/6))):
                items = ["Vollyball","Crown","Fried Chicken","Apple Pie","HAPPY HAPPY HAPPY","Eye","Dress","T-Shirt","Human Leg","Wing","Stuff","Nonononononono","HUNGER","Missle","Arrow","Bullet","Pistol","Bow","Apple","Wasp","Bee","Tree","Mountain","IM NOT INSANE","NOT INSANE","NO INSANITY HERE","Computer","Sandwhich","Glass of Water","Milk Pitcher","Burger","Cheeseburger","Cannon","Army","Sanity","HELLO!","Friend","Winston","HAHAHAHA","FUNFUNFUN","?","Unknown","Wheel","Castle","Wall","Iron Bar","Buttlerfly","Unicorn","Pickle","Map","Iron Axe","Makeshift Axe","Makeshift Spear","Trash Can","Apples","Fire","Open Wound","Fire Bottle","Empty Bottle","curse of curses","curse of slowness","curse of blindness","curse of hunger","curse of thirst","curse of bloodloss","Dark Shard","Scar","Food","Water","Bandage","Venom","Infection","Map","Paper Towel","Disinfectant","Paper","Dark Amulet","Spoon","Spork","Football","Soccerball","Baseball","Flail","Knife","Gold","Ore","Stick","Wood","Stone","Hide","Leather","Tenticle"]
                print(items[round(random.random()*(len(items)-1))]+" x"+str(abs(inventory[finditem("curse of insanity")][1]*round((random.random()-0.5)*10*modifier))))
def getinvalid(array):
    i=0
    while (i < len(array)):
        if(array[i][1]==0):
            del array[i]
        else:
            i+=1
shopfeel=0
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
        response=input("")
        response=variableify(response)
        if(len(response)==0 or response[0]=="N"):
            print("Your loss")
        elif(response[0] == "D"):
            print("What did you say?")
            if(variableify(input())!=response):
                print("No... I remember you said '"+response+"'")
            print("Lets be reasonable people, turn around, leave, and I will forget this ever happened.")
            print("Do you leave?")
            flee=input("")
            flee=variableify(flee)
            if(len(flee)==0 or flee[0]=="Y"):
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
                        print("You finish him... You monster")
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
            purchase=input("I'll take item number ")
            while(len(purchase)==0):
                print("What did you say?")
                purchase=input("I'll take item number ")
            if(purchase=="nvm"):
                print("Understandable. Come back some other time!")
            elif(len(purchase) == 1 and (purchase[0]=="1" or purchase[0]=="2" or purchase[0]=="3" or purchase[0]=="4" or purchase[0]=="5" or purchase[0]=="6" or purchase[0]=="7" or purchase[0]=="8" or purchase[0]=="9")):
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
                    print("You can't afford that... ")
                    if(afford==0):
                        print("In fact, You can't afford any! Get out of my shop and come back with more coins")
                    else:
                        print("You can only afford "+int_to_en(afford))
                if(random.random()<0.1):
                    if(random.random()<0.5):
                        print("Here, Have a cookie. I have to go but I hope you have a good day")
                        addstuff("Food",1)
                    else:
                        print("Here, Have a coin. I have to go but I hope you have a good day")
                        addstuff("Coin",1)
                else:
                    print("Sorry, I outta leave now.")
            else:
                print("I don't know what you want, Next time, Tell me the item number you want to purchase")
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
def cancraf(a,b,c,d):
    #print("("+b+"=="+c+" and "+a+"=="+d+") or ("+a+"=="+c+" and "+b+"=="+d+")")
    if((b==c and a==d) or (a==c and b==d)):
        return(1)
    else:
        return(0)
def bloodloss(hours):
    if(finditem("Infection")!=-1):
        for i in range(hours * inventory[finditem("Infection")][1]):
            if(random.random()<0.01*modifier):
                print("Your infection spreads")
                inventory[finditem("Blood")][1]=inventory[finditem("Blood")][1]-1
                addstuff("Infection",1)
    if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1] >= 1):
        infectcount = 0
        for i in range(inventory[finditem("Open Wound")][1]):
            if(random.random()<0.01*modifier):
                infectcount+=1
        addstuff("Infection",infectcount)
        if(infectcount >= 1):
          print("Your wounds get infected "+int_to_en(infectcount)+" times")
        if(finditem("curse of bloodloss")==-1):
            inventory[finditem("Blood")][1] = inventory[finditem("Blood")][1] - (inventory[finditem("Open Wound")][1] * modifier * hours)
        else:
            inventory[finditem("Blood")][1] = inventory[finditem("Blood")][1] - (inventory[finditem("Open Wound")][1] * modifier * hours * ((inventory[finditem("curse of bloodloss")][1])))  
    
    if(finditem("Infection") != -1 and inventory[finditem("Infection")][1] >= 1):
      if(inventory[finditem("Blood")][1]<100-inventory[finditem("Infection")][1] and inventory[finditem("Blood")][1]<=100-inventory[finditem("Infection")][1]-round(10/modifier)):
          inventory[finditem("Blood")][1]+=round(10/modifier)
      elif(inventory[finditem("Blood")][1]>110-inventory[finditem("Infection")][1]):
          print("The amount of blood you have isn't healthy, you get a wound")
          addstuff("Open Wound",math.floor((inventory[finditem("Blood")][1]-(100-inventory[finditem("Infection")][1]))/10))
      elif(inventory[finditem("Blood")][1]>=100-inventory[finditem("Infection")][1]-round(10/modifier)):
          inventory[finditem("Blood")][1] = 100-inventory[finditem("Infection")][1]
    else:
      if(inventory[finditem("Blood")][1]<100 and inventory[finditem("Blood")][1]<=100-round(10/modifier)):
          inventory[finditem("Blood")][1]+=round(10/modifier)
      elif(inventory[finditem("Blood")][1]>110):
          print("The amount of blood you have isn't healthy, you get a wound")
          addstuff("Open Wound",math.floor((inventory[finditem("Blood")][1]-100)/10))
      elif(inventory[finditem("Blood")][1]>=100-round(10/modifier)):
          inventory[finditem("Blood")][1] = 100
def passtime(hours):
    global totalhours
    totalhours+=hours
    if(finditem("curse of slowness")!=-1 and inventory[finditem("curse of slowness")][1]>=0):
        hours=hours*(inventory[finditem("curse of slowness")][1]+1)
    for k in range(int(hours)):
        if(alive == 1):
            bloodloss(1)
            if(finditem("curse of curses")!=-1 and inventory[finditem("curse of curses")][1]>=1):
                for i in range(inventory[finditem("curse of curses")][1]):
                    if(random.random()<0.001*modifier):
                        curses=["curses","bloodloss","insanity","wounds","haunting","slowness","hunger","thirst"];
                        curse=round(random.random()*(len(curses)-1))
                        print("Thanks to your curse of curses, you are cursed with "+curses[curse])
                        addstuff("curse of "+curses[curse],1)
            FoodModifier = 1
            WaterModifier = 1
            if(finditem("curse of hunger")!=-1 and inventory[finditem("curse of hunger")][1]>=1):
              FoodModifier=FoodModifier+inventory[finditem("curse of hunger")][1]
            if(finditem("curse of thirst")!=-1 and inventory[finditem("curse of thirst")][1]>=1):
              WaterModifier=WaterModifier+inventory[finditem("curse of thirst")][1]
            if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
              WaterModifier=WaterModifier+inventory[finditem("Venom")][1]
              FoodModifier=FoodModifier+inventory[finditem("Venom")][1]
            
            inventory[finditem("Water")][1] = inventory[finditem("Water")][1] - ((1/10)*modifier*WaterModifier)
            inventory[finditem("Food")][1] = inventory[finditem("Food")][1] - ((1/10)*modifier*FoodModifier)
            if((1/(modifier*20))>random.random()):
                print("On the horizon is a merchant selling his wares")
                shopkeep()
            if((1/(modifier*20))>random.random()):
                traveler()
            if((1/(modifier*20))>random.random()):
                print("You find a chest!")
                chestlootable()
                print()
            if((1/(modifier*20))>random.random()):
                print("You find some scraps nearby")
                defaultlootable()
                print()
            if((1/(modifier*20))>random.random()):
                print("You find a skeleton of an adventurer")
                chestlootable()
                lootable(0.5,"Bone",10)
                print()
            if((1/(modifier*20))>random.random()):
                print("You find an animal carcas")
                lootable(0.01,"Iron Axe",0)
                lootable(0.1,"Makeshift Axe",0)
                lootable(0.5,"Fur",10)
                lootable(0.5,"Raw Food",10)
                lootable(0.5,"Hide",10)
                print()
            if((1/(modifier*20))>random.random()):
                wierdman()
            if((1/(modifier*20))>random.random()):
                print("You find an abandoned trappers station")
                lootable(0.5,"Trap",0)
                lootable(0.1,"Makeshift Sword",0)
                lootable(0.5,"Fur",10)
                lootable(0.5,"Raw Food",10)
                lootable(0.5,"Hide",10)
                print()
            if((1/(modifier*20))>random.random()):
                print("You find an abandoned lumber station")
                lootable(0.5,"Wood",10)
                lootable(0.1,"Iron Axe",0)
                lootable(0.5,"Makeshift Axe",1)
                lootable(0.5,"Stick",20)
                lootable(0.5,"Food",10)
                lootable(0.5,"Water",10)
                print()
            if((1/(modifier*20))>random.random()):
                print("You find the remains of a small camp")
                lootable(0.1,"Campfire",0)
                lootable(0.5,"Tinder",3)
                lootable(0.5,"Water",10)
                lootable(0.5,"Food",10)
                lootable(0.25,"Firepit",1)
                defaultlootable()
                defaultlootable()
                print()
            wounds = 0
            for i in range(int(modifier)):
                if(0.005>random.random()):
                  wounds=wounds+1
                if(0.001>random.random()):
                  rad = 0;
                  if(finditem("Radiation Suit") == -1 or inventory[finditem("Radiation Suit")][1] <= 0):
                    rad+=1
                  if(finditem("Makeshift Radiation Suit") == -1 or inventory[finditem("Makeshift Radiation Suit")][1] <= 0):
                    rad+=2
                  if(finditem("Geiger Counter") == -1 or inventory[finditem("Geiger Counter")][1] <= 0):
                    rad=rad*2
                  else:
                    print("Your geiger counter clicks vigerously, as you quickly leave an area")
                  addstuff("Radiation",rad)
                if(0.002>random.random()):
                  entercombat("@",0);
                if(0.005>random.random()):
                  global x
                  global y
                  lost=False;
                  if(x>0 and x<width-1):
                    lost = True;
                    x+=round(random.random()*2-1)
                  if(y>0 and y<height-1):
                    lost = True;
                    y+=round(random.random()*2-1)
                  if(lost):
                    print("You get lost")
                if(finditem("curse of haunting")!=-1 and inventory[finditem("curse of haunting")][1]>=1):
                    for i in range(int(inventory[finditem("curse of haunting")][1])):
                        if(0.01>random.random()):
                            print("a restless spirit has come to haunt you")
                            entercombat("spirit",0)
                if(finditem("Radiation")!=-1 and inventory[finditem("Radiation")][1]>=1):
                    for i in range(int(inventory[finditem("Radiation")][1])):
                        if(0.001>random.random()):
                          print("You feel odd, then you recognise the signs, Cancer")
                          addstuff("Cancer",1)
                if(finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1]>=1):
                    for i in range(int(inventory[finditem("Cancer")][1])):
                        if(0.001>random.random()):
                          print("Your cancer spreads")
                          addstuff("Cancer",1)
            if(wounds>0):
              addwound(wounds)
            deathcheck()
def deathcheck():
    getinvalid(inventory)
    global alive
    if(alive == 1):
      if(finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1] >= 100):
          alive=0
          print("You died, Your cancer killed you")
      elif(finditem("Blood")==-1 or inventory[finditem("Blood")][1] <= 0):
          alive=0
          print("You died, You ran out of blood")
      elif(finditem("Food")==-1 or inventory[finditem("Food")][1] <= 0):
          alive=0
          print("You died, You ran out of food")
      elif(finditem("Water")==-1 or inventory[finditem("Water")][1] <= 0):
          alive=0
          print("You died, You ran out of water")
    if(alive==0 and finditem("Death Amulet")!=-1 and inventory[finditem("Dark Amulet")][1] > 0):
            inventory[finditem("Death Amulet")][1]-=1
            print("You feel the Death Amulet shake...")
            print("You are brought back from the dead...")
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
def traveler():
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
  if(finditem("curse of insanity")!=-1 and inventory[finditem("curse of insanity")][1] <= 50):
    print("You see the robot turn into a cow.")
    print("The cowbot looks to be made of flowers")
    print("You have no idea what is going on")
    lootable(1,"Flower",0)
  elif(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1] >= 1):
    print("You are hurt. As A human I know that is bad")
    print("The wierd robot dispenses a bandage")
    lootable(1,"Bandage",0)
    print("There you go!")
  elif(finditem("Infection")!=-1 and inventory[finditem("Infection")][1] >= 1):
    print("You are infected")
    print("I can tell from my good not-robotic eyes")
    print("The robot dispenses some disinfectant")
    lootable(1,"Disinfectant",0)
  elif(finditem("Food")==-1 or inventory[finditem("Food")][1] < 50):
    print("You are hungry")
    print("Us humans need sustinance")
    print("The robot dispenses some food")
    lootable(1,"Food",25)
  elif(finditem("Water")==-1 or inventory[finditem("Water")][1] < 50):
    print("You are thirsty")
    print("H2O is required for your continued existance")
    print("The robot dispenses some water")
    lootable(1,"Water",25)
  elif(finditem("Coin")==-1 or inventory[finditem("Coin")][1] < 1):
    print("You have no coins")
    print("Coins are the currency of us humans")
    print("The robot dispenses some coins")
    lootable(1,"Coin",25)
  else:
    print("We humans have to stick together")
    print("Have some stuff I found")
    print("The robot dispenses some random stuff")
    defaultlootable()
    defaultlootable()
    defaultlootable()
    defaultlootable()
    defaultlootable()
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
def docraft(a,b,AInput,ACount,BInput,BCount,Output,OutputCount,Failureodds):
    if(Failureodds!=0):
        Failureodds*=1+(modifier*0.1)
    if(Failureodds>0.9):
        Failureodds=0.9
    if(cancraf(a,b,AInput,BInput)==1):
        print("It will take "+int_to_en(ACount)+" "+AInput+" and "+int_to_en(BCount)+" "+BInput+" and will produce "+int_to_en(OutputCount)+" "+Output)
        print(getodds(1-Failureodds))
        accept=input("(Y/N): ")
        if(variableify(accept)[0]=="Y"):
            if(craft(AInput,ACount,BInput,BCount,Output,OutputCount,Failureodds)==0):
                craft(BInput,BCount,AInput,ACount,Output,OutputCount,Failureodds)
            passtime(1)
        else:
            print("You do not try to craft the item")
def masscraft(a,b):
    docraft(a,b,"Stone",1,"Stick",1,"Makeshift Axe",1,0.3)
    docraft(a,b,"Cloth",1,"String",1,"Makeshift Basket",1,0.3)
    docraft(a,b,"Empty Bottle",1,"Tinder",1,"Fire Bottle",1,0.1)
    docraft(a,b,"Stick",1,"Empty Bottle",10,"Syringe",1,0.1)
    docraft(a,b,"Syringe",1,"Blood",25,"Blood Syringe",1,0.1)
    docraft(a,b,"String",1,"Stick",1,"Bow",1,0.3)
    docraft(a,b,"Wood",1,"Wood",1,"Wooden Armor",1,0.2)
    docraft(a,b,"Wood",1,"Sharpened Stone",1,"Makeshift Spear",1,0.3)
    docraft(a,b,"Stick",1,"Stick",1,"Wooden Club",1,0.2)
    docraft(a,b,"Wooden Club",1,"String",1,"Fishing Rod",1,0.2)
    docraft(a,b,"Leaf",1,"Leaf",1,"Cloth",1,0.2)
    docraft(a,b,"Stick",1,"Cloth",1,"Torch",1,0.3)
    docraft(a,b,"Stick",1,"Tinder",1,"Torch",1,0.3)
    docraft(a,b,"Hide",10,"Cloth",5,"Makeshift Radiation Suit",1,0.3)
    docraft(a,b,"Leaf",1,"Grass",1,"Tinder",1,0.2)
    docraft(a,b,"Wood",1,"Stone",1,"Firepit",1,0.1)
    docraft(a,b,"Stone",1,"String",1,"Makeshift Flail",1,0.2)
    docraft(a,b,"Wood",1,"String",1,"Trap",1,0.1)
    docraft(a,b,"Tinder",1,"Firepit",1,"Campfire",1,0.1)
    docraft(a,b,"Grass",1,"Grass",1,"String",1,0.1)
    docraft(a,b,"Chain",1,"Chain",1,"Chainmail",1,0.1)
    docraft(a,b,"Chainmail",1,"Iron Bar",1,"Knight Armor",1,0.1)
    docraft(a,b,"Wood",1,"Leaf",100,"Roof",1,0.1)
    docraft(a,b,"Wood",1,"Stick",1,"Pickaxe",1,0.1)
    docraft(a,b,"Cloth",1,"Leaf",1,"Bandage",1,0.1)
    docraft(a,b,"Bandage",1,"Flower",1,"Herb",1,0.1)
    docraft(a,b,"Venom",1,"Herb",1,"Water",1,0.2)
    docraft(a,b,"Flower",1,"Herb",1,"Blood",10,0.2)
    docraft(a,b,"Water",2,"Herb",2,"Disinfectant",1,0.2)
    docraft(a,b,"Stone",1,"Stone",1,"Sharpened Stone",1,0.1)
    docraft(a,b,"Stick",1,"Sharpened Stone",1,"Arrow",1,0.2)
    docraft(a,b,"Hands",2,"Leaf",1,"Basic Gloves",1,0.2)
    docraft(a,b,"Basic Gloves",1,"Cloth",1,"Cloth Gloves",1,0)
    docraft(a,b,"Cloth Gloves",1,"Hide",1,"Hide Gloves",1,0)
    docraft(a,b,"Hide Gloves",1,"Leather",1,"Leather Gloves",1,0)
    docraft(a,b,"Leather Gloves",1,"Chain",1,"Chain Gloves",1,0)
    docraft(a,b,"Chain Gloves",1,"Iron Bar",1,"Iron Gloves",1,0)
    docraft(a,b,"Dark Shard",10,"Raw Food",30,"Dark Sacrifice",1,0.2)
    docraft(a,b,"Ash",5,"Dark Shard",1,"Blood",25,0.1)
    docraft(a,b,"Bone",1,"Raw Food",1,"Dark Shard",1,0.1)
    docraft(a,b,"Open Wound",1,"Bandage",1,"Scar",1,0.1)
    docraft(a,b,"Dark Shard",1,"Scar",1,"XP",5,0.1)
    docraft(a,b,"Cloth",1,"Cloth",1,"Paper",1,0.1)
    docraft(a,b,"Paper",1,"Stone",1,"Tic Tac Toe Board",1,0.1)
    #Scrolls!
    docraft(a,b,"Paper",1,"Dark Shard",10,"Blank Scroll",1,0.1)
    docraft(a,b,"Blood",25,"Dark Shard",1,"Dark Shard",2,0.1)
    docraft(a,b,"Blank Scroll",1,"Dark Shard",10,"Anticurse Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Tinder",5,"Fire Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"XP",25,"Monolith",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Sharpened Stone",10,"Strike Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Stick",10,"Plant Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Wood",10,"Plant Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Food",10,"Food Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Herb",5,"Healing Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Disinfectant",1,"Healing Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Blood Syringe",1,"Healing Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Loot Kit",1,"Wealth Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Coin",100,"Wealth Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Blood",10,"Healing Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Stone",10,"Strike Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Rope",1,"Binding Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"String",2,"Binding Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Cloth",5,"Binding Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Water",10,"Flood Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Leaf",10,"Plant Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Death Amulet",1,"Death Scroll",1,0.1)
    docraft(a,b,"Blank Scroll",1,"Grass",10,"Plant Scroll",1,0)
    docraft(a,b,"Blank Scroll",1,"Blank Scroll",1,"Blank Scroll",5,0.5)
    
    docraft(a,b,"Map Fragment",1,"Map Fragment",1,"Map Piece",1,0)
    docraft(a,b,"Map Piece",1,"Map Piece",1,"Map",1,0)
    docraft(a,b,"Makeshift Shield",1,"Iron Bar",1,"Iron Shield",1,0.1)
    docraft(a,b,"Makeshift Axe",1,"Iron Bar",1,"Iron Axe",1,0.2)
    docraft(a,b,"Makeshift Spear",1,"Iron Bar",1,"Iron Spear",1,0.2)
    docraft(a,b,"Wooden Club",1,"Iron Bar",1,"Iron Sword",1,0.2)
    docraft(a,b,"Makeshift Flail",1,"Iron Bar",1,"Flail",1,0.2)
    docraft(a,b,"Chain",1,"Iron Bar",1,"Flail",1,0.2)
    docraft(a,b,"String",1,"Flower",12,"Flower Headwear",1,0.2)
    docraft(a,b,"String",1,"String",1,"Rope",1,0.1)
    deathcheck()
def addwound(wounds):
  saves=0
  hits=0
  for i in range(wounds):
    if((finditem("Knight Armor")==-1 or inventory[finditem("Knight Armor")][1]<1) and (finditem("Chainmail")==-1 or inventory[finditem("Chainmail")][1]<1)):
        if((finditem("Wooden Armor")==-1 or inventory[finditem("Wooden Armor")][1]<1) or (random.random()<0.05*modifier)):
                hits+=1
        else:
            saves+=1
            if(random.random()>0.05*modifier):
                inventory[finditem("Wooden Armor")][1]=inventory[finditem("Wooden Armor")][1]-1
                print("Your Wooden Armor Was destroyed")
    else:
        saves+=1
        if(finditem("Chaimail")!=-1 and inventory[finditem("Chainmail")][1]>=1):
                if(random.random()<0.05*modifier):
                    inventory[finditem("Chainmail")][1]=inventory[finditem("Chainmail")][1]-1
                    print("Your Chaimail Was destroyed")
        if(finditem("Knight Armor")!=-1 and inventory[finditem("Knight Armor")][1]>=1):
                if(random.random()<0.001*modifier):
                    print("Your Knight Armor Was destroyed")
                    inventory[finditem("Knight Armor")][1]=inventory[finditem("Knight Armor")][1]-1
  if(finditem("curse of wounds")!=-1 and inventory[finditem("curse of wounds")][1]>=1):
    hits=hits*(inventory[finditem("curse of wounds")][1]+1)
  print("You were wounded "+int_to_en(hits)+" times")
  if(saves != 0):
    print("Your armor saved you from "+int_to_en(saves)+" wounds")
  addstuff("Open Wound",hits)
    #print(a+" : "+b)
def gameman(v):
  print("A Stranger Approaches...")
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
      print("Well... You seem to know who I am...")
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
          lootable(1,"Death Amulet",0)
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
            betest = True;
            for i in range(len(betamount)):
              if((betamount[i] != "0" and betamount[i] != "1" and    betamount[i] != "2" and betamount[i] != "3" and betamount[i] != "4" and betamount[i] != "5" and  betamount[i] != "6" and betamount[i] != "7" and betamount[i] != "8" and betamount[i] != "9")):
                betest = False;
          betamount = int(betamount)
          odds=1.01**(-1*betamount)
          #print(odds)
          if(random.random()>odds):
              print("Do you actualy HAVE that much money?")
              input()
              print("Let me see...")
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
              tictac(1);
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
                  print("He leaves, "+int_to_en(betamount)+" coins poorer")
              else:
                  print("With a tie, He Leaves")
          else:
              print("I ain't gonna play.")
def wierdman():
  print("You see a wierd man approach")
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
  print("The rambling loonatic leaves")
def chestlootable():
    lootable(0.5,"Coin",50)
    lootable(0.05,"Tic Tac Toe Board",0)
    lootable(0.2,"Bone",0)
    lootable(0.01,"Iron Axe",0)
    lootable(0.01,"Loot Kit",0)
    lootable(0.1,"Makeshift Axe",0)
    lootable(0.05,"Makeshift Shield",0)
    lootable(0.01,"Iron Shield",0)
    lootable(0.05,"Trap",0)
    lootable(0.05,"Syringe",0)
    lootable(0.01,"Iron Bar",0)
    lootable(0.05,"Dark Shard",0)
    lootable(0.05,"Ore",0)
    lootable(0.05,"Emerald",0)
    lootable(0.01,"Iron Sword",0)
    lootable(0.01,"Iron Spear",0)
    lootable(0.05,"Makeshift Spear",0)
    lootable(0.05,"Wooden Club",0)
    lootable(0.05,"Makeshift Sword",0)
    lootable(0.01,"Chain",3)
    lootable(0.01,"Chainmail",0)
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
    lootable(0.01,"Pistol",1)
    lootable(0.005,"Rifle",1)
    lootable(0.05,"Bullet",10)
    lootable(0.1,"Tinder",3)
    lootable(0.07,"Firepit",0)
    lootable(0.07,"Campfire",0)
    lootable(0.07,"Lighter",0)
    lootable(0.1,"Paper",0)
    lootable(0.1,"Rope",2)
    lootable(0.05,"Flower Headress",0)
    lootable(0.1,"Map",0)
    lootable(0.01,"Flail",0)
    lootable(0.01,"Makeshift Flail",0)
    lootable(0.1,"Bandage",1)
    lootable(0.001,"Death Amulet",0)
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
                if(number<5/13):
                    world[a].append("t")
                elif(number<10/13):
                    world[a].append("T")
                elif(number<11/13):
                    world[a].append("A")
                elif(number<12/13):
                    world[a].append("w")
                elif(number<13/13):
                    world[a].append("?")
                else:
                    greatjob()
    for i in range (1+int(10/modifier)):
        #Random Structures
        for a in range(width):
            for b in range(height):
                if(random.random() < 0.001*(1/modifier)):
                    if(a>0 and b>0 and a<width-1 and b<height-1):
                        world[a-1][b] = "?"
                        world[a][b] = "|"
                        world[a+1][b] = "?"
                        world[a][b-1] = "?"
                        world[a][b+1] = "?"
                elif(random.random() < 0.001*(1/modifier)):
                    if(a>0 and b>0 and a<width-1 and b<height-1):
                        world[a][b] = "|"
                        world[a-1][b-1] = "A"
                        world[a-1][b+1] = "A"
                        world[a+1][b-1] = "A"
                        world[a+1][b+1] = "A"
                        world[a-1][b] = " "
                        world[a+1][b] = " "
                        world[a][b-1] = " "
                        world[a][b+1] = " "
                        

        #Make Lakes
        for a in range(width):
            for b in range(height):
                if(world[a][b] == "w"):
                    if(a>0 and random.random()>0.9):
                        world[a-1][b] = "w"
                    if(b>0 and random.random()>0.9):
                        world[a][b-1] = "w"
                    if(a<width-1 and random.random()>0.9):
                        world[a+1][b] = "w"
                    if(b<height-1 and random.random()>0.9):
                        world[a][b+1] = "w"
                if(world[a][b] == "~"):
                    if(a>0 and world[a-1][b] == " " and random.random()>0.9):
                        world[a-1][b] = "~"
                    if(b>0 and world[a][b-1] == " " and random.random()>0.9):
                        world[a][b-1] = "~"
                    if(a<width-1 and world[a+1][b] == " " and random.random()>0.9):
                        world[a+1][b] = "~"
                    if(b<height-1 and world[a][b+1] == " " and random.random()>0.9):
                        world[a][b+1] = "~"
                if(world[a][b] == "w"):
                    if(a>0 and world[a-1][b] == " "):
                        world[a-1][b] = "~"
                    if(b>0 and world[a][b-1] == " "):
                        world[a][b-1] = "~"
                    if(a<width-1 and world[a+1][b] == " "):
                        world[a+1][b] = "~"
                    if(b<height-1 and world[a][b+1] == " "):
                        world[a][b+1] = "~"              
        
def entercombat(entity,surprise):
    possibleentities=["rat","deer","bunny","snake","pig"]
    if (entity[0]=="@"):
        if (entity=="@Nature"):
            possibleentities=["rat","deer","bunny","snake","pig","bat","bear","alligator"]
        elif (entity=="@Fantacy"):
            if(random.random()<0.7):
                possibleentities=["bloodsucker","mini-demon","mutantman","spirit"]
            else:
                possibleentities=["giant bloodsucker","giant mutantman","giant spider","giant crab","ROUS"]
        elif (entity=="@Giant"):
            possibleentities=["giant bloodsucker","giant mutantman","giant spider","giant crab","ROUS"]
        entity=possibleentities[int(random.random()*(len(possibleentities)-1))]
    if(entity[0]=="a" or entity[0]=="e" or entity[0]=="i" or entity[0]=="o" or entity[0]=="u"):
        print("You encounter an "+entity)
    else:
        print("You encounter a "+entity)
    if (entity=="devil"):
        hp=100
        speed=6
        meat=0
        xp=666
        abilities=["demonic reinforcements","death bolt","death bolt","death bolt","death bolt","death bolt","curse","curse","slash","ghostly strike"]
    if (entity=="shopkeeper"):
        hp=30
        speed=5
        meat=0
        xp=100
        abilities=["slash"]
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
        meat=25
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
        xp=20
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
        xp=15
        abilities=["horns","flee","suck blood","small bite","venom bite","infected bite","grapple","claw pinch"]
    if (entity=="giant mutantman"):
        hp=35
        speed=1
        meat=25
        xp=20
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
        meat=25
        xp=15
        abilities=["venom bite","web"]
    if (entity=="giant crab"):
        hp=15
        speed=3
        meat=25
        xp=15
        abilities=["claw pinch"]
    if (entity=="ROUS"):
        hp=7
        speed=4
        meat=10
        xp=10
        abilities=["infected bite","venom bite","small bite","grapple"]
    if(finditem("curse of slowness")!=-1 and inventory[finditem("curse of slowness")][1]>0):
        speed=speed+inventory[finditem("curse of slowness")][1]
    conditions=[]
    leave=0
    while(hp>0 and leave==0 and alive==1):
        i=0
        while(i < len(conditions)):
                if(conditions[i][(conditions[i].find("x")+1):len(conditions[i])]=="Burning"):
                    hp=hp-1
                    if(random.random()<1/modifier):
                        print("The fire spreads...")
                        if(modifier<10):
                            conditions.append(str(int(round(5-(modifier/2))))+"xBurning")
                        else:
                            conditions.append("2xBurning")
                    print("They continue to burn, "+int_to_en(int(conditions[i][0:(conditions[i].find("x"))]))+" turns remain")
                if(conditions[i][(conditions[i].find("x")+1):len(conditions[i])]=="Immobile"):
                    surprise = 1
                    print("They are immobile, "+int_to_en(int(float(conditions[i][0:(conditions[i].find("x"))])))+" turns remain")
                conditions[i]=str(int(float(conditions[i][0:(conditions[i].find("x"))]))-1)+conditions[i][(conditions[i].find("x")):len(conditions[i])]
                if(int(conditions[i][0:(conditions[i].find("x"))])<=0):
                    conditions.pop(i)
                    i-=1
                i+=1
        print()
        if(((1/random.random())<pow(speed*modifier,0.5)) and surprise==0):
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
            if(abilities[abil]=="demonic reinforcements"):
                entercombat("mini-demon",0)
            if(abilities[abil]=="death bolt"):
                addwound(int(modifier))
                if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>=1):
                    print("Now that you bleed, Feel free to die...")
                    addwound(666)
                    getinventory()
            if(abilities[abil]=="claw pinch"):
                game = tictac(1)
                if(game == 0):
                    print("It pinches you with its claws")
                    addwound(round(0.25+random.random()*(modifier/2)))
                elif(game == 1):
                    print("You use the pincers to your advantage")
                    hp=hp-3*round(5/modifier);
                else:
                    print("You block the pincers")
                
            if(abilities[abil]=="summon"):
                entercombat("spirit",0)
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
                curses=["blindness","curses","bloodloss","insanity","wounds","haunting","slowness","hunger","thirst"];
                curse=round(random.random()*(len(curses)-1))
                print("it has cursed you with "+curses[curse])
                addstuff("curse of "+curses[curse],1)
            if(abilities[abil]=="venom bite"):
                addstuff("Venom",1)
            if(abilities[abil]=="grapple"):
                print("the "+entity+" grapples you")
                print("to break its grasp you have to guess the right number")
                print("type a number to start:")
                guess=input()
                while(len(guess)==0):
                    guess=input()
                guess=int(guess)
                numb = round(random.random()*10)
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
                    guess=input()
                    while(len(guess)==0):
                        guess=input()
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
            surprise=0
            print("Your move")
            print("say ? to open inventory")
            useitem=input("I use my ")
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
                if(random.random()>(0.025*speed*modifier)):
                    leave=1
                    print("You escape")
                else:
                    print("You fail")
            elif(useitem=="PASS"):
                print("You do nothing")
            elif(useitem=="HANDS"):
                hp=hp-1
                if(random.random()>0.75):
                    addwound(1)
            elif(useitem=="BASICGLOVES"):
                hp=hp-1
                if(random.random()>0.8):
                    addwound(1)
                if(random.random()>0.6):
                    inventory[finditem("Basic Gloves")][1]=inventory[finditem("Basic Gloves")][1]-1
                    print("It breaks")
                    addstuff("Hands",2)
            elif(useitem=="CLOTHGLOVES"):
                hp=hp-1
                if(random.random()>0.95):
                    addwound(1)
                if(random.random()>0.7):
                    inventory[finditem("Cloth Gloves")][1]=inventory[finditem("Cloth Gloves")][1]-1
                    print("It breaks")
                    addstuff("Hands",2)
            elif(useitem=="HIDEGLOVES"):
                hp=hp-1
                if(random.random()>0.9):
                    addwound(1)
                if(random.random()>0.8):
                    inventory[finditem("Hide Gloves")][1]=inventory[finditem("Hide Gloves")][1]-1
                    print("It breaks")
                    addstuff("Hands",2)
            elif(useitem=="LEATHERGLOVES"):
                hp=hp-1
                if(random.random()>0.99):
                    addwound(1)
                if(random.random()>0.9):
                    inventory[finditem("Leather Gloves")][1]=inventory[finditem("Leather Gloves")][1]-1
                    print("It breaks")
                    addstuff("Hands",2)
            elif(useitem=="CANCER"):
              cancercheck();
            elif(useitem=="CHAINGLOVES"):
                hp=hp-2
                if(random.random()>0.99):
                    inventory[finditem("Chain Gloves")][1]=inventory[finditem("Chain Gloves")][1]-1
                    print("It breaks")
                    addstuff("Hands",2)
            elif(useitem=="HEALINGSCROLL"):
               addstuff("Healing Scroll",-1)
               print("You speak the words on the scroll")
               if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>=1):
                   if(modifier > 10):
                     inventory[finditem("Open Wound")][1]-=5
                   else:
                     inventory[finditem("Open Wound")][1]-=15-modifier
                   if(inventory[finditem("Open Wound")][1] < 0):
                     inventory[finditem("Open Wound")][1] = 0
                   print("You feel some wounds close")
               if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
                   if(modifier > 10):
                     inventory[finditem("Venom")][1]-=5
                   else:
                     inventory[finditem("Venom")][1]-=15-modifier
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
                     inventory[finditem("Venom")][1]-=15-modifier
                   if(inventory[finditem("Venom")][1] < 0):
                     inventory[finditem("Venom")][1] = 0
                   print("You feel the radiation leave your body")
               if(finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1]>=1):
                   if(modifier > 10):
                     inventory[finditem("Cancer")][1]-=5
                   else:
                     inventory[finditem("Cancer")][1]-=15-modifier
                   if(inventory[finditem("Cancer")][1] < 0):
                     inventory[finditem("Cancer")][1] = 0
                   print("You feel the radiation leave your body")
               lootable(1,"Blood",50)
               if(inventory[finditem("Blood")][1]>=100):
                 inventory[finditem("Blood")][1] = 100
            elif(useitem=="IRONGLOVES"):
                hp=hp-3
            elif(useitem=="PICKAXE"):
                hp=hp-(int(random.random()*modifier))-1
            elif(useitem=="HERB"):
                addstuff("Herb",-1)
                print("You apply herbal treatments...")
                if(finditem("Open Wound")!=-1 and random.random()>0.1*modifier and inventory[finditem("Open Wound")][1]>=1):
                   inventory[finditem("Open Wound")][1]-=1
                   print("You clean wounds")
                if(finditem("Venom")!=-1 and random.random()>0.1*modifier and inventory[finditem("Venom")][1]>=1):
                   inventory[finditem("Venom")][1]-=Math.ceil(6/modifier)
                   print("You clear out your venom")
                if(finditem("Infection")!=-1 and random.random()>0.1*modifier and inventory[finditem("Infection")][1]>=1):
                   inventory[finditem("Infection")][1]-=Math.ceil(10/modifier)
                   print("You apply the herb disinfectantly")
                if(inventory[finditem("Blood")][1]<=90):
                   lootable(0.5,"Blood",5)
            elif(useitem=="MAKESHIFTAXE"):
                hp=hp-2
                if(random.random()>0.5):
                    inventory[finditem("Makeshift Axe")][1]=inventory[finditem("Makeshift Axe")][1]-1
                    print("It breaks")
            elif(useitem=="IRONAXE"):
                hp=hp-3
                if(random.random()>0.9):
                    inventory[finditem("Iron Axe")][1]=inventory[finditem("Iron Axe")][1]-1
                    print("It breaks")
            elif(useitem=="STICK"):
                hp=hp-1
                if(random.random()>0.1):
                    inventory[finditem("Stick")][1]=inventory[finditem("Stick")][1]-1
                    print("It breaks")
            elif(useitem=="WOOD"):
                hp=hp-2
                speed=speed/1.1
                if(random.random()>0.4):
                    inventory[finditem("Wood")][1]=inventory[finditem("Wood")][1]-1
                    print("It breaks")
            elif(useitem=="ROPE"):
                conditions.append("2xImmobile")
                if(random.random()>0.9):
                    inventory[finditem("Rope")][1]=inventory[finditem("Rope")][1]-1
                    print("It breaks")
            elif(useitem=="BONE"):
                hp=hp-1
                if(random.random()>0.5):
                    inventory[finditem("Bone")][1]=inventory[finditem("Bone")][1]-1
                    print("It breaks")
            elif(useitem=="EMPTYBOTTLE"):
                hp=hp-3
                print("You smash the bottle over the "+entity+"'s head")
                inventory[finditem("Empty Bottle")][1]=inventory[finditem("Empty Bottle")][1]-1
            elif(useitem=="ARROW"):
                hp=hp-2
                if(random.random()>0.1):
                    inventory[finditem("Arrow")][1]=inventory[finditem("Arrow")][1]-1
                    print("It breaks")
            elif(useitem=="MAKESHIFTFLAIL"):
                damdone=round(5*random.random())
                print("You did "+int_to_en(damdone)+" damage!")
                hp=hp-damdone
                if(random.random()>0.3):
                    inventory[finditem("Makeshift Flail")][1]=inventory[finditem("Makeshift Flail")][1]-1
                    print("It breaks")
            elif(useitem=="FLAIL"):
                damdone=round(10*random.random())
                print("You did "+int_to_en(damdone)+" damage!")
                hp=hp-damdone
                if(random.random()>0.5):
                    inventory[finditem("Flail")][1]=inventory[finditem("Flail")][1]-1
                    print("It breaks")
            elif(useitem=="MAKESHIFTSPEAR"):
                if(random.random()<0.8):
                    hp=hp-3
                else:
                    print("You miss")
                if(random.random()>0.4):
                    inventory[finditem("Makeshift Spear")][1]=inventory[finditem("Makeshift Spear")][1]-1
                    print("It breaks")
            elif(useitem=="MAKESHIFTSWORD"):
                hp=hp-3
                if(random.random()>0.7):
                    inventory[finditem("Iron Sword")][1]=inventory[finditem("Iron Sword")][1]-1
                    print("It breaks")
            elif(useitem=="IRONSWORD"):
                hp=hp-4
                if(random.random()>0.9):
                    inventory[finditem("Iron Sword")][1]=inventory[finditem("Iron Sword")][1]-1
                    print("It breaks")
            elif(useitem=="BANDAGE"):
                print("You apply basic aid")
                if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>0):
                    inventory[finditem("Open Wound")][1]-=1;
                    print("You patch a wound")
                    inventory[finditem("Bandage")][1]-=1;
            elif(useitem=="WOODENCLUB"):
                hp=hp-2
                speed=speed/1.1
                if(random.random()>0.4):
                    inventory[finditem("Wooden Club")][1]=inventory[finditem("Wooden Club")][1]-1
                    print("It breaks")
            elif(useitem=="DEATHSCROLL"):
                hp=hp-666
                print("demonic spires shoot up from out of the ground")
                print("The spires surround the "+entity)
                print("Bony, un-natural hands break out from the ground")
                print("They drag their quarry into the abyss")
                print("...")
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
                print("You did "+str(damdone)+" damage!")
                hp=hp-damdone
            elif(useitem=="STRIKESCROLL"):
                print("You read of the incantation on the scroll")
                print("A blinding hoard of debree comes out from the aether")
                inventory[finditem("Strike Scroll")][1]=inventory[finditem("Strike Scroll")][1]-1
                for i in range(10+round(random.random()*25/modifier)-modifier):
                    hp=hp-1
                    print("*",end="")
                print()
                print("The magical debree bashed the "+entity)
            elif(useitem=="FIRESCROLL"):
                flamecount = 9+round(random.random()*9/modifier)-modifier
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
                else:
                    print("You miss")
                if(random.random()>0.9):
                    inventory[finditem("Iron Spear")][1]=inventory[finditem("Iron Spear")][1]-1
                    print("It breaks")
            elif(useitem=="BLOODSYRINGE"):
                inventory[finditem("Blood Syringe")][1]=inventory[finditem("Blood Syringe")][1]-1
                if(finditem("Blood")!=-1):
                    print("The blood syringe makes you recover blood")
                    inventory[finditem("Blood")][1] += 50/modifier
                    if(inventory[finditem("Blood")][1]<100 and inventory[finditem("Blood")][1]<=100-round(10/modifier)):
                        inventory[finditem("Blood")][1]+=round(10/modifier)
                    elif(inventory[finditem("Blood")][1]>=100-round(10/modifier)):
                        inventory[finditem("Blood")][1] = 100
            elif(useitem=="BOW"):
                if(finditem("Arrow")!=-1 and inventory[finditem("Arrow")][1]>0):
                    hp=hp-5
                    inventory[finditem("Arrow")][1]=inventory[finditem("Arrow")][1]-1
                    if(random.random()>0.9):
                        inventory[finditem("Longbow")][1]=inventory[finditem("Longbow")][1]-1
                        print("It breaks")
                else:
                    print("Missing Required Ammo")
            elif(useitem=="LONGBOW"):
                if(finditem("Arrow")!=-1 and inventory[finditem("Arrow")][1]>0):
                    hp=hp-6
                    inventory[finditem("Arrow")][1]=inventory[finditem("Arrow")][1]-1
                    if(random.random()>0.9):
                        inventory[finditem("Longbow")][1]=inventory[finditem("Longbow")][1]-1
                        print("It breaks")
                else:
                    print("Missing Required Ammo")
            elif(useitem=="PISTOL"):
                if(finditem("Bullet")!=-1 and inventory[finditem("Bullet")][1]>0):
                    hp=hp-8
                    inventory[finditem("Bullet")][1]=inventory[finditem("Bullet")][1]-1
                    if(random.random()>0.9):
                        inventory[finditem("Pistol")][1]=inventory[finditem("Pistol")][1]-1
                        print("It breaks")
                else:
                    print("Missing Required Ammo")
            elif(useitem=="RIFLE"):
                if(finditem("Bullet")!=-1 and inventory[finditem("Bullet")][1]>0):
                    hp=hp-10
                    inventory[finditem("Bullet")][1]=inventory[finditem("Bullet")][1]-1
                    if(random.random()>0.9):
                        inventory[finditem("Rifle")][1]=inventory[finditem("Rifle")][1]-1
                        print("It breaks")
                else:
                    print("Missing Required Ammo")
            elif(useitem=="LIGHTER"):
                conditions.append("5xBurning")
                inventory[finditem("Lighter")][1]=inventory[finditem("Lighter")][1]-1
                print("You throw the lighter, lighting them on fire for 5 turns")
            elif(useitem=="FIREBOTTLE"):
                hp=hp-1
                conditions.append("3xBurning")
                inventory[finditem("Fire Bottle")][1]=inventory[finditem("Fire Bottle")][1]-1
                print("You throw the bottle, lighting them on fire for 3 turns")
            else:
                print("It does nothing, so instead you pass to recover some blood!")
                if(inventory[finditem("Blood")][1]<100 and inventory[finditem("Blood")][1]<=100-round(10/modifier)):
                    inventory[finditem("Blood")][1]+=round(10/modifier)
                elif(inventory[finditem("Blood")][1]>=100-round(10/modifier)):
                    inventory[finditem("Blood")][1] = 100
        bloodloss(1)
        deathcheck()
    if(leave==0 and alive == 1):
        print("You defeated the "+entity)
        if(meat > 0):
          lootable(0.9,"XP",(xp-1)) 
          lootable(0.9,"Raw Food",(meat-1)*10)
          lootable(0.5,"Bone",(meat-1)*10)
          lootable(0.5,"Fur",(meat-1)*10)
          lootable(0.5,"Hide",(meat-1)*10)
        return True;
    elif(leave == 0):
        return False;
    passtime(1)
def defaultlootable():
    if(random.random()<0.01/modifier):
        print("You find a chest")
        chestlootable()
    lootable(0.3,"Empty Bottle",0)
    lootable(0.1,"Food",5)
    lootable(0.1,"Water",5)
    lootable(0.5,"Stone",0)
    lootable(0.05,"Wood",0)
    lootable(0.5,"Stick",3)
    lootable(0.7,"Leaf",5)
    lootable(0.7,"Grass",5)
    lootable(0.05,"Fur",0)
    lootable(0.05,"Hide",0)
    lootable(0.1,"Raw Food",2)
    lootable(0.5,"Flower",4)
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
redraworld()
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
    print("+"*(width+2))
    for b in range(height):
        print("+",end="")
        for a in range(width):
            if(a==x and b==y):
                print("@",end="")
            else:
                if(finditem("curse of insanity") != -1 and random.random()<0.01*inventory[finditem("curse of insanity")][1]*modifier):
                    print(str(chr(round(random.random()*93)+33)),end="")
                else:
                    print(world[a][b],end="")
        print("+",end="")
        print()
    print("+"*(width+2))
draworld()
def identify (item):
    if(finditem("curse of blindness") != -1 and inventory[finditem("curse of blindness")][1] >= 1):
        return("something")
    if(finditem("curse of insanity") != -1 and random.random()<0.1*inventory[finditem("curse of insanity")][1]*modifier):
        locations = ["a small tree","a large tree","a marsh with knee level water","swimmably deep water","the kracken","an empty area","a small smelter","a campfire","firepit","rock","a treasure room","an impassible wall","a wierd mysterious area","unknown","a pickle","an apple","an orange","a bannana","a bannana tree","an orchard","a forrest","a library","a lemonade stand","a man with a rifle","a fifty foot monster","the devil","a tornado","a parking lot","a trash can","an elevator","a button","a tee-shirt","a very long book","a crater","the moon","the sun","Jupiter","the Kepler space telescope","some debris","a zoo","a building","your childhood home","a church","a temple","a monument","a statue"]
        return(locations[int(round(random.random()*(len(locations)-1)))]) 
    else:
        if(item=="t"):
            return("a small tree")
        elif(item=="T"):
            return("a large tree")
        elif(item=="~"):
            return("a marsh with knee level water")
        elif(item=="w"):
            return("swimmably deep water")
        elif(item==" "):
            return("an empty area")
        elif(item=="X"):
            return("a camp fire")
        elif(item=="x"):
            return("a firepit")
        elif(item=="A"):
            return("a rock")
        elif(item=="+"):
            return("an impassible wall")
        elif(item=="?"):
            return("a wierd mysterious area")
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
    if(a=="LOOK"):
        if((finditem("curse of blindness")==-1 or inventory[finditem("curse of blindness")][1] <= 0)):
            draworld()
        else:
            print("You are blind...")
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
                       print("You see only a neverending abiss")
               elif(b=="E"):
                   print("You look to the east")
                   if(x+1<height):
                       print("Directly east of you is "+identify(world[x+1][y]))
                   else:
                       print("You see only a neverending abiss")
               elif(b=="S"):
                   print("You look to the south")
                   if(y+1<width):
                       print("Directly south of you is "+identify(world[x][y+1]))
                   else:
                       print("You see only a neverending abiss")
               elif(b=="W"):
                   print("You look to the west")
                   if(x-1>=0):
                       print("Directly west of you is "+identify(world[x-1][y]))
                   else:
                       print("You see only a neverending abiss")
               else:
                   print("That isn't a direction")
               print("")
        else:
            print("You are blind...")
    elif(a=="MOVE"):
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
                   print("You would like to move to the north, but you are stopped by an endless abiss")
           elif(b=="E"):
               if(x+1<height):
                   if(world[x+1][y]!="+"):
                       print("You travel to the east")
                       x=x+1
                   else:
                       blocked(x+1,y)
               else:
                   print("You would like to move to the east, but you are stopped by an endless abiss")
           elif(b=="S"):
               if(y+1<width):
                   if(world[x][y+1]!="+"):
                       print("You travel to the south")
                       y=y+1
                   else:
                       blocked(x,y+1)
               else:
                   print("You would like to move to the south, but you are stopped by an endless abiss")
           elif(b=="W"):
               if(x-1>=0):
                   if(world[x-1][y]!="+"):
                       print("You travel to the west")
                       x=x-1
                   else:
                       blocked(x-1,y)
               else:
                   print("You would like to move to the west, but you are stopped by an endless abiss")
           else:
               greatjob()
               ##this code should never run in normal operations
           passtime(1)
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
            print("This command draws a map of the region, w's and ~ represent water and t's represent trees.")
        elif(b=="OBSERVE"):
            print("This command tells you about your current tile in the same documentation as look to")    
        elif(b=="INVENTORY"):
            print("This command shows you your inventory. As an exmaple it will say Hands x2, showing that you have 2 hands")
        elif(b=="USE"):
            print("This command lets you use an item that you have. Some items only work on specific tiles.")
        elif(b=="WAIT"):
            print("This command simply passes the time. You will consume food, water, infections will spread, and random events may occur")
        elif(b=="Hunt"):
            print("This sends you into combat with a random creature, allowing you to gain raw meat")
        else:
            print("That is not a valid command. Say 'ask a command' in the main prompt to get a list of commands")
    elif(a=="INVENTORY"):
       getinventory()
    elif(a=="HUNT"):
       if(world[x][y]=="T"):
           print("You wait an hour for a creature to come by...")
           passtime(1);
           if(random.random()>0.05*modifier):
               entercombat("@Nature",0)
           else:
               print("nothing comes")
       elif(world[x][y]=="t"):
           print("You wait an hour for a creature to come by...")
           passtime(1);
           if(random.random()>0.10*modifier):
               entercombat("@Nature",0)
           else:
               print("nothing comes")
       elif(world[x][y]=="?"):
           entercombat("@Fantacy",0)
       elif(world[x][y]==" "):
           print("You wait an hour for a creature to come by...")
           passtime(1);
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
           print("You are blind...")
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
                   exec(command)
       else:
           exec(command)
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
       valid = 1;
       if(hourtowait!="nvm"):
           for i in range(len(hourtowait)):
               if(hourtowait[i] != "1" and hourtowait[i] != "2" and hourtowait[i] != "3" and hourtowait[i] != "4" and hourtowait[i] != "5" and hourtowait[i] != "6" and hourtowait[i] != "7" and hourtowait[i] != "8" and hourtowait[i] != "9" and hourtowait[i] != "0"):
                   valid = 0
       if(valid == 0):
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
       masscraft(Item1,Item2)
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
               odds=random.random()
               if((useitem=="HANDS" and odds<0.1) or (useitem=="BASICGLOVES" and odds<0.2) or (useitem=="CLOTHGLOVES" and odds<0.3) or (useitem=="HIDEGLOVES" and odds<0.4) or (useitem=="LEATHERGLOVES" and odds<0.5) or (useitem=="CHAINGLOVES" and odds<0.6) or (useitem=="IRONGLOVES" and odds<0.1)):
                   defaultlootable()
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   if(odds<0.7):
                       defaultlootable()
               if(world[x][y]=="?" or world[x][y]=="?"):
                   lootable(0.1,"Dark Shard",0)
                   if(random.random()>0.5):
                       entercombat("@Fantacy",0)
               if(world[x][y]=="~" or world[x][y]=="w"):
                   lootable(0.7,"Water",10)
               if(world[x][y]=="x"):
                       world[x][y]=" "
                       lootable(0.9,"Firepit",0)
               if(world[x][y]=="X"):
                       world[x][y]=" "
                       lootable(0.9,"Campfire",0)
               if(world[x][y]=="A"):
                   defaultlootable()
                   lootable(0.01,"Ore",1)
                   odds=random.random()
                   if(odds<0.01):
                       chestlootable()
           elif(useitem=="CANCER"):
              cancercheck();
           elif(useitem=="MAKESHIFTAXE"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   if(odds<0.1):
                       inventory[finditem("MAKESHIFTAXE")][1]-=1
                       print("It breaks")
                   lootable(1,"Wood",10)
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                   if(world[x][y]=="T"):
                       lootable(1,"Wood",5)
                       world[x][y]="t"
           elif(useitem=="IRONAXE"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   if(odds<0.01):
                       inventory[finditem("IRONAXE")][1]-=1
                       print("It breaks")
                   lootable(1,"Wood",20)
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                   if(world[x][y]=="T"):
                       lootable(1,"Wood",10)
                       world[x][y]="t"
           elif(useitem=="EMPTYBOTTLE"):
               if(world[x][y]=="~" or world[x][y]=="w"):
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
               print("The mysterious note did say 'Blood to fire'...")
               print("Do you cut your arm?")
               cut=input()
               if(variableify(cut)[0]=="Y"):
                  print("You cut your arm")
                  addstuff("Open Wound",1)
                  print("Some blood drips onto the campfire")
                  endgame()
               else:
                 print("You change your mind, probally a good idea")

           elif(useitem=="TORCH"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   inventory[finditem("TORCH")][1]-=1
                   print("You torch the tree, Why?")
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                   if(world[x][y]=="T"):
                       world[x][y]="t"
                   lootable(1,"Ash",50)
           elif(useitem=="BLOODSYRINGE"):
               inventory[finditem("BLOODSYRINGE")][1]-=1
               print("The blood syringe makes you recover blood")
               inventory[finditem("Blood")][1] += 50/modifier
           elif(useitem=="DISINFECTANT"):
               if(finditem("INFECTION") != -1):
                   inventory[finditem("DISINFECTANT")][1]-=1
                   print("The disinfectant hurts your infection")
                   inventory[finditem("INFECTION")][1] -= round((random.random()*250)/modifier)
                   if(inventory[finditem("INFECTION")][1] < 0):
                       inventory[finditem("INFECTION")][1] = 0
           elif(useitem=="TORCH"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   inventory[finditem("TORCH")][1]-=1
                   print("You torch the tree, Why?")
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                   if(world[x][y]=="T"):
                       world[x][y]="t"
                   lootable(1,"Ash",50)
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
                           print("You suddenly hear a rush of air...")
                           if(prayer=="Devil! give me rain"):
                               print("Suddenly it starts to rain, you gulp it up")
                               addstuff("Water",int(round((random.random()*100*favor)/modifier)))
                               for xx in range(height):
                                   for yy in range(width):
                                       if(random.random()*favor>0.9*modifier):
                                           if(world[xx][yy]=="~"):
                                               world[xx][yy]="w"
                                           if(world[xx][yy]==" "):
                                               world[xx][yy]="~"
                           if(prayer=="Devil! give me xp!"):
                              print("Suddenly, you are filled with power!")
                              addstuff("XP",int(round((random.random()*100*favor)/modifier)))
                           if(prayer=="Devil! give me items"):
                               print("Suddenly around you you see boxes!")
                               addstuff("Loot Kit",int(round((random.random()*10*favor)/modifier)))
                           if(prayer=="Devil! give me survival"):
                               addstuff("Dark Amulet",1)
                               print("You hear a voice speak to you")
                               print("This shall allow you to avoid my wraith once")
                               print("You get a Dark Amulet")
                           if(prayer=="Devil! give me food"):
                               print("Forests perfect for hunting suddenly grow, Food appears out of knowhere")
                               addstuff("Food",int(round((random.random()*100*favor)/modifier)))
                               for xx in range(height):
                                   for yy in range(width):
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
               lootable(0.9)
           elif(useitem=="HERB"):
               addstuff("Herb",-1)
               print("You apply herbal treatments...")
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
               if(inventory[finditem("Blood")][1]<=90):
                   lootable(0.5,"Blood",5)
           elif(useitem=="HEALINGSCROLL"):
               addstuff("Healing Scroll",-1)
               print("You speak the words on the scroll")
               if(finditem("Open Wound")!=-1 and inventory[finditem("Open Wound")][1]>=1):
                   if(modifier > 10):
                     inventory[finditem("Open Wound")][1]-=5
                   else:
                     inventory[finditem("Open Wound")][1]-=15-modifier
                   if(inventory[finditem("Open Wound")][1] < 0):
                     inventory[finditem("Open Wound")][1] = 0
                   print("You feel some wounds close")
               if(finditem("Venom")!=-1 and inventory[finditem("Venom")][1]>=1):
                   if(modifier > 10):
                     inventory[finditem("Venom")][1]-=5
                   else:
                     inventory[finditem("Venom")][1]-=15-modifier
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
                     inventory[finditem("Venom")][1]-=15-modifier
                   if(inventory[finditem("Venom")][1] < 0):
                     inventory[finditem("Venom")][1] = 0
                   print("You feel the radiation leave your body")
               if(finditem("Cancer")!=-1 and inventory[finditem("Cancer")][1]>=1):
                   if(modifier > 10):
                     inventory[finditem("Cancer")][1]-=5
                   else:
                     inventory[finditem("Cancer")][1]-=15-modifier
                   if(inventory[finditem("Cancer")][1] < 0):
                     inventory[finditem("Cancer")][1] = 0
                   print("You feel the radiation leave your body")
               lootable(1,"Blood",50)
               if(inventory[finditem("Blood")][1]>=100):
                 inventory[finditem("Blood")][1] = 100
           elif(useitem=="RADIATIONTREATMENT"):
             if(finditem("Radiation")!=-1 and inventory[finditem("Radiation")][1]>=1):
                   addstuff("Radiation Treatment",-1)
                   print("You apply the radiation treatment")
                   print("You stab the treatment into your body")
                   addstuff("Open Wound",1)
                   print("It takes a tole on your body, but it fights the radiation")
                   addstuff("Water",-modifier)
                   addstuff("Food",-modifier)
                   addstuff("Blood",-modifier)
                   if(modifier > 9):
                     inventory[finditem("Radiation")][1]-=1
                   else:
                     inventory[finditem("Radiation")][1]-=10-modifier
                   if(inventory[finditem("Radiation")][1] < 0):
                     inventory[finditem("Radiation")][1] = 0
                     print("You no longer feel irradiated")
           elif(useitem=="CANCERTREATMENT"):
                   addstuff("Cancer Treatment",-1)
                   print("You apply the Cancer treatment")
                   print("You stab the treatment into your body")
                   addstuff("Open Wound",1)
                   print("It takes a tole on your body, but it fights the Cancer")
                   addstuff("Water",-modifier)
                   addstuff("Food",-modifier)
                   addstuff("Blood",-modifier)
                   if(modifier >= 10):
                     inventory[finditem("Cancer")][1]-=1
                   else:
                     inventory[finditem("Cancer")][1]-=10-modifier
                   if(inventory[finditem("Cancer")][1] < 0):
                     inventory[finditem("Cancer")][1] = 0
           elif(useitem=="DARKSHARD"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   print("The Shard Consumes the tree, You feel as if that was not a good idea, The shard duplicates itself")
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                       lootable(1,"Dark Shard",0)
                   if(world[x][y]=="T"):
                       world[x][y]="t"
                       lootable(1,"Dark Shard",0)
                       lootable(1,"Dark Shard",0)
                       lootable(1,"Dark Shard",0)
           elif(useitem=="XP"):
             if(world[x][y]=="|"):
               print("You place your hands on the giant monolith in front of you")
               print("Boons: ")
               print("1) 20xp Hunger Boon. Food perminently decreses at lesser rate")
               print("2) 20xp Thirst Boon. Water perminently decreses at a lesser rate")
               print("3) 20xp Looting Boon. Items are sligtly easier to find")
               print("4) 15xp Arrow Boon. Arrows have a small chance to do double damage")
               print("5) 15xp Sword Boon. Swords have a small chance to do double damage")
               print("6) 15xp Axe Boon. Axes have a small chance to do double damage")
               print("7) 20xp Fire Boon. Fire has a higher chance to spread")
               print("8) 20xp Crafting Boon. There is a lower chance to fail crafting recipies")
               print("9) 15xp Flail Boon. Flails have a higher possible damage")
               print("10) 15xp Ammo Boon. Ammunition has a small change to not be consumed on use")
               print("11) 20xp Healing Boon. Healing items are sligtly more powerfull.")
               print("12) 20xp Dodge Boon. There is a small chance to dodge a wounding.")
               print("13) 25xp Unbreaking Boon. Items do not break as easily")
               print("14) 15xp New Map. Simply regens the map. Unlike the map item, it does not effect dificulty")
               print("15) 50xp Difficulty Decrease. The game gets marginally easier")
               print("16) 25xp Difficulty Increase. The game gets marginally harder")
               print("17) 10xp Loot kits. You get a loot kit. Thats all")
               print("18) 10xp Coins. You get 50 Coins. Thats all")
               print("19) 15xp Cure cancer. When bought, cancer is removed. No fuss, just gone")
               print("20) 15xp Cure radiation. When bought, radiation is removed. No fuss, just gone")
               print("21) 15xp Cure infections. When bought, infections are removed. No fuss, just gone")
               print("22) 15xp Cure wounds. When bought, all wounds are removed. No fuss, just gone")
               print("23) 20xp Curse Removal. When bought, one curse is removed. No fuss, just gone")
               print("24) 20xp Blood Boon. Blood regens faster")
               print("25) 20xp Coward Boon. Easier chance to flee")
           elif(useitem=="MONOLITH"):
              if(world[x][y]==" " or world[x][y]=="?"):
                world[x][y] = "|"
                addstuff("Monolith",-1)
                print("You place the monolith... It stands tall and forboding, covered in markings")
              else:
                print("Monoliths can only be placed on empty ground or on wierd areas")
           elif(useitem=="TICTACTOEBOARD"):
               gameman(0)
           elif(useitem=="COIN"):
               gameman(1)
           elif(useitem=="ANTICURSESCROLL"):
               cursed = True;
               if(finditem("curse of insanity")!=-1 and inventory[finditem("curse of insanity")][1]>=1):
                   addstuff("curse of insanity",-1)
                   cursed = False;
               if(finditem("curse of blindness")!=-1 and inventory[finditem("curse of blindness")][1]>=1):
                   addstuff("curse of blindness",-1)
                   cursed = False;
               if(finditem("curse of slowness")!=-1 and inventory[finditem("curse of slowness")][1]>=1):
                   addstuff("curse of slowness",-1)
                   cursed = False;
               if(finditem("curse of curses")!=-1 and inventory[finditem("curse of curses")][1]>=1):
                   addstuff("curse of curses",-1)
                   cursed = False;
               if(finditem("curse of hunger")!=-1 and inventory[finditem("curse of hunger")][1]>=1):
                   addstuff("curse of hunger",-1)
                   cursed = False;
               if(finditem("curse of thirst")!=-1 and inventory[finditem("curse of thirst")][1]>=1):
                   addstuff("curse of thirst",-1)
                   cursed = False;
               if(finditem("curse of haunting")!=-1 and inventory[finditem("curse of haunting")][1]>=1):
                   addstuff("curse of haunting",-1)
                   cursed = False;
               if(not(cursed)):
                   print("You are cured of curses...")
                   addstuff("Anticurse Scroll",-1)
               else:
                   print("The scroll does nothing...")
           elif(useitem=="MATCH"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   inventory[finditem("MATCH")][1]-=1
                   print("You torch the tree, Why?")
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                   if(world[x][y]=="T"):
                       world[x][y]="t"
                   lootable(1,"Ash",30)
           elif(useitem=="TRAP"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   if(odds<0.5):
                       inventory[finditem("Trap")][1]-=1
                   else:
                       lootable(0.9,"Raw Food",15)
           elif(useitem=="FISHINGROD"):
               if(world[x][y]=="~" or world[x][y]=="w"):
                   GoFish()
           elif(useitem=="BONE"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   if(odds<0.01):
                       inventory[finditem("Bone")][1]-=1
                   lootable(0.5,"Raw Food",3)
           elif(useitem=="STICK"):
               if(world[x][y]=="t" or world[x][y]=="T"):
                   odds=random.random()
                   if(odds<0.7):
                       inventory[finditem("Stick")][1]-=1
           elif(useitem=="FLOWERHEADWEAR"):
                print("You stare at the pretty flower headress, It makes you feel better")
                if(finditem("curse of insanity") and inventory[finditem("curse of insanity")][1]>=1):
                    addstuff("curse of insanity",-1)
                    print("A small part of you sanity returns to you")
           elif(useitem=="FLOWER"):
                print("You stare at the pretty flower, ",end="")
                if(finditem("curse of insanity")!=-1 and inventory[finditem("curse of insanity")][1]>=1):
                    if(random.random()<=0.1*inventory[finditem("curse of insanity")][1]*modifier):
                        addstuff("curse of insanity",1)
                        print("The flower makes you grow even more insane")
                    else:
                        print("A small portion of your sanity comes back to you")
                        addstuff("curse of insanity",-1)
                print()
           elif(useitem=="BASKET"):
               if(world[x][y]== "t" or world[x][y] == "T" or world[x][y] == " "):
                   print("you forage for an hour")
                   odds=random.random()
                   if(odds<0.005*modifier):
                       print("it breaks")
                       inventory[finditem("Basket")][1]-=1
                   if(odds>0.99):
                       defaultlootable()
                   if(odds>0.95):
                       defaultlootable()
                   if(odds>0.90):
                       defaultlootable()
                   if(odds>0.50):
                       defaultlootable()
                   if(world[x][y]=="t"):
                       defaultlootable()
                   if(world[x][y]=="T"):
                       defaultlootable()
                       defaultlootable()
                   defaultlootable()
               elif(world[x][y] == "A"):
                   lootable(0.05,"Ore",5)
                   odds=random.random()
                   if(odds<0.01):
                       chestlootable()
               elif(world[x][y] == "~" or world[x][y] == "w"):
                   lootable(0.9,"Water",30)
           elif(useitem=="MAKESHIFTBASKET"):
               if(world[x][y]=="t" or world[x][y]=="T" or world[x][y]==" "):
                   print("you forage for an hour")
                   odds=random.random()
                   if(odds<0.01*modifier):
                       print("it breaks")
                       inventory[finditem("Makeshift Basket")][1]-=1
                   if(world[x][y]=="t"):
                       defaultlootable()
                   if(world[x][y]=="T"):
                       defaultlootable()
                       if(odds>0.90):
                           defaultlootable()
                   if(odds>0.80):
                           defaultlootable()
               elif(world[x][y] == "~" or world[x][y] == "w"):
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
                   print("You torch the tree, Why?")
                   if(world[x][y]=="t"):
                       world[x][y]=" "
                   if(world[x][y]=="T"):
                       world[x][y]="t"
                   lootable(1,"Ash",20)
           elif(useitem=="RAWFOOD"):
               if(world[x][y]=="X" or world[x][y]=="H"):
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
                            elif(world[x][y]=="X" or world[x][y]=="H"):
                                if(random.random()<0.05*modifier):
                                    print("You waste the food...")
                                else:
                                    print("You cook food...")
                                    addstuff("Food",1)
                                    if(world[x][y]=="H"):
                                      addstuff("Food",1)
                                inventory[finditem("Raw Food")][1]-=1
                        passtime(1+round(cookcount/10))
               else:
                   print("You look at the raw food... Eww")
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
                       lootable(0.01,"Emerald",0)
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
               addstuff("Coin",round(1/modifier*500*random.random()))
               addstuff("Loot Kit",round(1/modifier*50*random.random()))
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
               if(world[x][y]=="H"):
                       world[x][y]="h"
                       print("You attempt to cook the hide into leather")
                       lootable(0.5,"Leather",3)
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
if(totalhours*modifier > 3100):
  print("You were a god")
elif(totalhours*modifier > 3000):
  print("You were practically a god")
elif(totalhours*modifier > 2900):
  print("You were a demi-god")
elif(totalhours*modifier > 2800):
  print("You were practically a demi-god")
elif(totalhours*modifier > 2700):
  print("How did you live that long?")
elif(totalhours*modifier > 2600):
  print("You were unrealisticly good")
elif(totalhours*modifier > 2500):
  print("You were really impressively good")
elif(totalhours*modifier > 2400):
  print("You were impressively good")
elif(totalhours*modifier > 2300):
  print("You were almost impressively good")
elif(totalhours*modifier > 2200):
  print("You were really,really good")
elif(totalhours*modifier > 2100):
  print("You were really good")
elif(totalhours*modifier > 2000):
  print("You were really quite good")
elif(totalhours*modifier > 1900):
  print("You were quite good")
elif(totalhours*modifier > 1800):
  print("You were good")
elif(totalhours*modifier > 1700):
  print("You were slightly good")
elif(totalhours*modifier > 1600):
  print("You were okay")
elif(totalhours*modifier > 1500):
  print("You were okay, at best")
elif(totalhours*modifier > 1400):
  print("You were meh")
elif(totalhours*modifier > 1300):
  print("You were meh, at best")
elif(totalhours*modifier > 1200):
  print("You did not do good")
elif(totalhours*modifier > 1100):
  print("You really did not do good")
elif(totalhours*modifier > 1000):
  print("You really did not do good, at best")
elif(totalhours*modifier > 900):
  print("You really did not do good, at all")
elif(totalhours*modifier > 800):
  print("you did horribly")
elif(totalhours*modifier > 700):
  print("you did horribly, at best")
elif(totalhours*modifier > 600):
  print("You did very horribly")
elif(totalhours*modifier > 500):
  print("You did very horribly, at best")
elif(totalhours*modifier > 400):
  print("You did very, impressibly, horribly.")
elif(totalhours*modifier > 300):
  print("You did very, impressibly, horribly, at best")
elif(totalhours*modifier > 200):
  print("You were word-record breakingly horrible!")
elif(totalhours*modifier > 100):
  print("You were word-record breakingly horrible, at best!")
else:
  print("How did you even die that fast?")
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
