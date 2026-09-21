from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="QuantumScape Genealogy API Demo - Meeting 1",
    version="0.1.0",
)

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

@app.get("/")
def root():
    return {
        "message": "QuantumScape Genealogy API Demo - Meeting 1",
        "docs": "/docs",
        "example": "/api/genealogy/BATTERY-01",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/genealogy/{battery_id}")
def get_genealogy(battery_id: str):
    normalized_id = battery_id.upper()
    path = SYNTHETIC_DATA.get(normalized_id)

    if path is None:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown unit '{normalized_id}'.",
        )

    return {
        "battery_id": normalized_id,
        "direction": "upstream",
        "data_source": "synthetic",
        "path": path,
    }