from bikeroute import Map, Route
from flask import Flask, render_template


app = Flask(__name__)
app.config['API_KEY'] = "copy_and_past_google_map_API_key_here"
route = Route("20180117_023924.tcx.xml")
map = Map(route.trackpoints)


@app.route('/')
def index():
    context = {
        "key": app.config['API_KEY'],
        "title": route.title
    }
    return render_template('template.html', map=map, context=context)


if __name__ == '__main__':
    app.run()