# open_manipulator_examples

## 環境構築


依存パッケージのインストール

```
sudo apt-get install ros-melodic-ros-controllers ros-melodic-gazebo* ros-melodic-moveit* ros-melodic-industrial-core
sudo apt-get install ros-melodic-dynamixel-sdk ros-melodic-dynamixel-workbench*
sudo apt-get install ros-melodic-robotis-manipulator
```

open_manipulator関連のパッケージのダウンロードとビルド

```
cd ~/catkin_ws/src/
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/open_manipulator.git
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/open_manipulator_msgs.git
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/open_manipulator_simulations.git
git clone https://github.com/ROBOTIS-GIT/open_manipulator_dependencies.git
cd ~/catkin_ws && catkin_make
```

U2D2のセットアップ

```
roscore
rosrun open_manipulator_controller create_udev_rules
```

## ROSのserviceを用いて操作

```
roslaunch open_manipulator_controller open_manipulator_controller.launch
rosrun open_manipulator_examples service_call.py
```