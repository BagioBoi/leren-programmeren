from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
moves = 1
robotArm.speed = 3
for i in range (4):
    for i in range(moves):
        robotArm.grab()
        for i in range (5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range (5):
            robotArm.moveLeft()
    robotArm.moveRight()
    moves += 1
robotArm.wait()