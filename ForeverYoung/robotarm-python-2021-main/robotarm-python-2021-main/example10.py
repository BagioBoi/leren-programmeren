from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
moves = 9
for i in range(5):
    robotArm.grab()
    for i in range(moves):
        robotArm.moveRight()
    robotArm.drop()
    moves -= 1
    for i in range(moves):
        robotArm.moveLeft()
    moves -= 1
robotArm.wait()