______ os, re

received_packages = re.compile(r"(\d) received")
status = ("no response","alive but losses","alive")

___ suffix __ r.. 20,30):
   ip = "192.168.178."+s..(suffix)
   ping_out = os.popen("ping -q -c2 "+ip,"r")
   print "... pinging ",ip
   w___ True:
      line = ping_out.readline()
      __ n.. line: break
      n_received = received_packages.findall(line)
      __ n_received:
         print ip + ": " + status[in.(n_received[0])]
         
