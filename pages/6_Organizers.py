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

st.markdown("#### Organizers")

st.markdown("The following personnel represented the School of New Media and Communication at Tianjin University in organizing this challenge.")
st.markdown("Any issues or questions can be directed to shaoml@tju.edu.cn.")

row1 = st.columns([4,1])
with row1[0]:
    st.markdown("##### Minglai Shao (Tianjin University, Primary Contact)")
    st.markdown("Dr. Shao is an Associate Professor in the School of New Media and Communication at Tianjin University. His research focuses on anomaly detection, domain generalization, trustworthy AI, machine learning *etc.* His work has been published in top-tier conferences and journals, including TDSC, TIFS, WWW, AAAI, CIKM, EMNLP, *etc.* Dr. Shao has served as a Program Committee member for AAAI, KDD, WWW, IJCAI, WSDM, *etc.* He serves as the reviewer of IEEE TKDE, IEEE TIFS, IEEE TNNLS, *etc.*")
with row1[1]:
    st.image('imgs/sml.jpg', caption='')

row2 = st.columns([1])
with row2[0]:
    st.markdown("##### Yang Zhang (Tianjin University)")
    st.markdown("Dr. Zhang is an Assistant Professor at the School of New Media and Communication at Tianjin University. She holds a Master's degree in Microelectronics from Peking University and a Ph.D. from the Institute of New Media. She was a postdoctoral fellow at Tsinghua University's School of Journalism and Communication. Her research focuses on AI ethics, algorithmic bias, digital divides, and international communication. She has authored papers on algorithmic bias, public opinion analysis on social media platforms, and international communication, published in top-tier journals and conferences like CSTIC, ICA, IAMCR, *etc.*")
# with row2[1]:
#     st.image('imgs/111.jpg', caption='')

row3 = st.columns([1])
with row3[0]:
    st.markdown("##### Yueheng Sun (Tianjin University)")
    st.markdown("Dr. Sun is currently a  associate professor at the College of Intelligence and Computing, Tianjin University. His research interests include social media processing, social computing and natural language processing. His work has been published in top-tier conferences and journals, including ACL, DASFAA, PAKDD, EMNLP, SIGIR, EMNLP, *etc.*")
# with row3[1]:
#     st.image('imgs/111.jpg', caption='')

row4 = st.columns([1])
with row4[0]:
    st.markdown("##### Wenjun Wang (Tianjin University)")
    st.markdown("Dr. Wang is currently a Professor at the College of Intelligence and Computing, Tianjin University. His research interests include computational social science, large-scale data mining, intelligence analysis, and multilayer complex network modeling. He has published more than 100 papers in main international journals and conferences, such as WWW, TOIS, TNNLS, ICDM, *etc.*")
# with row4[1]:
#     st.image('imgs/wwj.webp', caption='')

row5 = st.columns([1])
with row5[0]:
    st.markdown("##### Zan Wang (Tianjin University)")
    st.markdown("Dr. Wang is a Professor in the School of New Media and Communication at Tianjin University. He obtained his Ph.D. degree in 2009 from Tianjin University. His research interests mainly focus on concurrent program analysis, Deep neural network testing, and Self-driving autonomous vehicles' testing. He has published in top-tier conferences and journals, including ASE, ICSE, ISSTA, *etc.*")
# with row5[1]:
#     st.image('imgs/wwj.webp', caption='')

