#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose #verry important for this. Do this on package.xml (is it have turtlesim?)


def pose_callback(msg: Pose):
    rospy.loginfo("X="+str(msg.x) + " " + "Y="+str(msg.y))

if __name__ == '__main__':
    rospy.init_node("PoseScrb")
    rospy.loginfo("PoseScrb node started")
    rospy.sleep(1)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    rospy.spin()