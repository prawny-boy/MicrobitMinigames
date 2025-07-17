# FLAPPY BIRD

from microbit import *
from random import randint
from utime import ticks_ms

display.show(Image.COW)
# DIFFICULTY
print("Hold nothing for easy, A for medium, B for hard, both for very hard.")
sleep(3000)
button_a_down = button_a.is_pressed()
button_b_down = button_b.is_pressed()

def buttons_to_diffculty(button_a_down, button_b_down):
        buttons_pressed = (button_a_down, button_b_down)
        if buttons_pressed == (False, False): 
                return ("Easy", 250, 1000)
        if buttons_pressed == (True, False): 
                return ("Medium", 200, 500)
        if buttons_pressed == (False, True): 
                return ("Hard", 100, 250)
        if buttons_pressed == (True, True): 
                return ("Cooked", 60, 150)

difficulty_name, frame_wait_time, pipe_moving_delay = buttons_to_diffculty(button_a_down, button_b_down)

display.scroll(difficulty_name)

# ACTUAL GAME
while True:
        player_position = 2 # Start playing middle
        pipe_position = 4
        pipe_hole_position = 2
        next_time_to_move_column = 500
        previous_pipe_position = 4
        player_hit_checked_already = False
        score = 0
        
        screen_pixels = [
                "00000",
                "00000",
                "00000",
                "00000",
                "00000",
                ]
                
        cleared_screen = [
                "00000",
                "00000",
                "00000",
                "00000",
                "00000",
                ]
                        
                        
                        
        def change_row_at_index(index):
                row = ["0", "0", "0", "0", "0"]
                row[index] = "9"
                return row[0] + row[1] + row[2] + row[3] + row[4]
                
        def change_row_at_index_inverted(index):
                row = ["5", "5", "5", "5", "5"]
                row[index] = "0"
                return row[0] + row[1] + row[2] + row[3] + row[4]
                
        def screen_list_to_image(screen_list):
                return Image(screen_list[0] + ":" + screen_list[1] + ":" + screen_list[2] + ":" + screen_list[3] + ":" + screen_list[4])
                        
        while True:
                current_time = ticks_ms()
                
                if button_a.is_pressed() and player_position > 0:
                        player_position -= 1
                elif button_b.is_pressed() and player_position < 4:
                        player_position += 1
                
                if current_time > next_time_to_move_column:
                        previous_pipe_position = pipe_position
                        if pipe_position == 0:
                                pipe_position = 4
                                pipe_hole_position = randint(0, 4)
        
                        else:
                                pipe_position -= 1
                                player_hit_checked_already = False
                        
                        next_time_to_move_column = current_time + pipe_moving_delay
                
                pipe_column = change_row_at_index_inverted(pipe_hole_position)
                screen_pixels[pipe_position] = pipe_column
                
                if previous_pipe_position != pipe_position:
                        screen_pixels[previous_pipe_position] = "00000"
                
                if pipe_position == 0:
                        player_column = change_row_at_index(player_position)
                        screen_pixels[0] = player_column
                else:
                        player_column = change_row_at_index(player_position)
                        screen_pixels[0] = player_column
                
                if pipe_position == 0 and player_position != pipe_hole_position and player_hit_checked_already == False:
                        player_hit_checked_already = True
                        break
                
                display.show(screen_list_to_image(screen_pixels))
                
                score += 1
                
                sleep(frame_wait_time)
                
        display.show(Image.SAD)
        
        sleep(1000)
        
        display.scroll("Score: {}".format(score))
        
        sleep(1000)