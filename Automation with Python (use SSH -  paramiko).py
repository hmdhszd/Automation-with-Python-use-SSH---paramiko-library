import paramiko
import time

host = "124.158.236.3"
port = 22
username = "lg"
password = "lg"




ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password,allow_agent=False,look_for_keys=False)
connection = ssh.invoke_shell()

connection.send('ping 1.1.1.1 \n')
time.sleep(2)

connection.send('show ip bgp 194.156.140.0 best \n')
time.sleep(2)


out = connection.recv(9999)
print(out.decode("ascii"))



ssh.close() 

