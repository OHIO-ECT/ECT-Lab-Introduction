# WARNING - DO NOT THIS TASK UNLESS YOU ARE EXPLICITLY DIRECTED TO.

```bash
# Store IPv4/IPv6 settings from Wired connection 1
IPV4_METHOD=$(nmcli -g ipv4.method c show 'Wired connection 1')
IPV4_ADDR=$(nmcli -g ipv4.addresses c show 'Wired connection 1')
IPV4_GW=$(nmcli -g ipv4.gateway c show 'Wired connection 1')
IPV4_DNS=$(nmcli -g ipv4.dns c show 'Wired connection 1')
IPV6_METHOD=$(nmcli -g ipv6.method c show 'Wired connection 1')
IPV6_ADDR=$(nmcli -g ipv6.addresses c show 'Wired connection 1')
IPV6_GW=$(nmcli -g ipv6.gateway c show 'Wired connection 1')
IPV6_DNS=$(nmcli -g ipv6.dns c show 'Wired connection 1')

sudo nmcli c down 'Wired connection 1'
sudo nmcli c mod 'Wired connection 1' ipv4.method disabled
sudo nmcli c mod 'Wired connection 1' ipv6.method disabled
sudo nmcli c add ifname br-10-110 type bridge con-name br-10-110
sudo nmcli c mod 'Wired connection 1' master br-10-110 slave-type bridge
sudo nmcli c mod br-10-110 bridge.stp no
sudo nmcli c mod br-10-110 connection.autoconnect yes

# Apply stored IPv4 settings to bridge
[ -n "$IPV4_ADDR" ] && sudo nmcli c mod br-10-110 ipv4.addresses "$IPV4_ADDR"
[ -n "$IPV4_GW" ] && sudo nmcli c mod br-10-110 ipv4.gateway "$IPV4_GW"
[ -n "$IPV4_DNS" ] && sudo nmcli c mod br-10-110 ipv4.dns "$IPV4_DNS"
sudo nmcli c mod br-10-110 ipv4.method "$IPV4_METHOD"

# Apply stored IPv6 settings to bridge
[ -n "$IPV6_ADDR" ] && sudo nmcli c mod br-10-110 ipv6.addresses "$IPV6_ADDR"
[ -n "$IPV6_GW" ] && sudo nmcli c mod br-10-110 ipv6.gateway "$IPV6_GW"
[ -n "$IPV6_DNS" ] && sudo nmcli c mod br-10-110 ipv6.dns "$IPV6_DNS"
sudo nmcli c mod br-10-110 ipv6.method "$IPV6_METHOD"

sudo nmcli c down br-10-110
sudo nmcli c up br-10-110
```

```bash
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

```bash
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
