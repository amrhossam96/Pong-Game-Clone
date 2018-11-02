from tkinter import *
import random
import time


x_speed = random.uniform(0.01,0.05)
y_speed = random.uniform(0.01,0.05)


root = Tk()
root.title('home')
root.resizable(False, False)
root.geometry("400x400")
canvas = Canvas(root,height=400,width=400,bg='black')
canvas.pack()
oval = canvas.create_oval(200,200,220,220,fill='white')
paddle = canvas.create_rectangle(0,0,10,100,fill='white')
paddle2 = canvas.create_rectangle(385,0,395,100,fill='white')
p1_score = 0
p2_score = 0
def moveUp(event):
	
	canvas.move(paddle,0,-10)
def moveDown(event):
	canvas.move(paddle,0,10)


def moveUp2(event):
	
	canvas.move(paddle2,0,-10)
def moveDown2(event):
	canvas.move(paddle2,0,10)

canvas.create_text(195,40,text='pong',fill='white',font=('Times new roman',15,'bold'))
score1 = canvas.create_text(50,40,text='Player 1\nScore: {}'.format(str(p1_score)),fill='white')
score2 = canvas.create_text(360,40,text='Player 2\nScore: {}'.format(str(p2_score)),fill='white')

root.bind_all('<Down>', moveDown2)
root.bind_all('<Up>', moveUp2)
root.bind_all('<s>', moveDown)
root.bind_all('<w>', moveUp)


while True:

	firstPCoor = canvas.coords(paddle)
	secondPCoor = canvas.coords(paddle2)
	coord = canvas.coords(oval)
	if(coord[2]>400):
		x_speed*=-1
		p1_score+=1
		p1_score_text = 'Player 1\nScore: {}'.format(str(p1_score))
		canvas.itemconfigure(score1, text=str(p1_score_text))
		
		
	elif(coord[0]<=0):
		x_speed*=-1
		p2_score+=1
		p2_score_text = 'Player 2\nScore: {}'.format(str(p2_score))
		canvas.itemconfigure(score2, text=str(p2_score_text))
	elif(coord[1]<0):
		y_speed*=-1
	elif(coord[3]>400):
		y_speed*=-1



	if(coord[0]<firstPCoor[2] and coord[1]>firstPCoor[1] and firstPCoor[3]>coord[3]):
		x_speed*=-1
	if(coord[2]>secondPCoor[0] and coord[1]>secondPCoor[1] and coord[3]<secondPCoor[3]):
		x_speed*=-1

	canvas.move(oval,x_speed,y_speed)
	canvas.update()

root.mainloop()