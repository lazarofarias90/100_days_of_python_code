# Code written for the Reeborg's World environment
# I'll leave this here so you know how to implement functions in Python.

```python

def turn_right():
    for left in range(3):
        turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    jump()    

```