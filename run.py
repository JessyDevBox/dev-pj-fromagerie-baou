from app import create_app, db
from app.models import Cheese, CheeseBoard

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Cheese': Cheese,
        'CheeseBoard': CheeseBoard
    }

if __name__ == '__main__':
    app.run(debug=True)