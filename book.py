from book_routes import BookStore
from customer_routes import db


class Books:

    @staticmethod
    def create_book(data):
        new_user = BookStore(
            Title=data['Title'],
            Pages=data['Pages'],
            Author_Name=data['Author_Name'],
            Publish_Date=data['Publish_Date']
        )
        # Add the new book to the database
        db.session.add(new_user)
        db.session.commit()
        return "Book Added"

    @staticmethod
    def get_all_info(sort_by='id', filter_by=None):
        books = BookStore.query.all()

        # Convert the query result to a list of dictionaries
        books_list = [
            {
                'id': book.id,
                'Title': book.Title,
                'Pages': book.Pages,
                'Author_Name': book.Author_Name,
                'Publish_Date': book.Publish_Date
            }
            for book in books
        ]
        if filter_by:
            data = list(filter(lambda item: filter_by in item['Author_Name'], books_list))
            return data
        data = sorted(books_list, key=lambda item: item[sort_by])
        return data

    def get_by_id(self, id):
        target_book = BookStore.query.get(id)
        books = self.get_all_info()
        try:
            if target_book is not None:
                book_data = {                           # Convert the book data to a dictionary
                        'id': target_book.id,
                        'Title': target_book.Title,
                        'Pages': target_book.Pages,
                        'Author_Name': target_book.Author_Name,
                        'Publish_Date': target_book.Publish_Date
                        }
                return book_data
            return f"Please enter valid ID, the last item in Data Base is {books[-1]['id']}"
        except IndexError:
            return {}


    def delete_by_id(self, id):
        book = BookStore.query.get(id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return f"Book with id {id} deleted from DATABASE"

        return f"The Book with id {id} does not exist in DATABASE"

    @staticmethod
    def update_book(id_to_update, title, author_name, pages, publish_date):
        book = BookStore.query.get(id_to_update)            # query the book by using id into Database
        if not book:
            return f"Id {id_to_update} does not exist in DATABASE"

        # Update books fields if parameters are provided
        if title:
            book.Title = title
        if author_name:
            book.Author_Name = author_name
        if pages:
            book.Pages = pages
        if publish_date:
            book.Publish_Date = publish_date

        db.session.commit()
        return f"Book with ID {id_to_update} updated successfully"





