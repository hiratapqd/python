import win32security
import ntsecuritycon as con

#FILENAME = "whatever.txt"
FILENAME=input('Digite o nome do arquivo :')
user1 = input('digite o nome do usuario :')
userx, domain, type = win32security.LookupAccountName ("", user1)
sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)
dacl = sd.GetSecurityDescriptorDacl()



aysha= input('Qual a permissao? r, rw, full :')

if aysha=='r':
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ, userx)
elif aysha=='rw':
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_GENERIC_READ | con.FILE_GENERIC_WRITE, userx)
elif aysha=='full':
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, userx)
else:
    print('favor digitar uma permissao')

sd.SetSecurityDescriptorDacl(1, dacl, 0)   #
win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)

print('permissao alterada')
