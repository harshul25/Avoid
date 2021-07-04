import curses
from random import randint
from time import sleep
from random import uniform

class enemy:

    man = {
        'face':[1,0], #x,y
        'armL':[0,1],
        'armR':[2,1],
        'body':[1,1],
        'legL':[0,2],
        'legR':[2,2]
        }
    def __init__(self):
        return

    def __init__(self,y):
        self.man = {
        'face':[52,0+y], #x,y
        'armL':[51,1+y],
        'armR':[53,1+y],
        'body':[52,1+y],
        'legL':[51,2+y],
        'legR':[53,2+y]
        }
        return

    def get_enemy(self):
        return self.man

    def move_left(self,adj):
        self.man['body'][0] -= adj
        self.man['armR'][0] -= adj
        self.man['armL'][0] -= adj
        self.man['legL'][0] -= adj
        self.man['legR'][0] -= adj
        self.man['face'][0] -= adj
        return self.man
    def set_enemy_and_move(self, man, pace):
        self.man = man
        self.move_left(pace)
        return self.man
answer = ""

print("\n")
print("""   |    \\      /  /---\\   --|-- |---    """)
print("""  | |    \\    /  /     \\    |   |     \\ """)
print(""" |---|    \\  /   \\     /    |   |     /  """)
print("""|     |    \\/     \\___/   __|__ |___   """)
print("\n")
line1 = "Welcome to the game of Avoid! It is the year 2020 and the world is on the verge of facing a "
for x in line1:
    print(x,end='',flush=True)
    sleep(uniform(0,0.2))
line2 = "pandemic. The virus Covid 19 is highly contagious and spreads simply by human contact. You "
for x in line2:
    print(x,end='',flush=True)
    sleep(uniform(0,0.2))
line3 = "are on your way home and you must avoid contact from everyone else as they are either not aware"
for x in line3:
    print(x,end='',flush=True)
    sleep(uniform(0,0.2))
line4 = " or still in disbelief. Make sure to collect all available amenities (bonus points) on your way back! Stay safe!"
for x in line4:
    print(x,end='',flush=True)
    sleep(uniform(0,0.2))
while answer != "play":
    answer = input("\nType play to start or i for instructions!\n")
    if answer == "i":
       #print instructions
        print("""        ^       """)
        print("""        |       """)
        print("""        0       """)
        print(""" <---  -|-  --->""")
        print("""       / \\     """)
        print("""        |       """)
        print("""        v       """)
        line1 = "You can move the character up and down left right to maintain social distancing from other pedestrians while staying in the play zone"
        for x in line1:
            print(x,end='',flush=True)
            sleep(uniform(0,0.1))
        print("")
        print("""    0          """)
        print("""   -|-  ---> * """)
        print("""   / \\        """)
        line1 = "Collect as many points (available amenities) as you can on the way! "
        for x in line1:
            print(x,end='',flush=True)
            sleep(uniform(0,0.1))     
        line1 = "Each collected bonus gives +1 and contact with pedestrian gives -5. Be careful!"
        for x in line1:
            print(x,end='',flush=True)
            sleep(uniform(0,0.1))      



#setup up window
curses.initscr()
win = curses.newwin(20,60,0,0) #x,y
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1) 
enemiesList = []
#game logic
counter = 0
score = 0
ESC = 27
key = curses.KEY_RIGHT
man = {
    'face': [6,10], #x,y
    'armL':[5,11],
    'armR':[7,11],
    'body':[6,11],
    'legL':[5,12],
    'legR':[7,12]
    }
house = {
    'floor': [[1,11],[2,11],[3,11]],
    'roof': [[1,10],[2,10],[3,10]]
}
actor = man
points = (30,10)
win.addch(points[1],points[0],'*')
while key != ESC:

    #Add score
    win.addstr(0,2,'Score '+ str(score) + ' ')
    win.timeout(150-(1)//5 + (1)//10%120)#set speed
    #get next key
    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key #new key unless nothing pressed. 
    if key not in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_RIGHT, curses.KEY_LEFT]:
        key = prev_key
    #if we hit the boundry then break

    #movement
    if key == curses.KEY_DOWN:
        #remove the person
        win.addch(actor['face'][1],actor['face'][0],' ')
        win.addch(actor['armL'][1],actor['armL'][0],' ')
        win.addch(actor['body'][1],actor['body'][0],' ')
        win.addch(actor['armR'][1],actor['armR'][0],' ')
        win.addch(actor['legL'][1],actor['legL'][0],' ')
        win.addch(actor['legR'][1],actor['legR'][0],' ')
        #update coordinates
        actor['face'][1] +=1
        actor['armL'][1] +=1
        actor['armR'][1] +=1
        actor['legL'][1] +=1
        actor['legR'][1] +=1
        actor['body'][1] +=1
    if key == curses.KEY_UP:
        #remove the person
        win.addch(actor['face'][1],actor['face'][0],' ')
        win.addch(actor['armL'][1],actor['armL'][0],' ')
        win.addch(actor['body'][1],actor['body'][0],' ')
        win.addch(actor['armR'][1],actor['armR'][0],' ')
        win.addch(actor['legL'][1],actor['legL'][0],' ')
        win.addch(actor['legR'][1],actor['legR'][0],' ')
        #update coordinates
        actor['face'][1] -=1
        actor['armL'][1] -=1
        actor['armR'][1] -=1
        actor['legL'][1] -=1
        actor['legR'][1] -=1
        actor['body'][1] -=1
    if key == curses.KEY_LEFT:
        #remove the person
        win.addch(actor['face'][1],actor['face'][0],' ')
        win.addch(actor['armL'][1],actor['armL'][0],' ')
        win.addch(actor['body'][1],actor['body'][0],' ')
        win.addch(actor['armR'][1],actor['armR'][0],' ')
        win.addch(actor['legL'][1],actor['legL'][0],' ')
        win.addch(actor['legR'][1],actor['legR'][0],' ')
        #update coordinates
        actor['face'][0] -=1
        actor['armL'][0] -=1
        actor['armR'][0] -=1
        actor['legL'][0] -=1
        actor['legR'][0] -=1
        actor['body'][0] -=1
    if key == curses.KEY_RIGHT:
        #remove the person
        win.addch(actor['face'][1],actor['face'][0],' ')
        win.addch(actor['armL'][1],actor['armL'][0],' ')
        win.addch(actor['body'][1],actor['body'][0],' ')
        win.addch(actor['armR'][1],actor['armR'][0],' ')
        win.addch(actor['legL'][1],actor['legL'][0],' ')
        win.addch(actor['legR'][1],actor['legR'][0],' ')
        #update coordinates
        actor['face'][0] +=1
        actor['armL'][0] +=1
        actor['armR'][0] +=1
        actor['legL'][0] +=1
        actor['legR'][0] +=1
        actor['body'][0] +=1
    #move the house out of frame


        # for the enemies 
    if counter == 0 and score != 0:
        for i in range(randint(1,3)):
            enemiesList.append(enemy(randint(3,16)).get_enemy())
        counter = 1
    else:
        counter = 1


    for i in range(len(enemiesList)):
        
        
        tmp = enemiesList[i]

        win.addch(tmp['face'][1],tmp['face'][0],' ')
        win.addch(tmp['armL'][1],tmp['armL'][0],' ')
        win.addch(tmp['body'][1],tmp['body'][0],' ')
        win.addch(tmp['armR'][1],tmp['armR'][0],' ')
        win.addch(tmp['legL'][1],tmp['legL'][0],' ')
        win.addch(tmp['legR'][1],tmp['legR'][0],' ')

        #hacky fix to the missing point astrix when the enemy moves over it
        if points[1] == tmp['face'][1] and points[0] == tmp['face'][0]: win.addch(points[1],points[0],'*')
        if points[1] == tmp['legR'][1] and points[0] == tmp['legR'][0]: win.addch(points[1],points[0],'*')
        if points[1] == tmp['armR'][1] and points[0] == tmp['armR'][0]: win.addch(points[1],points[0],'*')
        if points[1] == tmp['legL'][1] and points[0] == tmp['legL'][0]: win.addch(points[1],points[0],'*')
        if points[1] == tmp['armL'][1] and points[0] == tmp['armL'][0]: win.addch(points[1],points[0],'*')
        if points[1] == tmp['body'][1] and points[0] == tmp['body'][0]: win.addch(points[1],points[0],'*')

        #break when two people collide perfectly
        if actor['face'][1] == tmp['face'][1] and actor['face'][0] == tmp['face'][0]: score -= 5
        if actor['face'][1]-1 == tmp['face'][1] and actor['face'][0] == tmp['face'][0]: score -= 5
        if actor['face'][1] == tmp['face'][1] and actor['face'][0]-1 == tmp['face'][0]: score -= 5 
        if actor['face'][1]+1 == tmp['face'][1] and actor['face'][0] == tmp['face'][0]: score -= 5
        if actor['face'][1] == tmp['face'][1] and actor['face'][0]+1 == tmp['face'][0]: score -= 5
        if actor['face'][1]+1 == tmp['face'][1] and actor['face'][0]+1 == tmp['face'][0]: score -= 5
        if actor['face'][1]-1 == tmp['face'][1] and actor['face'][0]-1 == tmp['face'][0]: score -= 5
    

        #if reached the end then you don't update. 
        if tmp['armL'][0] <= 3:
            continue
        else:
            tmp = enemy(0).set_enemy_and_move(tmp,randint(1,2))
                #break when two people collide perfectly
 
        
        #Add enemy body
        win.addch(tmp['face'][1],tmp['face'][0],'0')
        win.addch(tmp['armL'][1],tmp['armL'][0],'-')
        win.addch(tmp['body'][1],tmp['body'][0],'|')
        win.addch(tmp['armR'][1],tmp['armR'][0],'-')
        win.addch(tmp['legL'][1],tmp['legL'][0],'/')
        win.addch(tmp['legR'][1],tmp['legR'][0],'\\')


        enemiesList[i] = tmp

        



        
    #add new points as you move forward
    if actor['face'][0] == points[0] or actor['armR'][0] == points[0] or actor['armL'][0] == points[0] or actor['legL'][0] == points[0] or actor['legR'][0] == points[0]:
        if actor['face'][1] == points[1] or actor['armR'][1] == points[1] or actor['armL'][1] == points[1] or actor['legL'][1] == points[1] or actor['legR'][1] == points[0]:
            #you've got the point 
            score += 1
            counter = 0
            points = ()
            while points == ():
                points = (randint(3,55),randint(3,18))
                if actor['face'][0] == points[0] and actor['face'][1] == points[1]:
                    points = ()
                elif actor['armR'][0] == points[0] and actor['armR'][1] == points[1]:
                    points = ()
                elif actor['armL'][0] == points[0] and actor['armL'][1] == points[1]:
                    points = ()
                elif actor['legR'][0] == points[0] and actor['legR'][1] == points[1]:
                    points = ()
                elif actor['legL'][0] == points[0] and actor['legL'][1] == points[1]:
                    points = ()
                elif actor['body'][0] == points[0] and actor['body'][1] == points[1]:
                    points = ()
            win.addch(points[1],points[0],'*')        




    #break out of the iteration if you exceed the limits.
    if actor['armL'][1] == 1: break
    if actor['armR'][1] == 18: break
    if actor['face'][0] == 1: break
    if actor['legR'][0] == 58: break
    if score < 0: break


    #Add person
    win.addch(actor['face'][1],actor['face'][0],'0')
    win.addch(actor['armL'][1],actor['armL'][0],'-')
    win.addch(actor['body'][1],actor['body'][0],'|')
    win.addch(actor['armR'][1],actor['armR'][0],'-')
    win.addch(actor['legL'][1],actor['legL'][0],'/')
    win.addch(actor['legR'][1],actor['legR'][0],'\\')

    #Add hospital (only for the beginning)
    if house['roof'][2][0] > 0:
        
        if house['roof'][0][0] >= 0:
            win.addch(house['roof'][0][1],house['roof'][0][0],' ')
            win.addch(house['floor'][0][1],house['floor'][0][0],' ')
        if house['roof'][1][0] >= 0:
            win.addch(house['roof'][1][1],house['roof'][1][0],' ')
            win.addch(house['floor'][1][1],house['floor'][1][0],' ')
        if house['roof'][2][0] >= 0:    
            win.addch(house['roof'][2][1],house['roof'][2][0],' ')
            win.addch(house['floor'][2][1],house['floor'][2][0],' ')

        if score > 0:
            house['floor'][0][0] -=1
            house['floor'][1][0] -=1
            house['floor'][2][0] -=1
            house['roof'][0][0] -=1
            house['roof'][1][0] -=1
            house['roof'][2][0] -=1
    
    
    
    #hacky fix to maintain symmetry of playzone walls
    if house['roof'][2][0] == 0:  
        win.addch(house['roof'][2][1],house['roof'][2][0],'|')
        win.addch(house['floor'][2][1],house['floor'][2][0],'|')

    #move house back
    if house['roof'][2][0] > 0: 
        if house['roof'][0][0] >= 0:
            win.addch(house['roof'][0][1],house['roof'][0][0],'/')
            win.addch(house['floor'][0][1],house['floor'][0][0],'|')
        if house['roof'][1][0] >= 0:
            win.addch(house['roof'][1][1],house['roof'][1][0],'+')
            win.addch(house['floor'][1][1],house['floor'][1][0],'_')
        if house['roof'][2][0] >= 0:    
            win.addch(house['roof'][2][1],house['roof'][2][0],'\\')
            win.addch(house['floor'][2][1],house['floor'][2][0],'|')



        

curses.endwin()
print("Your score is: " + str(score)+" ")


