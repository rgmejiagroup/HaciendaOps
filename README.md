# HaciendaOps Field Guide

## 📘 Sustainable Agriculture Documentation System

**HaciendaOps** is a documentation-first project designed to support training, operations, and continuous improvement for organic farms and ecotourism sanctuaries.  

This repository currently focuses on a **lightweight Field Guide** that captures key agricultural knowledge in a structured, accessible format.

> 🔎 This version is *documentation-only* and is being developed as part of a university-level course on usability and technical writing. Future code-based components (e.g., syncing with `master_server.py`) will be added separately.

---

## 🌿 Project Purpose

The Field Guide supports:
- 📚 Learning for interns and new workers
- 🧠 Reference material for sustainable agriculture teams
- ✍️ Kaizen-style feedback from the field
- 🛠️ Preparation for future software automation (optional)

---

## 📁 Repository Contents

### `docs/field_guide/`
Structured data files written in Markdown (JSON-style):

| File              | Description                                                 |
|-------------------|-------------------------------------------------------------|
| `plant.md`        | Organic and medicinal plants, care zones, toxicity, usage   |
| `animal.md`       | Livestock profiles and traits (e.g., Pelibuey goats)        |
| `tool.md`         | Basic tools used in the field, with safety notes            |

### `docs/`
Additional documentation and submission materials:

| File                        | Description                                                   |
|-----------------------------|---------------------------------------------------------------|
| `overview.md`               | Overview of the Field Guide system and how it’s used          |
| `kaizen_entry_template.md`  | Template for proposing improvements or observations from the field |

---

## 🧪 Educational Context

This repository was built as part of a technical writing and usability course, with the following goals:

- 🛠️ Design documentation that can be used remotely and without moderation
- ✍️ Structure reference material for farm workers and students
- 🧭 Plan future integrations with automation and smart farm APIs

---

## 🧭 Future Integration Plans (Documentation Only)

The structure here is designed to support eventual connection to:
- `master_server.py` and `shared_data_service.py`
- Real-time goat and crop tracking systems
- Voice-based data entry and API sync for field conditions

> But for now, the **focus is strictly on documentation and usability testing**.

---

## 🧠 How the Field Guide Works

Each entry in the Field Guide (plant, animal, or tool) includes:

- `id`: Unique internal reference
- `name` or `species`
- `uses`, `zones`, or `traits`
- `kaizen_notes`: A field for observations or feedback

Approved suggestions from the field can be added via the `kaizen_entry_template.md`.

---

## 💡 Example Use Case

> A new intern is assigned to clear brush and monitor goats. They check:
>
> - `tool.md` → Safe handling of machetes  
> - `plant.md` → Which plants are toxic to goats  
> - `animal.md` → How to identify goats via RFID  
> - `kaizen_entry_template.md` → Submit a field note for future improvement

---

## 🗂️ Next Steps for Contributors

If you’d like to contribute:
- Submit new `plant`, `animal`, or `tool` entries
- Propose edits to `overview.md` for clarity
- Use `kaizen_entry_template.md` to suggest improvements

This project welcomes feedback from farmers, interns, and sustainability researchers.

---

## 📄 License

MIT License — for educational and documentation use.

---

**"Connecting people with nature through sustainable agriculture, organic food, and holistic wellness — one field guide at a time."**
