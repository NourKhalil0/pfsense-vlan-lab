# Feilsøking

Problemer jeg har truffet på i oppsettet. Mest notater til meg selv.

## VLAN 20 fikk ikke DHCP

Symptom: enhet på IOT-nettet fikk ingen IP.

Det jeg sjekket:

1. DHCP-server aktivert på IOT-interfacet → OK
2. Pakkefangst på pfSense (Diagnostics → Packet Capture på IOT) viste at DHCPDISCOVER kom inn → OK
3. Men ingen DHCPOFFER gikk ut

Årsak: DHCP-rangen jeg hadde satt overlappet med en statisk IP jeg hadde reservert for en test. Endret rangen og det fikset seg.

## Gjest kunne plutselig se TRUSTED

Symptom: kjørte `nmap` fra mobilen koblet til gjestenettet og fant min PC.

Årsak: jeg hadde lagt til en midlertidig "allow any" regel for å teste internettilgang under oppsettet, og glemt å fjerne den.

Læring: rydd opp etter testing. pfSense har en "disabled" toggle på regler, så jeg kan deaktivere en regel uten å slette den. Bedre enn å legge til på nytt senere.

## pfSense web-UI utilgjengelig etter VLAN-bytte

Symptom: byttet management-interface fra LAN til TRUSTED, og web-UI svarte ikke etter reboot.

Årsak: pfSense bytter management-IP når man bytter interface. Jeg var fortsatt koblet til den gamle IP-en. Måtte inn på VM-konsollen og resette LAN derfra.

Læring: ikke endre management-konfig uten konsolltilgang for hånden.

## WireGuard ga ingen handshake

Symptom: klient sa "no handshake" i appen.

Sjekklisten jeg gikk gjennom:

1. WAN-regel for 51820/UDP åpen → OK
2. Klientens public key matchet det pfSense hadde lagret → OK
3. Endpoint i klient-konfigen pekte på riktig hjemme-IP

Det som var galt: ISP-en hadde gitt meg en CGNAT-adresse. Sjekket på whatismyipaddress.com og fikk en 100.64.x-adresse. Måtte ringe ISP og be om ekte offentlig IP.

Læring: sjekk om du faktisk har en offentlig IP før du klandrer konfigen.

## pfSense reagerte tregt etter en stund

Symptom: web-UI ble seigt, og pakketap på TRUSTED.

Årsak: VM-en hadde fått for lite RAM (1 GB). Pakkebufferet ble fullt. Økte til 2 GB og det ble bra igjen.

Læring: pfSense klarer seg med lite, men ikke 1 GB hvis det er noen klienter på det.
