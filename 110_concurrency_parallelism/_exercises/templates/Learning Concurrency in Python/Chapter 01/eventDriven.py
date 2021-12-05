______ turtle

turtle.setup(500,500)                
window = turtle.Screen()              
window.title("Event Handling 101!")     
window.bgcolor("lightblue")             
nathan = turtle.Turtle()  

___ moveForward
    nathan.forward(50)

___ moveLeft
    nathan.left(30)

___ moveRight
    nathan.right(30)

___ start
    window.onkey(moveForward, "Up")
    window.onkey(moveLeft, "Left")
    window.onkey(moveRight, "Right")
    window.listen()
    window.mainloop()

__ _____ __ _____
    s..