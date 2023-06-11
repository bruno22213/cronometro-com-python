import time

def countDown(t):
    while t:
        min, sec =divmod(t,60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end ='\r')
        time.sleep(1)
        t -=  1
print ('cronometro')

t = input('coloque a quantidade de segundos:')

countDown(int(t))