#!/usr/bin/env python
import os, sys
bbuStatus = os.popen("hpssacli controller all show config detail | grep -E '(Battery/Capacitor Status)' | awk {'print $3'}").readline().strip()
if bbuStatus == "OK":
   print "BBU RAID OK - Current status - %s." % bbuStatus
   sys.exit(0)
elif bbuStatus == "Recharging":
   print "BBU RAID WARNING - Current status - %s." % bbuStatus
   sys.exit(1)
else:
   print "BBU RAID CRITICAL - Current status - %s." % bbuStatus
   sys.exit(2)
