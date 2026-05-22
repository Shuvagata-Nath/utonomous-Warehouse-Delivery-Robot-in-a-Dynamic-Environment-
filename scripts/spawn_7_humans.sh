#!/bin/bash

spawn_human () {
  NAME=$1
  X=$2
  Y=$3

  gz service -s /world/default/create --reqtype gz.msgs.EntityFactory --reptype gz.msgs.Boolean --timeout 1000 --req "sdf: \"<sdf version='1.7'><model name='$NAME'><pose>$X $Y 0.275 0 0 0</pose><link name='link'><inertial><mass>1.0</mass></inertial><visual name='visual'><geometry><cylinder><radius>0.08</radius><length>0.55</length></cylinder></geometry><material><ambient>1 0.2 0.2 1</ambient><diffuse>1 0.2 0.2 1</diffuse></material></visual><collision name='collision'><geometry><cylinder><radius>0.08</radius><length>0.55</length></cylinder></geometry></collision></link></model></sdf>\""
}

# Two humans for middle corridor
spawn_human human_vertical_1 6.65 -5.4
spawn_human human_vertical_2 7.35 5.4

# Five humans for aisles
spawn_human human_aisle_1 1.0 0.75
spawn_human human_aisle_2 3.0 0.35
spawn_human human_aisle_3 5.0 0.00
spawn_human human_aisle_4 8.3 -0.35
spawn_human human_aisle_5 10.3 -0.75