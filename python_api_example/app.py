from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger
from dotenv import load_dotenv
import os
import py_srb_google_utils

load_dotenv()

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

google_handle = py_srb_google_utils.HandlgeGoogle()

# add apidocs to the end of the url to see swagger endpoint

class UppercaseText(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """
        text = request.args.get('text')

        return {"text": text.upper()}, 200


class GetRecords(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """

        google_values = google_handle.read_google_sheet()

        return {"values": google_values}, 200

api.add_resource(UppercaseText, "/uppercase")
api.add_resource(GetRecords, "/getrecords")

if __name__ == "__main__":
    port_number = os.getenv("PORT")
    host_name = os.getenv("HOST")

    app.run(
        debug=True,
        port=port_number,
        host=host_name
    )
