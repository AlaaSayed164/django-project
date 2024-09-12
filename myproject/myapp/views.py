# myapp/views.py

from django.shortcuts import render
# Add your librires here
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn import preprocessing
import numpy as np


def welome_page(request):
    return render(request, 'welcome.html');


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def predict_page(request):
    predicted_price = None
    if request.method == 'POST':
        # Get form data
        income = float(request.POST.get('income'))
        house_age = float(request.POST.get('house_age')  )
        rooms = float(request.POST.get('rooms'))
        bedrooms = float(request.POST.get('bedrooms'))
        central_air = request.POST['central_air'] 
        if central_air=='yes':
            central_air1=1
        else:
            central_air1=0

        # Perform the prediction logic here
        # For simplicity, let's assume we return a random or calculated prediction.
        # You can replace this with your actual model prediction logic.
        df = pd.read_csv('myapp/House_price.csv')
        df=df.drop(['Address','Area Population'],axis=1)
        df['Number of Bedrooms']=df['Number of Bedrooms'].fillna(df['Number of Bedrooms'].mean())
        df["CentralAir"]=df["CentralAir"].replace(to_replace=["Y","Yes"],value="Y")
        df["CentralAir"]=df["CentralAir"].replace(to_replace=["N","No"],value="N")
        label_encoder = preprocessing.LabelEncoder()
        df['CentralAir']= label_encoder.fit_transform(df['CentralAir'])
        X = df[['CentralAir','Area Income','House Age','Number of Rooms','Number of Bedrooms']]
        y = df['Price']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
        regression_model = LinearRegression()
        regression_model.fit(X_train, y_train)
        predicted_price = regression_model.predict([[central_air1,income,house_age,rooms,bedrooms]]) 



        # Render the same page with the prediction result
        return render(request, 'predict.html', {
            'predicted_price': predicted_price,
            'income': income,
            'house_age': house_age,
            'rooms': rooms,
            'bedrooms': bedrooms,
            'central_air': central_air
        })

    return render(request, 'predict.html');
