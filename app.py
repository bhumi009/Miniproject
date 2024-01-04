import pickle
import numpy as np
import streamlit as st

with open("sale1.pkl","rb") as fo:
    model = pickle.load(fo)
#st.title("Item Outlet Sales Prediction")
st.markdown(
    """<style>
        .big-title {
            font-size: 3em;
            color: #0066cc;
            text-align:center;
        }
    </style>""",
    unsafe_allow_html=True,
)
st.markdown('<p class="big-title">Item Outlet Sales Prediction</p>', unsafe_allow_html=True)

item_fat_content_options = ['Low Fat', 'Regular']
item_type_options = ['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household', 'Others']
outlet_size_options = ['Small', 'Medium', 'High']
outlet_location_type_options = ['Tier 1', 'Tier 2', 'Tier 3']
outlet_type_options = ['Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3', 'Grocery Store']

Item_Identifier = st.number_input("Item_Identifier")
Item_Fat_Content = st.selectbox("Item_Fat_Content",item_fat_content_options)
Item_Weight = st.number_input("Item_Weight")
Item_Visibility = st.number_input("Item_Visibility")
Item_Type = st.selectbox("Item_Type",item_type_options)
Item_MRP = st.number_input("Item_MRP")
Outlet_Identifier = st.number_input("Outlet_Identifier")
Outlet_Establishment_Year = st.number_input("Outlet_Establishment_Year")
Outlet_Size = st.selectbox("Outlet_Size",outlet_size_options)
Outlet_Location_Type = st.selectbox("Outlet_Location_Type",outlet_location_type_options)
Outlet_Type = st.selectbox("Outlet_Type",outlet_type_options)

Item_Fat_Content = 0 if Item_Fat_Content == 'Low Fat' else 1
Item_Type = item_type_options.index(Item_Type)
Outlet_Size = outlet_size_options.index(Outlet_Size)
Outlet_Location_Type = outlet_location_type_options.index(Outlet_Location_Type)
Outlet_Type = outlet_type_options.index(Outlet_Type)

X = np.array([Item_Identifier, Item_Fat_Content, Item_Weight, Item_Visibility, 
              Item_Type, Item_MRP, Outlet_Identifier, Outlet_Establishment_Year, Outlet_Size, Outlet_Location_Type, Outlet_Type])

#X = np.array([487, 339, 0, 0.0263,  5, 79.4302, 1, 1987, 2, 2, 1])
X = X.reshape(1, -1)

if (st.button("Submit")):
    prediction = model.predict(X)[0]
    prediction = max(0, prediction)
    v=prediction*83.221
    st.write(f"Item Outlet Sales : {v} rupees")
    #st.write(f"Item Outlet Sales$ : {model.predict(X)[0]}")
else:
    st.write(f"Click on Submit button after entering feature values")
    