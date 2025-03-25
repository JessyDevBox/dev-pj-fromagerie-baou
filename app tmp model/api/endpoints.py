# app/api/endpoints.py
from flask import Blueprint
from flask_restx import Api, Resource, fields
from flask_login import current_user

from app.models import User, Garden
from app import db, api

bp = Blueprint("api", __name__)


# Create API instance
api = Api(
    bp,
    version="1.0",
    title="My little Garden API",
    description="API - Managing my little garden",
    doc="/docs/",
)

# Create namespaces in order to organise API
ns_users = api.namespace("users", description="Opérations sur les utilisateurs")
ns_gardens = api.namespace("gardens", description="Opérations sur les jardins")

# Swagger models
user_model = api.model(
    "User",
    {
        "id": fields.Integer(readonly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "rights": fields.Integer(required=True),
    },
)

garden_model = api.model(
    "Garden",
    {
        "id": fields.Integer(readonly=True),
        "name": fields.String(required=True),
        "description": fields.String(),
        "location": fields.String(),
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


@ns_gardens.route("/")
class GardenList(Resource):
    @api.marshal_list_with(garden_model)
    def get(self):
        """List all gardens"""
        return Garden.query.all()

    @api.expect(garden_model)
    @api.marshal_with(garden_model)
    def post(self):
        """Create a new garden"""
        data = api.payload
        garden = Garden(
            name=data["name"],
            description=data.get("description"),
            location=data.get("location"),
            user_id=current_user.id,
        )
        db.session.add(garden)
        db.session.commit()
        return garden


@ns_gardens.route("/<int:id>")
class GardenResource(Resource):
    @api.marshal_with(garden_model)
    def get(self, id):
        """Get a garden by ID"""
        return Garden.query.get_or_404(id)

    @api.expect(garden_model)
    @api.marshal_with(garden_model)
    def put(self, id):
        """Update a garden by id"""
        garden = Garden.query.get_or_404(id)
        data = api.payload
        garden.name = data.get("name", garden.name)
        garden.description = data.get("description", garden.description)
        garden.location = data.get("location", garden.location)
        db.session.commit()
        return garden

    def delete(self, id):
        """Remove a garden by id"""
        garden = Garden.query.get_or_404(id)
        db.session.delete(garden)
        db.session.commit()
        return "", 204
