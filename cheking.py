"""This file checks the input value."""

from flask import Flask, render_template, request, send_file


def main():
    """Main fun."""
    app = Flask('__name__', template_folder='templates')
    list_name = []

    @app.route('/hello/')
    def hello():
        return render_template('main.html')

    def cheking(name, list_name):
        if str(name).split("'")[3] in set(list_name):
            result = 'Вже бачилися, ' + str(name).split("'")[3]
        elif str(name).split("'")[3] not in set(list_name):
            list_name.append(str(name).split("'")[3])
            result = 'Привіт ' + str(name).split("'")[3]
        return result

    @app.route('/hello/', methods=['POST', 'GET'])
    def result():
        name = request.form
        return render_template('main.html', name=cheking(name, list_name))

    @app.route('/style.css')
    def style_enter():
        return send_file('templates/style.css')

    @app.route('/hello/list/', methods=['POST', 'GET'])
    def all_name():
        res = ''
        for name in list_name:
            res += name + ', '
        return render_template('list_name.html', all_names=res)

    @app.route('/hello/list/style.css')
    def style_list():
        return send_file('templates/style.css')

    app.run(debug=True)


main()
