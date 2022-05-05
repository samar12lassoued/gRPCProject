#!/usr/bin/env python
# -*- coding: utf-8 -*-

# write_bit
# write 4 bits to True, wait 2s, write False, restart...

import grpc
from lib import mqtt_pb2
from lib import mqtt_pb2_grpc
from lib import Config_pb2
from lib import Config_pb2_grpc
from pyModbusTCP.client import ModbusClient
import time
import logging 

logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(message)s')

class Modbus_Config():
    def run():
        global server_host,server_port
        with grpc.insecure_channel('localhost:50052') as channel :
            Config_pb2_grpc.ConfigManagerStub(channel)
            Conf_stub= Config_pb2_grpc.ConfigManagerStub(channel)
            logging.info("What's the protocol Name?\nPlease type Mqtt or ModbusTCP")
            Protocolname1=input()
            Protocolname2=Protocolname1.upper()
            Parameters= Conf_stub.getConfig(Config_pb2.Protocolrequest(Protocolname=Protocolname2))
            server_host=Parameters.__getattribute__('adresse')
            server_port=Parameters.__getattribute__('Port')
        logging.info('Configuration Parameters are {}:{}'.format(server_host,server_port))
        return Parameters


#SERVER_HOST = "localhost"
#SERVER_PORT = 502
c=ModbusClient()
Parameters=Modbus_Config.run()
server_host=Parameters.__getattribute__('adresse')
server_port=Parameters.__getattribute__('Port')

# uncomment this line to see debug message
#c.debug(True)

# define modbus server host, port
c.host(server_host )
c.port(server_port)
print('client connected to the ModBus server')
#toggle = True




#while True:
    # open or reconnect TCP to server
if not c.is_open():
    if not c.open():
        print("unable to connect to "+server_host+":"+str(server_port))

    # if open() is ok, write coils (modbus function 0x01)
if c.is_open():
        # write 4 bits in modbus address 0 to 3
        print("")
        print("write bits")
        print("----------")
        print("")
        #for addr in range(4):
            
        is_ok = c.write_single_coil(0,True)
        if is_ok:
            print("bit #" + str(0) + ": write to " + str(True))
        else:
            print("bit #" + str(0) + ": unable to write " + str(True))
            time.sleep(0.5)

        time.sleep(1)

        print("")
        print("read bits")
        print("---------")
        print("")
        bits = c.read_coils(0, 1)
        if bits:
            print("bits #0 : "+str(True))
        else:
            print("unable to read")
        

    #toggle = not toggle

    # sleep 2s before next polling
time.sleep(2)
def run():
    with grpc.insecure_channel('localhost:50051') as channel :
        mqtt_pb2_grpc.MQTTManagerStub(channel)
        stub= mqtt_pb2_grpc.MQTTManagerStub(channel)
        print('Donner Topic')
        topic2=input()
        #print('Donner Payload')
        #payload2=input()
        #print('Donner Qos')
        #qos2=input()
        Acknowledgment= stub.PublishMessages(mqtt_pb2.ComingData(Topic=topic2,Payload=str(bits)))
        print(Acknowledgment)



run()
