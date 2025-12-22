# Performance discrepencies in Ubridge when using a SOCK_RAW verses /dev/net/tun 

## Symptom
Very poor network performance in the GNS3 Child Virtual machines.  See the example "git clone" in the working section of this document takes less than 1 minute, but this configuration will take more than 15min, often much long, and sometimes will timeout.  

This performance issue does not appear on any other machine in the network including the GNS3 host itself.  We have also tested other qemu based  machines using a bridge interface.

# Broken configuration

GNS3 cloud exposing ens224 interface directly connected to a Ubuntu based  

## Data

### Download client

The following was ran for 2 minutes and completed less than 10% of the oject download.

```
itsclass@its-uc-xxx:~/tmp$ time git clone https://github.com/librenms/librenms.git
Cloning into 'librenms'...
remote: Enumerating objects: 244383, done.
remote: Counting objects: 100% (68/68), done.
remote: Compressing objects: 100% (62/62), done.
^Cfetch-pack: unexpected disconnect while reading sideband packet


real	2m0.755s
user	0m0.069s
sys	0m0.879s
```

### Packet capture anaylsis
 
The slow network performance can be observed via packet captures.  For example the previous test showed 2126 of 11164 (19%) packets were re-transmissions.

### Packet capture sample

```
No.     Time           Source                Destination           Protocol Length Info
     41 32.825752      132.235.207.231       132.235.9.75          DNS      81     Standard query 0x4873 A github.com OPT
     42 32.826374      132.235.207.231       132.235.9.75          DNS      81     Standard query 0x2690 AAAA github.com OPT
     43 32.826936      132.235.9.75          132.235.207.231       DNS      97     Standard query response 0x4873 A github.com A 140.82.112.3 OPT
     44 32.840333      132.235.9.75          132.235.207.231       DNS      146    Standard query response 0x2690 AAAA github.com SOA dns1.p08.nsone.net OPT
     45 32.845242      132.235.207.231       140.82.112.3          TCP      74     50624 → 443 [SYN] Seq=0 Win=32120 Len=0 MSS=1460 SACK_PERM TSval=3861724543 TSecr=0 WS=128
     46 32.860728      140.82.112.3          132.235.207.231       TCP      74     443 → 50624 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1380 SACK_PERM TSval=4053133752 TSecr=3861724543 WS=1024
     47 32.861427      132.235.207.231       140.82.112.3          TCP      66     50624 → 443 [ACK] Seq=1 Ack=1 Win=32128 Len=0 TSval=3861724560 TSecr=4053133752
     48 32.957305      132.235.207.231       140.82.112.3          TLSv1.3  461    Client Hello (SNI=github.com)
     49 32.975017      140.82.112.3          132.235.207.231       TLSv1.3  1434   Server Hello, Change Cipher Spec, Application Data
     50 32.975512      132.235.207.231       140.82.112.3          TCP      66     50624 → 443 [ACK] Seq=396 Ack=1369 Win=31872 Len=0 TSval=3861724674 TSecr=4053133866
     51 32.975668      140.82.112.3          132.235.207.231       TCP      1434   443 → 50624 [PSH, ACK] Seq=1369 Ack=396 Win=67584 Len=1368 TSval=4053133866 TSecr=3861724656 [TCP segment of a reassembled PDU]
     52 32.975980      140.82.112.3          132.235.207.231       TLSv1.3  862    Application Data, Application Data, Application Data
     53 32.976072      132.235.207.231       140.82.112.3          TCP      66     50624 → 443 [ACK] Seq=396 Ack=2737 Win=31872 Len=0 TSval=3861724675 TSecr=4053133866
     54 32.976381      132.235.207.231       140.82.112.3          TCP      66     50624 → 443 [ACK] Seq=396 Ack=3533 Win=31872 Len=0 TSval=3861724675 TSecr=4053133866
     55 32.977830      132.235.207.231       140.82.112.3          TLSv1.3  72     Change Cipher Spec
     56 32.980945      132.235.207.231       140.82.112.3          TLSv1.3  124    Application Data
     57 32.991580      132.235.207.231       140.82.112.3          TLSv1.3  152    Application Data
     58 32.991626      132.235.207.231       140.82.112.3          TLSv1.3  231    Application Data
     59 32.996321      140.82.112.3          132.235.207.231       TCP      66     443 → 50624 [ACK] Seq=3533 Ack=460 Win=67584 Len=0 TSval=4053133887 TSecr=3861724676
     60 32.996543      140.82.112.3          132.235.207.231       TLSv1.3  145    Application Data
     61 32.996584      140.82.112.3          132.235.207.231       TLSv1.3  145    Application Data
     62 32.997286      132.235.207.231       140.82.112.3          TCP      66     50624 → 443 [ACK] Seq=711 Ack=3691 Win=31872 Len=0 TSval=3861724696 TSecr=4053133887
     63 33.006932      140.82.112.3          132.235.207.231       TLSv1.3  130    Application Data
     64 33.007785      132.235.207.231       140.82.112.3          TLSv1.3  97     Application Data
     65 33.023317      140.82.112.3          132.235.207.231       TCP      66     443 → 50624 [ACK] Seq=3755 Ack=742 Win=68608 Len=0 TSval=4053133914 TSecr=3861724690
     66 33.027077      140.82.112.3          132.235.207.231       TLSv1.3  515    Application Data
     67 33.030457      140.82.112.3          132.235.207.231       TLSv1.3  250    Application Data
     68 33.030827      140.82.112.3          132.235.207.231       TLSv1.3  110    Application Data
     69 33.031860      132.235.207.231       140.82.112.3          TCP      66     50624 → 443 [ACK] Seq=742 Ack=4432 Win=31872 Len=0 TSval=3861724730 TSecr=4053133918
     70 33.034091      132.235.207.231       140.82.112.3          TLSv1.3  379    Application Data
     71 33.049521      140.82.112.3          132.235.207.231       TLSv1.3  114    Application Data
     72 33.057782      140.82.112.3          132.235.207.231       TLSv1.3  465    Application Data
     73 33.059845      132.235.207.231       140.82.112.3          TCP      66     50624 → 443 [ACK] Seq=1055 Ack=4879 Win=31872 Len=0 TSval=3861724758 TSecr=4053133941
     74 33.061129      140.82.112.3          132.235.207.231       TCP      1434   443 → 50624 [ACK] Seq=4879 Ack=1055 Win=69632 Len=1368 TSval=4053133952 TSecr=3861724732 [TCP segment of a reassembled PDU]
     75 33.061797      140.82.112.3          132.235.207.231       TLSv1.3  2869   Application Data, Application Data
     76 33.061863      140.82.112.3          132.235.207.231       TCP      1434   443 → 50624 [ACK] Seq=9050 Ack=1055 Win=69632 Len=1368 TSval=4053133952 TSecr=3861724732 [TCP segment of a reassembled PDU]
     77 33.061890      140.82.112.3          132.235.207.231       TLSv1.3  1434   Application Data
     78 33.061916      140.82.112.3          132.235.207.231       TLSv1.3  2802   Application Data, Application Data
     79 33.063319      132.235.207.231       140.82.112.3          TCP      78     50624 → 443 [ACK] Seq=1055 Ack=6247 Win=31872 Len=0 TSval=3861724761 TSecr=4053133952 SLE=9050 SRE=11786
     80 33.075154      140.82.112.3          132.235.207.231       TLSv1.3  1434   Application Data
     81 33.075217      140.82.112.3          132.235.207.231       TLSv1.3  1434   Application Data
     82 33.075238      140.82.112.3          132.235.207.231       TLSv1.3  1169   Application Data, Application Data, Application Data, Application Data
     83 33.075709      132.235.207.231       140.82.112.3          TCP      86     [TCP Dup ACK 79#1] 50624 → 443 [ACK] Seq=1055 Ack=6247 Win=31872 Len=0 TSval=3861724774 TSecr=4053133952 SLE=14522 SRE=17258 SLE=9050 SRE=11786
     84 33.076254      132.235.207.231       140.82.112.3          TCP      86     [TCP Dup ACK 79#2] 50624 → 443 [ACK] Seq=1055 Ack=6247 Win=31872 Len=0 TSval=3861724774 TSecr=4053133952 SLE=14522 SRE=18361 SLE=9050 SRE=11786
     85 33.091047      140.82.112.3          132.235.207.231       TCP      1434   [TCP Fast Retransmission] 443 → 50624 [ACK] Seq=6247 Ack=1055 Win=69632 Len=1368 TSval=4053133982 TSecr=3861724774 [TCP segment of a reassembled PDU]
     86 33.091128      140.82.112.3          132.235.207.231       TCP      1434   [TCP Retransmission] 443 → 50624 [ACK] Seq=7615 Ack=1055 Win=69632 Len=1368 TSval=4053133982 TSecr=3861724774
     87 33.091485      140.82.112.3          132.235.207.231       TCP      133    [TCP Retransmission] 443 → 50624 [PSH, ACK] Seq=8983 Ack=1055 Win=69632 Len=67 TSval=4053133983 TSecr=3861724774
     88 33.092661      132.235.207.231       140.82.112.3          TCP      86     50624 → 443 [ACK] Seq=1055 Ack=8983 Win=31872 Len=0 TSval=3861724791 TSecr=4053133982 SLE=14522 SRE=18361 SLE=9050 SRE=11786
     89 33.092779      132.235.207.231       140.82.112.3          TCP      78     50624 → 443 [ACK] Seq=1055 Ack=11786 Win=31872 Len=0 TSval=3861724791 TSecr=4053133983 SLE=14522 SRE=18361
     90 33.108102      140.82.112.3          132.235.207.231       TCP      2802   [TCP Retransmission] 443 → 50624 [PSH, ACK] Seq=11786 Ack=1055 Win=69632 Len=2736 TSval=4053133999 TSecr=3861724791
     91 33.392109      140.82.112.3          132.235.207.231       TCP      1434   [TCP Retransmission] 443 → 50624 [ACK] Seq=11786 Ack=1055 Win=69632 Len=1368 TSval=4053134283 TSecr=3861724791
     92 33.394296      132.235.207.231       140.82.112.3          TCP      78     50624 → 443 [ACK] Seq=1055 Ack=13154 Win=31872 Len=0 TSval=3861725092 TSecr=4053134283 SLE=14522 SRE=18361
     93 33.409587      140.82.112.3          132.235.207.231       TCP      1434   [TCP Retransmission] 443 → 50624 [ACK] Seq=13154 Ack=1055 Win=69632 Len=1368 TSval=4053134301 TSecr=3861725092
     94 33.411069      132.235.207.231       140.82.112.3          TCP      66     50624 → 443 [ACK] Seq=1055 Ack=18361 Win=31872 Len=0 TSval=3861725109 TSecr=4053134301
     95 33.421354      132.235.207.231       140.82.112.3          TCP      1434   50624 → 443 [ACK] Seq=1055 Ack=18361 Win=31872 Len=1368 TSval=3861725120 TSecr=4053134301 [TCP segment of a reassembled PDU]
     96 33.421402      132.235.207.231       140.82.112.3          TCP      1434   50624 → 443 [PSH, ACK] Seq=2423 Ack=18361 Win=31872 Len=1368 TSval=3861725120 TSecr=4053134301 [TCP segment of a reassembled PDU]
     97 33.421412      132.235.207.231       140.82.112.3          TCP      66     [TCP Dup ACK 94#1] 50624 → 443 [PSH, ACK] Seq=3791 Ack=18361 Win=31872 Len=0 TSval=3861725120 TSecr=4053134301
     98 33.421421      132.235.207.231       140.82.112.3          TCP      1434   50624 → 443 [ACK] Seq=3791 Ack=18361 Win=31872 Len=1368 TSval=3861725120 TSecr=4053134301 [TCP segment of a reassembled PDU]
     99 33.421431      132.235.207.231       140.82.112.3          TLSv1.3  799    Application Data
    100 33.437096      140.82.112.3          132.235.207.231       TCP      66     443 → 50624 [ACK] Seq=18361 Ack=3791 Win=74752 Len=0 TSval=4053134328 TSecr=3861725120
    101 33.437187      140.82.112.3          132.235.207.231       TCP      66     443 → 50624 [ACK] Seq=18361 Ack=5892 Win=80896 Len=0 TSval=4053134328 TSecr=3861725120
    102 33.437215      140.82.112.3          132.235.207.231       TLSv1.3  114    Application Data
    103 33.445956      140.82.112.3          132.235.207.231       TLSv1.3  465    Application Data
    104 33.446741      132.235.207.231       140.82.112.3          TCP      66     50624 → 443 [ACK] Seq=5892 Ack=18808 Win=31872 Len=0 TSval=3861725145 TSecr=4053134328
    105 33.450659      140.82.112.3          132.235.207.231       TLSv1.3  110    Application Data
    106 33.473251      140.82.112.3          132.235.207.231       TCP      1827   443 → 50624 [PSH, ACK] Seq=18852 Ack=5892 Win=80896 Len=1761 TSval=4053134364 TSecr=3861725145 [TCP segment of a reassembled PDU], Application Data
    107 33.474395      140.82.112.3          132.235.207.231       TLSv1.3  206    Application Data
    108 33.475210      132.235.207.231       140.82.112.3          TCP      78     50624 → 443 [ACK] Seq=5892 Ack=18852 Win=31872 Len=0 TSval=3861725174 TSecr=4053134342 SLE=20613 SRE=20753
    109 33.476728      140.82.112.3          132.235.207.231       TLSv1.3  135    Application Data
    110 33.477285      132.235.207.231       140.82.112.3          TCP      78     [TCP Dup ACK 108#1] 50624 → 443 [ACK] Seq=5892 Ack=18852 Win=31872 Len=0 TSval=3861725176 TSecr=4053134342 SLE=20613 SRE=20822
    111 33.490601      140.82.112.3          132.235.207.231       TLSv1.3  2802   Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data, Application Data
    112 33.490962      140.82.112.3          132.235.207.231       TLSv1.3  2802   Application Data, Application Data
    113 33.492579      140.82.112.3          132.235.207.231       TLSv1.3  1434   Application Data
    114 33.493244      132.235.207.231       140.82.112.3          TCP      86     [TCP Dup ACK 108#2] 50624 → 443 [ACK] Seq=5892 Ack=18852 Win=31872 Len=0 TSval=3861725192 TSecr=4053134342 SLE=26294 SRE=27662 SLE=20613 SRE=20822
    115 33.499569      140.82.112.3          132.235.207.231       TCP      1434   [TCP Fast Retransmission] 443 → 50624 [ACK] Seq=18852 Ack=5892 Win=80896 Len=1368 TSval=4053134391 TSecr=3861725176 [TCP segment of a reassembled PDU]
    116 33.501038      132.235.207.231       140.82.112.3          TCP      86     50624 → 443 [ACK] Seq=5892 Ack=20220 Win=31872 Len=0 TSval=3861725199 TSecr=4053134391 SLE=26294 SRE=27662 SLE=20613 SRE=20822
    117 33.508524      140.82.112.3          132.235.207.231       TCP      459    [TCP Retransmission] 443 → 50624 [PSH, ACK] Seq=20220 Ack=5892 Win=80896 Len=393 TSval=4053134400 TSecr=3861725192
    118 33.509104      132.235.207.231       140.82.112.3          TCP      78     50624 → 443 [ACK] Seq=5892 Ack=20822 Win=31872 Len=0 TSval=3861725208 TSecr=4053134400 SLE=26294 SRE=27662
    119 33.516311      140.82.112.3          132.235.207.231       TCP      2802   [TCP Retransmission] 443 → 50624 [PSH, ACK] Seq=20822 Ack=5892 Win=80896 Len=2736 TSval=4053134407 TSecr=3861725199
    120 33.526726      140.82.112.3          132.235.207.231       TCP      2802   [TCP Retransmission] 443 → 50624 [PSH, ACK] Seq=23558 Ack=5892 Win=80896 Len=2736 TSval=4053134415 TSecr=3861725208
    121 33.771789      140.82.112.3          132.235.207.231       TCP      1434   [TCP Retransmission] 443 → 50624 [ACK] Seq=20822 Ack=5892 Win=80896 Len=1368 TSval=4053134663 TSecr=3861725208
    122 33.774791      132.235.207.231       140.82.112.3          TCP      78     50624 → 443 [ACK] Seq=5892 Ack=22190 Win=31872 Len=0 TSval=3861725471 TSecr=4053134663 SLE=26294 SRE=27662
    123 33.791294      140.82.112.3          132.235.207.231       TCP      1434   [TCP Retransmission] 443 → 50624 [ACK] Seq=22190 Ack=5892 Win=80896 Len=1368 TSval=4053134681 TSecr=3861725471
    124 33.791379      140.82.112.3          132.235.207.231       TCP      1434   [TCP Retransmission] 443 → 50624 [ACK] Seq=23558 Ack=5892 Win=80896 Len=1368 TSval=4053134681 TSecr=3861725471
    125 33.791828      132.235.207.231       140.82.112.3          TCP      78     50624 → 443 [ACK] Seq=5892 Ack=24926 Win=31872 Len=0 TSval=3861725490 TSecr=4053134681 SLE=26294 SRE=27662
    126 33.807277      140.82.112.3          132.235.207.231       TCP      1434   [TCP Retransmission] 443 → 50624 [ACK] Seq=24926 Ack=5892 Win=80896 Len=1368 TSval=4053134698 TSecr=3861725490
    127 33.807360      140.82.112.3          132.235.207.231       TLSv1.3  2802   Application Data
...
```

### Process list showing GNS3 running on the GNS3 host

For reference for Process IDs

```
   4051 ?        Sl     0:17  |   \_ /usr/share/gns3/gns3-gui/bin/python /usr/bin/gns3
   4066 ?        Sl     0:07  |       \_ /usr/share/gns3/gns3-server/bin/python /usr/bin/gns3server --local --allow --log=/home/itsvm/.config/GNS3/2.2/gns3_server.log --pid=/home/itsvm/.config/GNS3/2.2/gns3_server.pid
   4085 ?        Sl     0:03  |           \_ /usr/bin/ubridge -H localhost:42551
   4123 ?        Sl     1:59  |           \_ /usr/bin/qemu-system-x86_64 -name Ubuntu-CLI-1 -m 2048M -smp cpus=2,sockets=1 -enable-kvm -machine smm=off -boot order=c -drive file=/home/itsvm/GNS3/projects/Perf-test/project-files/qemu/2ceb5127-51c8-40a5-a00b-cf252f9bc681/hda_disk.qcow2,if=virtio,index=0,media=disk,id=drive0 -uuid 2ceb5127-51c8-40a5-a00b-cf252f9bc681 -serial telnet:127.0.0.1:5001,server,nowait -monitor tcp:127.0.0.1:35091,server,nowait -net none -device e1000,mac=0c:eb:51:27:00:00,netdev=gns3-0 -netdev socket,id=gns3-0,udp=127.0.0.1:10003,localaddr=127.0.0.1:10002 -nographic -cpu host
   4125 ?        Sl     0:02  |           \_ /usr/bin/ubridge -H localhost:41465
```

### UDP connections on the GNS3 Host

Additional reference for process IDs and port numbers.  Shows that ubidge with process ID 4125 is connected to '-netdev socket,id=gns3-0,udp=127.0.0.1:10003,localaddr=127.0.0.1:10002' on the qemu and to the other ubridge process 4085 that connects to the SOCK_RAW interface.

```
itsvm@BS-Faculty-GNS3-2025-12-22-001-saundeb1:~$ sudo ss -npu
Recv-Q        Send-Q               Local Address:Port                Peer Address:Port        Process                                   
0             0                        127.0.0.1:10000                  127.0.0.1:10001        users:(("ubridge",pid=4085,fd=5))        
0             0                        127.0.0.1:10001                  127.0.0.1:10000        users:(("ubridge",pid=4125,fd=6))        
0             0                        127.0.0.1:10003                  127.0.0.1:10002        users:(("ubridge",pid=4125,fd=5))  
```

### List of open files for first ubridge cloud process

Note the connection to SOCK_RAW

itsvm@BS-Faculty-GNS3-2025-12-22-001-saundeb1:~$ sudo lsof -p 4085
lsof: WARNING: can't stat() fuse.portal file system /run/user/120/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.portal file system /run/user/1001/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse file system /home/itsvm/thinclient_drives
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.gvfsd-fuse file system /run/user/1001/gvfs
      Output information may be incomplete.
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF     NODE NAME
ubridge 4085 itsvm  cwd    DIR    8,2     4096 28059016 /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276
ubridge 4085 itsvm  rtd    DIR    8,2     4096        2 /
ubridge 4085 itsvm  txt    REG    8,2    85944 22415878 /usr/bin/ubridge
ubridge 4085 itsvm  mem    REG    8,2   183024 22416212 /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
ubridge 4085 itsvm  mem    REG    8,2   149760 22416059 /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.34.0
ubridge 4085 itsvm  mem    REG    8,2   755864 22418821 /usr/lib/x86_64-linux-gnu/libzstd.so.1.5.5
ubridge 4085 itsvm  mem    REG    8,2   202904 22423484 /usr/lib/x86_64-linux-gnu/liblzma.so.5.4.5
ubridge 4085 itsvm  mem    REG    8,2  1340976 22424793 /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.4.3
ubridge 4085 itsvm  mem    REG    8,2   910592 22418413 /usr/lib/x86_64-linux-gnu/libsystemd.so.0.38.0
ubridge 4085 itsvm  mem    REG    8,2  2125328 22435670 /usr/lib/x86_64-linux-gnu/libc.so.6
ubridge 4085 itsvm  mem    REG    8,2   137440 22418817 /usr/lib/x86_64-linux-gnu/liblz4.so.1.9.4
ubridge 4085 itsvm  mem    REG    8,2    51536 22423476 /usr/lib/x86_64-linux-gnu/libcap.so.2.66
ubridge 4085 itsvm  mem    REG    8,2   133944 22422241 /usr/lib/x86_64-linux-gnu/libnl-3.so.200.26.0
ubridge 4085 itsvm  mem    REG    8,2   575344 22422221 /usr/lib/x86_64-linux-gnu/libnl-route-3.so.200.26.0
ubridge 4085 itsvm  mem    REG    8,2   317752 22415563 /usr/lib/x86_64-linux-gnu/libdbus-1.so.3.32.4
ubridge 4085 itsvm  mem    REG    8,2   138032 22416612 /usr/lib/x86_64-linux-gnu/libibverbs.so.1.14.50.0
ubridge 4085 itsvm  mem    REG    8,2   313752 22425068 /usr/lib/x86_64-linux-gnu/libpcap.so.1.10.4
ubridge 4085 itsvm  mem    REG    8,2   236616 22435664 /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
ubridge 4085 itsvm    0r   CHR    1,3      0t0        5 /dev/null
ubridge 4085 itsvm    1w   REG    8,2      973 28059017 /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276/ubridge.log
ubridge 4085 itsvm    2w   REG    8,2      973 28059017 /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276/ubridge.log
ubridge 4085 itsvm    3u  IPv4  41210      0t0      TCP localhost:42551 (LISTEN)
ubridge 4085 itsvm    4u  IPv4  41211      0t0      TCP localhost:42551->localhost:34064 (ESTABLISHED)
ubridge 4085 itsvm    5u  IPv4  55777      0t0      UDP localhost:10000->localhost:10001 
ubridge 4085 itsvm    6u  pack  55778      0t0      ALL type=SOCK_RAW

### Log file for first ubridge cloud process

itsvm@BS-Faculty-GNS3-2025-12-22-001-saundeb1:~$ cat /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276/ubridge.log
uBridge version 0.9.19 running with libpcap version 1.10.4 (with TPACKET_V3)
Hypervisor TCP control server started (IP localhost port 42551).
UDP tunnel connecting from local port 10000 to IPv4 address 127.0.0.1 on port 10001
Source NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-2 has started
Destination NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-2 has started
recv: Connection refused
recv: Connection refused
recv: Connection refused
send: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
UDP tunnel connecting from local port 10000 to IPv4 address 127.0.0.1 on port 10001
Destination NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-1 has started
Source NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-1 has started
Capturing to file '/home/itsvm/GNS3/projects/Perf-test/project-files/captures/Cloud1_ens224_to_Ubuntu-CLI-1_eth0.pcap'

### List of open files for ubridge wire process

itsvm@BS-Faculty-GNS3-2025-12-22-001-saundeb1:~$ sudo lsof -p 4125
lsof: WARNING: can't stat() fuse.portal file system /run/user/120/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.portal file system /run/user/1001/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse file system /home/itsvm/thinclient_drives
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.gvfsd-fuse file system /run/user/1001/gvfs
      Output information may be incomplete.
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF     NODE NAME
ubridge 4125 itsvm  cwd    DIR    8,2     4096 28059020 /home/itsvm/GNS3/projects/Perf-test/project-files/qemu/2ceb5127-51c8-40a5-a00b-cf252f9bc681
ubridge 4125 itsvm  rtd    DIR    8,2     4096        2 /
ubridge 4125 itsvm  txt    REG    8,2    85944 22415878 /usr/bin/ubridge
ubridge 4125 itsvm  mem    REG    8,2   183024 22416212 /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
ubridge 4125 itsvm  mem    REG    8,2   149760 22416059 /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.34.0
ubridge 4125 itsvm  mem    REG    8,2   755864 22418821 /usr/lib/x86_64-linux-gnu/libzstd.so.1.5.5
ubridge 4125 itsvm  mem    REG    8,2  1340976 22424793 /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.4.3
ubridge 4125 itsvm  mem    REG    8,2   910592 22418413 /usr/lib/x86_64-linux-gnu/libsystemd.so.0.38.0
ubridge 4125 itsvm  mem    REG    8,2  2125328 22435670 /usr/lib/x86_64-linux-gnu/libc.so.6
ubridge 4125 itsvm  mem    REG    8,2   202904 22423484 /usr/lib/x86_64-linux-gnu/liblzma.so.5.4.5
ubridge 4125 itsvm  mem    REG    8,2   137440 22418817 /usr/lib/x86_64-linux-gnu/liblz4.so.1.9.4
ubridge 4125 itsvm  mem    REG    8,2    51536 22423476 /usr/lib/x86_64-linux-gnu/libcap.so.2.66
ubridge 4125 itsvm  mem    REG    8,2   133944 22422241 /usr/lib/x86_64-linux-gnu/libnl-3.so.200.26.0
ubridge 4125 itsvm  mem    REG    8,2   575344 22422221 /usr/lib/x86_64-linux-gnu/libnl-route-3.so.200.26.0
ubridge 4125 itsvm  mem    REG    8,2   317752 22415563 /usr/lib/x86_64-linux-gnu/libdbus-1.so.3.32.4
ubridge 4125 itsvm  mem    REG    8,2   138032 22416612 /usr/lib/x86_64-linux-gnu/libibverbs.so.1.14.50.0
ubridge 4125 itsvm  mem    REG    8,2   313752 22425068 /usr/lib/x86_64-linux-gnu/libpcap.so.1.10.4
ubridge 4125 itsvm  mem    REG    8,2   236616 22435664 /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
ubridge 4125 itsvm    0r   CHR    1,3      0t0        5 /dev/null
ubridge 4125 itsvm    1w   REG    8,2      836 28059024 /home/itsvm/GNS3/projects/Perf-test/project-files/qemu/2ceb5127-51c8-40a5-a00b-cf252f9bc681/ubridge.log
ubridge 4125 itsvm    2w   REG    8,2      836 28059024 /home/itsvm/GNS3/projects/Perf-test/project-files/qemu/2ceb5127-51c8-40a5-a00b-cf252f9bc681/ubridge.log
ubridge 4125 itsvm    3u  IPv4  42132      0t0      TCP localhost:41465 (LISTEN)
ubridge 4125 itsvm    4u  IPv4  41318      0t0      TCP localhost:41465->localhost:55736 (ESTABLISHED)
ubridge 4125 itsvm    5u  IPv4  56624      0t0      UDP localhost:10003->localhost:10002 
ubridge 4125 itsvm    6u  IPv4  56625      0t0      UDP localhost:10001->localhost:10000 

### Log file for ubridge wire/connection process

itsvm@BS-Faculty-GNS3-2025-12-22-001-saundeb1:~$ cat /home/itsvm/GNS3/projects/Perf-test/project-files/qemu/2ceb5127-51c8-40a5-a00b-cf252f9bc681/ubridge.log
uBridge version 0.9.19 running with libpcap version 1.10.4 (with TPACKET_V3)
Hypervisor TCP control server started (IP localhost port 41465).
UDP tunnel connecting from local port 10003 to IPv4 address 127.0.0.1 on port 10002
UDP tunnel connecting from local port 10001 to IPv4 address 127.0.0.1 on port 10000
Source NIO listener thread for QEMU-2ceb5127-51c8-40a5-a00b-cf252f9bc681-0 has started
Destination NIO listener thread for QEMU-2ceb5127-51c8-40a5-a00b-cf252f9bc681-0 has started
UDP tunnel connecting from local port 10003 to IPv4 address 127.0.0.1 on port 10002
UDP tunnel connecting from local port 10001 to IPv4 address 127.0.0.1 on port 10000
Source NIO listener thread for QEMU-2ceb5127-51c8-40a5-a00b-cf252f9bc681-0 has started
Destination NIO listener thread for QEMU-2ceb5127-51c8-40a5-a00b-cf252f9bc681-0 has started

# Expected performance

Same system but through the Linux Bridge interface

## Change

A linux bridge interface was created and connected to the ens224 interface.  This did NOT change the poor performing connections with the direct ens224 SOCK_RAW interface.

Configuration of the bridge interface

sudo nmcli c add ifname br-PublicNet type bridge con-name br-PublicNet
sudo nmcli c mod 'Wired connection 2' master br-PublicNet slave-type bridge
sudo nmcli c mod br-PublicNet bridge.stp no
sudo nmcli c mod br-PublicNet connection.autoconnect yes
sudo nmcli c mod br-PublicNet ipv4.method disabled
sudo nmcli c mod br-PublicNet ipv6.method ignore
sudo nmcli c down 'Wired connection 2'
sudo nmcli c up 'Wired connection 2'
sudo nmcli c down br-PublicNet
sudo nmcli c up br-PublicNet

It was necessary to disconnect the cloud, enter its configuration and add the br-PublicNet configuration

Then in GNS3 the Ubuntu-CLI object is connected to the cloud via the br-PublicNet interface.

Since this is fundamentally the same LAN no network address changes are necessary.  The Ubuntu machine contined to work without changes.

## Data

### Download client

itsclass@its-uc-xxx:~/tmp$ time git clone https://github.com/librenms/librenms.git
Cloning into 'librenms'...
remote: Enumerating objects: 244383, done.
remote: Counting objects: 100% (48/48), done.
remote: Compressing objects: 100% (40/40), done.
remote: Total 244383 (delta 16), reused 8 (delta 8), pack-reused 244335 (from 2)
Receiving objects: 100% (244383/244383), 327.67 MiB | 10.36 MiB/s, done.
Resolving deltas: 100% (186137/186137), done.
Updating files: 100% (16005/16005), done.

real	0m51.867s
user	0m44.469s
sys	0m13.253s

### Wireshark

In Wireshark the connection contained 279447 Packets of which 337 or 0.1% packet loss

 Data

   4051 ?        Sl     0:28  |   \_ /usr/share/gns3/gns3-gui/bin/python /usr/bin/gns3
   4066 ?        Sl     0:10  |       \_ /usr/share/gns3/gns3-server/bin/python /usr/bin/gns3server --local --allow --log=/home/itsvm/.c
   4085 ?        Sl     0:11  |       |   \_ /usr/bin/ubridge -H localhost:42551
   4123 ?        Sl     4:35  |       |   \_ /usr/bin/qemu-system-x86_64 -name Ubuntu-CLI-1 -m 2048M -smp cpus=2,sockets=1 -enable-kvm -
   4125 ?        Sl     0:08  |       |   \_ /usr/bin/ubridge -H localhost:41465
   4717 ?        Z      0:00  |       \_ [tail] <defunct>
   4718 ?        Z      0:14  |       \_ [wireshark] <defunct>
   5230 ?        Z      0:30  |       \_ [wireshark] <defunct>

### Process list showing GNS3 running on the GNS3 host

itsvm@BS-Faculty-GNS3-2025-12-22-001-saundeb1:~$ sudo ss -npu
Recv-Q        Send-Q               Local Address:Port                Peer Address:Port        Process                                   
0             0                        127.0.0.1:10000                  127.0.0.1:10001        users:(("ubridge",pid=4085,fd=5))        
0             0                        127.0.0.1:10001                  127.0.0.1:10000        users:(("ubridge",pid=4125,fd=6))        
0             0                        127.0.0.1:10003                  127.0.0.1:10002        users:(("ubridge",pid=4125,fd=5)) 

### List of open files for first ubridge cloud process

Note the /dev/net/tun interface being open

itsvm@BS-Faculty-GNS3-2025-12-22-001-saundeb1:~$ sudo lsof -p 4085
lsof: WARNING: can't stat() fuse.portal file system /run/user/120/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.portal file system /run/user/1001/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse file system /home/itsvm/thinclient_drives
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.gvfsd-fuse file system /run/user/1001/gvfs
      Output information may be incomplete.
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF     NODE NAME
ubridge 4085 itsvm  cwd    DIR    8,2     4096 28059016 /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276
ubridge 4085 itsvm  rtd    DIR    8,2     4096        2 /
ubridge 4085 itsvm  txt    REG    8,2    85944 22415878 /usr/bin/ubridge
ubridge 4085 itsvm  mem    REG    8,2   183024 22416212 /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
ubridge 4085 itsvm  mem    REG    8,2   149760 22416059 /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.34.0
ubridge 4085 itsvm  mem    REG    8,2   755864 22418821 /usr/lib/x86_64-linux-gnu/libzstd.so.1.5.5
ubridge 4085 itsvm  mem    REG    8,2   202904 22423484 /usr/lib/x86_64-linux-gnu/liblzma.so.5.4.5
ubridge 4085 itsvm  mem    REG    8,2  1340976 22424793 /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.4.3
ubridge 4085 itsvm  mem    REG    8,2   910592 22418413 /usr/lib/x86_64-linux-gnu/libsystemd.so.0.38.0
ubridge 4085 itsvm  mem    REG    8,2  2125328 22435670 /usr/lib/x86_64-linux-gnu/libc.so.6
ubridge 4085 itsvm  mem    REG    8,2   137440 22418817 /usr/lib/x86_64-linux-gnu/liblz4.so.1.9.4
ubridge 4085 itsvm  mem    REG    8,2    51536 22423476 /usr/lib/x86_64-linux-gnu/libcap.so.2.66
ubridge 4085 itsvm  mem    REG    8,2   133944 22422241 /usr/lib/x86_64-linux-gnu/libnl-3.so.200.26.0
ubridge 4085 itsvm  mem    REG    8,2   575344 22422221 /usr/lib/x86_64-linux-gnu/libnl-route-3.so.200.26.0
ubridge 4085 itsvm  mem    REG    8,2   317752 22415563 /usr/lib/x86_64-linux-gnu/libdbus-1.so.3.32.4
ubridge 4085 itsvm  mem    REG    8,2   138032 22416612 /usr/lib/x86_64-linux-gnu/libibverbs.so.1.14.50.0
ubridge 4085 itsvm  mem    REG    8,2   313752 22425068 /usr/lib/x86_64-linux-gnu/libpcap.so.1.10.4
ubridge 4085 itsvm  mem    REG    8,2   236616 22435664 /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
ubridge 4085 itsvm    0r   CHR    1,3      0t0        5 /dev/null
ubridge 4085 itsvm    1w   REG    8,2     1495 28059017 /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276/ubridge.log
ubridge 4085 itsvm    2w   REG    8,2     1495 28059017 /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276/ubridge.log
ubridge 4085 itsvm    3u  IPv4  41210      0t0      TCP localhost:42551 (LISTEN)
ubridge 4085 itsvm    4u  IPv4  41211      0t0      TCP localhost:42551->localhost:34064 (ESTABLISHED)
ubridge 4085 itsvm    5u  IPv4  68390      0t0      UDP localhost:10000->localhost:10001 
ubridge 4085 itsvm    6u   CHR 10,200    0t190      137 /dev/net/tun

### Log file for first ubridge cloud process

itsvm@BS-Faculty-GNS3-2025-12-22-001-saundeb1:~$ cat /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276/ubridge.log
uBridge version 0.9.19 running with libpcap version 1.10.4 (with TPACKET_V3)
Hypervisor TCP control server started (IP localhost port 42551).
UDP tunnel connecting from local port 10000 to IPv4 address 127.0.0.1 on port 10001
Source NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-2 has started
Destination NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-2 has started
recv: Connection refused
recv: Connection refused
recv: Connection refused
send: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
UDP tunnel connecting from local port 10000 to IPv4 address 127.0.0.1 on port 10001
Destination NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-1 has started
Source NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-1 has started
Capturing to file '/home/itsvm/GNS3/projects/Perf-test/project-files/captures/Cloud1_ens224_to_Ubuntu-CLI-1_eth0.pcap'
UDP tunnel connecting from local port 10000 to IPv4 address 127.0.0.1 on port 10001
Source NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-2 has started
Destination NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-2 has started
recv: Connection refused
Capturing to file '/home/itsvm/GNS3/projects/Perf-test/project-files/captures/Cloud1_br-PublicNet_to_Ubuntu-CLI-1_eth0.pcap'

### List of open files for ubridge wire process

itsvm@BS-Faculty-GNS3-2025-12-22-001-saundeb1:~$ sudo lsof -p 4085
lsof: WARNING: can't stat() fuse.portal file system /run/user/120/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.portal file system /run/user/1001/doc
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse file system /home/itsvm/thinclient_drives
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.gvfsd-fuse file system /run/user/1001/gvfs
      Output information may be incomplete.
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF     NODE NAME
ubridge 4085 itsvm  cwd    DIR    8,2     4096 28059016 /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276
ubridge 4085 itsvm  rtd    DIR    8,2     4096        2 /
ubridge 4085 itsvm  txt    REG    8,2    85944 22415878 /usr/bin/ubridge
ubridge 4085 itsvm  mem    REG    8,2   183024 22416212 /usr/lib/x86_64-linux-gnu/libgcc_s.so.1
ubridge 4085 itsvm  mem    REG    8,2   149760 22416059 /usr/lib/x86_64-linux-gnu/libgpg-error.so.0.34.0
ubridge 4085 itsvm  mem    REG    8,2   755864 22418821 /usr/lib/x86_64-linux-gnu/libzstd.so.1.5.5
ubridge 4085 itsvm  mem    REG    8,2   202904 22423484 /usr/lib/x86_64-linux-gnu/liblzma.so.5.4.5
ubridge 4085 itsvm  mem    REG    8,2  1340976 22424793 /usr/lib/x86_64-linux-gnu/libgcrypt.so.20.4.3
ubridge 4085 itsvm  mem    REG    8,2   910592 22418413 /usr/lib/x86_64-linux-gnu/libsystemd.so.0.38.0
ubridge 4085 itsvm  mem    REG    8,2  2125328 22435670 /usr/lib/x86_64-linux-gnu/libc.so.6
ubridge 4085 itsvm  mem    REG    8,2   137440 22418817 /usr/lib/x86_64-linux-gnu/liblz4.so.1.9.4
ubridge 4085 itsvm  mem    REG    8,2    51536 22423476 /usr/lib/x86_64-linux-gnu/libcap.so.2.66
ubridge 4085 itsvm  mem    REG    8,2   133944 22422241 /usr/lib/x86_64-linux-gnu/libnl-3.so.200.26.0
ubridge 4085 itsvm  mem    REG    8,2   575344 22422221 /usr/lib/x86_64-linux-gnu/libnl-route-3.so.200.26.0
ubridge 4085 itsvm  mem    REG    8,2   317752 22415563 /usr/lib/x86_64-linux-gnu/libdbus-1.so.3.32.4
ubridge 4085 itsvm  mem    REG    8,2   138032 22416612 /usr/lib/x86_64-linux-gnu/libibverbs.so.1.14.50.0
ubridge 4085 itsvm  mem    REG    8,2   313752 22425068 /usr/lib/x86_64-linux-gnu/libpcap.so.1.10.4
ubridge 4085 itsvm  mem    REG    8,2   236616 22435664 /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
ubridge 4085 itsvm    0r   CHR    1,3      0t0        5 /dev/null
ubridge 4085 itsvm    1w   REG    8,2     1495 28059017 /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276/ubridge.log
ubridge 4085 itsvm    2w   REG    8,2     1495 28059017 /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276/ubridge.log
ubridge 4085 itsvm    3u  IPv4  41210      0t0      TCP localhost:42551 (LISTEN)
ubridge 4085 itsvm    4u  IPv4  41211      0t0      TCP localhost:42551->localhost:34064 (ESTABLISHED)
ubridge 4085 itsvm    5u  IPv4  68390      0t0      UDP localhost:10000->localhost:10001 
ubridge 4085 itsvm    6u   CHR 10,200    0t190      137 /dev/net/tun

### Log file for ubridge wire/connection process

itsvm@BS-Faculty-GNS3-2025-12-22-001-saundeb1:~$ cat /home/itsvm/GNS3/projects/Perf-test/project-files/builtin/13206a64-e3dd-47f1-95c1-a94fa3126276/ubridge.log
uBridge version 0.9.19 running with libpcap version 1.10.4 (with TPACKET_V3)
Hypervisor TCP control server started (IP localhost port 42551).
UDP tunnel connecting from local port 10000 to IPv4 address 127.0.0.1 on port 10001
Source NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-2 has started
Destination NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-2 has started
recv: Connection refused
recv: Connection refused
recv: Connection refused
send: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
recv: Connection refused
UDP tunnel connecting from local port 10000 to IPv4 address 127.0.0.1 on port 10001
Destination NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-1 has started
Source NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-1 has started
Capturing to file '/home/itsvm/GNS3/projects/Perf-test/project-files/captures/Cloud1_ens224_to_Ubuntu-CLI-1_eth0.pcap'
UDP tunnel connecting from local port 10000 to IPv4 address 127.0.0.1 on port 10001
Source NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-2 has started
Destination NIO listener thread for 13206a64-e3dd-47f1-95c1-a94fa3126276-2 has started
recv: Connection refused
Capturing to file '/home/itsvm/GNS3/projects/Perf-test/project-files/captures/Cloud1_br-PublicNet_to_Ubuntu-CLI-1_eth0.pcap'
