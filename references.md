Reference:
```
https://batteryspotlight.com/how-are-solid-state-batteries-made/
https://eureka.patsnap.com/article/what-are-transition-metal-oxides-in-battery-chemistry
```
# Components:
- anode (lithum)
- cathode (lithium oxides, let's just say made from nickel for now)
- solid electrolyte (ceramic maybe)

# Manufacturing process:
- powder formation (homogenizing / mixing)
- electrode fabrication (some form of pressing)
- layer assembly (lamination and such?)
- sintering (heating layers to fuse w/o melting)
- sealing (seal in protective packaging)

### Possible database:
```
SYNTHETIC_DATA = {
    "BATTERY-01": [
        {"id": "LOT-LI-44", "type": "material", "label": "Lithium Anode Lot 44"},
        {"id": "LOT-CATH-31", "type": "material", "label": "Nickel Oxide Cathode Lot 31"},
        {"id": "LOT-SE-12", "type": "material", "label": "Solid Electrolyte Ceramic Lot 12"},

        {"id": "MIX-208", "type": "process", "label": "Powder Mixing - Mixer 02"},
        {"id": "PRESS-114", "type": "process", "label": "Electrode Pressing - Press 01"},
        {"id": "LAM-551", "type": "process", "label": "Layer Assembly - Laminator 04"},
        {"id": "SINT-302", "type": "process", "label": "Sintering - Furnace 03"},
        {"id": "SEAL-209", "type": "process", "label": "Cell Sealing - Sealer 02"},

        {"id": "CELL-701", "type": "assembly", "label": "Cell 701"},
        {"id": "BATTERY-01", "type": "unit", "label": "Battery 01"}
    ]
}
```