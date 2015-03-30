'''
Created on Mar 29, 2015

@author: Sameer Adhikari
'''

from problemset02.room import RectangularRoom
from problemset02.robot import StandardRobot

# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    steps_all_trials = []
    for i in range(num_trials):
        room = RectangularRoom(width, height)
        robots = [robot_type(room, speed) for k in range(num_robots)]
        steps_one_trial = 0
        coverage = room.getNumCleanedTiles() / float(room.getNumTiles())
        while coverage < min_coverage:
            for robot in robots:
                robot.updatePositionAndClean()
            steps_one_trial += 1  # All the robots moving in an iteration counts as one step
            coverage = room.getNumCleanedTiles() / float(room.getNumTiles())
        steps_all_trials.append(steps_one_trial)
    return float(int(sum(steps_all_trials) / num_trials))

if __name__ == '__main__':
    print runSimulation(1, 1, 5, 5, 1, 100, StandardRobot)
    print runSimulation(3, 1, 20, 20, 1, 100, StandardRobot)
