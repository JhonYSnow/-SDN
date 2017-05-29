cd /usr/local/lib/python2.7/dist-packages/ryu/app/
ryu-manager ofctl_rest.py simple_switch_13.py

sudo mn --custom=my_topo.py --topo topo --switch ovs,protocols=OpenFlow13 --controller=remote,ip=127.0.0.1 --mac


