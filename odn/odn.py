#!/usr/bin/env python

from settings import *
from commands import getstatusoutput
import sys

def execcmd(cmd, errinfo):
	(status, output) = getstatusoutput(cmd)
	if status:
		print errinfo, ", command: ",cmd, ", errorinfo: ", output
		sys.exit(0)
	return (status, output)

if switches:
	print "Creating switches:"
	errinfo = "Error while creating switches"
	for s in switches:
		cmd = "".join(["ovs-vsctl add-br ", s])
		execcmd(cmd,  errinfo)
		print s
	print "Finished to create switches\n"

if controllers:
	print "Setting controllers: "
	errinfo = "Error while setting controllers"
	for s in controllers:
		cmd = "".join(["ovs-vsctl set-controller ", s, " ", controllers[s]])
		execcmd(cmd, errinfo)
		print "set controller: ", s, "-->", controllers[s]
	print "Finished to set controllers\n"

ID = {}
if hosts:
	print "Creating hosts:"
	errinfo = "Error while creating hosts"
	for h in hosts:
		cmd = "".join(["docker run --net=none --privileged=true --name=", h, " -it -d ", img, " /bin/bash"])
		(status, output) = execcmd(cmd, errinfo)
		ID[h] = output
		print h
	print "Finished to create hosts\n"

if links_ss:
	print "Creating links between switches:"
	errinfo = "Error while creating links between switches"
	for link in links_ss:
		patch1 = "".join(["patch_", link[0], "_to_", link[1]])
		patch2 = "".join(["patch_", link[1], "_to_", link[0]])
		
		cmd = "".join(["ovs-vsctl add-port ", link[0], " ", patch1])
		execcmd(cmd, errinfo)
		cmd = "".join(["ovs-vsctl add-port ", link[1], " ", patch2])
		execcmd(cmd, errinfo)

		cmd = "".join(["ovs-vsctl set interface ", patch1, " type=patch"])
		execcmd(cmd, errinfo)
		cmd = "".join(["ovs-vsctl set interface ", patch1, " options:peer=", patch2])
		execcmd(cmd, errinfo)
		cmd = "".join(["ovs-vsctl set interface ", patch2, " type=patch"])
		execcmd(cmd, errinfo)
		cmd = "".join(["ovs-vsctl set interface ", patch2, " options:peer=", patch1])
		execcmd(cmd, errinfo)
		print link[0], "<-->", link[1]
	print "Finished to create links between switches\n"

if links_sh:
	print "Creating links between switches and hosts:"
	errinfo = "Error while creating links between switches and hosts"
	for link in links_sh:
		(s, h) = link
		print s, h
		cmd = "".join(["ovs-docker add-port ", s, " eth0 ", ID[h]])
		execcmd(cmd, errinfo)
		cmd = "".join(["docker exec ", h, " ifconfig eth0 ", hosts[h]])
		execcmd(cmd, errinfo)
		print s, "<-->", h
	print "Finished to create links between switches and hosts\n"

print "Successfully create the ovs docker network!\n"
