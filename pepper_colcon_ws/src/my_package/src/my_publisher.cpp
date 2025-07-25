#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <chrono>

using namespace std::chrono_literals;

class MyPublisher : public rclcpp::Node {
public:
    MyPublisher() : Node("my_publisher") {
        publisher_ = this->create_publisher<std_msgs::msg::String>("chatter", 10);
        timer_ = this->create_wall_timer(
            500ms, std::bind(&MyPublisher::timer_callback, this));
    }

private:
    void timer_callback() {
        auto message = std_msgs::msg::String();
        message.data = "Hello ROS2! Message #" + std::to_string(count_++);
        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
        publisher_->publish(message);
    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    size_t count_ = 0;
};

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MyPublisher>());
    rclcpp::shutdown();
    return 0;
}
