from flask import Flask, jsonify, request, g

db = {}

def get_db():
    global db
    return db

def set_db(db_write):
    global db
    db = db_write

app = Flask(__name__)

@app.route("/set")
def set():
    db = get_db();
    writes = {}
    for (key, val) in request.args.iteritems():
        db[key] = val
        writes[key] = val
    set_db(db)
    response = jsonify(status="ok", **writes)
    response.status_code = 200
    return response

@app.route("/get")
def query():
    db = get_db();
    reads = {}
    for (key, _val) in request.args.iteritems():
        reads[key] = db.get(key, None)
    response = jsonify(status="ok", **reads)
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run()
