# Importing Libraries
import turtle as trtl
import random as rand
import sys
import time

# Set images to variable name
Pikachu_image = "Pikachu.gif"
Ampharos_image = "Ampharos.gif"
Title_image = "Title.gif"

wn = trtl.Screen()
#Register Images
wn.setup(width=1.0, height=1.0)
wn.addshape(Title_image)
wn.addshape(Pikachu_image)
wn.addshape(Ampharos_image)

# Set turtles/Variables
Title = trtl.Turtle()
monster = trtl.Turtle()
player = trtl.Turtle()
transition = trtl.Turtle()
player_hp = trtl.Turtle()
monster_hp = trtl.Turtle()
end = trtl.Turtle()
i = 0
Title.shape(Title_image)
monster.shape(Ampharos_image)
player.shape(Pikachu_image)

# Initialize positions
player_hp.hideturtle()
monster_hp.hideturtle()
transition.hideturtle()
monster.penup()
player.penup()
player_hp.penup()
player_hp.pensize(5)
monster_hp.penup()
monster_hp.pensize(5)
monster.hideturtle()
player.hideturtle()
player_hp.goto(-120,-120)
monster_hp.goto(-70,170)
monster.goto(200,150)
player.goto(-220,-150)

#turn System
player_turn = True
monster_turn = False

# Function for when player Wins
def no():
  wn.bgcolor("black")
  Title.hideturtle()
  time.sleep(4)
  sys.exit()

def gameOver():
  wn.bgcolor("black")
  end.color("white")
  end.goto(0,0)
  end.write("You Win!", font=("Arial", 40, "bold"))
  time.sleep(4)
  sys.exit()

#Function for when the player loses/quits
def gameOverLose():
  wn.bgcolor("black")
  end.color("white")
  end.goto(0,0)
  end.write("You Lost!", font=("Arial", 40, "bold"))
  time.sleep(4)
  sys.exit()

# Function for when the game starts, takes user name
def gameIntro():
  play = input("")
  if play.upper() == "YES":
    name = input("Sounds good! What is your trainer name?\n")
    print(f"Ok {name}, lets get exploring!")
  else:
    print("Ok, have a good day!")
    no()
    
def turnSys():
  global player_turn
  global num
  global monster_turn
  global player_hp
  global player
  global monster
  global monster_hp
  while int(player_hp.xcor()) > -120 and int(monster_hp.xcor()) > -70:
    if player_turn:
      player_choice = input("Encounter! Choose fight or run:")
      if player_choice.upper() == "RUN":
        gameOverLose()
      elif player_choice.upper() == "FIGHT":
        player_ability = input("Choose an ability: a)Electrocute b)Hydro Pump c)Tackle     d)Thundershock: ")
        if player_ability.upper() == "A":
          print ("You used Electrocute!")
          monster_hp_down(30)
          player_attack()
        elif player_ability.upper() == "B":
          print ("You used Hydro Pump!")
          monster_hp_down(15)
          player_attack()
        elif player_ability.upper() == "C":
          print ("You used Tackle!")
          monster_hp_down(40)
          player_attack()
        elif player_ability.upper() == "D":
          print ("You used Thundershock!")
          player_attack()
          monster_hp_down(50)
    elif monster_turn:
      abilities = ["Tackle", "Shock", "Solar Beam", "Shockwave"]
      monster_ability = rand.randint(0,3)
      if monster_ability == 0:
        monster_attack()
        player_hp_down(15)
        print ("Ampharos used", abilities[monster_ability])
      elif monster_ability == 1:
        monster_attack()
        player_hp_down(25)
        print ("Ampharos used", abilities[monster_ability])
      elif monster_ability == 2:
        monster_attack()
        player_hp_down(40)
        print ("Ampharos used", abilities[monster_ability])
      elif monster_ability == 3:
        monster_attack()
        player_hp_down(50)
        print ("Ampharos used", abilities[monster_ability])
    player_turn = not player_turn
    monster_turn = not monster_turn
      
# The function that uses maze animation to cut from start screen to fighting screen, setting background too
def encounterScreen():
  spirals = 26
  path_width = 30
  wall_length = path_width
  transition.speed(8)
  transition.pencolor("black")
  transition.pensize(80)
  for spiral in range(spirals):
    transition.forward(wall_length)
    transition.left(90)
    wall_length += path_width
  time.sleep(1)
  transition.clear()
  transition.penup()
  transition.goto(900,900)
  wn.bgcolor("lightblue")

# The function that takes the health off of the monster's health bar according to the player's damage from the ability they chose
def monster_hp_down(num):
  global monster_hp
  global monster
  if (monster_hp.xcor() > -60):
    monster_hp.color("lightblue")
    monster_hp.back(num)
    if (monster_hp.xcor() <= -60):
      monster.hideturtle()
      monster_hp.clear()
      gameOver()
  
# The function that takes the health off of the player's health bar according to the monster's damage from the ability they chose
def player_hp_down(num):
  global player_hp
  global player
  if (player_hp.xcor() > -110):
    player_hp.color("lightblue")
    player_hp.back(num)
    if (player_hp.xcor() <= -110):
      player.hideturtle()
      player_hp.clear()
      gameOverLose()

# Animation for both the player and the monster for when they attack to add life to the program
def monster_attack():
  global shake
  shake = 0
  while (shake < 3):
    player.speed(30)
    player.forward(10)
    player.back(10)
    shake += 1

def player_attack():
  global shake
  shake = 0
  while (shake < 3):
    monster.speed(30)
    monster.forward(10)
    monster.back(10)
    shake += 1

# Monster and player HP bar setup
monster_hp.pensize(5)
player_hp.goto(-120,-120)
monster_hp.goto(-70,170)
def drawHP():
  global i
  while (i < 2):
    player_hp.speed(30)
    player_hp.pendown()
    player_hp.forward(200)
    player_hp.right(90)
    player_hp.forward(30)
    player_hp.right(90)
    monster_hp.speed(30)
    monster_hp.pendown()
    monster_hp.forward(200)
    monster_hp.right(90)
    monster_hp.forward(30)
    monster_hp.right(90)
    i += 1
  player_hp.penup()
  player_hp.goto(-110,-135)
  monster_hp.penup()
  monster_hp.goto(-60,155)
  player_hp.pendown()
  player_hp.pensize(25)
  monster_hp.pendown()
  monster_hp.pensize(25)
  player_hp.pencolor("green")
  player_hp.forward(180)
  monster_hp.pencolor("green")
  monster_hp.forward(180)

gameIntro()
monster.showturtle()
player.showturtle()
Title.hideturtle()
monster.goto(-200,150)
player.goto(220,-150)
encounterScreen()
drawHP()
turnSys()