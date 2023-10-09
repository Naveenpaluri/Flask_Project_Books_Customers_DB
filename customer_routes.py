from flask import Blueprint, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from marshmallow_error import CustomerValidation

db = SQLAlchemy()

customer_blueprint = Blueprint("Customer Module", __name__, url_prefix="/customer")


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    city = db.Column(db.String(50))


from customer import Person


@customer_blueprint.route('/create/table/', methods=['POST'])
def create_user_table():
    db.create_all()
    return "Tables Created Successfully"


@customer_blueprint.route('/show/')
def get_all():
    # Query the database to retrieve all the customers
    customer_list = Person.get_all_info()
    return customer_list


@customer_blueprint.route('/create/', methods=['POST'])
def create_user():
    data = request.json           # Requests args from postman
    validation = CustomerValidation().load(data)       # load that json dict into marshmallow
    func_call = Person.create_user_db(data)
    return f"Data Inserted of user {data['name']}"


@customer_blueprint.route('/get/by/id/<id>/')
def get_user_by_id(id: int):
    func_call = Person().get_by_id(id)
    return func_call


@customer_blueprint.route('/delete/', methods=['DELETE'])
def delete_user():
    parameter_id = request.args.get('delete_by')
    func_call = Person().delete_by_id(parameter_id)
    return func_call


@customer_blueprint.route('/update/by/id', methods=['PUT'])
def update_user():
    id_to_update = request.args.get('id', type=int)

    if id_to_update is None:
        return "Please enter a valid id to update"

    name = request.args.get('name', default=None)
    city = request.args.get('city', default=None)
    age = request.args.get('age', type=int, default=None)
    func_call = Person.update_user(id_to_update, name, city, age)
    return func_call


@customer_blueprint.route('/delete/all/', methods=['DELETE'])
def delete_all_items():
    db.session.query(Users).delete()
    # After delete it will set auto increment to 1
    reset_sql = text("ALTER TABLE users AUTO_INCREMENT = 1;")
    db.session.execute(reset_sql)
    db.session.commit()
    return "All items in Table Deleted"






