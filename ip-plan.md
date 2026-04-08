# IP-plan og topologi

## VLAN-oversikt

| VLAN | Navn    | Nett             | Gateway      | Bruk                        |
|------|---------|------------------|--------------|-----------------------------|
| 10   | TRUSTED | 10.10.10.0/24    | 10.10.10.1   | PC, telefon, printer        |
| 20   | IOT     | 10.10.20.0/24    | 10.10.20.1   | Smartlys, smart-TV          |
| 30   | GUEST   | 10.10.30.0/24    | 10.10.30.1   | Gjester                     |

WAN: DHCP fra ISP.

## Topologi

```
[Internett]
     |
[ISP-router i bridge-modus]
     |
[pfSense WAN]
     |
[pfSense LAN] --- vSwitch (VLAN 10, 20, 30 tagget)
                       |
                  [ASUS AP]  --- WiFi, en SSID per VLAN
                       |
                  (klienter)
```

ASUS-routeren kan ikke tagge VLAN selv. Den fungerer kun som access point. Faktisk VLAN-tagging gjøres i VMware sin vSwitch og i pfSense.

## DHCP

pfSense kjører DHCP-server på alle tre interfacer.

- TRUSTED: 10.10.10.100–200
- IOT: 10.10.20.100–200
- GUEST: 10.10.30.100–150

DNS settes til pfSense, som videresender til 1.1.1.1.

## VPN-nettverk

WireGuard-tunnel: 10.99.99.0/24. Klienter får 10.99.99.x og kan rute inn til TRUSTED.
