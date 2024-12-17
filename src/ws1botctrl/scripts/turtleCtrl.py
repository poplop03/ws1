#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(pose: Pose):
    cmd = Twist()
    cmd.linear.x = 1
    cmd.angular.z = 0
    pub.publish(cmd)

if __name__ == '__main__':
    rospy.init_node("turtleCtrl") #name apper on "rosnode list"
    rospy.loginfo("turtleCtrl node started")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(0.1)
    rospy.sleep(0.5)
    
    while not rospy.is_shutdown():
        sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
        rate.sleep()

