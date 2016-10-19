# ovs_docker_net
A simple tool to create Docker network based on Open vSwitch.
### Environment requirements:

 - ubuntu 14.04
 - Docker 1.12.1
 - Open vSwitch 2.6.90
 - python 2.7.6

### Tutorial

 - Create an ovs docker network
**First**, you have to define your network in ```odn/settings.py```.
**Then**, you can create your network using the following commands:
```
    $ cd ovs_docker_net
    $ sudo python odn/odn.py
```
 - Clear the network you just created
You can use the following command to clear the network you just created:
```
    $ sudo python odn/clear.py
```
