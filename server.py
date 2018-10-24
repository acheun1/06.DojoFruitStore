#Dojo Fruit Store
#2018 10 01
#Cheung Anthony

# When you build this, please make sure that your program meets the following criteria:

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#our index route will handle the form
@app.route('/')
def index():
    return render_template('index.html')

#route to handle form submission that calls HTTP allowed for this route
@app.route('/checkout', methods=['POST'])
def checkout():
    ordertotal=int(request.form['Strawberry'])+int(request.form['Apples'])+int(request.form['Raspberries'])
    print(ordertotal)
    return render_template('checkout.html',ordertotal=ordertotal)

if __name__=="__main__":
    app.run(debug=True)


