#!/usr/bin/env python2

import socket
import configparser
import datetime
import xmlrpclib

def Main():

    shutdown = False
    today = datetime.datetime.now()

    config = configparser.ConfigParser()
    config.read('server.cfg')

    log = open("test_server.log" , "a")
   
    host = config['DEFAULT']['host'] #Server ip
    port = int(config['DEFAULT']['port'])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print(today.strftime("%c") + " fm_server starting on port " + str(port))
    log.write(today.strftime("%c") + " fm_server starting on port " + str(port)+ "\n")

    s1 = xmlrpclib.Server('http://localhost:8080')
    #s1.set_cent_freq(94700000)
    while not shutdown:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message from: " + str(addr))
        log.write("Message from: " + str(addr) + "\n")
        print("From connected user: " + data)
        log.write("From connected user: " + data + "\n")

        holder = data.split(" ")

        if holder[0]=="Tune":
            s1.set_cent_freq(float(holder[1].strip())*1000000)
            print("tune")
        elif holder[0]=="Pause":
            #pause
            s1.set_volume(0)
            print("pause")
        elif holder[0] == "Play":
            s1.set_volume(1)
            print("play")
        elif holder[0] == "Gain":
            s1.set_rx_gain(int(holder[1].strip()))
            print("gain")
        elif holder[0]=="Shutdown":
            shutdown = True
            #finish
            print("test")


        data = data.upper()
        print("Sending: " + data)
        log.write("Sending: " + data + "\n")
        s.sendto(data.encode('utf-8'), addr)
    s.close()
    log.close()

if __name__=='__main__':
    Main()