import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved model
Companystockprice_model = pickle.load(open('C:/Users/admin/Downloads/netflix/netflix/netflix.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Company stock price prediction using ML', ['Home', 'Prediction', 'About'], default_index=0)

# Company stock price prediction Page
if selected == 'Home':
    # Page title and image
    st.title('Company stock price prediction using ML')
    st.image("download1.jpg", caption='Stock Market Image', use_column_width=True)

elif selected == 'Prediction':
    st.markdown("## Company stock price prediction")
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Close = st.text_input('Enter the Close Price', value='')

    # Code for Prediction

    
            # Use the input data for model prediction
    if st.button('Predict'):

        close_price_input = float(Close)
        Companystockprice_prediction = Companystockprice_model.predict([[close_price_input]])
        st.success(f'The predicted stock price is: {Companystockprice_prediction[0]:.2f}')
      

# About Page
elif selected == 'About':
    st.title('About')
    st.markdown("This app uses a machine learning model to predict company stock prices based on the provided close price.")
    st.markdown("Built with Streamlit.")
