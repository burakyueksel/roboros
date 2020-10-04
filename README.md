# README #

This repository contains the SW of ROBO as a ROS package.

Admin of this repository and the author: Burak Y\"uksel

### What is this repository for? ###

* TBD

### How do I get set up? ###

* You have ROS [installed](http://wiki.ros.org/noetic/Installation/Ubuntu)
* See the ROS [tutorials] (http://wiki.ros.org/ROS/Tutorials) for more.
* Create your workspace and set it up [catkin_ws](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
* in your ~\.bashrc you have
```js
source /opt/ros/<ROS-DISTRO>/setup.bash
source ~/catkin_ws/devel/setup.bash
```
* Clone this repository under the following folder
```console
$ ~/catkin_ws/src
$ git clone https://burakyuksel@bitbucket.org/burakyuksel/roboros.git
```
* Build the package
```console
$ ~/catkin_ws
$ catkin_make
```

### Test your build ###

#### Using roslaunch

* Simply go to the launch file and rund it
```console
$ roscd roboros/launch
$ roslaunch testSend.launch
```
* You can listen to the published topics from either nodes, in separated terminals
```console
$ rostopic echo /cppTestChatter
```
or
```console
$ rostopic echo /pyTestChatter
```

#### Using rosrun

* In a terminal run
```console
$ roscore
```
* For testing the cpp sender test node, in another terminal run
```console
$ rosrun roboros cppTestSend
```
* For testing the py sender test node, in another terminal run
```console
$ rosrun roboros pyTestSend
```
* You can also listen to the published topics from either nodes, in separated terminals
```console
$ rostopic echo /cppTestChatter
```
or
```console
$ rostopic echo /pyTestChatter
```


### Contribution guidelines ###

* TBD

### Who do I talk to? ###

* Burak Y\"uksel