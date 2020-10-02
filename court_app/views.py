from rest_framework import viewsets
from court_app.models import Lawsuit
from court_app.serializers import LawsuitSerializer

from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from numpy import pi
import pandas as pd
from bokeh.resources import CDN


class LawsuitViewSet(viewsets.ModelViewSet):
    """Set the view of the application with its objects serialized"""
    queryset = Lawsuit.objects.all()
    serializer_class = LawsuitSerializer


class Status(Lawsuit):
    def status(request):

        loss = 0
        share = 0
        win = 0
        counts = []
        items = ["Loss", "Share", "Shirts"]

        stat = Lawsuit.objects.values()
        
        for i in stat:
            if  "Loss" in i.values():
                loss += 1
            elif ("Share" in i.values()):
                share += 1
            elif ("Win" in i.values()):
                win += 1   
        counts.extend([loss, share, win])

        plot = figure(x_range=items, plot_height=600, plot_width=600, title="Status",
            toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
        plot.title.text_font_size = '20pt'
        
        plot.xaxis.major_label_text_font_size = "14pt" 
        plot.vbar(items, top=counts, width=.4, color= "firebrick", legend="Status Counts")
        plot.legend.label_text_font_size = '14pt'

        script, div = components(plot)

        return render(request, 'status.html', {'script': script, 'div':div})