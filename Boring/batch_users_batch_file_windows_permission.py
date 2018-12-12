import win32security
import ntsecuritycon as con
import csv
import pandas as pd

#FILENAME='whatever.txt'
PERMFILE=input('Digite o nome e o caminho do arquivo de permissoes:')
df = pd.read_csv(PERMFILE, delimiter=',')
tuples = [tuple(x) for x in df.values]
#print(tuples)
#print (len(tuples))
list_x=[x for x,_,_ in tuples]
list_y=[y for _,y,_ in tuples]
list_z=[z for _,_,z in tuples]

i=0
while i < len(tuples):
    FILENAME=list_z[i]
    sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)
    dacl = sd.GetSecurityDescriptorDacl()   # instead of dacl = win32security.ACL()
    user1=list_x[i]
#    print (user1)
    userx, domain, type = win32security.LookupAccountName ("", user1)
    aysha=list_y[i]
#    print (aysha)
    if aysha=='r':
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ, userx)
#        print("read")
    elif aysha=='rw':
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE, userx)
#        print("read_write")
    elif aysha=='full':
        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, userx)
#        print('full access')
    else:
        print('favor digitar uma permissao')

    sd.SetSecurityDescriptorDacl(1, dacl, 0)   # may not be necessary
    win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)

    i+=1
#print (userx)
print("permissoes executadas ",PERMFILE)
