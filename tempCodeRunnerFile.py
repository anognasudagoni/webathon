@app.route('/collection',methods=['GET'])
def result():
    return render_template("collection.html")
