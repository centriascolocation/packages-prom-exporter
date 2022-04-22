import os
import platform
import sys

from sys import platform



def _get_manager():

   if platform == "linux" or platform == "linux2":
      if os.path.exists('/usr/bin/apt-get'):
         return 'apt'
      elif os.path.exists('/usr/bin/yum'):
           return 'yum'
   elif platform == "darwin":
        return "MacOS"
   elif platform == "win32":
        return ("Lauf weg")

def checkupdates():

    if _get_manager() == "yum":
        import yum_check
        return yum_check.packages()
    if _get_manager() == "apt":
        import apt_check
        from collections import namedtuple
        Options = namedtuple('Options', ['security_updates_unattended', 'show_package_names', 'readable_output'])
        options = Options(False, False, False)
        (num_updates, num_security_updates) = apt_check.run(options)
        return num_updates, num_security_updates
