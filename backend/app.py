"""Local Flask API for Parallel Universe Scanner. Camera frames are never received or stored."""
from flask import Flask, jsonify, send_from_directory
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
app = Flask(__name__, static_folder=str(ROOT / "dist"), static_url_path="")

UNIVERSES = [
    {"id": "aetheria", "name": "AETHERIA", "tag": "The Realm of Ancient Magic", "color": "#b98bff"},
    {"id": "nexora", "name": "NEXORA", "tag": "The Future Civilization", "color": "#55efff"},
    {"id": "velmora", "name": "VELMORA", "tag": "The Oceanic Kingdom", "color": "#3eddeb"},
    {"id": "lunaria", "name": "LUNARIA", "tag": "The Dream Universe", "color": "#ffa1e8"},
    {"id": "drakonia", "name": "DRAKONIA", "tag": "The Dragon Realm", "color": "#ff8a51"},
    {"id": "chronovia", "name": "CHRONOVIA", "tag": "The Universe of Time", "color": "#ffd36d"},
]

@app.get("/api/universes")
def universes(): return jsonify(UNIVERSES)

@app.get("/api/universe/<universe_id>")
def universe(universe_id):
    match = next((u for u in UNIVERSES if u["id"] == universe_id.lower()), None)
    return (jsonify(match), 200) if match else (jsonify({"error": "Unknown universe"}), 404)

@app.get("/")
def home(): return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__": app.run(debug=True, port=5000)
