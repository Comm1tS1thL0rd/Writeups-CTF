Get Wireshare and the pcap file.
Open the file in Wireshark.

The First frame is a request which asks for the flag
From 2nd frame till end its reply

In the 2nd frame itself we notice JFIF data, which indicated towards a jpeg image file type.

Upon chewcking the Hex, it starts with ff d8 which confirms its a jpeg file.

A jpeg file also ends with ff d9, which is observed in the last frame.
This implies that the entirety of the data is actually might be a jpeg image sent that is recorded by wireshark here.

Now with python(3.9.6) i wrote a series of codes to extract the image from the pcap.

Run this in order to get through extract.py > remove.py > rmline.py > join.py > convert.py.

with extract i extracted the hex data from the pcap
with remove i removed the first 84 characters from all lines of data as that is not related to the file data that we need
with rmline i removed the first line of hex which is a request command line and not the image data
with join i joined all the hex data in 1 line
with convert i converted the hex data to jpeg file and the file gives you the flag.

libraries used : scapy
