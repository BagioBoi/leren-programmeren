from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

for i in range(7):
    robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    robotArm.moveRight()
    for x in range(1):
        robotArm.drop()
    for x in range(2):
        robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()