from builtins import *

import atexit

from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim


host="vcenter.solvesystem.intranet"
user="svc_ldap@solvesystem.intranet"
password="W0rking@)!%"
port=443
l=[]

# If you use self signed certificates Python will not connect.
# This will give you an error for the check, but continues.
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    print ("There was an error with the SSL certificates. Continuing..")
    ssl._create_default_https_context = _create_unverified_https_context

def main():
    try:
        service_instance = connect.SmartConnect(host=host,
                                                user=user,
                                                pwd=password,
                                                port=port)

        # What to do when exiting
        atexit.register(connect.Disconnect, service_instance)


        content = service_instance.RetrieveContent()

        container = content.rootFolder  # starting point to look into
        viewType = [vim.VirtualMachine]  # object types to look for
        recursive = True  # whether we should look into it recursively

        # Create a view
        containerView = content.viewManager.CreateContainerView(
            container, viewType, recursive)

        # Loop through all obhects to return name and VMware tools version
        children = containerView.view
        for child in children:
            if child.summary.guest is not None:
                try:
                    #power_state=child.summary.guest.power_state
                    tools_version = child.summary.guest.toolsStatus
                    l.append(child.name)
#                    print("VM: {}, VMware-tools: {}, power_state: {}".format(child.name, tools_version,power_state))
                    print("VM: {}, VMware-tools: {}".format(child.name, tools_version))
                except:
                    print("Vmware-tools: None")

    except vmodl.MethodFault as error:
        print("Caught vmodl fault : " + error.msg)
        return -1
    print ("There are " + str(len(l))+ " VMs" + " in the Vcenter: " + host)
    return 0
# Start program
if __name__ == "__main__":
    main()
