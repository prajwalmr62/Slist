#text Game
#by Prajwal
#it is a text game in which user enters the directions and program will analyse
#that and moves the user in the grid.If treasures are found +50 or for neg, it
#is -20.Game will end when the user collects all the treasures.
#points will be displayed.
import random #for random functions
class User:#define user properties
    def __init__(self,name):
        User.name=name
        User.points=0
        User.flags=0
    def addpoint(self,value,sign):
        if(sign=="+"):
            User.points+=value
        else:
            User.points-=value
    def addflag():
        User.flags+=1
    def curbox(self,row,col):
        User.currow=row
        User.curcol=col

class Box:                              #define Box properties
    def __init__(self,row,column):
        Box.row=row
        Box.col=column
    def addpoints(self,value):
        Box.points=value
    def addflag(self,value):
        Box.flag=value
    def addvisit(self,value):
        Box.visit=value
    def flag():
        return(Box.flag)
    def points():
        return(Box.points)
    def visit():
        return(Box.visit)

class Uinput:                   #define input properties
    def __init__(self,dire):
        Uinput.dire=dire
        print "current:",user.currow,user.curcol
        Uinput.nexrow=user.currow
        Uinput.nexcol=user.curcol
        if(dire=="up" or dire=="UP"):
            Uinput.nexrow+=1
        elif(dire=="down" or dire=="DOWN"):
            Uinput.nexrow-=1
        elif(dire=="left" or dire=="LEFT"):
            Uinput.nexcol-=1
        elif(dire=="right" or dire=="RIGHT"):
            Uinput.nexcol+=1
        else :
            print ("invalid move\n")
            #method()
def check(): #check for errors : errors()
    #Tflags=MAX+1
    print "Next:",uinput.nexrow,uinput.nexcol
    if(Tflags>user.flags and uinput.nexrow>=0 and uinput.nexcol>=0):
        if(uinput.nexrow < MAX-1 and uinput.nexcol < MAX-1 ):
                proceed()
        else :
            print ("Invalid move\n")
    elif (Tflags==user.flags):
        print ("You've completed the game!")
        print (user.points)
    else :
        print ("invalid move\n")
        #method()

def proceed(): #proceed and also to add points
    if(grid[uinput.nexrow][uinput.nexcol].flag==1):
        print ("you got a treasure in row",uinput.nexrow,"column",uinput.nexcol)
        user.addpoint(50,"+")
        user.addflag()
        grid[uinput.nexrow][uinput.nexcol].addflag(0)
        print ("your total points =",user.points)
        user.curcol=uinput.nexcol
        user.currow=uinput.nexrow
        #method()
    elif (grid[uinput.nexrow][uinput.nexcol].flag==2):
        print ("you lost a treasure in row",uinput.nexrow,"column",uinput.nexcol)
        user.addpoint(20,"-")
        grid[uinput.nexrow][uinput.nexcol].addflag(0)
        print ("your total points =",user.points)
        user.curcol=uinput.nexcol
        user.currow=uinput.nexrow
        #method()
    else :
        print ("you are in row",uinput.nexrow,"column",uinput.nexcol)
        user.curcol=uinput.nexcol
        user.currow=uinput.nexrow
        #method()


#def method(): #main Game
    
name=raw_input("Enter your name")
MAX=input("enter max size of grid\n")
user=User(name) #Create user with their name
user.currow=random.randrange(0,MAX,1) #to get random row
user.curcol=random.randrange(0,MAX,1) #to get random col
print user.curcol,user.currow
Tflags=MAX+1
Tpoints=MAX*50
grid=list()
lis=list()
for j in range (0,MAX-1,1):
    for i in range (0,(MAX-1),1): #Grid init
        lis.append(Box(i,j))
        lis[i].visit=1
    grid.append(lis)
#get random points init
num=Tflags+1
while (num <= Tflags+1 and num>0):
    ranrow=random.randrange(0,MAX-1,1)
    rancol=random.randrange(0,MAX-1,1)
    grid[ranrow][rancol].addflag(1)
    grid[ranrow][rancol].addpoints(50)
    print ranrow,rancol,"tres+50"
    num-=1
# -ve points init
num=Tflags-1
while (num>0 and num <= Tflags-1):
    
    ranrow=random.randrange(0,MAX-1,1)
    rancol=random.randrange(0,MAX-1,1)
    grid[ranrow][rancol].addflag(2)
    grid[ranrow][rancol].addpoints(20)
    print ranrow,rancol,"tres-20"
    num-=1
 #calling actual game
while (Tflags>user.flags):
    get=raw_input("enter direction\n")
    uinput=Uinput(get)
    check()
