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

st.markdown("#### Data")

st.markdown("##### Introduction")

st.markdown("Our dataset is a large-scale face recognition dataset with more than 50k images. All images in the dataset are real and have been professionally annotated manually. The annotations include 38 attributes, as shown in Table 1. It is worth noting that for ease of application, we have split multi-class attributes into binary attributes during annotation. For example, the race attribute is divided into three binary attributes: Asian, Black, and Other Races.")

col1, col2, col3 = st.columns([1,3,1])

with col1:
    st.write(' ')

with col2:
    st.image('imgs/table1.jpg', caption='Table 1: 38 binary attributes in dataset.')

with col3:
    st.write(' ')



st.markdown("To address the problem of *domain generalization concerning fairness*, the images in the dataset are categorized into four domains: **Photo**, **Art**, **Cartoon**, and **Sketch**, as illustrated in Figure 1. The gender or race attributes of each image can be considered sensitive attributes. Note that since this is a raw dataset, some necessary preprocessing is required before applying it to the problem. We need to be mindful that our dataset should not be disseminated without permission.")

st.image('imgs/figure1.png', caption='Figure 1: Partial display and quantity of images from four different domains in the dataset.')

st.markdown("##### Download")

st.markdown("We have kept the Sketch domain as the test set and used data from other domains as the training set. Due to the requirement in the setting of the domain generalization that the test set is unseen, participating teams can only obtain data on the training set. The download link is:", unsafe_allow_html=True)

st.markdown("https://pan.baidu.com/s/1nNAerRcq1P0y9IQDau6bkg", unsafe_allow_html=True)
st.markdown("Extracted code: 73w5", unsafe_allow_html=True)
