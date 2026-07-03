import streamlit as st
import pandas as pd
from datetime import datetime
st.set_page_config(page_title = "Health Remark,layout="centered")
st.title("Health Remark Bot")
st.caption("Enter your details and get a remark.")
with st.form("Health_Details")
col1,col2 = st.columns(2)
with col1:
    name = st.text_input("Name*")
    email = st.text_input("Email*")
    gender = st.selectbox("Gender,["Male","Female","child<15"])

with col 2:
age = st.number_input("Age",min_value =1,max_value=120,value=25)
hb = st.number_input("Haemoglobin g/dl*",min_values=2.0,max_value=20.0,step=0.1)
sugar_type = st.selectbox("Sugar Type",["Fasting","Post-MealPP","HbA1c%"])
cholesterol = st.number_input("Total Cholesterol mg/dl*",min_value=50,max_value=500,step=1)

if sugar_type =="Fasting":
    sugar = st.number_input("Fasting Sugar mg/dl*",min_value=40,max_value=400,step=1)
else sugar_type =="Post-MealPP":
    sugar = st.number_input("Post-meal Sugar mg/dl*",min_value=60,max_value=500,step=1)
submitted = st.form_submit_button("Get Remark",type="primary")

def get_remark(gender,age,hb,cholesterol,sugartype,sugar):
    remarks = []

    if gender =="Child<15":
        low,high = 11.0,16.0
    elif gender =="Female":
        low,high = 12.0,15.0
    else:
        low,high = 13.5,17.0

    if hb<low:
        remarks.append(f"Hb{hb}:Low Please Consult Doctor.")
    elif hb>high:
        remarks.append(f"Hb {hb}: High,need to take a review")
    else:
        remarks.append(f"Hb{hb}:Normal")

    if cholesterol<200:
        remarks.append(f"Cholesterol{cholesterol}:Normal")
    elif cholesterol<240:
        remarks.append(f"Cholesterol{cholesterol}:Borderline high")
    else:
        remarks.append(f"Cholesterol{cholesterol}:High,Consult a Doctor")

    if sugar_type=="Fasting":
        if sugar< 70:
            remarks.append(f"Fasting Sugar{sugar}:Low")
        elif sugar <= 100:
            remarks.append(f"Fasting Sugar {sugar}:Normal")
        elif sugar<=125:
            remarks.append(f"Fasting Sugar{Sugar}:Pre-Diabetic")
        else:
            remarks.append(f"Fasting Sugar{sugar}: High")

    elif sugar_type=="Post-meal PP":
        if sugar<140"
            remarks.append(f"PP Sugar {sugar}:Normal")
        elif sugar<=199:
            remarks.append(f"PP Sugar{sugar}: Pre-diabetic")
        else :
            remarks.append(f"PP Sugar{sugar}:High")
    else:
        if sugar<5.7:
            remarks.append(f"HbA1c{sugar}%:Normal")
        elif sugar<6.5:
            remarks.append(f"Hba1c{sugar}% :pre-diabetic")
        else:
            remarks.append(f"Hba1c{sugar}%:High")

 return"|".join(remarks)
 if submitted:
    if not name or not email or hb==0 or cholesugsterol==0 or sugar==0:
        st.error("Please fill *marked with details")
    else:
        remark = get_remark(gender,ge,hb,chol,sugar_type,sugar)

        st.success(f"Remark for {name}:**")
        st.write(remark)

        data={
            "Timestamp":datetime.now().strftime("%y-%m-%d %H:%M:%S"),
            "Name":name,
            "Email":email,
            "Gender":gender,
            "Age":age,
            "Hb g/dL":hb,
            "Cholesterol mg/dL":cholesterol,
            f"Sugar{sugar_type}":sugar,
            "Remark":remark

        }

        df = pd.DataFrame([data])
        st.dataframe(df,use_container_width=True)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Result CSV",csv,f"health_report-{name}.csv","text/csv")

        st.divider()
        st.caption("Made with Streamlit. Ranges used:Hb Male 13.5-17,Female 12-15,Child 11-16 Cholesterol <200 normal. Sugar as per ADA Guidelines ")


        

    


  
