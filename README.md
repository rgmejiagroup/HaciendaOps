# 🌱 HaciendaOps – Field Guide System

**HaciendaOps** is a documentation-first knowledge system supporting sustainable agriculture and ecotourism teams in rural Nicaragua. Originally designed as a Flask API, this project now focuses on structured field knowledge, Kaizen workflows, and educational integration.

## 🧭 Field Guide Overview

This repository includes a Markdown-based training and operations guide used by rural teams and students to support sustainable farming and eco-projects across 2,000+ manzanas of land.

**Docs Live In:** `docs/field_guide/`

- `plant.md` – Medicinal, aromatic, and food crops
- `animal.md` – Livestock specs (e.g., Pelibuey goats)
- `tool.md` – Equipment profiles + safety/Kaizen notes
- `overview.md` – How to use the Field Guide system

---

## 🛠️ Kaizen Integration

Field workers submit improvement ideas using:
- `docs/kaizen_entry_template.md`

Once approved, Kaizen entries are added to the official Markdown pages for future reference and process tuning.

---

## 🎓 Educational Use Case

This project was restructured as part of a university-level documentation course to demonstrate:
- Multi-layered documentation design
- Integration of field, operational, and legal insights
- Modular growth from docs to API → automation

---

## 📂 Example Use Flow

1. A worker scans a QR code at a planting site.
2. They reference the relevant `plant.md` entry for care instructions.
3. If a better method is discovered, they log a Kaizen proposal.
4. Once approved, the `docs/` folder is updated with the new best practice.

---

## 💡 Future Integration Possibilities

When ready, this Markdown-based system can sync with:
- 🛠️ `master_server.py` → For voice/photo reporting
- 📡 `websocket_sync.py` → Live dashboard updates
- 🧾 `audit_logger.py` → Immutable activity records

These are included in local development but are **not active parts of the current doc-only deployment**.

---

## 👤 Credits & License

Based on the field methodology and sustainability vision of **Yorby Duartes**.

MIT License · Educational Use Only

---

> “Simple documentation today builds intelligent ecosystems tomorrow.” – Los Primos Unidos
