#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import keyboard

def talker():
    pub = rospy.Publisher('wasd', String, queue_size=10)
    rospy.init_node('web_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = "0"
	if keyboard.is_pressed('w'):
	    msg  = '1'
	elif keyboard.is_pressed('a'):
	    msg  = '4'
	elif keyboard.is_pressed('s'):
	    msg  = '3'
	elif keyboard.is_pressed('d'):
	    msg  = '2'
	else:
	    msg = '0'

        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
