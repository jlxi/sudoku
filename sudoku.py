easy = [[7,9,[],[],[],[],3,[],[]],
        [[],[],[],[],[],6,9,[],[]],
        [8,[],[],[],3,[],[],7,6],
        [[],[],[],[],[],5,[],[],2],
        [[],[],5,4,1,8,7,[],[]],
        [4,[],[],7,[],[],[],[],[]],
        [6,1,[],[],9,[],[],[],8],
        [[],[],2,3,[],[],[],[],[]],
        [[],[],9,[],[],[],[],5,4]]

medium = [[[],[],[],[],[],9,[],2,[]],
        [[],5,[],[],3,2,[],[],[]],
         [[],9,3,[],4,5,7,[],8],
        [[],1,7,[],[],[],4,[],2],
        [[],4,[],[],[],[],[],8,[]],
        [8,[],5,[],[],[],9,1,[]],
        [4,[],9,5,8,[],2,7,[]],
        [[],[],[],4,2,[],[],5,[]],
        [[],2,[],9,[],[],[],[],[]]]

hard = [[1,[],2,[],4,[],[],[],[]],
        [[],[],8,2,3,6,5,[],[]],
         [[],[],[],[],[],8,[],9,[]],
        [9,[],7,[],[],[],[],5,4],
        [[],[],[],9,6,4,[],[],[]],
        [3,6,[],[],[],[],1,[],9],
        [[],8,[],6,[],[],[],[],[]],
        [[],[],1,3,2,5,9,[],[]],
        [[],[],[],[],8,[],7,[],2]]

board = hard
def insertposs():
    for n in range(9):
        for y in range(9):
            if board[y][n] == []:
                board[y][n] = [x for x in range(1,10)]

def row(x,y,c):
    if 1<= c <=9:
        if type(board[y][x]) == list:
           if c in board[y] and c in board[y][x]:
               board[y][x].remove(c)
        row(x,y,c+1)

def column(x,y,c):
    if 1<= c <=9:
        for a in range(9):
            if board[a][x] == c and c in board[y][x]:
                board[y][x].remove(c)
        column(x,y,c+1)
def box(x,y,boxx,boxy,c):
    if 1<= c <=9:
        for n in range((boxx-1)*3, boxx*3):
            for r in range(((boxy-1)*3),boxy*3):
                if type(board[r][n]) == int:
                    if board[r][n] == c and c in board[y][x]:
                        board[y][x].remove(c)
        box(x,y,boxx,boxy,c+1)


def reduceposs():
    for r in range(9):
        for c in range(9):
            if type(board[r][c]) == list:
                row(c,r,1)
                box(c,r,(c/3)+1,(r/3)+1,1)
                column(c,r,1)

def rowanswer(y,c):
    indexc = []
    for n in range(9):
        if type(board[y][n]) == list:
            if c in board[y][n]:
                indexc.append(n)
    if len(indexc) == 1:
        board[y][indexc[0]] = c
        colupdate(indexc[0],c)
        boxupdate((indexc[0]/3)+1,(y/3)+1,c)

def colanswer(x,c):
    indexc = []
    for n in range(9):
        if type(board[n][x]) == list:
            if c in board[n][x]:
                indexc.append(n)
    if len(indexc) == 1:
        board[indexc[0]][x] = c
        boxupdate((x/3)+1,(indexc[0]/3)+1,c)
        rowupdate(indexc[0],c)

def boxanswer(boxx,boxy,c):
    indexc = []
    for x in range((boxx-1)*3, boxx*3):
        for y in range(((boxy-1)*3),boxy*3):
            if type(board[y][x]) == list:
                if c in board[y][x]:
                    indexc.append([y,x])
    if len(indexc) == 1:
        board[indexc[0][0]][indexc[0][1]] = c
        rowupdate(indexc[0][0],c)
        colupdate(indexc[0][1],c)

def rowupdate(r,n):
    for x in range(9):
        if type(board[r][x]) == list:
            if n in board[r][x]:
                board[r][x].remove(n)
def colupdate(c,n):
    for y in range(9):
        if type(board[y][c]) == list:
            if n in board[y][c]:
                board[y][c].remove(n)
def boxupdate(boxx,boxy,c):
    for n in range((boxx-1)*3, boxx*3):
        for r in range(((boxy-1)*3),boxy*3):
            if type(board[r][n]) == list:
                if c in board[r][n]:
                    board[r][n].remove(c)
def updatesingle(x,y):
    if type(board[y][x]) == list:
        if len(board[y][x]) == 1:
            c = board[y][x][0]
            board[y][x] = c
            rowupdate(y,c)
            colupdate(x,c)
            boxupdate((x/3)+1,(y/3)+1,c)

def checkdone():
    done = True
    for y in board:
        for n in y:
            if type(n) == list:
                done = False
    return done



def answer():
    for y in range(9):
        for n in range(1,10):
            rowanswer(y,n)
    for x in range(9):
        for n in range(1,10):
            colanswer(x,n)
    for boxX in range(1,4):
        for boxY in range(1,4):
            for n in range(1,10):
                boxanswer(boxX,boxY,n)
    for x in range(9):
        for y in range(9):
            updatesingle(x,y)
    checkdone()

insertposs()
reduceposs()
while checkdone() != True:
    answer()