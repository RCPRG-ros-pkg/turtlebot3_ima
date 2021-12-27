# Start simulation
## Start simulation in the **empty world**:
 >roslaunch ima_control turtlebot_control.launch

## Start simulation in the **basic world**:
 >roslaunch ima_control turtlebot_control.launch world:=basic

# PID parameters modification:
## print current value of a parameter:
 >rosparam get /turtlebot/wheel_[left][right]_effort_controller/pid/[p][i][d]
 e.g.
 >rosparam get /turtlebot/wheel_right_effort_controller/pid/p
## set value of a parameter:
 >rostopic pub /turtlebot/wheel_[left][right]_effort_controller/command std_msgs/Float64 "data: [value]"
 e.g.
 >rostopic pub /turtlebot/wheel_right_effort_controller/command std_msgs/Float64 "data: 0.0019"
