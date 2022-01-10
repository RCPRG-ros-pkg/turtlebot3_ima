#!/usr/bin/env python
# encoding: utf8
import rospy
import datetime
from gazebo_msgs.msg import ModelStates
from std_msgs.msg import Float64
import numpy as np 

import matplotlib
from matplotlib import pyplot as plt

GAZEBO_SCALE=1

def callback(data):
    global plot_omega, plot_vu, ros_time, plot_time
    vu = data.twist[1].linear.x
    omega = data.twist[1].angular.z
    print 'vu: ', vu, '\n omega: ', omega
    plot_vu.append(vu)
    plot_omega.append(omega)
    time_stamp = rospy.Time.now()-ros_time
    plot_time.append(time_stamp.to_sec()) 
    
def listener():
    global plot_omega, plot_vu, ros_time, plot_time
    rospy.init_node('ima_plot', anonymous=True)
    plot_omega = []
    plot_vu = []
    plot_time = []
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    raw_input("Press Enter to continue...")
    ros_time = rospy.Time.now()
    rospy.Subscriber("/gazebo/model_states", ModelStates, callback)
    # EFFORT CONTROLLER CONFIGURATION
    left_wheel = rospy.Publisher("/turtlebot/wheel_left_effort_controller/command", Float64, queue_size=10)
    right_wheel = rospy.Publisher("/turtlebot/wheel_right_effort_controller/command", Float64, queue_size=10)
    # VELOCITY CONTROLLER CONFIGURATION
    # left_wheel = rospy.Publisher("/turtlebot/wheel_left_velocity_controller/command", Float64, queue_size=10)
    # right_wheel = rospy.Publisher("/turtlebot/wheel_right_velocity_controller/command", Float64, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    while not rospy.is_shutdown():
        rospy.sleep(1)
        left_wheel.publish(0.0015*GAZEBO_SCALE)
        right_wheel.publish(-0.0015*GAZEBO_SCALE)
        rospy.sleep(10)
        left_wheel.publish(0.0015*GAZEBO_SCALE)
        right_wheel.publish(0.0*GAZEBO_SCALE)
        rospy.sleep(5)
        left_wheel.publish(-0.0015*GAZEBO_SCALE)
        right_wheel.publish(-0.0015*GAZEBO_SCALE)
        rospy.sleep(5)
        left_wheel.publish(0.0*GAZEBO_SCALE)
        right_wheel.publish(0.0*GAZEBO_SCALE)
        rospy.sleep(10)
        break

    plt.plot(plot_time,plot_vu);
    plt.title("Linear velocity")
    plt.show()    
    plt.plot(plot_time,plot_omega);
    plt.title("Angular velocity")
    plt.show()    

if __name__ == '__main__':
    listener()
