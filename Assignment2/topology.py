#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
import sys
from mininet.node import Controller, RemoteController
from mininet.cli import CLI

class create_Topology(Topo):
	def build(self, n = 2, N = 4):
		for i in range(n):
			switch = self.addSwitch('s%s'%(i+1))
			for j in range(i):
				self.addLink(switch, ('s%s'%(1+j)))
		ratio = N/n
		remaining = N%n
		I = 1
		for i in range(n):
			switch = ('s%s'%(i+1))
			for j in range(ratio):
				host = self.addHost('h%s'%I)
				self.addLink(host, switch)
				I += 1
		for i in range(remaining):
			host = self.addHost('h%s'%I)
			self.addLink(host, ('s%s'%(i+1)))
			I += 1

if __name__ == '__main__':
	setLogLevel('info')
	nswitches = int(sys.argv[1])
	nhosts = int(sys.argv[2])
	net = Mininet(topo=create_Topology(nswitches, nhosts), controller=RemoteController)
	net.start()
	net.addController('c0',controller=RemoteController, ip='127.0.0.1', port=6633)
	for x in xrange(nhosts):
		for y in xrange(nhosts):
			if x%2==0 and y%2==1:
				net.nameToNode["h"+str(x+1)].cmd("iptables -A OUTPUT -o h"+str(x+1)+"-eth0 -d 10.0.0."+ str(y+1)+" -j DROP")
	dumpNodeConnections(net.switches)
	CLI(net)
	net.stop()