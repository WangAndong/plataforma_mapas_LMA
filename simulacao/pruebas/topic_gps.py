#!/usr/bin/env python
import rospy
# from std_msgs.msg import Float64
from sensor_msgs.msg import NavSatFix

file = open('datos.txt','w')

def callback(data):
	file.write ("%s\t%s\t%s\t%s\n" % (data.header.stamp, data.latitude, data.longitude, data.altitude))
    	print data.header.stamp, data.latitude, data.longitude, data.altitude

def getGPS():
    rospy.init_node('getGPS', anonymous=True)
    rospy.Subscriber("lowcost_gps", NavSatFix, callback)
    rospy.spin()


if __name__ == '__main__':
	
    getGPS()
