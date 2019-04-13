import numpy as np
import urllib

from AdaptiveQuiz import quizhandler
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import ast

app = Flask(__name__)
api = Api(app)

class Main(Resource):

    def get(self):
            
            ablLevel = float(request.args.get('ablLevel'))
            quesid = int(request.args.get('quesid'))
            print(quesid, type(quesid))
            answer_status = int(request.args.get('status'))
            history = request.args.get('history')
            history = ast.literal_eval(history)
            return quizhandler(quesid, answer_status, history, ablLevel)
        

        

        #read1, read2 = OCR.readRC(warped)
        #dic = parseRC.parseToJSON(read1, read2, state)

        #print(dic)

        #return jsonify(dic)

api.add_resource(Main, '/flow')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
