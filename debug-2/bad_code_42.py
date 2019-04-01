left_motor = "56691261256684536973978"
right_motor = "56694973530028008008356"
#limit_switch = "36384566494538849932"

def autonomous_setup():
    pass

def autonomous_main():
    Robot.set_value(left_motor, "duty_cycle", -1)
    Robot.set_value(right_motor, "duty_cycle", 1)

async def autonomous_actions():
    pass

def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
    if Gamepad.get_value('r_trigger' > .5):
        Robot.set_value(right_motor, "duty_cycle", 0.5)
    else:
        Robot.set_value(right_motor, "duty_cycle", 0)
    if Gamepad.get_value("l_trigger" > .5):
        Robot.set_value(left_motor, "duty_cycle", 0.5)
    else:
        Robot.set_value(left_motor, "duty_cycle", 0)