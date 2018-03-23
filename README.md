# Plot cycling route with Google Maps API and Flask web framework

This repository contains python code that parse a cycling activity TCX file and plot the route with Google Maps API and Flask web framework.

A Simple Example
----------------

.. code-block:: python

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

For more details about the codes, refer to my blog post [How to plot cycling route with Google Maps API and Flask web framwork](https://www.e-tinkers.com/2018/03/how-to-plot-cycling-route-using-google-maps-api-and-flask-web-framework/).
