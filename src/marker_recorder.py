#!/usr/bin/env python
import sys
import rospy
from geometry_msgs.msg import PoseStamped


def callback_marker(data):
    global f_marker
    x_marker = data.pose.position.x
    y_marker = data.pose.position.y
    z_marker = data.pose.position.z
    qx_marker = data.pose.orientation.x
    qy_marker = data.pose.orientation.y
    qz_marker = data.pose.orientation.z
    qw_marker = data.pose.orientation.w
    f_marker.write(str(x_marker)+' '+str(y_marker)+' '+str(z_marker)+' '+
            str(qx_marker)+' '+str(qy_marker)+' '+str(qz_marker)+' '+
            str(qw_marker)+' '+'\n')
    rospy.loginfo("marker data recording")    


if __name__ == '__main__':
    
    # ros node init
    rospy.init_node('recorder_marker_node', anonymous=True)
    
    # maker file read directory
    fileDir_marker = sys.path[0]+"/../datasets/marker_data0.txt"
    f_marker=open(fileDir_marker,'w')
    rospy.Subscriber("/aruco_tracker/pose", PoseStamped, callback_marker)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()