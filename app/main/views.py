from app.main import main


@main.route('/')
def main():
    return '<h1>RUNNING</h1>'