from flask import Blueprint, request
from customer_routes import db
from marshmallow_error import BookValidation
from sqlalchemy import text
book_blueprint = Blueprint("Book Module", __name__, url_prefix="/books")


class BookStore(db.Model):
    __tablename__ = 'Books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Title = db.Column(db.String(80), unique=True, nullable=False)
    Pages = db.Column(db.Integer)
    Author_Name = db.Column(db.String(50))
    Publish_Date = db.Column(db.String(20))


@book_blueprint.route('/create/table/', methods=['POST'])
def create_user_table():
    db.create_all()
    return "Tables Created Successfully"


from book import Books


@book_blueprint.route('/create/book/', methods=['POST'])
def add_book():
    data = request.json                           # Requests args from postman
    validation = BookValidation().load(data)        # load that json dict into marshmallow
    func_call = Books.create_book(data)
    return f"Data Inserted of Book {data['Title']}"


@book_blueprint.route('/show/')
def get_all():
    sort_by_id = request.args.get('sort_by', default='id')
    filter_by = request.args.get('filter_by', default=None)
    func_call = Books.get_all_info(sort_by=sort_by_id, filter_by=filter_by)
    return func_call


@book_blueprint.route('/get/by/id/<id>/')
def get_book_by_id(id: int):
    func_call = Books().get_by_id(id)
    return func_call


@book_blueprint.route('/delete/', methods=['DELETE'])
def delete_book():
    parameter_id = request.args.get('delete_by')
    func_call = Books().delete_by_id(parameter_id)
    return func_call


@book_blueprint.route('/update/by/id', methods=['PUT'])
def update_book():
    id_to_update = request.args.get('id', type=int)

    if id_to_update is None:
        return "Please enter a valid id to update"

    title = request.args.get('Title', default=None)
    author_name = request.args.get('Author_Name', default=None)
    pages = request.args.get('Pages', type=int, default=None)
    publish_date = request.args.get('Publish_Date', default=None)

    func_call = Books.update_book(id_to_update, title, author_name, pages, publish_date)
    return func_call


@book_blueprint.route('/delete/all/', methods=['DELETE'])    # For delete all items in table
def delete_all_items():
    db.session.query(BookStore).delete()
    # After delete it will set auto increment to 1
    reset_sql = text("ALTER TABLE Books AUTO_INCREMENT = 1;")
    db.session.execute(reset_sql)
    db.session.commit()
    return "All items in Table Deleted"






