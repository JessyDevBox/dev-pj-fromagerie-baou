# app/api/endpoints.py
from flask import Blueprint
from flask_restx import Api, Resource, fields
from flask_login import current_user

from app.models import User, Cheese
from app import db, api

bp = Blueprint("api", __name__)


# Create API instance
api = Api(
    bp,
    version="1.0",
    title="Fromagerie du Baou API",
    description="API - Managing my Fromagerie du Baou",
    doc="/docs/",
)

# Create namespaces in order to organise API
ns_users = api.namespace("users", description="Managing - Users")
ns_cheeses = api.namespace("cheeses", description="Managing - Cheeses")

# Swagger models
user_model = api.model(
    "User",
    {
        "id": fields.Integer(readonly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "first_name": fields.String(required=True),
        "last_name": fields.String(required=True),
        "rights": fields.Integer(required=True),
        "description": fields.Integer(),
    },
)

cheese_model = api.model(
    "Cheese",
    {
        "id": fields.Integer(readonly=True),
        "name": fields.String(required=True),
        "quality_label": fields.String(),
        "is_bio": fields.Boolean(),
        "age_days_min": fields.Integer(),
        "age_days_max": fields.Integer(),
        "description": fields.String(),
        "country_code": fields.String(),
        "price_per_kg": fields.Integer(),
    },
)


# Endpoints
@ns_users.route("/")
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return User.query.all()


@ns_users.route("/<int:id>")
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self, id):
        """Get user by ID"""
        return User.query.get_or_404(id)


@ns_cheeses.route("/")
class CheeseList(Resource):
    @api.marshal_list_with(cheese_model)
    def get(self):
        """List all cheese"""
        return Cheese.query.all()

    @api.expect(cheese_model)
    @api.marshal_with(cheese_model)
    def post(self):
        """Create a new cheese"""
        data = api.payload
        cheese = Cheese(
            name=data["name"],
            description=data.get("description"),
            location=data.get("location"),
            user_id=current_user.id,
        )
        db.session.add(cheese)
        db.session.commit()
        return cheese


@ns_cheeses.route("/<int:id>")
class CheeseResource(Resource):
    @api.marshal_with(cheese_model)
    def get(self, id):
        """Get a cheese by ID"""
        return Cheese.query.get_or_404(id)

    @api.expect(cheese_model)
    @api.marshal_with(cheese_model)
    def put(self, id):
        """Update a cheese by id"""
        cheese = Cheese.query.get_or_404(id)
        data = api.payload
        cheese.name = data.get("name", cheese.name)
        cheese.description = data.get("description", cheese.description)
        cheese.location = data.get("location", cheese.location)
        db.session.commit()
        return cheese

    def delete(self, id):
        """Remove a cheese by id"""
        cheese = Cheese.query.get_or_404(id)
        db.session.delete(cheese)
        db.session.commit()
        return "", 204
