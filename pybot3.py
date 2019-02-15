import sys
import time
import random
import tempfile
import string

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben
#download, getting batch script files, installing system monitoring software, accessing all file types

last=0
print("System access is successful.")
time.sleep(1)
print("PROJECT INVADER has started.")
time.sleep(1)
count=0
while(count!=101):
            progress(count,100,'Initializing')
            count=count+1
            if(count<10):
                time.sleep(1)
            elif(count>20):
                time.sleep(random.uniform(0.01, 0.09))
            else:
                time.sleep(random.uniform(0.1,0.9))
count1=0
while(count1!=-1):
    time.sleep(0.1)
    a=random.randint(0,6)
    if(a==0):
        if (last == a):
            continue
        tf = tempfile.NamedTemporaryFile()
        print("Getting batch script file from "+tf.name)
    elif(a==1):
        if(a==last):
            continue
        count=0
        while(count!=101):
            progress(count,100,'Downloading and installing necessary resources')
            count=count+1
            time.sleep(0.1)
        print("")
    elif(a==2):
        if (a == last):
            continue
        print("Updating central system files...")
    elif(a==3):
        if (a == last):
            continue
        print("Granting global network access from this computer...")
    elif(a==4):
        if (a == last):
            continue
        print("Reconfiguring system data and assignments.")
    elif (a == 5):
        if (a == last):
            continue
        z=random.randint(64,128)
        x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(z))
        y = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(z))
        print("Encrypting C:/system/"+str(x)+"/"+str(y))
    else:
        if (a == last):
            continue
        print("Accessing admin protected files and uninstalling security softwares....")
    last = a