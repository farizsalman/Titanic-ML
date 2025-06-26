# streamlit
import joblib
import streamlit as st

le1=joblib.load(r"C:\Users\salma\OneDrive\Desktop\project\le1.pk1")
le2=joblib.load(r"C:\Users\salma\OneDrive\Desktop\project\le2.pk1")
model=joblib.load(r'C:\Users\salma\OneDrive\Desktop\project\titanic_model.pk1')


st.header('Titanic')
st.subheader('Survival Prediction')
st.image('https://www.worldhistory.org/img/r/p/1500x1500/14047.png')
st.text("RMS Titanic was a British ocean liner that sank in the early hours of 15 April 1912 as a result of striking an iceberg on her maiden voyage from Southampton, England, to New York City, United States. Of the estimated 2,224 passengers and crew aboard, approximately 1,500 died (estimates vary), making the incident one of the deadliest peacetime sinkings of a single ship.[4] Titanic, operated by White Star Line, carried some of the wealthiest people in the world, as well as hundreds of emigrants from the British Isles, Scandinavia, and elsewhere in Europe who were seeking a new life in the United States and Canada. The disaster drew public attention, spurred major changes in maritime safety regulations, and inspired a lasting legacy in popular culture. It was the second time White Star Line had lost a ship on her maiden voyage, the first being RMS Tayleur in 1854.Titanic was the largest ship afloat upon entering service and the second of three Olympic-class ocean liners built for White Star Line. The ship was built by the Harland and Wolff shipbuilding company in Belfast. Thomas Andrews Jr., the chief naval architect of the shipyard, died in the disaster. Titanic was under the command of Captain Edward John Smith, who went down with the ship. J. Bruce Ismay, White Star Line's chairman, managed to get into a lifeboat and survived")
st.subheader("Lets check the survival")
pclass=st.number_input('enter pclass: [1,2,3]')
sex=st.text_input('Enter Sex:[male,female]')
age=st.number_input('Age')
sibsp=st.number_input('sibsp')
parch=st.number_input('parch')
fare=st.number_input('fare')
embarked=st.text_input('embarked:[S,C,Q]')


if st.button('Predict'):
    sex=le2.transform([sex])[0]
    embarked=le1.transform([embarked])[0]
    prediction=model.predict([[pclass,sex,age,sibsp,parch,fare,embarked]])[0]
    if prediction==1:
        st.success("Survived")
    else:
        st.error("Not Survived")
