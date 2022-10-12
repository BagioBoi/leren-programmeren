from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

for i in range(5):
    robotArm.grab()
    for m in range(2):
        robotArm.moveRight()
    robotArm.drop()
    if i < 4:    
        for m in range(2):
            robotArm.moveLeft()
    
for i in range(5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    if i < 4:
        robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()