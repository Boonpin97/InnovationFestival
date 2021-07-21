#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
import keyboard
import time

delay = 5

def callback(data):
    global delay
    if data == 'True':
	time.sleep(delay)    
	lock_publisher = rospy.Publisher('/lock', Bool , queue_size=10)
    	lock_publisher.publish(True)

    else:
	pass

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('/lock_node', anonymous=True)
    rospy.Subscriber("/lock", Bool, callback)



    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
