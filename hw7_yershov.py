# Создать view функцию выводящую `count` самых продаваемых треков с суммой продаж. `count` - необязательный параметр
# GET запроса. Если он не указан вывести все все продажи отсортированные в порядке убывания сумм.
#
# Задачу решить средствами Python.

from flask import Flask
from db import execute_query
from formater import list_rec2html_br, records2dct
from utils import get_revenue

from webargs import fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.route('/tracks')
@use_kwargs(
    {
        'count': fields.Int(
            required=False,
            missing=None
        )
    },
    location='query'
)
def get_top_tracks(count):
    sql = 'select TrackId , Quantity , UnitPrice from invoice_items '
    sql_tracks = 'select TrackId , Name from tracks'

    records = execute_query(sql)
    records_tracks = execute_query(sql_tracks)

    revenue = get_revenue(records)
    tracks_dct = records2dct(records_tracks)

    revenue_dct = {}
    for _ in revenue:
        revenue_dct[tracks_dct[_]] = revenue[_]

    res_lst = []
    revenue_lst = sorted(revenue_dct.items(), key=lambda item: item[1], reverse=True)
    for track, revenue in revenue_lst[:count]:
        res_lst += [f'{track}: {revenue}']

    return list_rec2html_br(res_lst)


app.run(debug=True, port=5001)
