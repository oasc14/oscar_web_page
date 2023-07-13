from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTOS = [
  {
    'id':1,
    'title': 'Flores',
    'description': 'Sativa, Indica e Híbridas'
    
  },
  {
    'id':2,
    'title': 'Vapeadores',
    'description': 'Extracción y Líquido'
    
  },
  {
    'id':3,
    'title': 'Comestibles',
    'description': 'Galletas, Dulces y más'
    
  }
  
]

@app.route('/')
def hello_world():
  return render_template('home.html', productos=PRODUCTOS)

@app.route('/producto')
def list_products():
  return jsonify(PRODUCTOS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)