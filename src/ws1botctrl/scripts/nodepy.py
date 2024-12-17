#!/usr/bin/env python3

import rospy

if __name__ == '__main__':
    rospy.init_node("testNode")
    rospy.loginfo("nodepy.py started")
    #rospy.logwarn("this is a warning")
    #rospy.logerr("this is an error")
    #rospy.sleep(1)
    #rospy.loginfo("program end")
    rospy.sleep(1)
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("hello loop")
        rate.sleep()