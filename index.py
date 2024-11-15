from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def principal():
    return render_template('./index.html')


@app.route('/investigation')
def mostrarcancer():
    return render_template('./investigation.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/pictures')
def pictures():
    return render_template('pictures.html')


@app.route('/groups')
def groups():
    return render_template('groups.html')


@app.route('/gossip')
def gossip():
    return render_template('gossip.html')


if __name__ == '__main__':
    app.run(debug=True, port=5017)
