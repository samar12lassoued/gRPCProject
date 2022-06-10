"""Modbus TCP Client"""

# Modbus library
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import grpc

# MQTT gRPC library
import mqtt_pb2
import mqtt_pb2_grpc
import Config_pb2 
import Config_pb2_grpc 
Parameters=Config_pb2.ProtocolConfig()
# Tools
#from utils import log_info
import logging 
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(message)s')
# Default modbus server
MODBUS_SERVER_HOST = "localhost"
MODBUS_SERVER_PORT = 5020
class Modbus_Config():
    def run():
        global server_host,server_port
        with grpc.insecure_channel('localhost:50052') as channel :
            Config_pb2_grpc.ConfigManagerStub(channel)
            Conf_stub= Config_pb2_grpc.ConfigManagerStub(channel)
            Parameters= Conf_stub.getConfig(Config_pb2.Protocolrequest(Protocolname="ModBusTCP"))
            server_host=Parameters.__getattribute__('adresse')
            server_port=Parameters.__getattribute__('Port')
        logging.info('Configuration Parameters are {}:{}'.format(server_host,server_port))
        return Parameters

# Connect to Config Managercd 
#with grpc.insecure_channel('127.0.0.1:50050') as config_channel:
    #CONFIG_STUB = Config_pb2_grpc.ConfigParameters(config_channel)
    #MODBUS_SERVER_HOST = CONFIG_STUB.getConfig(pb2_grpc.Configuration(bloc="modbustcp", config="server")).value
    #MODBUS_SERVER_PORT = CONFIG_STUB.getConfig(pb2_grpc.Configuration(bloc="modbustcp", config="port")).value
    #logging.info("[ModbusClient] Connecting to modbus server: {}:{}".format(MODBUS_SERVER_HOST, MODBUS_SERVER_PORT))

Parameters=Modbus_Config.run()

server_host1=Parameters.__getattribute__('adresse')
server_port1=Parameters.__getattribute__('Port')
MODBUS_CLIENT = ModbusClient(MODBUS_SERVER_HOST, port=MODBUS_SERVER_PORT)
MODBUS_CLIENT.connect()



UNIT = 0x1

def run():
    """Main modbus client method"""
    with grpc.insecure_channel('0.0.0.0:50051') as mqtt_channel:
        mqtt_stub = mqtt_pb2_grpc.MQTTManagerStub(mqtt_channel)
        modbus_data = MODBUS_CLIENT.read_holding_registers(0, 1, unit=UNIT)
        for mdata in modbus_data.registers:
            Acknowledgment= mqtt_stub.PublishMessages(mqtt_pb2.ComingData(Payload=str(mdata), Topic="modbustcp"))
            print(Acknowledgment)



#logging.info('Configuration Parameters are {}:{}'.format(server_host1, server_port1))

if __name__ == '__main__':
    try:
       run()
    except KeyboardInterrupt:
        logging.info("[ModbusClient] Shutting down ..")
