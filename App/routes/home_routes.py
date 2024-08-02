from App import app

@app.route("/", methods=['GET'])
def page_home():
    return 'Hello world'