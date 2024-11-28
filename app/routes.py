from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import SearchForm
from app.airports_service import AirportsService
from app.helpers import format_airports_html, prettify_airports_type
import logging

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        city = form.city.data
        postal_code = form.postal_code.data
        amount = form.amount.data
        return redirect(url_for('search', city=city, postal_code=postal_code, amount=amount))
    return render_template("index.html", form=form)

@app.route("/search")
def search():
    logging.debug(request.args)
    postal_code = request.args.get("postal_code")
    city = request.args.get("city")
    try:
        amount = int(request.args.get("amount", 5))
    except (ValueError, TypeError):
        amount = 5
    
    if not postal_code and not city:
        return redirect(url_for("index"))
    air_service = AirportsService(app.config['AIRPORTS_FILE_PATH'])
    
    try:
        if postal_code and city:
            airports, location = air_service.search_by_city_and_code(city_name=city,postal_code=postal_code, amount=amount)
            searched_for = f"{postal_code}, {city}"
        elif city:
            airports, location = air_service.search_by_city(city_name=city, amount=amount)
            searched_for = f"{city}"
        elif postal_code:
            airports, location = air_service.search_by_postal_code(postal_code=postal_code, amount=amount)
            searched_for = f"{postal_code}, Deutschland"
    except ValueError as e:
        flash(str(e))
        return redirect(url_for("index"))
    
    prettify_airports_type(airports=airports)
    html = format_airports_html(airports=airports)
    return render_template("search.html", table_html=html, searched_for=searched_for, found_address=location.address, airports_amount=amount)