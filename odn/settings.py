# Define switches(OVS bridges) and specify the SDN controllers
# The format is like:
#	switches = ["s1", "s2" ,]
#	controllers = {
#		"s1": "tcp:192.168.106.226:6653",
#		"s2": "tcp:192.168.106.226:6653",
#	}

switches = ["s1",]
controllers = {
	"s1": "tcp:192.168.106.226:6653",
}


# Define hosts(Docker containers)
# The format is like:
# 	hosts = {
#		"h1": "192.168.107.101/24",
#		"h2": "192.168.108.101/24",
#	}

img = "ubuntu:14.04"
hosts = {
	"h1": "192.168.107.101/24",
	"h2": "192.168.107.102/24",
}


# Define the links between switches
# The format is like:
#	links_ss = [("s1", "s2"), ("s3", "s4"),]

links_ss = []


#Define the links between hosts and switches
# The format is like:
#	links_sh = [("s1", "h1"), ("s2", "h2"),]

links_sh = [("s1", "h1"), ("s1", "h2"),]
