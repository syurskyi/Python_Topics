import paramiko

hostname = "127.0.0.1"
username = "phil"
passwd = "pythoncode"
port = 22
src = "/home/phil/install.deb"
sav = "/tmp/install-download.deb"
upl = "/tmp/install-upload.deb"

try:
    p = paramiko.Transport((hostname,port))
    p.connect(username=username,password=passwd)
    print("[*] Connected to " + hostname + "via SSH")
    sftp = paramiko.SFTPClient.from_transport(p)
    print("[*] Starting file download")
    sftp.get(src,sav)
    print("[*] File download complete")
    print("[*] Starting file upload")
    sftp.put(src,upl)
    print("[*] File upload complete")
    p.close()
    print("[*] Disconnected from server")

except Exception as err:
    print("[!] " +str(err))