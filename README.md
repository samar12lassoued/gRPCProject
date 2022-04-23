__Author__== Samar Lassoued


###### gRPCProject

***This is a Multiprotocol Platform that works as  a Gateway that 
 implements different protocols ***


THis platform is based mainly on gRPC that gurantees the communication and 
the transfer of data exchanged between the servers and the clients .

**This is a Gateway that manages distincts protocls including:

     1.MQTT
     2.ModBus TCP
     3.ModBus RTU 
     4.wIFI
     5.ZigBee
     6.LoRa
     7.BLE
     
In this project we implemented just 2 protocols which are :
MQTT and ModBus TCP 


**Implemented Protocls :
   1.  MQTT
   2.  ModBusTCP 
   
   
 Main Actors of this Gateway are :
 
**ModBus TCP Client :
      This actor will initiate the communication in the platform after receiving the data from the 
     ModBus TCP server .
     
**MQTT Server:
      This actor provides the main service in the platform which is  to publish the
      data received into  the Mosquitto Broker. It makes the link between the ModBus TCP client
      and the Broker :it  is like a Gateway.
 
**ConfigManager Server:
     This actor provides an essential service for the launch of any client or
     server present in the platform. In fact, any client or server before
     starting the communication, he must send a request to this server to 
     provide him with the necessary connection parameters.
     
**ModBus TCP Server:
    This actor is the starting point of the communication, it is this one who
    allows the ModBus TCP client to acquire the data.
 
  
      
      
      
   
 ![PlateformeschemaGlobal](https://user-images.githubusercontent.com/73782851/164945148-e084b1f4-064e-4584-ace7-98b9d2291736.jpg)
 
  



