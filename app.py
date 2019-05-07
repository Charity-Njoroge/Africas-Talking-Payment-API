"""
A python project that uses the Africa's Talking API to charge a user's mobile
money account while making payments online.
"""
import os
from flask import Flask, request, render_template, url_for
import africastalking

app = Flask(__name__)

# adding africa's talking sdk to the app
username = "sandbox"
apikey = "2c39bbebd39a0aa9c78b0efff2dfedcb8ce1e884d88acfebf45baac4dbe19bf1"

africastalking.initialize(username, apikey)
pay = africastalking.Payment


# route to process user's payment
@app.route("/checkout", methods=["GET", "POST"])
def check_out():

    if request.method == "POST":
        product_name = "Test Store"
        phone_number = request.form["phoneNumber"]
        currency_code = "KES"
        amount = 250

        try:
            response = pay.mobile_checkout(product_name, phone_number, currency_code, amount)
            print(response)
        except Exception as e:
            print(f"Houston, we have a problem {e}")

    return render_template("checkout.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))