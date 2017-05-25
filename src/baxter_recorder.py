#!/usr/bin/env python
import sys
import rospy
from sensor_msgs.msg import JointState


def callback_marker(data):
    global f_baxter
    
    robot_states = ""
    for i in range(len(data.position)):
        robot_states = robot_states+ " "+ str(data.position[i])

    f_baxter.write(str(data.header.stamp)+' '+
        robot_states+'\n')
    rospy.loginfo("baxter data recording")    


if __name__ == '__main__':
    
    # ros node init
    rospy.init_node('recorder_baxter_node', anonymous=True)
    
    # maker file read directory
    fileDir_baxter = sys.path[0]+"/../datasets/baxter_data0.txt"
    f_baxter = open(fileDir_baxter,'w')
    rospy.Subscriber("/robot/joint_states", JointState, callback_marker)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()