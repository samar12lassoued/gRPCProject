
import grpc
from lib import Config_pb2
from lib import Config_pb2_grpc
from concurrent import futures
import json 
import logging
import Config


logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(message)s')
adresse1=""
port1=0

class ConfigManagerServicer(Config_pb2_grpc.ConfigManagerServicer):
    def getConfig(self, request, context):
        ProtocolName=request.Protocolname
        
        if ProtocolName=='MQTT':
            with open('Config.json','r') as jsonfile1:
                data= json.load(jsonfile1)
                adresse1=data["MQTT"]['BrokerAdress']
                port1=data["MQTT"]['port']
                

      

        elif ProtocolName=='ModBusTCP':
            with open('Config.json','r') as jsonfile1:
                data= json.load(jsonfile1)
                adresse1=data["ModBusTCP"]['ServerAdress']
                port1=data["ModBusTCP"]['port']

        else:
            
            adresse1='Try Again please!!!!'
            port1=00000000000000000
            
        
        return Config_pb2.ProtocolConfig(adresse=adresse1,Port=port1)

def main():
    server =grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    Config_pb2_grpc.add_ConfigManagerServicer_to_server(ConfigManagerServicer(),server)
    logging.info("The Configuration Manager Server is Starting !")
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

main()        
