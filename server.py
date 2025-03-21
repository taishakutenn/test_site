from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route("/")
@app.route('/index')
def index():
    return "Мой сайт!"


if __name__ == '__main__':
    main()
