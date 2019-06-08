#Configurando internet en la BBG
echo l > /proc/sys/net/ipv4/ip_forward

internal=usb1
external=

/sbin/iptables -t nat -A POSTRUTING-o $external -j MASQUERADE
/sbin/iiptables -A FORWARD -i $external -o $internal -m state --state RELATED,ESTABLISHED -j ACCEPT
/sbin/iptables -A FORWARD -i $internal -o $external -j ACCEPT
