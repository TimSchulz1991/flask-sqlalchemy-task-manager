from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")

@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    # so with this code I am getting an array of all saved categories
    # ordered by name; .all() needs to be in the end
    return render_template("categories.html", categories=categories)
    # so now we can access the saved categories in the HTML

@app.route("/add_category", methods=["GET","POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")

@app.route("/edit_category/<int:category_id>", methods=["GET","POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    # the category is grabbed with the respective id
    # if something gets posted on this edit page, then update
    # the category name with the inputted name from the form
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)