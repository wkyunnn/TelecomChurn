import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('churn_model.pkl')

# Define the prediction function
def predict_churn(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return 'Yes' if prediction[0] == 1 else 'No'

# Streamlit app
st.title("Churn Prediction System")

# Input form
st.header("Enter Customer Details")

# Collect input data for each feature used in the model
MonthlyRevenue = st.number_input('Monthly Revenue', value=0.0)
MonthlyMinutes = st.number_input('Monthly Minutes', value=0.0)
TotalRecurringCharge = st.number_input('Total Recurring Charge', value=0.0)
DirectorAssistedCalls = st.number_input('Director Assisted Calls', value=0.0)
OverageMinutes = st.number_input('Overage Minutes', value=0.0)
RoamingCalls = st.number_input('Roaming Calls', value=0.0)
PercChangeMinutes = st.number_input('Percentage Change Minutes', value=0.0)
PercChangeRevenues = st.number_input('Percentage Change Revenues', value=0.0)
DroppedCalls = st.number_input('Dropped Calls', value=0.0)
BlockedCalls = st.number_input('Blocked Calls', value=0.0)
UnansweredCalls = st.number_input('Unanswered Calls', value=0.0)
CustomerCareCalls = st.number_input('Customer Care Calls', value=0.0)
ThreewayCalls = st.number_input('Threeway Calls', value=0.0)
ReceivedCalls = st.number_input('Received Calls', value=0.0)
OutboundCalls = st.number_input('Outbound Calls', value=0.0)
InboundCalls = st.number_input('Inbound Calls', value=0.0)
PeakCallsInOut = st.number_input('Peak Calls In Out', value=0.0)
OffPeakCallsInOut = st.number_input('Off Peak Calls In Out', value=0.0)
DroppedBlockedCalls = st.number_input('Dropped Blocked Calls', value=0.0)
CallForwardingCalls = st.number_input('Call Forwarding Calls', value=0.0)
CallWaitingCalls = st.number_input('Call Waiting Calls', value=0.0)
MonthsInService = st.number_input('Months In Service', value=0)
UniqueSubs = st.number_input('Unique Subs', value=0)
ActiveSubs = st.number_input('Active Subs', value=0)
Handsets = st.number_input('Handsets', value=0)
HandsetModels = st.number_input('Handset Models', value=0)
CurrentEquipmentDays = st.number_input('Current Equipment Days', value=0.0)
AgeHH1 = st.number_input('Age HH1', value=0)
AgeHH2 = st.number_input('Age HH2', value=0)
ChildrenInHH = st.number_input('Children In HH', value=0)
HandsetRefurbished = st.selectbox('Handset Refurbished', options=['No', 'Yes'])
HandsetWebCapable = st.selectbox('Handset Web Capable', options=['No', 'Yes'])
TruckOwner = st.selectbox('Truck Owner', options=['No', 'Yes'])
RVOwner = st.selectbox('RV Owner', options=['No', 'Yes'])
Homeownership = st.selectbox('Homeownership', options=['No', 'Yes'])
BuysViaMailOrder = st.selectbox('Buys Via Mail Order', options=['No', 'Yes'])
RespondsToMailOffers = st.selectbox('Responds To Mail Offers', options=['No', 'Yes'])
OptOutMailings = st.selectbox('Opt Out Mailings', options=['No', 'Yes'])
OwnsPC = st.selectbox('Owns PC', options=['No', 'Yes'])
OwnsMobileDevice = st.selectbox('Owns Mobile Device', options=['No', 'Yes'])
NewCellphoneUser = st.selectbox('New Cellphone User', options=['No', 'Yes'])
OwnsMotorcycle = st.selectbox('Owns Motorcycle', options=['No', 'Yes'])
MadeCallToRetentionTeam = st.selectbox('Made Call To Retention Team', options=['No', 'Yes'])
CreditRating = st.selectbox('Credit Rating', options=['1-Highest', '2-High', '3-Good', '4-Medium', '5-Low', '6-Very Low'])
PrizmCode = st.selectbox('Prizm Code', options=['Suburban', 'Town', 'Rural', 'Other'])
Occupation = st.selectbox('Occupation', options=['Professional', 'Crafts', 'Service', 'Other'])
MaritalStatus = st.selectbox('Marital Status', options=['No', 'Yes'])

# Convert categorical inputs to match one-hot encoded columns
input_data = {
    'MonthlyRevenue': MonthlyRevenue,
    'MonthlyMinutes': MonthlyMinutes,
    'TotalRecurringCharge': TotalRecurringCharge,
    'DirectorAssistedCalls': DirectorAssistedCalls,
    'OverageMinutes': OverageMinutes,
    'RoamingCalls': RoamingCalls,
    'PercChangeMinutes': PercChangeMinutes,
    'PercChangeRevenues': PercChangeRevenues,
    'DroppedCalls': DroppedCalls,
    'BlockedCalls': BlockedCalls,
    'UnansweredCalls': UnansweredCalls,
    'CustomerCareCalls': CustomerCareCalls,
    'ThreewayCalls': ThreewayCalls,
    'ReceivedCalls': ReceivedCalls,
    'OutboundCalls': OutboundCalls,
    'InboundCalls': InboundCalls,
    'PeakCallsInOut': PeakCallsInOut,
    'OffPeakCallsInOut': OffPeakCallsInOut,
    'DroppedBlockedCalls': DroppedBlockedCalls,
    'CallForwardingCalls': CallForwardingCalls,
    'CallWaitingCalls': CallWaitingCalls,
    'MonthsInService': MonthsInService,
    'UniqueSubs': UniqueSubs,
    'ActiveSubs': ActiveSubs,
    'Handsets': Handsets,
    'HandsetModels': HandsetModels,
    'CurrentEquipmentDays': CurrentEquipmentDays,
    'AgeHH1': AgeHH1,
    'AgeHH2': AgeHH2,
    'ChildrenInHH': ChildrenInHH,
    'HandsetRefurbished_Yes': 1 if HandsetRefurbished == 'Yes' else 0,
    'HandsetWebCapable_Yes': 1 if HandsetWebCapable == 'Yes' else 0,
    'TruckOwner_Yes': 1 if TruckOwner == 'Yes' else 0,
    'RVOwner_Yes': 1 if RVOwner == 'Yes' else 0,
    'Homeownership_Yes': 1 if Homeownership == 'Yes' else 0,
    'BuysViaMailOrder_Yes': 1 if BuysViaMailOrder == 'Yes' else 0,
    'RespondsToMailOffers_Yes': 1 if RespondsToMailOffers == 'Yes' else 0,
    'OptOutMailings_Yes': 1 if OptOutMailings == 'Yes' else 0,
    'OwnsPC_Yes': 1 if OwnsPC == 'Yes' else 0,
    'OwnsMobileDevice_Yes': 1 if OwnsMobileDevice == 'Yes' else 0,
    'NewCellphoneUser_Yes': 1 if NewCellphoneUser == 'Yes' else 0,
    'OwnsMotorcycle_Yes': 1 if OwnsMotorcycle == 'Yes' else 0,
    'MadeCallToRetentionTeam_Yes': 1 if MadeCallToRetentionTeam == 'Yes' else 0,
    'CreditRating_2-High': 1 if CreditRating == '2-High' else 0,
    'CreditRating_3-Good': 1 if CreditRating == '3-Good' else 0,
    'CreditRating_4-Medium': 1 if CreditRating == '4-Medium' else 0,
    'CreditRating_5-Low': 1 if CreditRating == '5-Low' else 0,
    'CreditRating_6-Very Low': 1 if CreditRating == '6-Very Low' else 0,
    'PrizmCode_Town': 1 if PrizmCode == 'Town' else 0,
    'PrizmCode_Rural': 1 if PrizmCode == 'Rural' else 0,
    'PrizmCode_Other': 1 if PrizmCode == 'Other' else 0,
    'Occupation_Crafts': 1 if Occupation == 'Crafts' else 0,
    'Occupation_Service': 1 if Occupation == 'Service' else 0,
    'Occupation_Other': 1 if Occupation == 'Other' else 0,
    'MaritalStatus_Yes': 1 if MaritalStatus == 'Yes' else 0
}

# Predict churn
if st.button('Predict Churn'):
    result = predict_churn(input_data)
    st.write(f'The customer will churn: {result}')
