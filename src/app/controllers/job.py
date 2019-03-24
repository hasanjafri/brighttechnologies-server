import datetime

from flask import jsonify, make_response
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('job_name', required=True, help='Please enter a job name')
parser.add_argument('job_summary', required=True, help='Please enter a preview for this job posting')

class JobController(Resource):
    """ Handles Job Postings CRUD operations. """

    def post(self):
        """ Creates a new job posting """
        args = parser.parse_args()