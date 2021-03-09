import streamlit as st
from pickle import dump, load
import numpy as np
import warnings
warnings.filterwarnings("ignore")
def predict(col1,col2):

     # Loading pretrained logistic classifier from pickle file
    classifier = load(open('exam_svcrbf_model.pkl', 'rb'))


    prediction =classifier.predict(np.array([col1,col2]).reshape(1,-1))

    return prediction

def main():



    col1 = st.number_input('Test', value=1.)
    col2= st.number_input('Test1', value=1.)

    prediction = predict(col1,col2)

    if(prediction==1):

            st.write("Yes :sunglasses:")
            st.write(prediction)
    else:
            st.write("No :cry:")

            st.write(prediction)



if(__name__ == '__main__'):
    main()
