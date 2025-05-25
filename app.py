from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'hacienda-dev-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///hacienda.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    
    # Create API with documentation
    api = Api(
        app,
        title='HaciendaOps API',
        version='1.0',
        description='Sustainable Agriculture & Ecotourism Management System\n\nBased on Yorby Duartes sustainable agriculture project',
        doc='/docs/'  # Swagger documentation at /docs/
    )
    
    # Sample Plant model
    class Plant(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        species = db.Column(db.String(100), nullable=False)
        category = db.Column(db.String(50), nullable=False)  # hortalizas, frutales, etc.
        planting_date = db.Column(db.DateTime, default=datetime.utcnow)
        harvest_date = db.Column(db.DateTime)
        status = db.Column(db.String(20), default='growing')  # growing, ready, harvested
        location = db.Column(db.String(100))
        care_notes = db.Column(db.Text)
        
        def to_dict(self):
            return {
                'id': self.id,
                'name': self.name,
                'species': self.species,
                'category': self.category,
                'planting_date': self.planting_date.isoformat() if self.planting_date else None,
                'harvest_date': self.harvest_date.isoformat() if self.harvest_date else None,
                'status': self.status,
                'location': self.location,
                'care_notes': self.care_notes
            }
    
    # Sample Task model
    class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(200), nullable=False)
        description = db.Column(db.Text)
        task_type = db.Column(db.String(50), nullable=False)  # riego, fertilizar, poda, etc.
        due_date = db.Column(db.DateTime, nullable=False)
        completed = db.Column(db.Boolean, default=False)
        plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'))
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        
        def to_dict(self):
            return {
                'id': self.id,
                'title': self.title,
                'description': self.description,
                'task_type': self.task_type,
                'due_date': self.due_date.isoformat() if self.due_date else None,
                'completed': self.completed,
                'plant_id': self.plant_id,
                'created_at': self.created_at.isoformat() if self.created_at else None
            }
    
    # API Namespaces
    plants_ns = api.namespace('plants', description='Plant management operations')
    tasks_ns = api.namespace('tasks', description='Task scheduling and management')
    
    # Plants API endpoints
    @plants_ns.route('/')
    class PlantList(Resource):
        def get(self):
            """Get all plants"""
            plants = Plant.query.all()
            return [plant.to_dict() for plant in plants]
        
        def post(self):
            """Add a new plant"""
            data = api.payload
            plant = Plant(
                name=data.get('name'),
                species=data.get('species'),
                category=data.get('category'),
                location=data.get('location'),
                care_notes=data.get('care_notes')
            )
            db.session.add(plant)
            db.session.commit()
            return plant.to_dict(), 201
    
    @plants_ns.route('/<int:plant_id>')
    class PlantDetail(Resource):
        def get(self, plant_id):
            """Get plant by ID"""
            plant = Plant.query.get_or_404(plant_id)
            return plant.to_dict()
        
        def put(self, plant_id):
            """Update plant information"""
            plant = Plant.query.get_or_404(plant_id)
            data = api.payload
            
            plant.name = data.get('name', plant.name)
            plant.species = data.get('species', plant.species)
            plant.category = data.get('category', plant.category)
            plant.location = data.get('location', plant.location)
            plant.care_notes = data.get('care_notes', plant.care_notes)
            plant.status = data.get('status', plant.status)
            
            db.session.commit()
            return plant.to_dict()
        
        def delete(self, plant_id):
            """Remove plant"""
            plant = Plant.query.get_or_404(plant_id)
            db.session.delete(plant)
            db.session.commit()
            return {'message': 'Plant deleted successfully'}
    
    # Tasks API endpoints
    @tasks_ns.route('/')
    class TaskList(Resource):
        def get(self):
            """Get all tasks"""
            tasks = Task.query.all()
            return [task.to_dict() for task in tasks]
        
        def post(self):
            """Create a new task"""
            data = api.payload
            task = Task(
                title=data.get('title'),
                description=data.get('description'),
                task_type=data.get('task_type'),
                due_date=datetime.fromisoformat(data.get('due_date').replace('Z', '+00:00')),
                plant_id=data.get('plant_id')
            )
            db.session.add(task)
            db.session.commit()
            return task.to_dict(), 201
    
    @tasks_ns.route('/<int:task_id>/complete')
    class TaskComplete(Resource):
        def put(self, task_id):
            """Mark task as completed"""
            task = Task.query.get_or_404(task_id)
            task.completed = True
            db.session.commit()
            return task.to_dict()
    
    # Root endpoint
    @api.route('/api/status')
    class Status(Resource):
        def get(self):
            """API status and information"""
            return {
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
            }
    
    # Create database tables
    with app.app_context():
        db.create_all()
        
        # Add sample data if database is empty
        if Plant.query.count() == 0:
            # Sample plants from your documents
            sample_plants = [
                Plant(name='Lechuga', species='Lactuca sativa', category='hortalizas', location='Jardín A'),
                Plant(name='Tomate', species='Solanum lycopersicum', category='hortalizas', location='Jardín A'),
                Plant(name='Limón Tahití', species='Citrus × latifolia', category='frutales', location='Huerto B'),
                Plant(name='Aguacate', species='Persea americana', category='frutales', location='Huerto B'),
                Plant(name='Albahaca', species='Ocimum basilicum', category='aromáticos', location='Jardín C'),
                Plant(name='Orégano', species='Origanum vulgare', category='especias', location='Jardín C')
            ]
            
            for plant in sample_plants:
                db.session.add(plant)
            
            # Sample tasks
            sample_tasks = [
                Task(title='Riego matutino', description='Regar plantas del jardín A', 
                     task_type='riego', due_date=datetime.now()),
                Task(title='Aplicar compost orgánico', description='Fertilizar con compost de café y cáscaras', 
                     task_type='fertilizar', due_date=datetime.now()),
                Task(title='Control de plagas', description='Aplicar mezcla de ajo y vinagre', 
                     task_type='control_plagas', due_date=datetime.now())
            ]
            
            for task in sample_tasks:
                db.session.add(task)
            
            db.session.commit()
    
    return app

# For development
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
