#!/usr/bin/env python3

import rospy
#from turtlesim.msg import Pose #verry important for this. Do this on package.xml (is it have turtlesim?)
from geometry_msgs.msg import Twist

def cmdvel_callback(msg: Twist):
    rospy.loginfo("Xvel="+str(msg.linear.x)+ " " "Yvel="+str(msg.linear.y))
    linearx = msg.linear.x
    lineary = msg.linear.y
    if linearx == 0.5 and lineary == 0:
        setpoint1 = 2
        setpoint2 = 2
    if linearx == 0.5 and lineary == 0.5:
        setpoint1 = 2
        setpoint2 = 1.5
    if linearx == 0.5 and lineary == -0.5:
        setpoint1 = 1.5
        setpoint2 = 2


if __name__ == '__main__':
    rospy.init_node("subcmd")
    rospy.loginfo("subcmd node started")
    rospy.sleep(1)
    sub = rospy.Subscriber("/cmd_vel", Twist, callback=cmdvel_callback)
    rospy.spin()