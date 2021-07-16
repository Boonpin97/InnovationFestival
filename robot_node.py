#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import keyboard
import time

movement_cmd = Twist()
current_header = 1
header = 1
turn_time = 2

def callback(data):
    global movement_cd, header, turn_time

    movement_cmd.linear.y = 0
    movement_cmd.linear.z = 0 
    movement_cmd.angular.x = 0 
    movement_cmd.angular.y = 0  

    msg = int(data.data)
    rospy.loginfo(msg)

    
    if msg == 0:
        movement_cmd.linear.x = 0  
	movement_cmd.angular.z = 0
    else:
	error = header - msg
	if error == 0:
	    rospy.loginfo('forward')
	    movement_cmd.linear.x = 0.2
	    movement_cmd.angular.z = 0 

	elif (abs(error) > 2 and error < 0) or (abs(error) < 2 and error > 0):
	    rospy.loginfo('turn left')
	    movement_cmd.linear.x = 0
	    movement_cmd.angular.z = 3
	    movement_publisher = rospy.Publisher('cmd_vel', Twist , queue_size=10)
	    movement_publisher.publish(movement_cmd)
	    if abs(error) > 2:
		error = abs(error) - 2
	    rospy.loginfo("Error {}".format(error))
	    time.sleep(turn_time * abs(error))
	    movement_cmd.linear.x = 0  
	    movement_cmd.angular.z = 0
	    movement_publisher = rospy.Publisher('cmd_vel', Twist , queue_size=10)
	    movement_publisher.publish(movement_cmd)

	elif (abs(error) <= 2 and error < 0) or (abs(error) >= 2 and error > 0):
            rospy.loginfo('turn right')
	    movement_cmd.linear.x = 0
	    movement_cmd.angular.z = -3
	    movement_publisher = rospy.Publisher('cmd_vel', Twist , queue_size=10)
	    movement_publisher.publish(movement_cmd)
	    if abs(error) > 2:
		error = abs(error) - 2
	    rospy.loginfo("Error {}".format(error))
	    time.sleep(turn_time * abs(error))
	    movement_cmd.linear.x = 0  
	    movement_cmd.angular.z = 0
	    movement_publisher = rospy.Publisher('cmd_vel', Twist , queue_size=10)
	    movement_publisher.publish(movement_cmd)

        header = msg

    rospy.logdebug("Publishing")
    movement_publisher = rospy.Publisher('cmd_vel', Twist , queue_size=10)
    movement_publisher.publish(movement_cmd)
    
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
