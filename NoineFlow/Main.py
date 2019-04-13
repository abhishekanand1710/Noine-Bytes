import numpy as np
import urllib


from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Main(Resource):

    def get(self):

        typeOfReq = request.args.get('type')
        if typeOfReq == "send" :
        
            ablLevel = request.args.get('ablLevel')
            quesid = request.args.get('quesid')
            answer_status = request.args.get('status')
            history = request.args.get('history')


            return (ablLevel, quesid, answer_status, history)
        

        

        #read1, read2 = OCR.readRC(warped)
        #dic = parseRC.parseToJSON(read1, read2, state)

        #print(dic)

        #return jsonify(dic)

api.add_resource(Main, '/flow')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
