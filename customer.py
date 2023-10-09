from customer_routes import db, Users


class Person:
    @staticmethod
    def get_all_info():
        customers = Users.query.all()

        # Convert the query result to a list of dictionaries
        customers_list = [
            {
                'id': customer.id,
                'name': customer.name,
                'age': customer.age,
                'city': customer.city,
            }
            for customer in customers
        ]
        return customers_list

    @staticmethod
    def create_user_db(data):
        new_user = Users(
            name=data['name'],
            age=data['age'],
            city=data['city'],
        )
        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return "User Added"

    def get_by_id(self, id):
        user = Users.query.get(id)
        customers = self.get_all_info()
        try:
            if user is not None:
                # Convert the user data to a dictionary
                user_data = {
                    'id': user.id,
                    'name': user.name,
                    'age': user.age,
                    'city': user.city,
                    }
                return user_data
            return f"Please enter valid ID, the last item in Data Base is {customers[-1]['id']}"
        except IndexError:
            return {}


    def delete_by_id(self, id):
        user = Users.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return f"User with id {id} deleted from DATABASE"

        return f"The user with id {id} does not exist in DATABASE"

    @staticmethod
    def update_user(id_to_update, name, city, age):
        user = Users.query.get(id_to_update)                    # query the customer by using id into Database
        if not user:
            return f"id {id_to_update} does not exist in DATABASE"

        # Update user fields if parameters are provided
        if name:
            user.name = name
        if city:
            user.city = city
        if age:
            user.age = age

        db.session.commit()
        return f"User with ID {id_to_update} updated successfully"
