from flask import Flask, jsonify, request
from datetime import datetime
import json
import os

app = Flask(__name__)

# Simple in-memory storage (for demo purposes)
plants = [
    {
        'id': 1,
        'name': 'Lechuga',
        'species': 'Lactuca sativa',
        'category': 'hortalizas',
        'location': 'Jardín A',
        'status': 'growing',
        'planting_date': '2024-01-15'
    },
    {
        'id': 2,
        'name': 'Tomate',
        'species': 'Solanum lycopersicum',
        'category': 'hortalizas',
        'location': 'Jardín A',
        'status': 'growing',
        'planting_date': '2024-01-20'
    },
    {
        'id': 3,
        'name': 'Limón Tahití',
        'species': 'Citrus × latifolia',
        'category': 'frutales',
        'location': 'Huerto B',
        'status': 'growing',
        'planting_date': '2024-01-10'
    }
]

tasks = [
    {
        'id': 1,
        'title': 'Riego matutino',
        'description': 'Regar plantas del jardín A',
        'task_type': 'riego',
        'due_date': '2024-01-25',
        'completed': False
    },
    {
        'id': 2,
        'title': 'Aplicar compost orgánico',
        'description': 'Fertilizar con compost de café y cáscaras',
        'task_type': 'fertilizar',
        'due_date': '2024-01-26',
        'completed': False
    }
]

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to HaciendaOps API',
        'status': 'running',
        'version': '1.0',
        'endpoints': {
            'status': '/api/status',
            'plants': '/api/plants',
            'tasks': '/api/tasks'
        }
    })

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'active',
        'message': 'HaciendaOps API is running',
        'version': '1.0',
        'description': 'Sustainable Agriculture & Ecotourism Management System',
        'author': 'Based on Yorby Duartes project',
        'features': [
            'Plant inventory management',
            'Task scheduling (riego, fertilizar, poda)',
            'Organic care tracking',
            'Lunar calendar integration',
            'Financial tracking',
            'Recipe management'
        ]
    })

@app.route('/api/plants', methods=['GET', 'POST'])
def handle_plants():
    if request.method == 'GET':
        return jsonify(plants)
    
    elif request.method == 'POST':
        new_plant = request.get_json()
        new_plant['id'] = len(plants) + 1
        new_plant['planting_date'] = datetime.now().strftime('%Y-%m-%d')
        plants.append(new_plant)
        return jsonify(new_plant), 201

@app.route('/api/plants/<int:plant_id>')
def get_plant(plant_id):
    plant = next((p for p in plants if p['id'] == plant_id), None)
    if plant:
        return jsonify(plant)
    return jsonify({'error': 'Plant not found'}), 404

@app.route('/api/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'GET':
        return jsonify(tasks)
    
    elif request.method == 'POST':
        new_task = request.get_json()
        new_task['id'] = len(tasks) + 1
        new_task['completed'] = False
        tasks.append(new_task)
        return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['completed'] = True
        return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    print("🌱 Starting HaciendaOps API...")
    print("📍 Access the API at: http://localhost:5000")
    print("📊 Check status at: http://localhost:5000/api/status")
    print("🌿 View plants at: http://localhost:5000/api/plants")
    app.run(debug=True, host='0.0.0.0', port=5000)
