from marshmallow import Schema, fields


class CustomerValidation(Schema):      # Checks for the Customer Schema
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    city = fields.String(required=True)


class BookValidation(Schema):         # Checks for the Book_Schema
    Title = fields.String(required=True)
    Pages = fields.Integer(required=True)
    Author_Name = fields.String(required=True)
    Publish_Date = fields.String(required=True)


