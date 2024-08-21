import streamlit as st

st.write(r'''<style>
    
    [data-testid="baseButton-header"] {
        display:none !important;
         
    }
    [data-testid="stSidebarContent"] {
        background-color: #1E1C63 !important;
        color: white !important;
    }
    [data-testid="stSidebarContent"] span{
        color: white !important;
        font-size: calc(1rem * 1.2) !important;
    }

    </style>
         
         ''', unsafe_allow_html=True)



st.markdown("<center style='font-size:1.5rem'><b>IEEE Big Data 2024</b></center>", unsafe_allow_html=True)
st.markdown("<center>Washington DC, USA</center>", unsafe_allow_html=True)

st.markdown("### <span style='color:#1E1C63'>Challenges of Trustworthy AI in Distribution Shifts and Algorithmic Fairness 2024</span>", unsafe_allow_html=True)

st.markdown("#### Important Dates")

st.markdown(""" 
+ **April 30, 2024:** Website of the challenge opens. The task is revealed and training dataset is released.
+ **May 15, 2024:** The submission portal opens. Participants can now register their team and make submissions for the first stage for evaluation.
+ **September 15, 2024:** The deadline for the first stage submission has passed. The interim results will be announced within one week, and the final stage submission will commence.
+ **November 30, 2024:** BigData Cup challenge ends. The final results will be announced within one week. Participants should submit their final source code.
+ **December 15-18, 2024:** IEEE BigData 2024 Conference, Washington DC, USA.
""", unsafe_allow_html=True)

# + **July 15, 2024:** The deadline for the first stage submission has passed. The interim results will be announced within one week, and the second stage submission will commence.