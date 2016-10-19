#!/usr/bin/env python

from settings import switches, hosts
from commands import getstatusoutput

def execcmd(cmd, errinfo):
	(status, output) = getstatusoutput(cmd)
	if status:
		print errinfo, ", command: ",cmd, ", errorinfo: ", output
		sys.exit(0)
	return (status, output)

if hosts:
	print "Removing hosts:"
	for h in hosts:
		cmd = "".join(["docker stop ", h, " && docker rm ", h])
		execcmd(cmd, "Error while removing hosts")
		print h
	print "Finished to remove hosts\n"

if switches:
	print "Removing switches:"
	print "hello"
	for s in switches:
		cmd = "".join(["ovs-vsctl del-br ", s])
		execcmd(cmd, "Error while removing switches")
	print "Finished to remove switches\n"

print "Successfully clear the ovs docker network!\n"
