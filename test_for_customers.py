import unittest
from main import app
from customer import Person
from customer_routes import delete_all_items


class TestForUsers(unittest.TestCase):

    def test_get_all(self):
        with app.app_context():       # used when we are using any applications like Database etc
            func_call_data = Person.get_all_info()
            assert isinstance(func_call_data, list)    # Check if instance of list

    def test_create_user(self):
        with app.app_context():
            data = {"name": "Marin", "age": 52, "city": "Norway"}
            func_call = Person.create_user_db(data)
            assert func_call == "User Added"

    def test_get_user_by_id(self):
        with app.app_context():
            id = 9
            func_call = Person().get_by_id(id)
            data = Person.get_all_info()
            assert isinstance(func_call,
                              dict) or func_call == f"Please enter valid ID, the last item in Data Base is {data[-1]['id']}"

    def test_delete_by_id(self):
        with app.app_context():
            id = 33
            func_call = Person().delete_by_id(id)
            assert func_call == f"User with id {id} deleted from DATABASE" or func_call == f"The user with id {id} does not exist in DATABASE"

    def test_update_user(self):
        with app.app_context():
            id_to_update = 1
            name = 'Umesh'
            city = 'GVP'
            age = 96
            func_call = Person.update_user(id_to_update=id_to_update, name=name, city=city,
                                           age=age)
            assert func_call == f"id {id_to_update} does not exist in DATABASE" or func_call == f"User with ID {id_to_update} updated successfully"

    def test_delete_all(self):
        with app.app_context():
            func_call = delete_all_items()        # Imported this func directly from customer_routes
            assert func_call == "All items in Table Deleted"












