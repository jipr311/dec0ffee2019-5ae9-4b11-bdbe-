#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pip3 install paho-mqtt python-etcd

import paho.mqtt.client as mqtt 

broker_address="198.41.30.241" 
#broker_address="iot.eclipse.org" 

client = mqtt.Client("P1")
client.connect(broker_address)
client.publish("house/main-light","OFF1")

