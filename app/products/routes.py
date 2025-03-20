from flask import render_template
from app.products import bp
from app.models import Cheese, CheeseBoard
from app import db

@bp.route('/cheeses')
def cheeses():
    cheeses = Cheese.query.all()
    return render_template('products/cheeses.html', cheeses=cheeses)

@bp.route('/boards')
def boards():
    boards = CheeseBoard.query.all()
    return render_template('products/boards.html', boards=boards)