# REACTION TIME TEST

from microbit import *
from random import randint
from utime import ticks_ms

print("TEXTURE PACK NAMES: arrows, thin arrows, glow, fade, simple, any number from 0-4")

texture_pack_name = "glow"
texture_packs = [
    [Image.ARROW_W, Image.ARROW_E, " "],
    ["<", ">", " "],
    [Image("86300:97310:97410:97310:86300"), Image("00368:01379:01479:01379:00368"), Image("00100:00100:00100:00100:00100")],
    [Image("97531:97531:97531:97531:97531"), Image("13579:13579:13579:13579:13579"), Image("01210:01210:01210:01210:01210")],
    [Image("99500:99500:99500:99500:99500"), Image("00599:00599:00599:00599:00599"), Image("00000:00000:00000:00000:00000")],
]

def get_texture_pack_index_from_name(name):
    if name == "arrows":
        return 0
    if name == "thin arrows":
        return 1
    if name == "glow":
        return 2
    if name == "fade":
        return 3
    if name == "simple":
        return 4
    else:
        return int(name)

left_image, right_image, waiting_image = texture_packs[get_texture_pack_index_from_name(texture_pack_name)]

minimum_wait_time = 100
maximum_wait_time = 3000
penalty = 0
number_of_penalties = 0
number_of_trials = 20
trials = 0
all_reaction_times = []
total_reaction_time = 0
while True:
    if button_a.is_pressed() or button_b.is_pressed():
        number_of_penalties += 1
        total_reaction_time += penalty
        print("Penalty")
    
    wait_for_this_long = randint(minimum_wait_time, maximum_wait_time)
    display.show(waiting_image)
    
    sleep(wait_for_this_long)
    time_arrows_were_shown = ticks_ms()

    left_or_right = randint(0, 1)
    if left_or_right == 0: # Left
        display.show(left_image)
    
        while True:
            if button_a.is_pressed(): # Correct, left
                how_long_it_took_to_react = ticks_ms() - time_arrows_were_shown
                break

            if button_b.is_pressed(): # Wrong, right
                number_of_penalties += 1
                total_reaction_time += penalty
                print("Penalty")
    
    else: # Right
        display.show(right_image)

        while True:
            if button_a.is_pressed(): # Wrong, left
                number_of_penalties += 1
                total_reaction_time += penalty
                print("Penalty")
            
            if button_b.is_pressed(): # Correct, right
                how_long_it_took_to_react = ticks_ms() - time_arrows_were_shown
                break

    display.clear()
    all_reaction_times.append(how_long_it_took_to_react)
    total_reaction_time += how_long_it_took_to_react
    trials += 1
    if trials == number_of_trials:
        break

slowest_reaction_time = max(all_reaction_times)
fastest_reaction_time = min(all_reaction_times)
average_reaction_time = total_reaction_time / number_of_trials

results_list = [
    ["minimum_wait_time", minimum_wait_time],
    ["maximum_wait_time", maximum_wait_time],
    ["penalty", penalty],
    ["number_of_penalties", number_of_penalties],
    ["number_of_trials", number_of_trials],
    ["all_reaction_times", all_reaction_times],
    ["total_reaction_time", total_reaction_time],
    ["slowest_reaction_time", slowest_reaction_time],
    ["fastest_reaction_time", fastest_reaction_time],
    ["average_reaction_time", average_reaction_time]
]

for result_name, value in results_list:
    print(result_name, value)

display.scroll("Avg: {} ms".format(average_reaction_time))
sleep(1000)
display.scroll("Pnt: {}".format(number_of_penalties))
sleep(1000)