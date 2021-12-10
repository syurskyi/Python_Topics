
______ os, re, _

c_ ip_check(_.?):
   ___ -  ip):
      _.?.- (self)
      ip = ip
      __successful_pings = -1
   ___ run
      ping_out = os.popen("ping -q -c2 "+ip,"r")
      w___ True:
        line = ping_out.readline()
        __ n.. line: break
        n_received = re.findall(received_packages,line)
        __ n_received:
           __successful_pings = int(n_received[0])
   ___ status
      __ __successful_pings == 0:
         r_ "no response"
      elif __successful_pings == 1:
         r_ "alive, but 50 % package loss"
      elif __successful_pings == 2:
         r_ "alive"
      else:
         r_ "shouldn't occur"
received_packages = re.compile(r"(\d) received")

check_results   # list
___ suffix __ r.. 20,70):
   ip = "192.168.178."+s..(suffix)
   current = ip_check(ip)
   check_results.a.. (current)
   current.s..

___ el __ check_results:
   el.j..
   print "Status from ", el.ip,"is",el.status()
   
