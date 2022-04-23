
import grpc
import MQTT_pb2_grpc
import MQTT_pb2
import paho.mqtt.client as mqtt
from concurrent import futures
import time
import Config_pb2
import Config_pb2_grpc


#Global variable that contains the MQTT Configuration Parameters 
Parameters2= Config_pb2.ProtocolConfig()


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
class MQTTManagerServicer(MQTT_pb2_grpc.MQTTManagerServicer):
    def PublishMessages(self,request,context):
        topic1=request.Topic
        payload1=request.Payload
        qos1=request.Qos
        #Broker='127.0.0.1'
        #Port=1883
        print('Connecting to the Mosquitto Broker .....')
        Mqttclient= mqtt.Client("grpc",clean_session=False)
        Mqttclient.connect(c ,c1)
        Mqttclient.publish(topic=topic1,payload=payload1)
        print("The server is still waiting for Upcoming Data ")

        return MQTT_pb2.ACKPublish(Acknowledgment='Published successfully')

    

def main():

    server =grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    MQTT_pb2_grpc.add_MQTTManagerServicer_to_server(MQTTManagerServicer(),server)
    print("The server is Starting !")
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__=='__main__':

    Parameters=Clientrun.run()
    #print(type(Parameters))
    Parameters2=Parameters
    c=Parameters.__getattribute__('adresse')
    c1=Parameters.__getattribute__('Port')

    #print(c)
    #print(c1)

main()

