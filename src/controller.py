#!/usr/bin/python3
import rospy
from hw_0.msg import proximity
from hw_0.msg import direction

def callback(proximity):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s %s %s %s" ,proximity.up, proximity.down, proximity.left, proximity.right)

    sub = []

    sub.append(proximity.up)
    sub.append(proximity.down)
    sub.append(proximity.left)
    sub.append(proximity.right)

    max_1 = sub.index(max(sub))

    m_1 = direction()#left
    m_2 = direction()#right

    if max_1 == 0:
        m_1.c_wise = 2
        m_1.c_c_wise = 0
        m_2.c_wise = 0
        m_2.c_c_wise = 2
    
    if max_1 == 1:
        m_1.c_wise = 0
        m_1.c_c_wise = 0
        m_2.c_wise = 0
        m_2.c_c_wise = 0
    
    if max_1 == 2:
        m_1.c_wise = 1
        m_1.c_c_wise = 0
        m_2.c_wise = 0
        m_2.c_c_wise = 1
    
    if max_1 == 3:
        m_1.c_wise = 0
        m_1.c_c_wise = 1
        m_2.c_wise = 1 
        m_2.c_c_wise = 0

    talker_1(m_1)
    talker_2(m_2)

def talker_1(proximity_1):
 
    pub  = rospy.Publisher("motor1", direction, queue_size = 10)
    # rospy.init_node("sensor", anonymous= True)
    #rate = rospy.Rate(10)
                    
    
        # msg = proximity()

        # msg.up = 10
        # msg.down= 20
        # msg.left = 30
        # msg.right = 40

        # rospy.loginfo(msg)
    pub.publish(proximity_1)

        
    

def talker_2(proximity_2):
 
    pub  = rospy.Publisher("motor2", direction, queue_size = 10)
    # rospy.init_node("sensor", anonymous= True)
    #rate = rospy.Rate(10)
                    
    
        

        # rospy.loginfo(msg)
    pub.publish(proximity_2)



def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('controller', anonymous=True)

    rospy.Subscriber("distance", proximity, callback)
    

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()