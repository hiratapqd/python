#!/usr/bin/python
import vm_include

def main():
    #change these to match your installation
    host="vcenter.solvesystem.intranet"
    user="sergio.hirata"
    pw="YT!#))0118"

    #connect to the host
#    hostcon=vm_include.connectToHost(host,user,pw)

def connectToHost(host,host_user,host_pw):
    #create server object
    s=VIServer()
    #connect to the host
    try:
        s.connect(host,host_user,host_pw)
        return s
    except VIApiException:
        print ("Cannot connect to host: ")+host+(" error message: ")+err
    #list server type
    print ("Type:"),hostcon.get_server_type()

    #disconnect from the host
    hostcon.disconnect()

#if __name__ == '__main__':
#        main()
connectToHost("vcenter.solvesystem.intranet","sergio.hirata","YT!#))0118")
