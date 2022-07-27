from pyexpat import features, model
import streamlit as st
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score

#make containers

header =st.container()
datasets= st.container()
features=st.container()
model_training= st.container()

with header:
    st.title('Ship App')
    st.text("In the project we will work with Ship data")

with datasets:
    st.header("The board are sink!")
    #import data
    df=sns.load_dataset('titanic')
    df=df.dropna()
    st.write(df.head())
    st.bar_chart(df['sex'].value_counts())

    #other plot
    st.subheader('Class Plot')
    st.bar_chart(df['class'].value_counts())

    #barplot
    st.bar_chart(df['age'].sample(10))

with features:
    st.header('These are our project features.')
    st.markdown('1. **Feature 1**: This is a simple feature')

with model_training:
    st.header("Ship model")
    input, display = st.columns(2)

    #columns selection points
    max_depth= input.slider("How many people do you know?", min_value=10 , max_value=100, value=20, step=5)


#n_estimators
n_estimators= input.selectbox("How many tree should be there Rf?", options=[50,200,300,400,500,"No limit"])

# adding list of features
input.write(df.columns)



# input features from user
input_features=input.text_input("Enter the features")


#machine learing model

model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)
if n_estimators == 'No limit':
    model = RandomForestRegressor(max_depth=max_depth)
else:
    model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
#define x and y

x=df[[input_features]]
y=df[['fare']]

#fit our model

model.fit(x,y)

perd = model.predict(x)

#display metrics

display.subheader("Mean absolute error of model is: ")
display.write(mean_absolute_error)
display.subheader("Mean squared error of model is: ")
display.write(mean_squared_error)
display.subheader("R error of model is: ")
display.write(r2_score(x,perd))