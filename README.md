# PCAP-Parser
PCAP Parser Project by Kazi Ahsan and Jayne Rutledge                  Date: 1/23/2021
# Python Tutorials for Security Engineers

Three scripts to get you started with your adventure into the world of Cyber Security-- specfically ARP and its use for Man in the Middle attacks. Developed and tested on Kali Linux.

***

## So where do we begin?

1. **Network Analysis** with Wireshark

  - First we want to export http objects from wireshark into a pcap file to see if they may be malicious. 

2. **PCAP-Parser Software** with Python and Bash 

- Now we are going to parse the PCAP file through our software to see if there are any known viruses – 

3. **Export and Append** to a .csv File

- Create an excel file and save it as FromPython.csv (If you want to change the name of the .csv file you need to go to the md5parser.py file and change it within the file).


## Network Analysis** with Wireshark

-We are using a pcap file from malware-analysis-traffic.net to generate network traffic for this scenario. 
 
![wireshark -r subnet](images/wireshark1.PNG)

-The first thing we will do is go up to Statistics, to Protocol Hierarchy to see what protocols are being used in this pcap. We are interested in TCP application traffic.
- We can see that there is a lot of HTTP which is related to web traffic.



 









-We will select a filter to return only on layer 7, HTTP protocol. 
 



-For this demonstration, we are interested in retrieving GET and POST requests for now. So we type in http.request. 


 



-To get the actual file we need to go to File, Export Objects, and HTTP.
 


-We can now see all the file objects that were downloaded in this packet capture. We then sort by Content Type. In this save we see gifs, and text and applications. 
-In this example, there are three different types of Applications which appear suspicious we will look at: java, Microsoft executable download and shockwave-flash. 
-I’m going to save this PCAP file in the same folder with my other two md5parser and pcap parser file. 



 

*This simple network scanner functions much like 
Kali Linux's built-in netdiscover command.*

Our scanner uses ARP requests instead of pings to discover what hosts are running on the netwrok.

<details> 
<summary><B>Why is an ARP request preferrable in this instance?</B>
</summary>

> ARP is an automated part of the day-to-day functioning of many network devices, so blue teamers are less likely to flag it in their logs and investigate us. ARP requests are also less likely to be blocked by firewall rules.
</details></p>

Here's what we'd expect to find using the built-in Kali tool **netdiscover**.

![netdiscover -r subnet](./image/netd_cmd.png)

    Note that we are giving netdiscover our own subnet

![netdiscover output](./image/netd_output.png)

    netdiscover outputs the subnet IP and MAC addresses of other devices on our network

We should get the same output by running [ARP_scanner.py](/ARP_netscan.py). Make sure to change the py_scan variable (at the end of the script) to the address of the subnet you want to scan!


<details> 
<summary><b>Why does the python script broadcast to "ff:ff:ff:ff:ff:ff"?</b>
</summary>

> "ff:ff:ff:ff:ff:ff" is the broadcast MAC address, so this message will reach all computers on our network. Once we get a reply from a device, we replace "ff:ff:ff:ff:ff:ff" with the known MAC address, which gets used for the remainder of the script.
</details><p>

</p>

Now that we have a few devices to target, let's use an ARP attack to see what we can do.

***

## **PCAP-Parser Software** with Python and Bash 

 
 
 
<details> 
  <summary><b>What is an our PCAP Parser software and why would anyone use it?</b>
</summary>

> The location of the scripts can be found at: (https://github.com/KaziSAhsan/PCAP-Parser/blob/main/pcapp) 
(https://github.com/KaziSAhsan/PCAP-Parser/blob/main/md5parser.py)
- Make sure you place them in the same directory. When you execute pcapp then this will call the md5parser.py and execute it. Before that you need to change your executable permission to run this script. This will take less than 30 seconds to run this script. 

</details><p>

</p>


![ARP Attacker](./image/attack_hostname_gatrway.png)


2. When we run an ARP scan of the network from our attack client, we find a number of machines, including the one we want to attack: 10.0.2.4.

![ARP Scan](./image/arp_scan.png)


3. This is the IP Address of the machine I am targetting. <p><b>IMPORTANT: I own this target machine. Do not execute this attack against any machine that is not yours without explicit written permission.</b>

![ARP Spoof Target](./image/target_ip.png)

<i>Again, note that my attack and target clients share the same gateway router</i>


4. With this information, we can launch the attack and gain Man in the Middle access.

![ARP Attack](./image/spoof_attack.png)


[This script](/arp_spoof.py) sends alternating packets to our gateway router and our target machine; these ARP packets match our MAC address to two different IP addresses. That is, we are telling the gateway router that our machine has the victim's IP address, and we are telling the victim that our machine has the gateway router's IP address. That way, traffic back and forth from the victim to the router flows through us.

***

## Mac Address Spoofing


Sometimes, we need to spoof our MAC address to bypass certain Access Control Lists that may have caught on to our bad behavior. We can do this at the command line, but why not put it into a script? Here's how.

### Command line method:

1. Check our MAC Address

![ifconfig](./image/ifconfig.png)

    note my interface is eth0 and my MAC Address 08:00:27:23:ff:90

2. Linux Commands to change our MAC 

![ifconfig](./image/manualChange.png)

3. Confirm our MAC was changed

![ifconfig](./image/changedMac.png)
    
     My new MAC address is 66:55:44:33:22:11

How do we do this in Python? Why, there's a module for that!

>[This module](https://docs.python.org/3/library/subprocess.html) will let us use command line arguments in our python script

> We get the desired MAC address and network interface from the user during the execution of the script by using the input() function.


Check out the Mac Changer Script [here](/MACchanger.py).

<details> 
  <summary>Besides bypassing ACLs, why else might a hacker spoof their MAC address?
  </summary>

> To hide themselves on a network or impersonate another device.
</details>


