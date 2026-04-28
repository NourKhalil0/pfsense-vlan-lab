# pfsense-vlan-lab

Hjemmenett-lab med pfSense i VMware. Tre VLAN (TRUSTED, IOT, GUEST) og WireGuard for fjerntilgang. Satt opp ved siden av Cisco Networking-stoffet på studiet.

## Kjøre gateway-sjekk

```
python scripts/check_gateways.py
```

Pinger gatewayen i hvert VLAN. Exit 1 hvis noen ikke svarer.

## Hva jeg lærte

VLAN i seg selv gjør ikke nettet sikrere – det er brannmurreglene mellom dem som gjør jobben. Brukte en stund på å skjønne at nye pfSense-interfacer har default deny på all trafikk, mens LAN har default allow.
