from flask import Blueprint, render_template, jsonify, request
from .services.yfinance_api import get_stock_quote


stocks_bp = Blueprint('stocks', __name__, template_folder='templates')

@stocks_bp.route('/stocks')
def ir_stocks():
    stocks = {
    "AAPL": 193.15,
    "MSFT": 421.75,
    "GOOGL": 178.52,
    "AMZN": 189.87,
    "TSLA": 234.12
    }

    stocks_info = {
        "AAPL": {
            "name": "Apple Inc.",
            "price": 193.15,
            "sector": "Technology",
            "market_cap": "3.3T"
        },
        "MSFT": {
            "name": "Microsoft Corporation",
            "price": 421.75,
            "sector": "Technology",
            "market_cap": "3.5T"
        },
        "GOOGL": {
            "name": "Alphabet Inc.",
            "price": 178.52,
            "sector": "Communication Services",
            "market_cap": "2.2T"
        },
        "AMZN": {
            "name": "Amazon.com Inc.",
            "price": 189.87,
            "sector": "Consumer Discretionary",
            "market_cap": "2.0T"
        },
        "TSLA": {
            "name": "Tesla Inc.",
            "price": 234.12,
            "sector": "Automotive / Clean Energy",
            "market_cap": "750B"
        }
    }

    return render_template('stocks.html', stocks=stocks, stocks_info=stocks_info)


@stocks_bp.route('/stocks/<id>')
def obtener_stock(id):
    stocks = {
    "AAPL": 193.15,
    "MSFT": 421.75,
    "GOOGL": 178.52,
    "AMZN": 189.87,
    "TSLA": 234.12
    }

    stocks_info = {
        "AAPL": {
            "name": "Apple Inc.",
            "price": 193.15,
            "sector": "Technology",
            "market_cap": "3.3T"
        },
        "MSFT": {
            "name": "Microsoft Corporation",
            "price": 421.75,
            "sector": "Technology",
            "market_cap": "3.5T"
        },
        "GOOGL": {
            "name": "Alphabet Inc.",
            "price": 178.52,
            "sector": "Communication Services",
            "market_cap": "2.2T"
        },
        "AMZN": {
            "name": "Amazon.com Inc.",
            "price": 189.87,
            "sector": "Consumer Discretionary",
            "market_cap": "2.0T"
        },
        "TSLA": {
            "name": "Tesla Inc.",
            "price": 234.12,
            "sector": "Automotive / Clean Energy",
            "market_cap": "750B"
        }
    }

   
    stock = next((stock for stock, precio in stocks.items() if stock.lower() == id.lower()), None)
    stock_info2 = next((info for stock, info in stocks_info.items() if stock.lower() == id.lower()), None)
    
    symbol = stock.upper()
    live_data = get_stock_quote(symbol)
    
    if stock:
        return render_template('stocks2.html',stock=stock, stocks_info2=stock_info2, live=live_data)

    return jsonify({"error": "Usuario no encontrado"}), 404


# # para sacar la info con un query params en "localhost/stocks/quote?symbol=MSFT"
# @stocks_bp.route('/stocks/quote')
# def quote():
#     symbol = request.args.get("symbol", "AAPL").upper()
#     data = get_stock_quote(symbol)
#     return jsonify(data)