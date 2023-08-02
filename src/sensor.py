#!/usr/bin/python3

import rospy
import random
from std_msgs.msg import String
from hw_0.msg import proximity
def talker():
 
    pub  = rospy.Publisher("distance", proximity, queue_size = 10)
    rospy.init_node("sensor", anonymous= True)
    rate = rospy.Rate(10)
                    
    while not rospy.is_shutdown():
        msg = proximity()

        msg.up = sen_rand()[0]
        msg.down= sen_rand()[1]
        msg.left = sen_rand()[2]
        msg.right = sen_rand()[3]

        rospy.loginfo(msg)
        pub.publish(msg)

        rate.sleep()

def sen_rand():
    a = []
    for i in range(4):
        a.append(random.randint(10,200))
    return a

if __name__=="__main__":
    talker()

