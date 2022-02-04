from flask import Flask,request,jsonify
app=Flask(__name__)
tasks=[
     {
     'id': 1,
     'name': u'Nityanth', 
     'contact': u'9052506653', 
     'done': False
     },
     {
     'id': 2,
     'name': u'Tanish', 
     'contact': u'9876543210', 
     'done': False
     },
]
@app.route("/get-task")
def get_task():
    return jsonify({
        "data":tasks
    })

@app.route("/add-task",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
        "status": "error",
        "message":"Please provide the data"
    },400)
    task = { 'id': tasks[-1]['id'] + 1, 'name': request.json['name'], 'contact': request.json.get('contact', ""), 'done': False }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message":"Please provide the data"
    },400)

if __name__ == "__main__":
    app.run(debug=True)