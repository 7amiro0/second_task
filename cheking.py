"""This file checks the input value."""

from flask import Flask, render_template, request, send_file


def main():
    """Main."""
    app = Flask('__name__', template_folder='templates')
    list_name = set()

    @app.route('/main/index/home/')
    def hello():
        return render_template('main.html')

    def cheking(name, list_name):
        title = str(name).split("'")[3]

        if title in list_name:
            result = 'Вже бачилися, ' + title
        elif title not in list_name:
            list_name.add(title)
            result = 'Привіт ' + title
        return result

    @app.route('/main/index/home/', methods=['POST', 'GET'])
    def result():
        name = request.form
        return render_template('main.html', name=cheking(name, list_name))

    @app.route('/style.css')
    def style_enter():
        return send_file('templates/style.css')

    @app.route('/main/index/home/list/', methods=['POST', 'GET'])
    def all_name():
        res = ', '.join(list_name)
        return render_template('list_name.html', all_names=res)

    @app.route('/main/index/home/list/style.css')
    def style_list():
        return send_file('templates/style.css')

    app.run(debug=True)


main()
