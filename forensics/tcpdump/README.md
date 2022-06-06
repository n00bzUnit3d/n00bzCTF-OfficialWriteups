# tcpdump | Censored1375 
- Description: ohhh a pcap file, i wonder what it contains?. Wrap flag in n00bz{}

cap.pcap:/attachments/tcpdump/cap.pcap

# Write up

Get all the raw tcp data and write it into a file with using python scapy

```py
from scapy.all import * 

pcap = rdpcap('cap.pcap')
output = open('ouput.png', 'wb')

for packet in pcap: 
    if Raw in packet: 
        output.write(packet[Raw].load)
output.close()
``` 

# Flag - n00bz{D1D_Y0U_GET_EVERYTH1NG_!?}