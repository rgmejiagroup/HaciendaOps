# HaciendaOps API

## Sustainable Agriculture & Ecotourism Management System

Based on Yorby Duartes' comprehensive sustainable agriculture project, HaciendaOps is a Flask-based API for managing organic farms, ecotourism sanctuaries, and holistic wellness experiences.

## 🌱 Project Overview

This system combines:
- **Organic Agriculture Management** - Track 200+ plant species with organic care schedules
- **Ecotourism Operations** - Manage visitor experiences and wellness retreats  
- **Financial Tracking** - Monitor expenses, revenue, and sustainability metrics
- **Task Automation** - Lunar calendar-based scheduling for optimal plant care
- **Holistic Integration** - Mind-body-spirit connection through nature

## 🚀 Features

### Plant Management
- Inventory tracking for vegetables, fruits, herbs, and medicinal plants
- Organic care schedules (riego, fertilizar, poda, control de plagas)
- Growth monitoring and harvest planning
- Location-based organization

### Task Scheduling  
- Automated reminders for plant care activities
- Lunar calendar integration for optimal timing
- Organic compost and pest control recipes
- Maintenance tracking


🧭 Field Guide & Documentation
This repository includes a training-oriented Field Guide for rural teams and students using the system in real-world environments.

📂 docs/field_guide/ contains:

-plant.md – Organic and medicinal plants tracked by zone and usage
-animal.md – Livestock profiles (e.g., Pelibuey goats)
-tool.md – Basic field tools with safety and Kaizen notes

📄 Additional Docs:

-overview.md – Purpose of the Field Guide
-kaizen_entry_template.md – Template for submitting field-based improvements and insights

This system supports Kaizen integration: field workers can submit suggestions that are reviewed and linked to live entries via kaizen_notes.

✨ This Field Guide is also being used as part of an educational deliverable for a university-level documentation course focused on building real-world, integrated technical projects.

### API Endpoints

#### Plants
- `GET /api/plants` - List all plants
- `POST /api/plants` - Add new plant
- `GET /api/plants/{id}` - Get plant details
- `PUT /api/plants/{id}` - Update plant info
- `DELETE /api/plants/{id}` - Remove plant

#### Tasks
- `GET /api/tasks` - List all tasks
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/{id}/complete` - Mark task complete

#### Status
- `GET /api/status` - API health and info

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Local Development
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/HaciendaOps.git
cd HaciendaOps

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

### Access the API
- **Application**: http://localhost:5000
- **API Documentation**: http://localhost:5000/docs/
- **Sample API Call**: http://localhost:5000/api/status

## 📊 Sample Data

The application includes sample data based on the original project:

### Plants Categories
- **Hortalizas**: Lechuga, Tomate, Cilantro, Espinaca
- **Frutales**: Limón Tahití, Aguacate, Mango, Papaya  
- **Aromáticos**: Albahaca, Menta, Romero
- **Especias**: Orégano, Tomillo, Cúrcuma
- **Medicinales**: Sábila, Ruda, Cola de caballo

### Organic Care Tasks
- **Riego**: Daily watering schedules
- **Fertilizar**: Organic compost application (coffee grounds, eggshells, ash)
- **Control de plagas**: Natural pest control (garlic, vinegar, bicarbonate)
- **Poda**: Pruning based on lunar calendar

## 🌙 Lunar Calendar Integration

Based on the original project's emphasis on natural cycles:
- **Planting**: New moon phase
- **Fertilizing**: Days 25-30 each month  
- **Pruning**: Days 18-25 each month
- **Pest Control**: Days 2-11 each month

## 🌿 Organic Recipes

### Solid Compost
- Coffee grounds (dried)
- Eggshells (crushed)
- Wood ash
- Lime (50g)
- Black soil

### Liquid Fertilizer  
- Rice water (fermented)
- Banana peels
- Cinnamon powder
- Onion scraps

### Pest Control Mix
- Garlic cloves (3, crushed)
- White vinegar (200ml)
- Baking soda (10 córdobas worth)

## 💰 Economic Model

### Investment Phases
- **Phase 1**: Garden setup - $5,500
- **Phase 2**: Infrastructure - $4,500  
- **Phase 3**: Operations - $50,000/year

### Revenue Streams
- **Day passes**: $20,000/month
- **Organic café**: $15,000/month
- **Fresh produce**: $15,000/month
- **Total projected**: $50,000/month

## 🎯 Future Features

- [ ] Mobile app integration
- [ ] IoT sensor integration for automated monitoring
- [ ] Financial reporting and analytics
- [ ] Recipe management for seasonal menus
- [ ] Animal tracking (tilapia, chickens, pigs)
- [ ] Visitor booking system
- [ ] Weather integration
- [ ] Multi-language support

## 📚 Based on Original Research

This project implements concepts from Yorby Duartes' comprehensive research including:
- Sustainable agriculture practices
- Ecotourism sanctuary development  
- Holistic wellness integration
- Aquaponics systems
- Higher consciousness connection through nature

## 🤝 Contributing

This is an educational project. Contributions welcome for:
- Additional plant species data
- Organic care recipe improvements
- API endpoint enhancements
- Documentation updates

## 📄 License

MIT License - See LICENSE file for details

## 👤 Author

Educational project based on Yorby Duartes' sustainable agriculture research.

---

**"Connecting people with nature through sustainable agriculture, organic food production, and holistic wellness experiences"**
