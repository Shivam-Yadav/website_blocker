__author__ = 'Shivam'
import time
from datetime import datetime as dt #import datetime method from datetime module
                                    #dt=datetime.datetime

hosts_path=r"C:\Windows\System32\drivers\etc\hosts" #telling python that its a row to avoid '\n' type case
#hosts_temp="hosts"

redirect="127.0.0.1"
website_list=["www.facebook.com","cyro.se","kissanime.io","facebook.com"]

while(1):
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,11):
         print("working time")
         with open(hosts_path,'r+') as file:
             content=file.read()               #loads the entire file contents as a string in variable content
             for website in website_list:
                 if website in content:
                     pass                        #passes to other statement
                 else:
                     file.write(redirect+"  " +website+ "\n")

    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("awesome")
    time.sleep(5)