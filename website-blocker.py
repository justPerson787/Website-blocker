import time
print('start')
from datetime import datetime as dt
hosts_temp = "hosts" #temp copy  of hosts file for practice
hosts_path = 'C:\Windows\System32\Drivers\etc\hosts' #access to hosts file
redirect = '127.0.0.1' #where browser will be redirected
website_list = ['www.facebook.com', 'facebook.com', 'www.1tv.ru', '1tv.ru']#websites to block

while True:
    #the if condition checks if it is working time now
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        # add undesired websites into hosts file unless they are already there
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for  website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+"\n")
        print('W hours')

    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines() #produces a list of lines 
            file.seek(0) #place the coursor just before the first character of the file content
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate() #this method removes everything after that
        print('Not working hours')
    time.sleep(300) #code will run after every 300 sec