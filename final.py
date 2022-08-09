import socket

file = open('/Users/aalbert/Desktop/python/ips.txt', 'r').readlines()
file_set = set(file)


file_no_duplicate = open ('noduplicateips.txt', 'w')

for i in file_set:
    file_no_duplicate.write(i)
file_no_duplicate.close()    

ips = open('/Users/aalbert/Desktop/python/noduplicateips.txt', 'r')

ip_list = []

for x in ips.readlines():

    ip_list.append(x.rstrip()) 
    
file = open ('google.txt', 'w')
file2 = open ('yandex.txt', 'w')
file3 = open ('msn.txt', 'w')

for y in ip_list:
    try: 
      reversed_dns = socket.gethostbyaddr(y)
      if str.__contains__(reversed_dns[0], 'googlebot.com') or str.__contains__(reversed_dns[0], 'google.com'):
        temp_ip = socket.gethostbyaddr(str(reversed_dns[2]).strip("'[]'"))
        if reversed_dns == temp_ip:
           print(y , '-->',  socket.gethostbyaddr(y), '\n')
           file.write(y+ '-->' + str(socket.gethostbyaddr(y)) + '\n')
      elif str.__contains__(reversed_dns[0], 'yandex.com') or str.__contains__(reversed_dns[0], 'yandex.net') or str.__contains__(reversed_dns[0], 'yandex.ru'):  
         temp_ip = socket.gethostbyaddr(str(reversed_dns[2]).strip("'[]'"))
         if reversed_dns == temp_ip:
           print(y , '-->',  socket.gethostbyaddr(y), '\n')
           file2.write(y+ '-->' + str(socket.gethostbyaddr(y)) + '\n')
      elif str.__contains__(reversed_dns[0], 'search.msn.com'):
         temp_ip = socket.gethostbyaddr(str(reversed_dns[2]).strip("'[]'"))
         if reversed_dns == temp_ip: 
           print(y , '-->',  socket.gethostbyaddr(y), '\n')
           file3.write(y+ '-->' + str(socket.gethostbyaddr(y)) + '\n')    
    except socket.herror:
        pass     
file.close()    
file2.close()
file3.close()