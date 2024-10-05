import pgzrun

WIDTH=700
HEIGHT=700
questions=[]

welcome=Rect(10,10,680,50)
question=Rect(15,85,500,140)
answer1=Rect(15,240,270,140)
answer2=Rect(15,410,270,140)
answer3=Rect(300,240,270,140)
answer4=Rect(300,410,270,140)
ansbox=[answer1,answer2,answer3,answer4]

def draw():
    screen.fill("black")
    screen.draw.filled_rect(welcome,"grey")
    screen.draw.filled_rect(question,"grey")
    screen.draw.textbox("Welcome to QuizMaster!", welcome, color="white")
    screen.draw.textbox(Q[0], question, color="white")
    for i in ansbox:
        screen.draw.filled_rect(i,"grey")

def readquestions():
    global questions
    file=open("L.6/questions.txt", "r")        
    for i in file:
      questions.append(i)

def splitting():
  Q1=questions[0].split(",")
  return Q1


readquestions()    
Q=splitting()


pgzrun.go()