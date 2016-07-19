import os
import time
import netifaces
#import scapy
from scapy.all import *
import interfaces


def menu():
    global ipsrc, ipdst
    os.system("clear")

    print """

     `yhhhhhyo-              shhhhhhhhhhhh-                     `o/      ohdmmmds-
     `mM:.../dMs             .....+Md.....`                     -Mh      -.`  `:mM/
     `mM-    -MN`/ms     `hm-     /Md    -sdmdmdo.   :ymmdddh` +dMNhhho         yM+   om+sdmm-
     `mM-  `-hMh  sM+    yM+      /Md   oMs`   -dN. .Nm`    .   -Mh        /ssymd/    sMm:
     `mMmmmmdy/   `hN:  +Ms       /Md  .NNoooooohMo  yNds+/.    -Mh        .::/sNd-   sM+
     `mM-          `mN.:Nh        /Md  .MN:-------.   `-/oyNm:  -Mh             :Mm   sM/
     `mM-           .NmNm`        /Md   sMy`     .` `.     oMs  .Mm`    `.     .yMy   sM/
     `mN-            /MN-         :my    :ymdddddh` .dmdddddo`   /hdddo -dmmmmmmh/    om:
                    `hM/
                  sdmd:                                                                    """

    print "\n     Welcome to PyTest3r\n"
    print "           Menu:"
    print "-----------------------------"
    print "1 ... Network intefaces & IPs"
    print "2 ... Type of packets"
    print "3 ... Show all settings"
    print "4 ... Start sending packets"
    print "q ... Quit"
    option = raw_input("\n->")
    while option != "q":
        if option == "1":
            option1()
            menu()
            break
        elif option =="2":
            option2()
            menu()
            break
        elif option =="3":
            option3()
            menu()
            break
        elif option =="4":
            option4()
            menu()
            break
        else:
            menu()
            break

def verify_value(value,range_start,range_stop):
    try:
        int(value)
    except ValueError:
        return False
    else:
        value = int(value)
    if type(value) == int:
        if int(value) in range(range_start,range_stop+1):
            return True
        else:
            return False
    else:
        return False

def option1():
    global ipsrc, ipdst
    iplist = []
    os.system("clear")
    a = 1
    print "Network interfaces & IPs"
    print "------------------------"
    for i in interfaces.interfaces():
        print "%d. Interface name: " % a, i, ", IP: ", interfaces.interfaces()[i]
        iplist.append(interfaces.interfaces()[i])
        a+=1
    while True:
        out_int = raw_input("Output interface: ")
        try:
            ipsrc = iplist[int(out_int)-1]
            break
        except IndexError:
            print "Try again!"
    while True:
        in_int = raw_input("Input interface: ")
        if out_int <> in_int:
            try:
                ipdst = iplist[int(in_int) - 1]
                break
            except IndexError:
                print "Try again!"
        else:
            print "Try again!"
    print "________________________________________________________________\n"
    print "Source IP: ",ipsrc,"\n","Destination IP: ", ipdst
    raw_input("\nPress enter to return to main menu...")

def option2():
    global traffic_type,cos_value1, dei_value1, vlan1_value,vlan2_value,cos_value2, dei_value2
    os.system("clear")
    print "Type of packets"
    print "------------------------"
    print "Type of traffic:"
    print "1 ... Untagged"
    print "2 ... Dot1Q"
    print "3 ... QinQ"
    opt_tot = raw_input("\n-> ")
    while opt_tot not in ("1","2","3"):
        print "Please select a valid option!"
        opt_tot = raw_input("\n-> ")

    if opt_tot == "1":
            traffic_type = 1

    elif opt_tot == "2":
            traffic_type = 2
            print "\nTag protocol identifier (TPID): 0x8100\n"
            print "Tag control information (TCI)"
            print "-----------------------------"

            print "Priority code point (PCP) / Class of service (COS)"
            cos_value1 = raw_input("A value from 0 to 7: ")
            while not verify_value(cos_value1,0,7):
                cos_value1 = raw_input("A value from 0 to 7: ")

            print "\nDrop eligible indicator (DEI) / formerly Canonical Format Indicator (CFI)"
            dei_value1 = raw_input("A value of 0 or 1: ")
            while not verify_value(dei_value1,0,1):
                dei_value1 = raw_input("Please select a value of 0 or 1: ")

            print "\nVLAN identifier (VID)"
            vlan1_value = raw_input("A value from 1 to 4094: ")
            while not verify_value(vlan1_value,1,4094):
                vlan1_value = raw_input("Please select a value of 0 or 4094: ")



    elif opt_tot == "3":
            traffic_type = 3
            print "First tag:"
            print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
            print "\nTag protocol identifier (TPID): 0x88A8\n"
            print "Tag control information (TCI)"

            print "Priority code point (PCP) / Class of service (COS)"
            cos_value1 = raw_input("A value from 0 to 7: ")
            while not verify_value(cos_value1,0,7):
                cos_value1 = raw_input("Please select a value from 0 to 7: ")

            print "\nDrop eligible indicator (DEI) / formerly Canonical Format Indicator (CFI)"
            dei_value1 = raw_input("A value of 0 or 1: ")
            while not verify_value(dei_value1,0,1):
                dei_value1 = raw_input("Please select a value of 0 or 1: ")

            print "\nVLAN 1 identifier (VID)"
            vlan1_value = raw_input("A value from 1 to 4094: ")
            while not verify_value(vlan1_value,1,4094):
                vlan1_value = raw_input("Please select a value of 0 or 4094: ")

            print "\nSecond tag:"
            print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"

            print "\nTag protocol identifier (TPID): 0x8100\n"
            print "Tag control information (TCI)"

            print "Priority code point (PCP) / Class of service (COS)"
            cos_value2 = raw_input("A value from 0 to 7: ")
            while not verify_value(cos_value2,0,7):
                cos_value2 = raw_input("Please select a value from 0 to 7: ")

            print "\nDrop eligible indicator (DEI) / formerly Canonical Format Indicator (CFI)"
            dei_value2 = raw_input("A value of 0 or 1: ")
            while not verify_value(dei_value2,0,1):
                dei_value2 = raw_input("Please select a value of 0 or 1: ")

            print "\nVLAN 2 identifier (VID)"
            vlan2_value = raw_input("A value from 1 to 4094: ")
            while not verify_value(vlan2_value,1,4094):
                vlan2_value = raw_input("Please select a value of 0 or 4094: ")








    raw_input("\nPress any key to return to main menu...")

def option3():
    os.system("clear")
    print "All settings"
    print "-------------------------------\n"
    print "IP source        ",ipsrc
    print "IP destination   ",ipdst
    print "Traffic type     ",traffic_type
    print "First tag:"
    print "COS value        ",cos_value1
    print "DEI(CFI) value   ",dei_value1
    print "VLAN 1 value (S) ",vlan1_value
    print "Second tag:"
    print "COS value        ",cos_value2
    print "DEI(CFI) value   ",dei_value2
    print "VLAN 2 value (C) ",vlan2_value
    raw_input("\nPress any key to return to main menu...")

def option4():
    os.system("clear")
    print "Starting transmission..."
    print "------------------------"
    print "to be continued"
    core_server()
    raw_input("\nPress any key to return to main menu...")


def core_server():
    nr = raw_input("How many packets(max 10000, 0 for continous CTRL+C to stop):")
    load_ = str("hello")
    dot1qlay1 = Dot1Q()
    dot1qlay1.type = 0x88A8
    dot1qlay1.vlan = int(vlan1_value)
    dot1qlay1.prio = int(cos_value1)
    dot1qlay1.id = int(dei_value1)
    #print dot1qlay1.show()

    dot1qlay2 = Dot1Q()
    #dot1qlay2.type = 0x8100
    dot1qlay2.vlan = int(vlan2_value)
    dot1qlay2.prio = int(cos_value2)
    dot1qlay2.id = int(dei_value2)
    #print dot1qlay2.show()

    iplay = IP()
    iplay.src = ipsrc
    iplay.dst = ipdst
    #print iplay.show2()

    pkt = dot1qlay1/dot1qlay2/iplay/fuzz(Raw())
    i = 0
    while not verify_value(nr,0,10000):
        nr = raw_input("How many packets:")

    if int(nr)==0:
        try:
            while True:
                fuzzload = fuzz(Raw())
                payload = str(i)+" "+fuzzload
                send(dot1qlay1/dot1qlay2/iplay/"hello"+payload)
                i+=1
        except KeyboardInterrupt:
            pass
    else:
        send(pkt, count=int(nr))




print "\x1b[8;40;100t"
global ipsrc, ipdst,traffic_type,cos_value1, dei_value, vlan1_value,vlan2_value,cos_value2
traffic_type = 0
cos_value1 = 0
dei_value1 = 0
cos_value2 = 0
dei_value2 = 0
vlan2_value = 0
vlan1_value = 0
ipsrc = 0
ipdst = 0
menu()
