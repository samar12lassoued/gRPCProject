#!/bin/bash
if [ ${UID} -ne 0 ]; then
    echo "[x] Must run as root !"
    exit 1
fi

# Configuration Manager
systemctl start Config_Manager 
# MQTT Manager
systemctl start Mqtt_Manager
#Modbus Client 
systemctl start MOdbusClient
                                      
