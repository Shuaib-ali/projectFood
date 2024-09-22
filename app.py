from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def menu():
    return render_template('menu.html')

# Route to handle order submission
@app.route('/order', methods=['POST'])
def order():
    # Get form data
    item = request.form['item']
    quantity = request.form['quantity']
    
    # Create a response message
    response_message = f"Order Placed! You ordered {quantity} {item}(s)."
    
    return f"<html><body><h1>{response_message}</h1></body></html>"

if __name__ == '__main__':
    app.run(debug=True)
