import random

from flask import Flask, render_template

import data

app = Flask(__name__)


@app.route('/')
def render_main():
    l = list(data.tours.keys())
    selected_list = []
    random.seed()
    for i in range(0, 6):
        item = random.choice(l)
        selected_list.append(item)
        l.remove(item)
    return render_template('index.html', keys=selected_list, tours=data.tours, departures=data.departures,
                           active_dep='')


@app.route('/departures/<departure>/')
def render_departures_item(departure):
    selected_tours = {}
    for key in data.tours:
        if data.tours[key]["departure"] == departure:
            selected_tours[key] = data.tours[key]
    return render_template('departure.html', tours=selected_tours, departures=data.departures, active_dep=departure)


@app.route('/tours/<int:id>/')
def render_tours_item(id):
    return render_template('tour.html', turid=id, turinfo=data.tours[id], departures=data.departures,
                           active_dep=(data.tours[id])['departure'])


if __name__ == '__main__':
    app.run()
