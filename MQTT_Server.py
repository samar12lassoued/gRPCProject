
import grpc
import mqtt_pb2
import mqtt_pb2_grpc
import Config_pb2
import Config_pb2_grpc
import paho.mqtt.client as mqtt
from concurrent import futures
import time
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(message)s')

connack_rc=-1

# The Callback function that determines if the client connected
# to the Mosquitto Broker and returns the Return Code(rc)
def onconnect(client,userdata,flag,rc):
    global connack_rc
    if  rc==0:
        logging.debug('Client Connnected OK ')
        connack_rc=rc
        
    elif rc==1:
        logging.debug('Connection Refused :incorrect protocol version ')
        connack_rc=rc
    elif rc==2:
        logging.debug('Connection refused:bad client id')
        connack_rc=rc
    elif rc==3:
        logging.debug('Connection refused:Server unvailable')
        connack_rc=rc
    elif rc==4:
        logging.debug('Connection refused:bad username or password')
        connack_rc=rc
    else :
        logging.debug('Connection refused:not authorized')
        connack_rc=rc
    return(rc)



#Global variable that contains the MQTT Configuration Parameters 
Parameters2= Config_pb2.ProtocolConfig()


#this Side implements the MQTTServer as a client for the ConfigManager 
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


#This Side implements the MQTT Server as a server for the ModBusClient 
class MQTTManagerServicer(mqtt_pb2_grpc.MQTTManagerServicer):
    def PublishMessages(self,request,context):
        topic1=request.Topic
        payload1=request.Payload
        qos1=request.Qos
       
        if connack_rc==0:

            Mqttclient.publish(topic=topic1,payload=payload1)
            status=Mqttclient.publish(topic=topic1,payload=payload1)
            if status.rc==0:
                logging.debug("Publish Sucess")

                ACKK=mqtt_pb2.Publish_Success     
                
            else:
                logging.debug("Publish Failed")
                ACKK=mqtt_pb2.PublishFailed
                
               
        elif connack_rc==1:
            logging.debug('Connection Refused :incorrect protocol version ')
            ACKK=mqtt_pb2.Incorrect_Proto_Version

        elif connack_rc==2:
            logging.debug('Connection refused:bad client id')
            ACKK=mqtt_pb2.Bad_Client_ID

        elif connack_rc==3:
            logging.debug('Connection refused:Server unvailable')
            ACKK=mqtt_pb2.Server_Unvailable

        elif connack_rc==4:
            logging.debug('Connection refused:bad username or password')
            ACKK=mqtt_pb2.Bad_User_Pw

        else :
            logging.debug('Connection refused:not authorized')
            ACKK=mqtt_pb2.Not_AUTH
            
            
              
        logging.debug("The server is still waiting for Upcoming Data ")
        return mqtt_pb2.ReturnType(Acknowledgment=ACKK)
    

def main():

    server =grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    mqtt_pb2_grpc.add_MQTTManagerServicer_to_server(MQTTManagerServicer(),server)
    logging.debug("The server is Starting !")
    logging.debug('Connecting to the Mosquitto Broker .....')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


#Getting the Connection parameters from the Config Server
Parameters=Clientrun.run()
Parameters2=Parameters
c=Parameters.__getattribute__('adresse')
c1=Parameters.__getattribute__('Port')

#Creating the MqttClient and starting the process of connection   

Mqttclient= mqtt.Client("grpc",clean_session=False)
Mqttclient.on_connect=onconnect

Mqttclient.loop_start()

Mqttclient.connect(c,c1)


main()

