# Brannmurregler

Regelene er satt på hvert VLAN-interface i pfSense. Reglene vurderes ovenfra og ned, så rekkefølgen betyr noe.

## TRUSTED

| # | Action | Source       | Destination     | Port   | Kommentar                                     |
|---|--------|--------------|-----------------|--------|-----------------------------------------------|
| 1 | Pass   | TRUSTED-net  | This Firewall   | 53     | DNS til pfSense                               |
| 2 | Pass   | TRUSTED-net  | This Firewall   | 80,443 | pfSense web-UI                                |
| 3 | Pass   | TRUSTED-net  | IOT-net         | any    | Lov å nå IOT (styre lys fra appen)            |
| 4 | Block  | TRUSTED-net  | GUEST-net       | any    | Ingen grunn til at TRUSTED snakker med GUEST  |
| 5 | Pass   | TRUSTED-net  | any             | any    | Lov ut på internett                           |

## IOT

| # | Action | Source   | Destination   | Port | Kommentar                                |
|---|--------|----------|---------------|------|------------------------------------------|
| 1 | Pass   | IOT-net  | This Firewall | 53   | DNS                                      |
| 2 | Pass   | IOT-net  | This Firewall | 67   | DHCP                                     |
| 3 | Block  | IOT-net  | RFC1918       | any  | IOT skal ikke nå andre interne nett      |
| 4 | Pass   | IOT-net  | any           | 443  | Skytjenester                             |
| 5 | Pass   | IOT-net  | any           | 123  | NTP                                      |
| 6 | Block  | IOT-net  | any           | any  | Default deny                             |

## GUEST

| # | Action | Source     | Destination   | Port | Kommentar                              |
|---|--------|------------|---------------|------|----------------------------------------|
| 1 | Pass   | GUEST-net  | This Firewall | 53   | DNS                                    |
| 2 | Pass   | GUEST-net  | This Firewall | 67   | DHCP                                   |
| 3 | Block  | GUEST-net  | RFC1918       | any  | Ingen tilgang til interne nett         |
| 4 | Pass   | GUEST-net  | any           | any  | Lov ut på internett                    |

## Det som ikke var åpenbart

- pfSense har default deny på alle interfacer utenom LAN. Jeg lagde TRUSTED som nytt interface og fikk ingen trafikk før jeg satte regler. Brukte en halvtime på å finne ut av det.
- "This Firewall" er en innebygd alias som dekker alle pfSense-IP-er. Mye bedre enn å hardkode IP-en til hvert interface – jeg slipper å oppdatere reglene om jeg bytter IP på et interface.
- For RFC1918-blokken trengte jeg en alias som dekker 10.0.0.0/8, 172.16.0.0/12 og 192.168.0.0/16. Default har ikke pfSense den – jeg lagde den selv.
- Logging er av som default på hver regel. Skrudde på logging på blokk-reglene så jeg kan se i Status → System Logs hvis noe rart skjer.
