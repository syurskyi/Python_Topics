
______ os, re, _

class ip_check(_.?):
   ___ __init__ (self,ip):
      _.?.__init__(self)
      self.ip = ip
      self.__successful_pings = -1
   ___ run(self):
      ping_out = os.popen("ping -q -c2 "+self.ip,"r")
      w___ True:
        line = ping_out.readline()
        if not line: break
        n_received = re.findall(received_packages,line)
        if n_received:
           self.__successful_pings = int(n_received[0])
   ___ status(self):
      if self.__successful_pings == 0:
         r_ "no response"
      elif self.__successful_pings == 1:
         r_ "alive, but 50 % package loss"
      elif self.__successful_pings == 2:
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
   el.join()
   print "Status from ", el.ip,"is",el.status()
   
