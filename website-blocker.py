import time
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
            content= file.read()
            for  website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+"\n")

    else:
        print('Not working hours')
    time.sleep(5) #code will run after every 5 sec