#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def pyTestSend():
    pub = rospy.Publisher('pyTestChatter', String, queue_size=10)
    rospy.init_node('pyTestSend', anonymous=True)
    rate = rospy.Rate(100) # 100hz
    while not rospy.is_shutdown():
        hello_str = "roboros py says hello %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        pyTestSend()
    except rospy.ROSInterruptException:
        pass
