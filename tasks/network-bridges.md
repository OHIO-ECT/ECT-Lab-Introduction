# WARNING - DO NOT THIS TASK UNLESS YOU ARE EXPLICITLY DIRECTED TO.

```
sudo nmcli c down 'Wired connection 2'
sudo nmcli c mod 'Wired connection 2' ipv4.method disabled
sudo nmcli c mod 'Wired connection 2' ipv6.method disabled
sudo nmcli c add ifname br-PublicNet type bridge con-name br-PublicNet
sudo nmcli c mod 'Wired connection 2' master br-PublicNet slave-type bridge
sudo nmcli c mod br-PublicNet bridge.stp no
sudo nmcli c mod br-PublicNet connection.autoconnect yes
sudo nmcli c mod br-PublicNet ipv4.method disabled
sudo nmcli c mod br-PublicNet ipv6.method disabled
sudo nmcli c down br-PublicNet
sudo nmcli c up br-PublicNet
```

```
sudo nmcli c down 'Wired connection 3'
sudo nmcli c mod 'Wired connection 3' ipv4.method disabled
sudo nmcli c mod 'Wired connection 3' ipv6.method disabled
sudo nmcli c add ifname br-zOtherNet type bridge con-name br-zOtherNet
sudo nmcli c mod 'Wired connection 3' master br-zOtherNet slave-type bridge
sudo nmcli c mod br-zOtherNet bridge.stp no
sudo nmcli c mod br-zOtherNet connection.autoconnect yes
sudo nmcli c mod br-zOtherNet ipv4.method disabled
sudo nmcli c mod br-zOtherNet ipv6.method disabled
sudo nmcli c down br-zOtherNet
sudo nmcli c up br-zOtherNet
```
