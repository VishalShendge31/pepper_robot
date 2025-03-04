#include "ros/ros.h"
#include "std_msgs/String.h"

void messageCallback(const std_msgs::String::ConstPtr& msg) {
    ROS_INFO("Received: [%s]", msg->data.c_str());
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "my_subscriber");
    ros::NodeHandle nh;
    
    // Subscribe to "chatter" topic with queue size 10
    ros::Subscriber sub = nh.subscribe("chatter", 10, messageCallback);
    
    ros::spin();
    return 0;
}
