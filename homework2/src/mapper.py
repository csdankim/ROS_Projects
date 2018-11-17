#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

import message_filters
from sensor_msgs.msg import LaserScan

from math import sin,cos


# This callback synchronizes odometry and lidar messages.  It also calculates the heading of the robot as an Euler angle, so 
# that it's easier to use with trigonometric functions.
def callback(odom_msg, lidar_msg):
	(_, _, heading) = euler_from_quaternion([odom_msg.pose.pose.orientation.x, odom_msg.pose.pose.orientation.y, odom_msg.pose.pose.orientation.z, odom_msg.pose.pose.orientation.w])
	print 'Pose: ', odom_msg.pose.pose.position.x, odom_msg.pose.pose.position.y, heading
	print 'Lidar[0]', lidar_msg.ranges[0]
	print


if __name__ == '__main__':
	rospy.init_node('mapper')

	odom_sub = message_filters.Subscriber('/odom', Odometry)
	lidar_sub = message_filters.Subscriber('/scan', LaserScan)
	sub = message_filters.TimeSynchronizer([odom_sub, lidar_sub], 10)
	sub.registerCallback(callback)

	rospy.spin()
