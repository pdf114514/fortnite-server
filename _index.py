from flask import Flask, Response

app=Flask('index')

@app.route('/')
def getroot():
    return Response('"Ya :D"', mimetype='application/json')
  
app.run(host='0.0.0.0', port=8000, threaded=True)