
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from telnetlib import RCP
import grpc
import mqtt_pb2
import mqtt_pb2_grpc
import paho.mqtt.client as mqtt
from concurrent import futures
import time
import Config_pb2
import Config_pb2_grpc

global ACKK 
#ss=mqtt_pb2.enum_type_wrapper.EnumTypeWrapper.Name()

def onconnect(client,userdata,flags,rc):
   
    if  rc==0:
        print('client connnected OK')
        return(rc)
    elif rc==1:
        print('Connection Refused :incorrect protocol version ')
        return(rc)
    elif rc==2:
        print('Connection refused:bad client id')
        return(rc)
    elif rc==3:
        print('Connection refused:Server unvailable')
        return(rc)
    elif rc==4:
        print('Connection refused:bad username or password')
        return(rc)
    else :
        print('Connection refussed:not authorized')
        return(rc)



#Global variable that contains the MQTT Configuration Parameters 
Parameters2= Config_pb2.ProtocolConfig()

#ACKK=mqtt_pb2.Bad_Client_ID


#this side implements the MQTTServer as a client for the ConfigManager 
class Clientrun():
    def run():
        with grpc.insecure_channel('localhost:50052') as channel :
            Config_pb2_grpc.ConfigManagerStub(channel)
            stub= Config_pb2_grpc.ConfigManagerStub(channel)
            print("What's the protocol Name?\nPlease type Mqtt or ModbusTCP")
            Protocolname1=input()
            Protocolname2=Protocolname1.upper()
            Parameters= stub.getConfig(Config_pb2.Protocolrequest(Protocolname=Protocolname2))
        
        print(Parameters)
        return Parameters


#This side implements the MQTT Server as a server for the ModBusClient 
class MQTTManagerServicer(mqtt_pb2_grpc.MQTTManagerServicer):
    def PublishMessages(self,request,context):
        topic1=request.Topic
        payload1=request.Payload
        qos1=request.Qos
        print('Connecting to the Mosquitto Broker .....')

        rrc=onconnect(Mqttclient._client_id,Mqttclient._userdata,True,rc=0)
       
        if rrc==0:
            
            Mqttclient.publish(topic=topic1,payload=payload1)
            status=Mqttclient.publish(topic=topic1,payload=payload1)
            if status.rc==0:
                print("publish success")
                ACKK=mqtt_pb2.PublishSuccess
                
            else:
                print("publish failed")
                ACKK=mqtt_pb2.PublishFailed
               
        else:
            
            print('Publish failed')
            ACKK=mqtt_pb2.PublishFailed
            
              
        print("The server is still waiting for Upcoming Data ")
        return mqtt_pb2.ReturnType(Acknowledgment=ACKK)
    

def main():

    server =grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    mqtt_pb2_grpc.add_MQTTManagerServicer_to_server(MQTTManagerServicer(),server)
    print("The server is Starting !")
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


#Getting the connection parameters from the Config Server

Parameters=Clientrun.run()
Parameters2=Parameters
c=Parameters.__getattribute__('adresse')
c1=Parameters.__getattribute__('Port')

   

Mqttclient= mqtt.Client("grpc",clean_session=False)
Mqttclient.on_connect=onconnect
Mqttclient.connect(c,c1)

main()
