easy = [[7,9,[],[],[],[],3,[],[]],
        [[],[],[],[],[],6,9,[],[]],
        [8,[],[],[],3,[],[],7,6],
        [[],[],[],[],[],5,[],[],2],
        [[],[],5,4,1,8,7,[],[]],
        [4,[],[],7,[],[],[],[],[]],
        [6,1,[],[],9,[],[],[],8],
        [[],[],2,3,[],[],[],[],[]],
        [[],[],9,[],[],[],[],5,4]]

easysolved = [[7, 9, 6, 8, 5, 4, 3, 2, 1],
 [2, 4, 3, 1, 7, 6, 9, 8, 5],
 [8, 5, 1, 2, 3, 9, 4, 7, 6],
 [1, 3, 7, 9, 6, 5, 8, 4, 2],
 [9, 2, 5, 4, 1, 8, 7, 6, 3],
 [4, 6, 8, 7, 2, 3, 5, 1, 9],
 [6, 1, 4, 5, 9, 7, 2, 3, 8],
 [5, 8, 2, 3, 4, 1, 6, 9, 7],
 [3, 7, 9, 6, 8, 2, 1, 5, 4]]

easytest = [[7, 9, 6, 8, 5, [], 3, 2, 1],
 [2, 4, 3, 1, 7, 6, 9, 8, 5],
 [8, 5, 1, 2, 3, 9, 4, 7, 6],
 [1, 3, 7, 9, 6, 5, 8, 4, 2],
 [9, 2, 5, 4, 1, 8, 7, 6, 3],
 [4, 6, 8, 7, 2, 3, 5, 1, 9],
 [6, 1, 4, 5, 9, 7, 2, 3, 8],
 [5, 8, 2, 3, 4, 1, 6, 9, 7],
 [3, 7, 9, 6, 8, 2, 1, 5, 4]]

medium = [[[],[],[],[],[],9,[],2,[]],
        [[],5,[],[],3,2,[],[],[]],
         [[],9,3,[],4,5,7,[],8],
        [[],1,7,[],[],[],4,[],2],
        [[],4,[],[],[],[],[],8,[]],
        [8,[],5,[],[],[],9,1,[]],
        [4,[],9,5,8,[],2,7,[]],
        [[],[],[],4,2,[],[],5,[]],
        [[],2,[],9,[],[],[],[],[]]]

mediumsolved = [[1, 8, 4, 7, 6, 9, 3, 2, 5],
 [7, 5, 6, 8, 3, 2, 1, 9, 4],
 [2, 9, 3, 1, 4, 5, 7, 6, 8],
 [9, 1, 7, 6, 5, 8, 4, 3, 2],
 [6, 4, 2, 3, 9, 1, 5, 8, 7],
 [8, 3, 5, 2, 7, 4, 9, 1, 6],
 [4, 6, 9, 5, 8, 3, 2, 7, 1],
 [3, 7, 1, 4, 2, 6, 8, 5, 9],
 [5, 2, 8, 9, 1, 7, 6, 4, 3]]

hard = [[1,[],2,[],4,[],[],[],[]],
        [[],[],8,2,3,6,5,[],[]],
         [[],[],[],[],[],8,[],9,[]],
        [9,[],7,[],[],[],[],5,4],
        [[],[],[],9,6,4,[],[],[]],
        [3,6,[],[],[],[],1,[],9],
        [[],8,[],6,[],[],[],[],[]],
        [[],[],1,3,2,5,9,[],[]],
        [[],[],[],[],8,[],7,[],2]]
hardsolved = [[1, 3, 2, 5, 4, 9, 8, 7, 6],
 [7, 9, 8, 2, 3, 6, 5, 4, 1],
 [5, 4, 6, 1, 7, 8, 2, 9, 3],
 [9, 2, 7, 8, 1, 3, 6, 5, 4],
 [8, 1, 5, 9, 6, 4, 3, 2, 7],
 [3, 6, 4, 7, 5, 2, 1, 8, 9],
 [2, 8, 3, 6, 9, 7, 4, 1, 5],
 [4, 7, 1, 3, 2, 5, 9, 6, 8],
 [6, 5, 9, 4, 8, 1, 7, 3, 2]]

#These are the 2D array gameboards for the different difficulties. 
#Easy will load "Easytest" board which will make it easier to test the scoreboard and winning screen.

def disptime():
    global speedup,timefill,startime,mins,dispm,disps
    """If the wrong number is pressed, the timer will speedup by 5 secs and speedup is the variable that controls it.
    Timefill is the color of the time text, which is black and turns red then back to black when the time is speeded up.
    Starttime is the variable that stores when the game began. subtract 5 seconds to that number whenever speedup is needed.
    mins is how many minutes has passed, dispm is the minutes in string format for displaying (ex. mins = 5, dispm = "05" for formatting)
    disps has the same function as dispm, ex. 5 seconds -> "05" """
    fill(0)
    textAlign(RIGHT)
    if len(str((millis()-startime)/1000)) < 2: #if the current second is a 1 digit number, make the disps the seconds with a 0 in the front
        disps = "0"+ str((millis()-startime)/1000) 
    else:
        disps = str((millis()-startime)/1000) #if current second is 2 digits, simply turn it into a string. 
    if len(str(mins)) <2: #Same for minutes, if minutes is 1 digit number make it "0x" instead of x seconds.
        dispm = "0"+str(mins)
    else:
        dispm = str(mins)
    if speedup == True: #When wrong number is pressed, timefill will gradually turn red
        if timefill < 255:
            timefill +=5
        if timefill == 255:
            speedup = "d" #Once timefill reaches red (255), timefill starts to go back down to black
    elif speedup == "d":
        if timefill > 0:
            timefill -=5
        if timefill == 0:
            speedup =False #Once the time's colour animation has finished, speedup goes back to false
    fill(timefill,0,0)    #Color of the time's text based on timefill
    text(dispm+":"+disps,850,100) 
    fill(255)  
    if (millis()-startime)/1000 >= 60: #If seconds reaches 60, add one to minutes and put current second back to 0. 
        startime = millis()  
        mins +=1 
    textAlign(LEFT)

class Tile: #Tile class, each number tile in the game is an object. 
    def __init__(self,x,y,indexx,indexy,boxx,boxy): 
        """x and y is the x,y, position on the board. indexxindexy is the index of the tile in the 2d board array.
        boxx boxxy is the index of which box it is in on the board (top left: box 0,0  bottom right: box 2,2) """
        self.x,self.y,self.indexx,self.indexy,self.boxx,self.boxy = x,y,indexx,indexy,boxx,boxy
        self.clicked = False 
    def drawtile(self):
        if self.clicked == True: #If the tile is selected it will be grey
            fill(200)
        if self.clicked == False:
            fill(255)
        rect(self.x,self.y,60,60)
        fill(0)
        if type(board[self.indexy][self.indexx]) != list: #Displays what number the tile should be based on the current board.
            textSize(25)
            text(board[self.indexy][self.indexx],self.x+22,self.y+40)
        if type(board[self.indexy][self.indexx]) == list: #If the tile is a list, it means there are notes in it and display the notes accordingly.
            textSize(15) #smaller text for notes
            for n in board[self.indexy][self.indexx]:
                if 1 <= n <= 3:
                    text(n,self.x+(n*18)-10,self.y+15)
                if 4 <= n <= 6:
                    text(n,self.x+((n-3)*18)-10,self.y+35)
                if 7<= n <= 9:
                    text(n,self.x+((n-6)*18)-10,self.y+55)
            textSize(25)
        fill(255)
tiles = [] #list that stores all the tile objects

def selection():  #selection sort function for sorting the scoreboard
    global scoreboard
    for x in range(5): #only need to get the top 5 scores
        max= 0
        for n in range(len(scoreboard)-x):
            if scoreboard[n] > max:
                max = scoreboard[n]
                maxi = n
        org = scoreboard[len(scoreboard)-1-x]
        scoreboard[len(scoreboard)-1-x] = max
        scoreboard[maxi] = org

for y in range(9): #Creates the 2d array of tile objects with all the appropriate variables
    row = []
    for x in range(9):
        row.append(Tile(100+(y*60),50+(x*60),x,y,(x/3)+1,(y/3)+1))
    tiles.append(row)

def checkdone(): #Checks if there are any remaining empty tiles in the list. 
    global done,board
    done = True
    for n in board:
        for x in n:
            if type(x) == list:
                done = False
    return done #This will return False if there are any unfilled tiles in the board
 
def setup():
    global mins,current,clicks,mode,pencil,note,eraser,speedup,timefill,gamestate,selecte,selectm,selecth,name, scoreboard,score
    size(1000,750)
    mins = 0 #Starting up all the variables
    speedup = False
    current = []
    clicks = 0 
    mode = "w" # mode w = writing mode, mode n = note mode, mode e = erasing mode for notes 
    pencil = loadImage("pencil.jpg")  #Loading the pencil, notepad, eraser images
    note = loadImage("note.jpg")    
    eraser = loadImage("eraser.png")
    timefill = 0
    gamestate = "title"
    selecte,selectm,selecth = 255,255,255
    name = ""
    scoreboard = []
    score = open("score.txt") #Open the score file 
    scores = score.readlines()
    for n in range(len(scores)): #Put them all into a scoreboard array for this game 
        scoreboard.append([int(scores[n].split()[0]), str(scores[n].split()[1]), str(scores[n].split()[-1])])
    selection() #Sort the imported scoreboard list 

def reset():
    global mins,current,clicks,mode,speedup,timefill,gamestate,selecte,selectm,selecth,name
    #Reset function, basically has the same variables and assignments as setup. 
    mins = 0
    speedup = False
    current = []
    clicks = 0 
    mode = "w"
    timefill = 0
    gamestate = "title"
    selecte,selectm,selecth = 255,255,255
    name = ""    
    for n in tiles: #Unclicks all of the tiles. 
        for x in n:
            x.clicked = False
    
    
def draw():
    global gamestate,board,pencil,note,eraser,selecte,selectm,selecth,done,wintime,dispm,disps,name,time
    background(255)
    if gamestate == "title":
        textSize(60) #Title screen
        textAlign(CENTER)
        fill(0)
        text("Sudoku",500,140)
        textSize(50)
        text("Select a difficulty",500,250)
        fill(selecte)
        rect(100,350,250,150)
        fill(selectm)
        rect(400,350,250,150)
        fill(selecth)
        rect(700,350,250,150)
        fill(0)
        text("Easy",225,430)
        text("Medium",525,430)
        text("Hard",825,430)
        
    if gamestate == "play": #Playmode
        if mode == "w": #Highlights the pencil, notepad, or eraser according to the current mode
            rect(762,147,106,106)
        if mode == "n":
            rect(762,267,106,106)
        if mode == "e":
            rect(762,397,106,106)
        image(pencil,765,150,100,100) #Displays the pencil,notepad,eraser images
        image(note,765,270,100,100)
        image(eraser,765,400,100,100)
        for n in tiles:
            for x in n:
                x.drawtile()
        for y in range(3): #This creates borders around the 9 3x3 boxes on the board 
            for x in range(3):
                noFill()
                strokeWeight(3)
                rect(100+(x*180),50+(y*180),180,180)
                strokeWeight(1)
                fill(255)
        for n in range(1,10): #This is what displays the 9 numbers on the bottom of the board
            rect((n*90)-20,630,75,75)
            fill(0)
            text(n,(n*90)+10,677)
            fill(255)
        disptime() #Displays current time
        textAlign(LEFT)
        if checkdone() == True: #If the checkdone()function returns True
            gamestate = "win" #The gamestate becomes win and the time the player has one is stored
            time = (int(dispm)*60)+int(disps) #This is the winning time in seconds
            wintime = dispm+":"+disps #This is how the time will be displayed in minutes:seconds string form
        noFill()
        rect(745,530,300,70) #This is the reset button
        fill(0)
        text("Return to title",760,570)
        fill(255)
    
    if gamestate == "win": #Winning screen
        fill(0)
        textSize(50) 
        text("Congratulations~!",275,115)
        text("Your time: "+wintime,290,220)
        text("Enter your name:",100,330)
        text(name,520,330) #This name variable is changed from keyTyped(), will display the user input
        text("Press enter when done",200,500)
    if gamestate == "scoreboard": 
        fill(0)
        textSize(50)
        text("Scoreboard",350,100) #Displays the scoreboard
        for n in range(5): #Goes through the top 5 scores in the sorted scoreboard list and displays it
            text(str(n+1)+".  "+scoreboard[n][-1],200,200+(n*75))
            text(scoreboard[n][1],600,200+(n*75))   
        
            
        
def mouseMoved():
    global gamestate,selecte,selectm,selecth
    if gamestate == "title": #This will highlight the easy, medium, hard buttons on the startup screen 
        if 350 <= mouseY <= 500:
            if 100 <= mouseX <= 350:
                selecte = 200
            elif 100 > mouseX or mouseX > 350:
                selecte = 255 
            if 400 <= mouseX <= 650:
                selectm = 200
            elif 400 > mouseX or mouseX > 650:
                selectm = 255
            if 700 <= mouseX <= 950:
                selecth = 200
            elif 700 > mouseX or mouseX > 950:
                selecth = 255
        else:
            selecte,selectm,selecth = 255,255,255
def mouseClicked():
    global clicks,current,startime,mode,speedup,done,gamestate,startime,selecte,selectm,selecth,board,solved
    if mouseButton == LEFT:
        if gamestate == "play":
            if 765 <= mouseX <= 865 and 150 <= mouseY <= 250: #This checks if the gamemode has been changed, if the mouse clicked on one of the 3 images
                mode = "w"
            if 765 <= mouseX <= 865 and 270 <= mouseY <= 370:
                mode = "n"
            if 765 <= mouseX <= 865 and 400 <= mouseY <= 500:
                mode = "e"
            if 630 <= mouseY <= 705 and 70 <= mouseX <= 865 and current != []: #This is for when you select numbers 1-9 at the bottom of the game 
                if mode == "w":
                    if solved[current[0]][current[1]] == (mouseX+20)/90 : #If the number the player chose the correct number
                        board[current[0]][current[1]] = (mouseX+20)/90 #Put the entered number into the current board
                        tiles[current[0]][current[1]].clicked = False 
                        clicks = 0 #clicks variable keeps track of how many tiles are selected at the moment, at most 1. 
                        current = []
                        checkdone() #Every time a number is entered check if the game is finished
                    elif solved[current[0]][current[1]] != (mouseX+20)/90: #If the player chooses the wrong number
                        startime -= 5000 #Add 5 seconds to the timer and start the speedup color change animation
                        speedup = True
                if mode == "n": 
                    if type(board[current[0]][current[1]]) == list: #When in note mode the clicked numbers will be stored in a list and displayed with smaller text
                        board[current[0]][current[1]].append((mouseX+20)/90)
                if mode == "e": 
                    if type(board[current[0]][current[1]]) == list and (mouseX+20)/90 in board[current[0]][current[1]]:
                        board[current[0]][current[1]].remove((mouseX+20)/90) #This erases a chosen number note the player has made already 
                
            elif 50 <= mouseY <= 570 and 100 <= mouseX <= 650: #This is for when you click on the game board
                    if type(board[((mouseX-50)/60)-1][((mouseY-100)/60)+1]) == list: #This makes sure you click on an empty tile, as filled tiles can't be changed
                        if tiles[((mouseX-50)/60)-1][((mouseY-100)/60)+1].clicked == False: #Make sure the tile isn't selected already
                            if current != [] and clicks == 1: #If there is already a selected tile,
                                tiles[current[0]][current[1]].clicked = False  #You have to unselect the previous tile
                                current = [((mouseX-50)/60)-1,((mouseY-100)/60)+1] #And store the current selected tile 
                                tiles[current[0]][current[1]].clicked = True #And make that tile.clicked equal true
                            else: #if there is no tile currently selected
                                tiles[((mouseX-50)/60)-1][((mouseY-100)/60)+1].clicked = True #No need to unselect anything and store the clicked tile position in current
                                clicks = 1 
                                current = [((mouseX-50)/60)-1,((mouseY-100)/60)+1]
                
                        elif tiles[((mouseX-50)/60)-1][((mouseY-100)/60)+1].clicked == True: #If you click on a tile that's already selected
                            tiles[((mouseX-50)/60)-1][((mouseY-100)/60)+1].clicked = False #Unclick that tile 
                            clicks = 0
                            current = []
            elif 745 <= mouseX <= 1045 and 530 <= mouseY <= 600: #If you press the reset button, call the reset function and reset the game 
                reset()
        if gamestate == "title": #For the title screen
            if selecte == 200: #Check the color of each button, if the button is highlighted while it's clicked it means that difficulty has been selected 
                textAlign(LEFT)
                board = easytest #Change this to easy for the real easy board, easytest for testing purposes
                solved = easysolved 
                gamestate = "play" 
                startime = millis() #Initialize the start time 
            elif selectm == 200:
                textAlign(LEFT)
                board = medium 
                solved = mediumsolved
                gamestate = "play"
                startime = millis()
            elif selecth == 200:
                textAlign(LEFT)
                board = hard
                solved = hardsolved
                startime = millis()
                gamestate = "play"
        if gamestate == "scoreboard": #If you click the screen on the scoreboard it goes back to the title screen 
            reset()


def keyTyped():
    global name,gamestate #This is for inputting the users name on the winning screen 
    if key in "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVMVNB!@#$%^&*()?" and len(name) < 10 and gamestate == "win":
        name += key 

def keyPressed():
    global gamestate,scoreboard,name,wintime,time,score
    if key == ENTER and gamestate == "win": #This checks if the user has finished typing their name, aka pressing en ter
        gamestate = "scoreboard"
        scoreboard.append([time,wintime,name]) #Add this users score and name into scoreboard and sort
        selection()
        scoreboard.remove(scoreboard[-1]) 
        f = open('score.txt', 'a+') # Open the scores text file and write this users name into it 
        ad = str(time)+" "+str(wintime)+" "+str(name)+"\n"
        f.write(ad)
        f.close() #Remember to close the file

        
