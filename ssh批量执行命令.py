 1 # python3.5 + paramiko
 2 # pip 是python的包管理工具，在shell里执行如下命令安装paramoko模块
 3 # pip install paramiko
 4 #
 5 
 6 import paramiko
 7 
 8 def ssh_bat_cmd(ip, port,username,password,command):
 9     ssh = paramiko.SSHClient()
10     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
11     # ssh.connect("172.16.2.10", 22, "root", "123123")
12     ssh.connect(ip, port, username, password)   # 注意这里的IP 用户名 密码都是字符串
13     #stdin, stdout, stderr = ssh.exec_command(command)
14     stdin, stdout, stderr = ssh.exec_command(command) #注意这里的command 是字符串
15 
16     stdout_info = stdout.readlines()
17     err_info = stderr.readlines()
18     if err_info:
19         print("{} is failed: {}".format(ip,err_info))
20     else:
21         print("{} is successful: {}".format(ip, stdout_info))
22     ssh.close()
23 
24 IP_dic  = {
25     #    "IP":[port,"username","password"],
26     "1.1.1.2":[22,"username","password"],
27     "1.1.1.3":[22,"username","password"],
28     "1.1.1.4":[22,"username","password"],
29 }
30 
31 for ip in IP_dic:
32     ssh_bat_cmd(ip, IP_dic[ip][0], IP_dic[ip][1], IP_dic[ip][2], """  df -Th   """)