# Code written for the Reeborg's World environment
# I'll leave this here so you know how to implement loop whiles in Python.

```python

def turn_right():
    for left in range(3):
        turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
```