from mininet.topo import Topo

class Testtopo(Topo):
	def __init__(self):
		
		Topo.__init__(self)

		S1=self.addSwitch('s1')
		S2=self.addSwitch('s2')
		H1=self.addHost('h1')
		H2=self.addHost('h2')
		H3=self.addHost('h3')
		H4=self.addHost('h4')

		self.addLink(S1,S2)
		self.addLink(S1,H1)
		self.addLink(S1,H2)
		self.addLink(S2,H3)
		self.addLink(S2,H4)
topos={
	'topo':(lambda: Testtopo())
}

