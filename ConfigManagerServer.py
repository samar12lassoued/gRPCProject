
import grpc
import Config_pb2
import Config_pb2_grpc
from concurrent import futures
import json 
from pprint import pprint

#file1="modbusTCP.json"
#file2="mqtt.json"
adresse1=""
port1=0

class ConfigManagerServicer(Config_pb2_grpc.ConfigManagerServicer):
    def getConfig(self, request, context):
        ProtocolName=request.Protocolname
        
        if ProtocolName=='MQTT':
            with open('mqtt.json','r') as jsonfile1:
                data= json.load(jsonfile1)
                adresse1=data['adresse']
                port1=data['port']
                #print(adresse1)


        elif ProtocolName=='MODBUSTCP':
            with open('modbusTCP.json','r') as jsonfile2:
                data1= json.load(jsonfile2)
                adresse1=data1['adresse']
                port1=data1['port']

        else:
            #context.set_code()
            #grpc.ServicerContext.abort('notoj','repeat')
            #raise Exception("Try Again")
            adresse1='Try Again please!'
            port1=00000000000000000
            
        
        return Config_pb2.ProtocolConfig(adresse=adresse1,Port=port1)

def main():
    server =grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    Config_pb2_grpc.add_ConfigManagerServicer_to_server(ConfigManagerServicer(),server)
    print("The Configuration Server is Starting !")
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

main()        