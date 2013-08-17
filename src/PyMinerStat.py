import sys
import json
import pygal
from pygal.style import *
import urllib
import sqlite3 as lite


api = "YOUR API KEY"  # get one from here: https://mining.bitcoin.cz/accounts/token-manage/

path = "/var/www/miner/"  # change this according to the wiki https://github.com/agilob/PyMinerStat#pyminerstat

url = "http://mining.bitcoin.cz/accounts/profile/json/" + api


if __name__ == __name__:

    data = json.load(urllib.urlopen(url))

    con = lite.connect(path + 'db.sqlite3')
    db = con.cursor()

    db.execute(
        "CREATE TABLE IF NOT EXISTS wallet(ID integer primary key, " +
        "confirmed varchar, unconfirmed varchar, estimated varchar, " +
        "total varchar, time datetime default (datetime(current_timestamp)));")
    con.commit()

    db.execute(
        "INSERT INTO wallet (confirmed, unconfirmed, estimated, total) VALUES ( '" +
        str(data['confirmed_reward']) + "', '" +
        str(data['unconfirmed_reward']) + "', '" +
        str(data['estimated_reward']) + "', '" +
        str(float(data['confirmed_reward']) + float(data['unconfirmed_reward'])) + 
        "' );")

    con.commit()

    confirmed = []
    unconfirmed = []
    estimated = []
    total = []
    dates = []

    db.execute("SELECT * FROM wallet;")

    rows = db.fetchall()

    for row in rows:
        confirmed.append(float(str(row[1])))
        unconfirmed.append(float(str(row[2])))
        estimated.append(float(str(row[3])))
        total.append(float(str(row[4])))
        dates.append(str(row[5]))

    chart = pygal.Line(fill=True, x_title='Dates', x_label_rotation=60,
                       legend_at_bottom=True, style=CleanStyle)
    chart.x_labels = map(str, dates)
    chart.add("confirmed", confirmed)
    chart.render_to_file(path + 'confirmed.svg')

    chart = pygal.Line(fill=True, x_title='Dates', x_label_rotation=60,
                       legend_at_bottom=True, style=CleanStyle)
    chart.x_labels = map(str, dates)
    chart.add("unconfirmed", unconfirmed)
    chart.render_to_file(path + 'unconfirmed.svg')

    chart = pygal.Line(fill=True, x_title='Dates', x_label_rotation=60,
                       legend_at_bottom=True, style=CleanStyle)
    chart.x_labels = map(str, dates)
    chart.add("estimated", estimated)
    chart.render_to_file(path + 'estimated.svg')

    chart = pygal.Line(fill=True, x_title='Dates', x_label_rotation=60,
                       legend_at_bottom=True, style=CleanStyle)
    chart.x_labels = map(str, dates)
    chart.add("total", total)
    chart.add("confirmed", confirmed)
    chart.render_to_file(path + 'total.svg')

    chart = pygal.Line(fill=True, x_title='Dates', x_label_rotation=60,
                       legend_at_bottom=True, style=CleanStyle)
    chart.x_labels = map(str, dates)
    chart.add("total", total)
    chart.add("confirmed", confirmed)
    chart.add("unconfirmed", unconfirmed)
    chart.add("estimated", estimated)
    chart.render_to_file(path + 'all.svg')
