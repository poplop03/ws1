#!/usr/bin/env python3
#this node is publishing to cmd_vel at 2hz to draw a circle
import rospy

from geometry_msgs.msg import Twist


if __name__ == '__main__':
    rospy.init_node("cmdvelPub")
    rospy.loginfo("cmdvelPub node started")
    pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 2
        msg.angular.z = 0
        pub.publish(msg)   
        rate.sleep()
        