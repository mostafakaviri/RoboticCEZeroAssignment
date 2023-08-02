#!/usr/bin/python3
import rospy
from std_msgs.msg import String
from hw_0.msg import proximity
from hw_0.msg import direction

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "go %s %s", data.c_wise, data.c_c_wise)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('motor_1', anonymous=True)

    rospy.Subscriber("motor1", direction, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()