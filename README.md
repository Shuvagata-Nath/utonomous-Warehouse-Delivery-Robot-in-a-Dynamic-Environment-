# Autonomous Warehouse Delivery Robot

A ROS 2 and Gazebo based autonomous warehouse robot simulation built for shelf-to-shelf delivery in a dynamic environment.

The project combines SLAM mapping, AMCL localization, Nav2 autonomous navigation, and dynamic obstacle avoidance using TurtleBot3 inside a warehouse world.

---

## Features

- warehouse environment with 10 shelves
- Autonomous navigation using Nav2
- SLAM-generated occupancy map
- AMCL localization
- Dynamic moving human obstacles
- Python-based delivery mission controller
- LiDAR-based obstacle detection and avoidance

---

## Technologies Used

- ROS 2 Jazzy
- Gazebo
- RViz
- TurtleBot3
- Nav2
- Python
- LiDAR / LaserScan
- AMCL
- Cartographer SLAM

## Demo Video:
https://www.youtube.com/watch?v=UdvFLvprOGI

## Project Structure

```bash
warehouse_robot/
│
├── maps/
│   ├── custom_warehouse_map.yaml
│   └── custom_warehouse_map.pgm
│
├── scripts/
│   ├── delivery_robot.py
│   ├── move_7_humans.py
│   ├── spawn_shelves.sh
│   └── spawn_7_humans.sh
│
├── worlds/
│   └── warehouse_10_shelves.sdf
│
├── README.md 


