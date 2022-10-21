from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
move = 9
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for i in range(move):
            robotArm.moveRight()
        move -= 1
        robotArm.drop()
        for i in range(move):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
        move -= 1
robotArm.wait()