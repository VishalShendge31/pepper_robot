import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
from naoqi_bridge_msgs.srv import SetString

class PepperCoreControl(Node):
    def __init__(self):
        super().__init__('pepper_core_control')
        
        # Service clients
        self.wakeup_client = self.create_client(Trigger, '/naoqi_driver/motion/wake_up')
        self.alife_client = self.create_client(SetString, '/naoqi_driver/alife/set_state')
        
        # Wait for services
        self.wait_for_service(self.wakeup_client)
        self.wait_for_service(self.alife_client)

    def wait_for_service(self, client, timeout=10.0):
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f'Waiting for {client.srv_name}...')

    def wake_up(self):
        req = Trigger.Request()
        future = self.wakeup_client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result().success

    def set_alife_state(self, state: str):
        req = SetString.Request()
        req.data = state
        future = self.alife_client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result().success

def main(args=None):
    rclpy.init(args=args)
    controller = PepperCoreControl()
    
    try:
        # Disable autonomous life first
        if controller.set_alife_state("disabled"):
            controller.get_logger().info("Disabled autonomous life")
            
            # Wake up motors
            if controller.wake_up():
                controller.get_logger().info("Motors awakened!")
            else:
                controller.get_logger().error("Wakeup failed")
                
        rclpy.spin(controller)
        
    except KeyboardInterrupt:
        pass
    finally:
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
