import turtle

#create window
#variable?

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

#speed
turtle.speed()

#wait for user to end
turtle.exitonclick()
