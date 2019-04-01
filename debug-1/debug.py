left_motor = 1563872856371375
right_motor = 7567382956378165
servo = 9275392915737265

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    pass

async def autonomous_actions():
    print("Autonomous action sequence started")
    await Actions.sleep(1.0)
    print("1 second has passed in autonomous mode")

def teleop_setup():
    print("Tele-operated mode has started!")

def move_arm();
    Robot.get_value(left_motor, serv0, 1)
    time.sleep(2)
    Robot.get_value(left_motor, serv0, 0)

def teleop_main():
    if gamepad.get_value("r_trigger") > 0.5:
        while True:
            # move forward
            Robot.get_value(left_motor, "duty_cycle", -1.0)
            Robot.get_value(right_motor, "duty_cycle", -1.0)
    else if gamepad.get_value("l_trigger") > 0.5:
        while True:
            # move backward
            Robot.get_value(left_motor, "duty_cycle", 1.0)
            Robot.get_value(right_motor, "duty_cycle", 1.0)
    else if 1.0 > gamepad.get_value("joystick_left_y") > 0.75
        while True:
            # turn right
            Robot.get_value(left_motor, "duty_cycle", 1.0)
            Robot.get_value(right_motor, "duty_cycle", -1.0)
            time.sleep(1)
    else if 1.0 > gamepad.get_value("joystick_right_y") > 0.75)
        while True:
            # turn left
            Robot.get_value(left_motor, "duty_cycle", -1.0)
            Robot.get_value(right_motor, "duty_cycle", 1.0)
            time.sleep(1)
    if gamepad.get_vlue("button_a") == 1:
        move_arm()
