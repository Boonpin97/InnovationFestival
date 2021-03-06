#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import keyboard
import time

header = '1'

def callback(data):
    global header

    msg = data.data
    rospy.loginfo(msg)
    
    if msg == '0':
        pass
        rospy.loginfo('dont move')

    else:

	if header == msg:
	    rospy.loginfo('forward')
	    if msg == '1':
	        keyboard.press_and_release('up')
    	    elif msg == '3':
		keyboard.press_and_release('down')
    	    elif msg == '4':
		keyboard.press_and_release('left')
    	    elif msg == '2':
		keyboard.press_and_release('right')

	else:
	    rospy.loginfo('turn')
	    time.sleep(1)
	    if msg == '1':
	        keyboard.press_and_release('up')
    	    elif msg == '3':
		keyboard.press_and_release('down')
    	    elif msg == '4':
		keyboard.press_and_release('left')
    	    elif msg == '2':
		keyboard.press_and_release('right')
    	header = msg
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('gather_town', anonymous=True)

    rospy.Subscriber("wasd", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
