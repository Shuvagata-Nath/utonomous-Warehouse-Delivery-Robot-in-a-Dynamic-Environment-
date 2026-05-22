#!/bin/bash

spawn_shelf () {
  NAME=$1
  X=$2
  Y=$3

  gz service -s /world/default/create --reqtype gz.msgs.EntityFactory --reptype gz.msgs.Boolean --timeout 1000 --req "sdf: \"<sdf version='1.7'><model name='$NAME'><static>true</static><link name='link'><visual name='visual'><geometry><box><size>0.5 4 2</size></box></geometry><material><ambient>0.2 0.4 0.8 1</ambient><diffuse>0.2 0.4 0.8 1</diffuse></material></visual><collision name='collision'><geometry><box><size>0.5 4 2</size></box></geometry></collision></link><pose>$X $Y 1 0 0 0</pose></model></sdf>\""
}

spawn_shelf shelf_1 2 -3
spawn_shelf shelf_2 4 -3
spawn_shelf shelf_3 6 -3
spawn_shelf shelf_4 8 -3
spawn_shelf shelf_5 10 -3
spawn_shelf shelf_6 2 3
spawn_shelf shelf_7 4 3
spawn_shelf shelf_8 6 3
spawn_shelf shelf_9 8 3
spawn_shelf shelf_10 10 3chmod +x /mnt/e/robotics_projects/warehouse_robot/scripts/spawn_shelves.sh
/mnt/e/robotics_projects/warehouse_robot/scripts/spawn_shelves.sh
