#! /usr/bin/env python

import rospy
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest
from math import pi
import time

rospy.init_node('service_set_joint_position_client')
rospy.wait_for_service('/goal_joint_space_path')
rospy.wait_for_service('/goal_tool_control')

arm_planning_group = 'arm'
arm_joint_names = ['joint1', 'joint2', 'joint3', 'joint4']

gripper_planning_group = 'gripper'
gripper_joint_names = ['gripper']

def move_arm(position, planning_time=2.0):
    service = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition)
    request = SetJointPositionRequest()
    
    request.planning_group = arm_planning_group
    request.joint_position.joint_name = arm_joint_names
    request.joint_position.position = position
    request.joint_position.max_accelerations_scaling_factor = 1.0
    request.joint_position.max_velocity_scaling_factor = 1.0
    request.path_time = planning_time

    service(request)

    time.sleep(3)

def move_gripper(action, planning_time=2.0):
    service = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)
    request = SetJointPositionRequest()


    if action == "open":
        position = [0.007] # from 0.01 to -0.01
    elif action == "close":
        position = [-0.007]
    
    request.planning_group = gripper_planning_group
    request.joint_position.joint_name = gripper_joint_names
    request.joint_position.position = position
    request.joint_position.max_accelerations_scaling_factor = 1.0
    request.joint_position.max_velocity_scaling_factor = 1.0
    request.path_time = planning_time

    service(request)

    time.sleep(3)

# go to home
move_arm([0, - pi / 4, 0, pi / 4])

# go down
move_arm([0,  0.4, - 0.25, 1.35])

# grab the object
move_gripper("close")

# go back to home
move_arm([0, - pi / 4, 0, pi / 4])

# go down
move_arm([0,  0.4, - 0.25, 1.35])

# grab the object
move_gripper("open")

# go back to home
move_arm([0, - pi / 4, 0, pi / 4])