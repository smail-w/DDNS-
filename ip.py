import socket
import io
import sys
import os
import subprocess
def get_ip_list(domain): # 获取域名解析出的IP列表
  ip_list = []
  try:
    addrs = socket.getaddrinfo(domain, None)
    for item in addrs:
      if item[4][0] not in ip_list:
        ip_list.append(item[4][0])
  except Exception as e:
    # print(str(e))
    pass
  return ip_list

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径

	else:
		print ("---  There is this folder!  ---")

		
file = "DDNS"
mkdir(file)             #调用函数

inputip = str(sys.argv[1])

file = open('./DDNS/%s' % inputip,'a+')
file.seek(0, 0)    #移动文件指针到0
fileip = file.read()


ip = get_ip_list(str(inputip))
ip_str=''.join(ip)
print(ip_str,"新IP")
print(fileip,"文件储存IP")

if (fileip == ip_str):
	print("IP未作改变")
	file.close()
	sys.exit(0)
else:
	print("DDNS已刷新")

fp = open('./DDNS/%s' % inputip,'w+')
fp.write(ip_str)
fp.close()
sys.exit(0)
