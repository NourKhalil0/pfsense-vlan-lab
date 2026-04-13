# WireGuard VPN

Brukes for å nå hjemmenettet når jeg er ute.

## Konfig på pfSense

- Tunnel-nett: 10.99.99.0/24
- Port: 51820/UDP
- Listen på WAN

Klienter får IP fra 10.99.99.0/24-rangen.

## Klient (telefon)

Installerte WireGuard-appen og scannet QR-koden pfSense genererte. Det funket på første forsøk.

Det som måtte fikses for at det skulle gå:

- Brannmurregel på WAN som slipper inn 51820/UDP. Ikke standard.
- Rute 10.10.10.0/24 (TRUSTED) gjennom tunnelen, ikke alt. Hvis jeg ruter alt, går mobildata-bruken opp og det er litt unødvendig.

## Sjekkliste når jeg legger til ny klient

1. Generer ny peer i pfSense WireGuard-konfig
2. Sett AllowedIPs på serversiden til klientens tunnel-IP /32
3. Eksporter konfig (QR-kode eller .conf-fil)
4. Test fra mobildata. Ikke fra WiFi hjemme – da går trafikk uansett ikke gjennom tunnelen

## Hvorfor WireGuard

Pensum bruker mest IPsec og OpenVPN, men WireGuard kom inn i pfSense som offisiell pakke. Jeg ville se hva det faktisk innebar å sette det opp. Konfigfilen er kortere enn jeg trodde, og det var lettere å forstå hva som faktisk skjer mellom server og klient.
