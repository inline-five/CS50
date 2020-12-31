import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required # "decaotrator" required to be logged in to view  /index
def index():
    uID = session["user_id"]
    holdings_lookup = db.execute("SELECT symbol, name, total_shares FROM holdings WHERE user_id = :uID ORDER BY symbol", uID=uID)
    cash_lookup = db.execute("SELECT cash FROM users WHERE id = :uID", uID=uID)
    cash_available = round(float(cash_lookup[0]["cash"]), 2)

    holdings_value = 0

    for each_company in holdings_lookup:
        quote = lookup(each_company["symbol"]) ## dict
        price = round(quote["price"], 2)
        holdings_value += (each_company["total_shares"] * price)
        each_company.update({'price': price})

    return render_template("index.html", holdings_lookup=holdings_lookup, cash_available=cash_available, holdings_value=holdings_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html", buy=buy)

    else:
        if not request.form.get("symbol"):
            return apology("Please enter a stock symbol")
        elif not request.form.get("shares"):
            return apology("Please enter a positive share count")

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("Please enter a correct stock symbol")

        uID = session["user_id"]
        shares = int(request.form.get("shares"))
        sql_return = db.execute("Select * FROM users WHERE id = :uID", uID=uID)
        cash_available = round(float(sql_return[0]["cash"]), 2)
        total_trade_cost = round(float(quote["price"]) * shares, 2)

        if total_trade_cost < cash_available:
            db.execute("INSERT INTO trades (id, bought_sold, num_shares, timestamp, symbol, name, execute_price) VALUES(?, ?, ?, ?, ?, ?, ?)", uID, "b", shares, datetime.now().replace(microsecond=0), quote["symbol"], quote["name"], quote["price"])
            db.execute("UPDATE users SET cash = :cash WHERE id = :uID", cash=(cash_available - total_trade_cost), uID=uID )
            update_holdings_table = db.execute("SELECT total_shares, symbol FROM holdings WHERE user_id = :uID AND symbol = :symbol", uID=uID, symbol=quote["symbol"])

            current_num_shares = [item for item in update_holdings_table if item["symbol"] == quote["symbol"]]

            if current_num_shares:
                '''update holdings with new amount'''
                shares_add = update_holdings_table[0]["total_shares"]
                db.execute("UPDATE holdings SET total_shares = :total_shares WHERE user_id = :uID AND symbol = :symbol", total_shares=(shares + shares_add), uID=uID, symbol=quote["symbol"])

            elif not current_num_shares:
                '''update holdings with new entry'''
                db.execute("INSERT INTO holdings (user_id, symbol, name, total_shares) VALUES (?, ?, ?, ?)", uID, quote["symbol"], quote["name"], shares)

            flash("Your bought some stock.")
            return redirect("/")

        else:
            return apology("your cannot afford to buy the amount of shares requested")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    uID = session["user_id"]
    trade_history_query = db.execute("SELECT symbol, num_shares, bought_sold, execute_price, timestamp FROM trades WHERE id=:uID ORDER BY timestamp", uID=uID)

    return render_template("history.html", trade_history_query=trade_history_query)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :user_name",
                          user_name=username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash('Logged In!')
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    else:
        if not request.form.get("symbol"):
            return apology("missing symbol")

        symbol_dict = lookup(request.form.get("symbol"))

        if symbol_dict == None:
            return apology("invalid symbol")
        else:
            quoted = 1
            return render_template("quote.html", quoted=quoted, quote=symbol_dict)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # check for username entered in form
        if not username:
            return apology("must provide username", 403)

        #check for password entered into form, and check that both passwords are correct
        elif not password or password != confirm_password:
            return apology("must provide password or password does not match", 403)

        # check if username already taken, if not, register the user
        rows = db.execute("SELECT * FROM users WHERE username = :user_name", user_name=username)
        if len(rows) > 0:
            return apology("username already taken, please choose another")
        else:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))
            rows = db.execute("SELECT * FROM users WHERE username = :user_name", user_name=username)
            session["user_id"] = rows[0]["id"]
            flash("Registered!")
            return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        uID = session["user_id"]
        update_holdings_table = db.execute("SELECT symbol FROM holdings WHERE user_id = :uID ORDER BY symbol", uID=uID)

        holdings_list = []

        for each in update_holdings_table:
            holdings_list.append(each["symbol"])

        return render_template("sell.html", holdings_list=holdings_list)

    else:
        if not request.form.get("symbol"):
            return apology("Please enter a stock symbol")
        elif not request.form.get("shares"):
            return apology("Please enter a positive share count")

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("Please enter a correct stock symbol")

        uID = session["user_id"]
        shares_to_sell = int(request.form.get("shares"))

        share_count_holdings = 0
        update_holdings_table = db.execute("SELECT symbol, total_shares FROM holdings WHERE user_id = :uID AND symbol = :symbol", uID=uID, symbol=quote["symbol"])
        share_count_holdings = update_holdings_table[0].get("total_shares")

        total_trade_value = round(float(quote["price"]) * shares_to_sell, 2)

        if shares_to_sell <= share_count_holdings:
            db.execute("INSERT INTO trades (id, bought_sold, num_shares, timestamp, symbol, name, execute_price) VALUES(?, ?, ?, ?, ?, ?, ?)", uID, "s", shares_to_sell, datetime.now().replace(microsecond=0), quote["symbol"], quote["name"], quote["price"])
            db.execute("UPDATE holdings SET total_shares = :total_shares WHERE user_id = :uID AND symbol = :symbol", total_shares=(share_count_holdings-shares_to_sell), uID=uID, symbol=quote["symbol"])
            db.execute("UPDATE users SET cash = cash + :total_trade_value WHERE id = :uID", total_trade_value=total_trade_value, uID=uID )

            if share_count_holdings - shares_to_sell == 0:
                db.execute("DELETE FROM holdings WHERE total_shares = 0")

            flash("Your sold some stock.")
            return redirect("/")
        else:
            return apology("you do not have that many shares to sell")


#@app.route("/test")
#@login_required # "decaotrator" required to be logged in to view  /index
#def test():
#    """TEST PAGE HERE"""



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
