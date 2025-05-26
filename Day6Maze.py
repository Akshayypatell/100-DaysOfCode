while front_is_clear() == True:
    move()
turn_left()
while at_goal() != True:
    if right_is_clear() == True:
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()
        
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
