# STARFALL

from microbit import *
from random import randint

player_x = 0

stars = [[4, 3], [3, 2], [4, 1], [3, 0]]

presses_a = 0
presses_b = 0 

score = 0 - len(stars)
stars_falling_speed = 300

display.clear()

game_over = False

while True:
    display.clear()

    if button_a.is_pressed() and player_x > 0: # If the player is not at the very left
        player_x -= 1 # Move to the left
    
    if button_b.is_pressed() and player_x < 4:
        player_x += 1
    
    for star in stars:
        star[1] += 1 # Move the star down
        if star[1] > 4:
            if player_x == star[0]:
                game_over = True
                break
            
            star[0] = randint(0,4)
            star[1] = 0
            
            score += 1
            if stars_falling_speed > 100:
                stars_falling_speed -= 1
    
    if game_over:
        break
    
    for star in stars:
        star_x = star[0]
        star_y = star[1]
        
        display.set_pixel(star_x, star_y, 5)
        
        if star_y > 0: # Moving the star down
            display.set_pixel(star_x, star_y - 1, 3) # Trail        
        if star_y > 1:
            display.set_pixel(star_x, star_y - 2, 1)
                
    display.set_pixel(player_x, 4, 9)
    
    sleep(stars_falling_speed)
    
display.scroll("Score: {}".format(score))