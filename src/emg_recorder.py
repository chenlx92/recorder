#!/usr/bin/env python
import sys
import rospy
from myo_driver.msg import emgState


def callback_emg(data):
    global f_emg
    f_emg.write( str(data.header.stamp)+' '+
            str(data.ch0)+' '+str(data.ch1)+' '+str(data.ch2)+' '+
            str(data.ch3)+' '+str(data.ch4)+' '+str(data.ch5)+' '+
            str(data.ch6)+' '+str(data.ch7)+' '+'\n')
    rospy.loginfo("emg data recording")    


if __name__ == '__main__':
    
    # ros node init
    rospy.init_node('recorder_emg_node', anonymous=True)
    
    #emg file read directory
    fileDir_emg = sys.path[0]+"/../datasets/emg_data0.txt"
    f_emg=open(fileDir_emg,'w')
    rospy.Subscriber("myo_raw_pub", emgState, callback_emg)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
