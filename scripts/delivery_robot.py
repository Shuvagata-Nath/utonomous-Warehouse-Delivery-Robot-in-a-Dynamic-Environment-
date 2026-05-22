import rclpy
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
import math
import time


def yaw_to_quaternion(yaw):
    return {
        "z": math.sin(yaw / 2.0),
        "w": math.cos(yaw / 2.0)
    }


class DeliveryRobot:
    def __init__(self):
        rclpy.init()
        self.node = rclpy.create_node("warehouse_delivery_robot")
        self.client = ActionClient(self.node, NavigateToPose, "navigate_to_pose")

        self.node.get_logger().info("Waiting for Nav2 action server...")
        self.client.wait_for_server()
        self.node.get_logger().info("Connected to Nav2.")

    def go_to(self, name, x, y, yaw=0.0):
        goal = NavigateToPose.Goal()

        pose = PoseStamped()
        pose.header.frame_id = "map"
        pose.header.stamp = self.node.get_clock().now().to_msg()

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0

        q = yaw_to_quaternion(yaw)
        pose.pose.orientation.z = q["z"]
        pose.pose.orientation.w = q["w"]

        goal.pose = pose

        self.node.get_logger().info(f"Going to {name}: x={x}, y={y}")

        send_future = self.client.send_goal_async(goal)
        rclpy.spin_until_future_complete(self.node, send_future)

        goal_handle = send_future.result()

        if not goal_handle.accepted:
            self.node.get_logger().error(f"Goal rejected: {name}")
            return False

        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self.node, result_future)

        result = result_future.result()
        self.node.get_logger().info(f"Reached {name}")
        return True

    def run_delivery_mission(self):
        # Safe points in front of shelves.
        # Lower shelf row is around y = -3, front corridor is y = -0.7
        # Upper shelf row is around y = 3, front corridor is y = 0.7

        pickup_shelf_2 = (4.0, -0.7, -math.pi / 2)
        dropoff_shelf_10 = (10.0, 0.7, math.pi / 2)

        self.go_to("Pickup: Shelf 2", *pickup_shelf_2)

        self.node.get_logger().info("Picking up product...")
        time.sleep(2)

        self.go_to("Drop-off: Shelf 10", *dropoff_shelf_10)

        self.node.get_logger().info("Dropping off product...")
        time.sleep(2)

        self.node.get_logger().info("Delivery mission completed.")

    def shutdown(self):
        self.node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    robot = DeliveryRobot()
    try:
        robot.run_delivery_mission()
    finally:
        robot.shutdown()
