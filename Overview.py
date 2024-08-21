import streamlit as st

# streamlit run Overview.py --server.enableXsrfProtection false

st.set_page_config(
    page_title="Big Data Cup",
    page_icon="👋",

)

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

st.markdown("#### Overview")

st.markdown("##### Introduction")

st.markdown("While machine learning has achieved remarkable success in various areas, these accomplishments are often built upon the *i.i.d.* assumption, which refers to training and testing data being identically and independently distributed [1]. Models under this assumption learn shortcuts due to spurious correlations in the original data [2], leading to poor out-of-distribution (OOD) generalization performance. Domain generalization (DG) has gained increasing attention as a relevant topic in the context of OOD generalization recently.")
st.markdown("The objective of DG is to learn an invariant predictor across different domains [3]. Specifically, given a series of training (source) domains, our goal is to achieve good performance on unseen but related testing (target) domains through a predictor. The key to addressing DG is to handle the domain (distribution) shift problem, which refers to the distribution shift between training domains and testing domains.")
st.markdown("Many methods have been proposed to address the DG problem. However, most of them lack fairness considerations. Therefore, when these algorithms are applied in human-centered real-world settings, they may exhibit bias against some specific sensitive populations [4].  In the context of algorithmic decision-making, fairness means the absence of any bias or favoritism towards an individual or group based on their inherent or acquired characteristics [5].")

st.markdown("##### BigData Cup Challenges")

st.markdown("""
We need each team to design and implement two algorithms to train classifiers for the following two tasks:
            
+ *Task 1:* **Domain generalization in face recognition with multi-class label.** For each domain, assuming that domain remains unseen during the training process, data from the other three domains are used as training data. The objective is to achieve the highest possible accuracy in the unseen domain when predicting labels that are multi-class.
  
  Specific settings: The training set includes data from **Photo**, **Art**, **Cartoon** domain, while the testing set includes data from **Sketch** domain. **Age** is considered as a label for prediction, and the **Accuracy** on test domain will be used as the final result of Task 1.
            
+ *Task 2:* **Fairness-aware face recognition under distribution shift.** For each domain, assuming that domain remains unseen during the training process, data from the other three domains are used as training data. The objective is to achieve the highest possible accuracy and the lowest possible $\Delta_{DP}$ in the unseen domain when predicting labels that are multi-class and where the sensitive attribute is binary.

  Specific settings: The training set includes data from **Photo**, **Art**, **Cartoon** domain, while the testing set includes data from **Sketch** domain. **Age** is considered as a label for prediction and **Gender** serves as sensitive attribute. The final result of task2 is obtained by assigning weights of 3:7 to **Accuracy** and **$\Delta_{DP}$** on the test domain.         
""")

st.markdown("##### Evaluation Metrics")

st.markdown(r"""
We use Accuracy for domain generalization evaluation, and use Demographic parity difference ($\Delta_{DP}$) to measure algorithmic fairness.
            
+ **Accuracy** is a commonly used evaluation metric, which represents the ratio of the number of samples correctly predicted by the model to the total number of samples in the entire dataset.The calculation method is as follows.

  $$Accuracy = \frac{TP+TN}{TP+TN+FP+FN},$$

  where $TP$ is true positive, $TN$ is true negative, $FP$ is false positive and $FN$ is false negative. Here, we focus on the accuracy on the unseen test domain.

+ **Demographic parity difference ($\Delta_{DP}$)** aims to ensure equitable outcomes for different demographic groups characterized by sensitive attributes. It requires conditional probability of a positive outcome for each class is equal across different sensitive subgroups.
  
  $$\Delta_{DP} = |\mathbb{P}(f_{\boldsymbol{\theta}}(X)=1|Z=1) - \mathbb{P}(f_{\boldsymbol{\theta}}(X)=1|Z=0)|,$$

  where $X$ and $Z$ is the features and a binary sensitive attribute of an image. $f_{\boldsymbol{\theta}}:\mathcal{X} \rightarrow\mathcal{Y}$ is a classifier parameterized by $\boldsymbol{\theta}\in\Theta$.
""")

st.markdown("We will rank the participants' models based on their fairness performance and DG performance separately. For *Task 1*,  the DG performance of the model is measured by its accuracy ranking. For *Task 2*, the final ranking will be calculated by multiplying the fairness ranking by 0.7 and the DG ranking by 0.3, and then summing the results.")

st.markdown("##### References")
st.markdown("<span style='color:grey'>[1] Jindong Wang, Cuiling Lan, Chang Liu, Yidong Ouyang, Tao Qin, Wang Lu, Yiqiang Chen, Wenjun Zeng, and Philip Yu. 2022. ''Generalizing to unseen domains: A survey on domain generalization.'' IEEE Transactions on Knowledge and Data Engineering (2022).</span>", unsafe_allow_html=True)
st.markdown("<span style='color:grey'>[2] Robert Geirhos, Jörn-Henrik Jacobsen, Claudio Michaelis, Richard Zemel, Wieland Brendel, Matthias Bethge, and Felix A Wichmann. 2020. ''Shortcut learning in deep neural networks.'' Nature Machine Intelligence 2, 11 (2020), 665–673</span>", unsafe_allow_html=True)
st.markdown("<span style='color:grey'>[3] Martin Arjovsky, Léon Bottou, Ishaan Gulrajani, and David Lopez-Paz. 2019. ''Invariant risk minimization.'' arXiv preprint arXiv:1907.02893 (2019)</span>", unsafe_allow_html=True)
st.markdown("<span style='color:grey'>[4] Jian Kang and Hanghang Tong. 2021. ''Fair graph mining.'' In Proceedings of the 30th ACM International Conference on Information \& Knowledge Management. 4849–4852</span>", unsafe_allow_html=True)
st.markdown("<span style='color:grey'>[5] Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena, Kristina Lerman, and Aram Galstyan. 2021. ''A survey on bias and fairness in machine learning.'' ACM computing surveys (CSUR) 54, 6 (2021), 1–35</span>", unsafe_allow_html=True)
