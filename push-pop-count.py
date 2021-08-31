from flask import Flask, request, jsonify
from werkzeug.wrappers import response #aquí importamos la librería Flask en nuestro archivo.
app = Flask(__name__) #aquí creamos una nueva instancia del servidor Flask.

@app.route("/") #aquí definimos el primer path de la API: GET /
def hello(): #este método se llamará cuando el cliente haga el request
    return "Hello World!" #flask devolverá "Hello World, esto podría ser un string HTML o un string JSON.

@app.route("/api/queue/push", methods=['POST']) # aquí especificamos que estos endpoints aceptan solicitudes POST y GET.
def handle_api_push():
  if request.method == 'POST': # podemos entender qué tipo de request estamos manejando usando un condicional
    bodyrqst1 = {
'status': 'ok',
}
    return jsonify(bodyrqst1)
    
@app.route("/api/queue/pop", methods=['POST']) # aquí especificamos que estos endpoints aceptan solicitudes POST y GET.
def handle_api_pop():
  if request.method == 'POST': # podemos entender qué tipo de request estamos manejando usando un condicional
    bodyrqst2 = {
'status': 'ok',
}
    return jsonify(bodyrqst2)

@app.route("/api/queue/count", methods=['GET']) # aquí especificamos que estos endpoints aceptan solicitudes POST y GET.
def handle_api_count():
  if request.method == 'GET': # podemos entender qué tipo de request estamos manejando usando un condicional
    bodyrqst3 = {
'status': 'ok',
}
    return jsonify(bodyrqst3)

app.run(host='0.0.0.0') #finalmente iniciamos el servidor en el localhost.
