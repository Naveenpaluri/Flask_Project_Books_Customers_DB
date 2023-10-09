import unittest
from main import app
from book import Books
from book_routes import delete_all_items


class TestForUsers(unittest.TestCase):
    def test_create_user(self):
        with app.app_context():
            data = {
                "Title": "Elbaph Dairies",
                "Pages": 5528,
                "Author_Name": "Moria",
                "Publish_Date": "19th Mar 1553"
            }
            func_call = Books.create_book(data)
            assert func_call == "Book Added"

    def test_get_all(self):
        with app.app_context():       # used when we are using any applications like Database etc
            func_call_data = Books.get_all_info()
            assert isinstance(func_call_data, list)    # Check if instance of list

    def test_get_by_id(self):
        with app.app_context():
            id = 99
            func_call = Books().get_by_id(id)
            data = Books.get_all_info()           # Call this function to get id of last element
            assert isinstance(func_call, dict) or func_call == f"Please enter valid ID, the last item in Data Base is {data[-1]['id']}"

    def test_delete_by_id(self):
        with app.app_context():
            id = 17
            func_call = Books().delete_by_id(id)
            assert func_call == f"Book with id {id} deleted from DATABASE" or func_call == f"The Book with id {id} does not exist in DATABASE"

    def test_update_book(self):
        with app.app_context():
            id_to_update = 1
            title = "Beautiful"
            pages = 5528
            author_name = "Moria"
            publish_date = "19th Mar 1553"
            func_call = Books.update_book(id_to_update=id_to_update, title=title, pages=pages, author_name=author_name,
                                          publish_date=publish_date)
            assert func_call == f"Id {id_to_update} does not exist in DATABASE" or func_call == f"Book with ID {id_to_update} updated successfully"

    def test_delete_all(self):
        with app.app_context():
            func_call = delete_all_items()     # Imported this func directly from book_routes
            assert func_call == "All items in Table Deleted"

