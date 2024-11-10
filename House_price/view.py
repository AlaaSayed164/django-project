from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def predict_page(request):
    predicted_price = None
    if request.method == 'POST':
        # Get form data
        area=int(request.POST.get('area'))
        house_age = int(request.POST.get('house_age')  )
        bedrooms = int(request.POST.get('bedrooms'))
        bathrooms= int(request.POST.get('bathrooms'))
        central_air = request.POST['central_air'] 
        hotwaterheating = request.POST['hotwaterheating'] 
        furnishingstatus = request.POST['furnishingstatus'] 
       # Add your librires here
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn import metrics
        from sklearn import preprocessing
        import numpy as np
       # make If-else statment to cahnge hotwaterheating, furnishingstatus, central_air to number (TAKE  CARE TO PUT IT IN NEW PARAMETER with same name+1 ex "furnishingstatus1" )
        if central_air == 'yes':
            central_air1 = 1
        else:
            central_air1 = 0

        if hotwaterheating == 'yes':
            hotwaterheating1 = 1
        else:
            hotwaterheating1 = 0

        if furnishingstatus == 'furnished':
            furnishingstatus1 = 0
        elif furnishingstatus == 'semi-furnished':
            furnishingstatus1 = 1
        else:
            furnishingstatus1 = 2

        print(f" Area: {area}, House Age: {house_age}, Bedrooms: {bedrooms}, Bathrooms: {bathrooms},Central Air: {central_air1}, Hotwater Heating: {hotwaterheating1}, Furnishing Status: {furnishingstatus1}")
        ## write your code [AI Model] here 
        df = pd.read_csv('Housing.csv')

        df=df.drop(['Address'],axis=1)
        df['bedrooms']=df['bedrooms'].fillna(df['bedrooms'].mean()) 
        df["furnishingstatus"]=df["furnishingstatus"].replace(to_replace=["fully furnished"],value="furnished")
        df["furnishingstatus"]=df["furnishingstatus"].replace(to_replace=["empty"],value="unfurnished")
        label_encoder = preprocessing.LabelEncoder()
        df['hotwaterheating']= label_encoder.fit_transform(df['hotwaterheating']) # 0: no 1:yes
        df['airconditioning']= label_encoder.fit_transform(df['airconditioning']) # 0: no 1:yes
        df['furnishingstatus']= label_encoder.fit_transform(df['furnishingstatus']) # 0: furnished 1:semi-furnished 2:unfurnished
        
        X = df[['area','bedrooms','bathrooms','House Age','hotwaterheating','airconditioning','furnishingstatus']]
        y = df['price']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
        
        regression_model = LinearRegression()
        regression_model.fit(X_train, y_train)
        predicted_price = regression_model.predict([[area, bedrooms, bathrooms, house_age, hotwaterheating1, central_air1, furnishingstatus1]]) 
       
        
        # Render the same page with the prediction result
        return render(request, 'predict.html', {
            'predicted_price': predicted_price,
            'area': area,
            'house_age': house_age,
            'bathrooms': bathrooms,
            'bedrooms': bedrooms,
            'central_air': central_air,
            'hotwaterheating': hotwaterheating,
            'furnishingstatus': furnishingstatus,
        })

    return render(request, 'predict.html');
