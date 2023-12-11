# import the cozmo and image libraries
import cozmo

# import libraries for movement
from cozmo.util import degrees, distance_mm, speed_mmps


def move_triangle(robot):
    for _ in range(3):
        robot.drive_straight(distance_mm(200), speed_mmps(100)).wait_for_completed()
        robot.turn_in_place(degrees(120)).wait_for_completed()


def move_rectangle(robot):
    for _ in range(4):
        robot.drive_straight(distance_mm(200), speed_mmps(100)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()


def move_pentagon(robot):
    for _ in range(5):
        robot.drive_straight(distance_mm(200), speed_mmps(100)).wait_for_completed()
        robot.turn_in_place(degrees(72)).wait_for_completed()


def move_hexagon(robot):
    for _ in range(6):
        robot.drive_straight(distance_mm(200), speed_mmps(100)).wait_for_completed()
        robot.turn_in_place(degrees(60)).wait_for_completed()


def move_circle(robot):
    robot.drive_wheels(100, -20, None, None, 5.5)
