import RPi.GPIO as GPIO
import time
import smtplib
import time
import getpass

print ('Tavoite on 5 sec')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
count = 0
valo = 0
lähettäjä = input('lähettäjä. ')
vastaanottaja = input('vastaanottaja: ')
salasana = getpass.getpass('salasana: ')
x = input('Anna aika: ' )
aika = int(x)
print('LED päällä')
start = time.time()
while count < aika:
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    count +=1
end = time.time()
time.sleep(1)
GPIO.output(23,GPIO.LOW)
print('LED pois')
elapsed = end - start
print (elapsed)
time.sleep(1)
if count == 5:
    print (count, 'sec \n','Onnistuit')
    while valo <10:
        GPIO.output(25,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.1)
        valo +=1
    fromaddr = (lähettäjä)
    toaddrs = (vastaanottaja)
    msg = 'Onnistuit!!' + str(elapsed) + 'sec'
    username = (lähettäjä)
    password = (salasana)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
else:
    print (count, 'sec \n','Et Onnistunut')
    while valo <10:
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(23,GPIO.LOW)
        time.sleep(0.1)
        valo +=1
    fromaddr = (lähettäjä)
    toaddrs = (vastaanottaja)
    msg = 'Oho, et onnistunut!!' + str(elapsed) + 'sec'
    username = (lähettäjä)
    password = (salasana)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
