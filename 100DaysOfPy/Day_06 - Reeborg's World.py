# TITLE: Reeborg's World 
# DESCRIPTION: Code to solve Reeborg World's maze: 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# DATE: 01Feb2023

# while not at_goal():
#     if right_is_clear():
#         turn_left()
#         turn_left()
#         turn_left()
#         move()
#     elif front_is_clear():move()
#     elif wall_on_right():
#         turn_left()
#     else: 
#         turn_left()
 
# Reflection:
# The layout of the maze puts the goal in the top right of 
# the coordinate plane. To avoid back tracing, the robot needs 
# to check it its right is clear to escape an infinite loop at (4,2).
# Otherwise it will continue to loop endlessly in the the bottom area. 
    