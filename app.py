# Task 2: Create a new file named app.py and set up a Flask server to serve the GraphQL API. Set up Flask Server: Use Flask alongside Flask-GraphQL to serve the GraphQL API.
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enable GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run(debug=True)
