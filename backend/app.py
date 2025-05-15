from flask import Flask
from flask_graphql import GraphQLView
from esquema import schema
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Habilitamos GraphiQL para probar desde navegador
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(debug=True)
