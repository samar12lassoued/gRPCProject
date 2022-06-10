"""Modbus TCP server Simulation"""
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Import tools
#from gw_mp_tools import log_info
import logging 
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(message)s')
# Server data
DATABLOCK = [0x01, 0xFF, 0x99, 0x54, 0xEE, 0x6A, 0x11, 0x00]

def run_server():
    """initialize the server information"""
    store = ModbusSlaveContext(hr=ModbusSequentialDataBlock(0, DATABLOCK), zero_mode=True)
    context = ModbusServerContext(slaves=store, single=True)
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'DATAKOM WATER METER/VALVE SIMULATOR'
    identity.ProductCode = 'DATAKOM DKM-407'
    identity.VendorUrl = 'https://sofia-technologies.com/'
    identity.ProductName = 'Water meter/valve'
    identity.ModelName = 'Water valve/meter DATAKOM DKM-407'
    identity.MajorMinorRevision = '1.1'

    logging.info ("[ModbusTCP] Starting Server ..")
    StartTcpServer(context, identity=identity, address=("0.0.0.0", 5020))

if __name__ == "__main__":
    run_server()
