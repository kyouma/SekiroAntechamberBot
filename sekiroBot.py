import time
import sekiro
import pydirectinput


# Run this to begin the farm bot program.


def bot_start_timer(seconds):
    print(f"\n\nStarting Sekiro Farmer bot in {seconds} seconds.")
    print(" Set window focus to the game and exit any menus.")
    print(" View the README for instructions on setup.")
    for i in range(0, seconds):
        print(f" -- {i + 1}")
        time.sleep(1)
    print(" Proceeding with farmbot...")

def use_idol():
    ### If your computer loads faster or slower, you may need to change this setting.
    # Use a stopwatch to time using the idol - stop when game is fully loaded.
    # add about 3 seconds as it's a good time to alt tab and stop the script
    wait_time = 20
    print(" -- Using Idol.")
    sekiro.item_use()
    sekiro.menu_down()
    sekiro.menu_select()
    print(f" -- Waiting {wait_time} seconds for Loading Screen.")
    time.sleep(wait_time)

def bulwark_line_up():
    print(" -- Lining up with bulwark.")
    sekiro.camera_left(130)
    sekiro.walk_slow_start()
    sekiro.walk_forward(4)
    sekiro.walk_slow_stop()

def bulwark_jump():
    print(" -- Jumping over bulwark.")
    sekiro.walk_slow_start()
    sekiro.walk_forward_hold_start()
    sekiro.jump()
    time.sleep(1)
    sekiro.walk_slow_stop()
    time.sleep(.8)
    sekiro.walk_forward_hold_stop()

def ledge_jump():
    print(" -- Jumping from ledge.")
    sekiro.walk_forward_hold_start()
    time.sleep(.8)
    sekiro.jump()
    sekiro.walk_forward_hold_stop()
    sekiro.grapple_repeat_for(.5, 2)

def platform_grapple():
    print(" -- Grappling to platform.")
    sekiro.camera_right(135)
    sekiro.walk_forward(1)
    sekiro.camera_up(45)
    sekiro.grapple(2)

def first_enemy_approach():
    print(" -- Approaching first enemy.")
    sekiro.walk_slow_start()
    sekiro.walk_forward(.2)
    sekiro.walk_slow_stop()

def kill_and_collect():
    print(" -- Killing and collecting loot.")
    sekiro.camera_lock()
    sekiro.attack()
    time.sleep(1.6)
    sekiro.interact_hold(1.2)

def platform_drop_off():
    print(" -- Dropping off platform.")
    sekiro.walk_backwards(1)
    sekiro.toggle_stealth()
    time.sleep(.2)

def second_platform_drop_off():
    print(" -- Dropping off second platform.")
    sekiro.walk_forward(1.2)
    time.sleep(.3)

def second_enemy_approach():
    print(" -- Approaching second enemy.")
    sekiro.camera_lock()
    sekiro.walk_slow_start()
    sekiro.walk_forward(.8)
    sekiro.walk_slow_stop()
    
def farm_route_instructions():
    use_idol()
    
    sekiro.walk_backwards(0.01)
    time.sleep(.1)
    sekiro.camera_lock()
    
    sekiro.walk_forward(10)
    time.sleep(.1)
    
    sekiro.camera_left(0.8)
    time.sleep(.1)
    sekiro.camera_lock()
    
    sekiro.walk_slow_start()
    sekiro.walk_forward(4)
    time.sleep(.1)
    sekiro.walk_right(0.5)
    time.sleep(.1)
    sekiro.walk_forward(2)
    sekiro.walk_slow_stop()
    
    sekiro.attack()
    
    time.sleep(3)
    sekiro.interact_hold(1.2)

def print_farm_report(run_count):
    # Change these variables to match the xp/money given for a kill.
    # My numbers are based on NG4
    money_from_kill = 320
    exp_from_kill = 3156
    # This is only useful if you write a new route, it will always be 2 for this bot.
    enemies_per_run = 1
    kill_count = run_count * enemies_per_run
    money_earned = run_count * money_from_kill * enemies_per_run
    experience_earned = run_count * exp_from_kill * enemies_per_run
    print("---------- Farm Bot Report ----------")
    print(f"  Run {run_count} completed.")
    print(f"  {kill_count} kills.")
    print(f"  {money_earned} money earned.")
    print(f"  {experience_earned} experience points earned.\n")

if __name__ == "__main__":
    bot_start_timer(10)
    counter = 0
    while True:
        counter += 1
        print(f"\nBeginning run {counter}.")
        farm_route_instructions()
        print_farm_report(counter)
