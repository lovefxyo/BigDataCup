import streamlit as st
import pandas as pd

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

conn = st.connection('bigdatacupdb', type='sql')

st.markdown("#### Leaderboard")

st.markdown("##### Stage 1")

st.markdown("###### Task 1 Ranking")

leaderboard_df_stage_1 = conn.query(f"select * from leaderboard where stage=1;", ttl=2)
leaderboard_df_stage_1 = leaderboard_df_stage_1.drop(columns=['team_id'])
df1 = leaderboard_df_stage_1.iloc[:, [0, 1]]
df1 = df1.rename(columns={
    'team_name': 'Team Name',
    'task1_accuracy': 'Accuracy',
})
df1['Ranking'] = df1['Accuracy'].rank(ascending=False)
df1 = df1.sort_values(by='Ranking')
df1 = df1.reset_index(drop=True)
st.dataframe(df1, hide_index=True, column_order=("Ranking", "Team Name",'Accuracy'))

# col1, col2 = st.columns([1,1])

# df2_1 = leaderboard_df_stage_1.iloc[:, [0, 2]]
# df2_1 = df2_1.rename(columns={
#     'team_name': 'Team Name',
#     'task2_accuracy': 'Accuracy',
# })
# df2_1['Ranking'] = df2_1['Accuracy'].rank(ascending=False)
# df2_1 = df2_1.sort_values(by='Ranking')
# df2_1 = df2_1.reset_index(drop=True)
# with col1:
#     st.markdown("###### Task 2 DG Ranking")
#     st.dataframe(df2_1, height=280, hide_index=True, column_order=("Ranking", "Team Name",'Accuracy'))

# df2_2 = leaderboard_df_stage_1.iloc[:, [0, 3]]
# df2_2 = df2_2.rename(columns={
#     'team_name': 'Team Name',
#     'task2_dp': 'DP',
# })
# df2_2['Ranking'] = df2_2['DP'].rank(ascending=True)
# df2_2 = df2_2.sort_values(by='Ranking')
# df2_2 = df2_2.reset_index(drop=True)
# with col2:
#     st.markdown("###### Task 2 Fairness Ranking")
#     st.dataframe(df2_2, height=280, hide_index=True, column_order=("Ranking", "Team Name",'DP'))

# 得到task2最终排名
df_sorted_accuracy = leaderboard_df_stage_1.sort_values(by='task2_accuracy', ascending=False).reset_index(drop=True)
df_sorted_accuracy['accuracy_rank'] = df_sorted_accuracy.index + 1

df_sorted_dp = leaderboard_df_stage_1.sort_values(by='task2_dp').reset_index(drop=True)
df_sorted_dp['dp_rank'] = df_sorted_dp.index + 1

df_merged = pd.merge(df_sorted_accuracy, df_sorted_dp, on=['team_name', 'task1_accuracy', 'task2_accuracy', 'task2_dp'])
df_merged['weighted_rank'] = (0.3 * df_merged['accuracy_rank']) + (0.7 * df_merged['dp_rank'])
df_merged = df_merged.drop(columns=['task1_accuracy'])
df_final_rank = df_merged.sort_values(by='weighted_rank').reset_index(drop=True)
df_final_rank = df_final_rank.rename(columns={
    'team_name': 'Team Name',
    'task2_accuracy': 'Accuracy',
    'task2_dp': 'DP',
    'accuracy_rank': 'Accuracy Rank',
    'dp_rank':  'DP Rank',
    'weighted_rank': 'Weighted Rank'
})
df_final_rank['Ranking'] = df_final_rank['Weighted Rank'].rank(ascending=True)

st.markdown("###### Task 2 Ranking")
st.dataframe(df_final_rank, hide_index=True, column_order=("Ranking", "Team Name",'DP','DP Rank','Accuracy','Accuracy Rank','Weighted Rank'))

st.markdown("##### Stage 2")

st.markdown("###### Task 1 Ranking")

leaderboard_df_stage_1 = conn.query(f"select * from leaderboard where stage=2;", ttl=2)
leaderboard_df_stage_1 = leaderboard_df_stage_1.drop(columns=['team_id'])
df1 = leaderboard_df_stage_1.iloc[:, [0, 1]]
df1 = df1.rename(columns={
    'team_name': 'Team Name',
    'task1_accuracy': 'Accuracy',
})
df1['Ranking'] = df1['Accuracy'].rank(ascending=False)
df1 = df1.sort_values(by='Ranking')
df1 = df1.reset_index(drop=True)
st.dataframe(df1, hide_index=True, column_order=("Ranking", "Team Name",'Accuracy'))

# 得到task2最终排名
df_sorted_accuracy = leaderboard_df_stage_1.sort_values(by='task2_accuracy', ascending=False).reset_index(drop=True)
df_sorted_accuracy['accuracy_rank'] = df_sorted_accuracy.index + 1

df_sorted_dp = leaderboard_df_stage_1.sort_values(by='task2_dp').reset_index(drop=True)
df_sorted_dp['dp_rank'] = df_sorted_dp.index + 1

df_merged = pd.merge(df_sorted_accuracy, df_sorted_dp, on=['team_name', 'task1_accuracy', 'task2_accuracy', 'task2_dp'])
df_merged['weighted_rank'] = (0.3 * df_merged['accuracy_rank']) + (0.7 * df_merged['dp_rank'])
df_merged = df_merged.drop(columns=['task1_accuracy'])
df_final_rank = df_merged.sort_values(by='weighted_rank').reset_index(drop=True)
df_final_rank = df_final_rank.rename(columns={
    'team_name': 'Team Name',
    'task2_accuracy': 'Accuracy',
    'task2_dp': 'DP',
    'accuracy_rank': 'Accuracy Rank',
    'dp_rank':  'DP Rank',
    'weighted_rank': 'Weighted Rank'
})
df_final_rank['Ranking'] = df_final_rank['Weighted Rank'].rank(ascending=True)

st.markdown("###### Task 2 Ranking")
st.dataframe(df_final_rank, hide_index=True, column_order=("Ranking", "Team Name",'DP','DP Rank','Accuracy','Accuracy Rank','Weighted Rank'))

st.markdown("##### Stage 3 (Final stage)")

st.markdown("###### Task 1 Ranking")

leaderboard_df_stage_1 = conn.query(f"select * from leaderboard where stage=3;", ttl=2)
leaderboard_df_stage_1 = leaderboard_df_stage_1.drop(columns=['team_id'])
df1 = leaderboard_df_stage_1.iloc[:, [0, 1]]
df1 = df1.rename(columns={
    'team_name': 'Team Name',
    'task1_accuracy': 'Accuracy',
})
df1['Ranking'] = df1['Accuracy'].rank(ascending=False)
df1 = df1.sort_values(by='Ranking')
df1 = df1.reset_index(drop=True)
st.dataframe(df1, hide_index=True, column_order=("Ranking", "Team Name",'Accuracy'))

# 得到task2最终排名
df_sorted_accuracy = leaderboard_df_stage_1.sort_values(by='task2_accuracy', ascending=False).reset_index(drop=True)
df_sorted_accuracy['accuracy_rank'] = df_sorted_accuracy.index + 1

df_sorted_dp = leaderboard_df_stage_1.sort_values(by='task2_dp').reset_index(drop=True)
df_sorted_dp['dp_rank'] = df_sorted_dp.index + 1

df_merged = pd.merge(df_sorted_accuracy, df_sorted_dp, on=['team_name', 'task1_accuracy', 'task2_accuracy', 'task2_dp'])
df_merged['weighted_rank'] = (0.3 * df_merged['accuracy_rank']) + (0.7 * df_merged['dp_rank'])
df_merged = df_merged.drop(columns=['task1_accuracy'])
df_final_rank = df_merged.sort_values(by='weighted_rank').reset_index(drop=True)
df_final_rank = df_final_rank.rename(columns={
    'team_name': 'Team Name',
    'task2_accuracy': 'Accuracy',
    'task2_dp': 'DP',
    'accuracy_rank': 'Accuracy Rank',
    'dp_rank':  'DP Rank',
    'weighted_rank': 'Weighted Rank'
})
df_final_rank['Ranking'] = df_final_rank['Weighted Rank'].rank(ascending=True)

st.markdown("###### Task 2 Ranking")
st.dataframe(df_final_rank, hide_index=True, column_order=("Ranking", "Team Name",'DP','DP Rank','Accuracy','Accuracy Rank','Weighted Rank'))