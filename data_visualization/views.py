# Create your views here.
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.http import HttpResponse

# write your code here for data preparation only
#  use this path to read csv'Housing.csv'


def chart_view(request):
    # # Generate the Pie Chart using Plotly
    # pie_fig1 = px.pie([1,2,3], names=['a','b'])
    # graph1 = pie_fig1.to_html()

    # pie_fig2=px.pie([1,2,3], names=['a','b'])
    # graph2 = pie_fig2.to_html()

    # bar_fig1 =px.pie([1,2,3], names=['a','b'], width=600,height=600)
    # bar_fig1.update_layout(
    #     plot_bgcolor= 'white' ,  # Background color of the plot area
    #     xaxis_showgrid=False,         # Remove vertical gridlines in one go
    #     yaxis_showgrid=False,
    #     showlegend=False     
    #     # bordercolor='black'
    #              # Remove horizontal gridlines in one go
    # )
    # graph3 = bar_fig1.to_html()


    # bar_fig2 = px.pie([1,2,3], names=['a','b'], width=600,height=600)
    # bar_fig2.update_layout(
    #     plot_bgcolor= 'white' ,  # Background color of the plot area
    #     xaxis_showgrid=False,         # Remove vertical gridlines in one go
    #     yaxis_showgrid=False,
    #     showlegend=False               # Remove horizontal gridlines in one go
    # )
    # graph4 = bar_fig2.to_html()
 # Generate the Pie Chart using Plotly
  # Read the CSV file
    df = pd.read_csv('Housing.csv')
    df['bedrooms']=df['bedrooms'].fillna(df['bedrooms'].mean())
    df["furnishingstatus"]=df["furnishingstatus"].replace(to_replace=["fully furnished"],value="furnished")
    df["furnishingstatus"]=df["furnishingstatus"].replace(to_replace=["empty"],value="unfurnished")
    pie_fig1 = px.pie(df, names="airconditioning", title='Count of people have Air Condition', color="airconditioning", width=800,height=800)
    graph1 = pie_fig1.to_html()

    pie_fig2=px.pie(df,names="hotwaterheating",title='Count of people have hot water heating' ,color="hotwaterheating", width=800,height=800)
    graph2 = pie_fig2.to_html()

    furnish_counts =pd.DataFrame(df['furnishingstatus'].value_counts())
    bar_fig1 = px.bar(furnish_counts, title='Furnishing Status', color=furnish_counts.index, width=800,height=800)
    bar_fig1.update_layout(
        plot_bgcolor= 'white' ,  # Background color of the plot area
        xaxis_showgrid=False,         # Remove vertical gridlines in one go
        yaxis_showgrid=False,
        showlegend=False     
        # bordercolor='black'
                 # Remove horizontal gridlines in one go
    )

    graph3 = bar_fig1.to_html()

    furnish_counts =pd.DataFrame(df['House Age'].value_counts())
    bar_fig2 = px.bar(furnish_counts, title='House Age', width=800,height=800)
    bar_fig2.update_layout(
        plot_bgcolor= 'white' ,  # Background color of the plot area
        xaxis_showgrid=False,         # Remove vertical gridlines in one go
        yaxis_showgrid=False,
        showlegend=False               # Remove horizontal gridlines in one go
    )
    graph4 = bar_fig2.to_html()
    return render(request, 'chart.html', {'graph1': graph1,'graph2': graph2,'graph3': graph3,'graph4': graph4})#,'graph5': graph5  })
