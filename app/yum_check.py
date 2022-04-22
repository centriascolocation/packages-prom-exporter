import os

def packages():
    list_upgrades = ""
    list_security = ""
    upgrades = 0
    security_updates = 0
    list_upgrades = os.popen('yum check-update -q|egrep -v "Loaded plugins: langpacks, product-id, subscription-manager|^$"|wc -l').read()
    list_security = os.popen('yum check-update --security -q|egrep -v "Loaded plugins: langpacks, product-id, subscription-manager|^$"|wc -l').read()
    upgrades = list_upgrades
    security_updates = list_security
    return (upgrades, security_updates)