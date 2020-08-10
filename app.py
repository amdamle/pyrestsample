from flask import Flask,jsonify,request,Response
import os,json
basepath='./data/json/'
app = Flask(__name__)

@app.route('/hello')
def home():
   return "My First Flask App"


@app.route('/detail')
def getDetails():
       id = request.args.get('id')
       print("id -->"+id)
       filename = os.path.join(basepath, '{}.json'.format(id))
       print("filename -->"+filename)
       with open(filename) as data_file:
        data = json.load(data_file)
        print("data -->{}".format(data))
        return Response(json.dumps(data),  mimetype='application/json')

@app.route('/status',methods=["POST"])
def setDetails():
       id = request.form.get('id')
       status = request.form.get('status')
       print("Transformer id --->"+id)
       print("Transformer Status --->"+status)
       data = {'code':'OK','msg':'Status Updated Successfully'}
       return Response(json.dumps(data),  mimetype='application/json')
       

if __name__ == '__main__':
    app.run(debug=True)

