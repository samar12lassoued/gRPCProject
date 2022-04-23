import grpc
import MQTT_pb2_grpc
import MQTT_pb2

def run():
    with grpc.insecure_channel('localhost:50051') as channel :
        MQTT_pb2_grpc.MQTTManagerStub(channel)
        stub= MQTT_pb2_grpc.MQTTManagerStub(channel)
        print('Donner Topic')
        topic2=input()
        print('Donner Payload')
        payload2=input()
        #print('Donner Qos')
        #qos2=input()
        Acknowledgment= stub.PublishMessages(MQTT_pb2.ComingData(Topic=topic2,Payload=payload2))
        print(Acknowledgment)



if __name__== '__main__':
    print('client starting the publishment')
    run()