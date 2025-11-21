# select intrerprete de python i seleccionamos nuestro entorno virtual
from flask import Flask, render_template,jsonify, send_from_directory
from stocks.rutas import stocks_bp


app = Flask(__name__)
app.register_blueprint(stocks_bp)



@app.route('/')
def index():
   
    
    return render_template('index_real.html')

@app.route('/base')
def base():
    
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
