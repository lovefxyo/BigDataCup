import streamlit as st
import sqlalchemy.exc
from sqlalchemy.sql import text
from utils import generate_random_string, is_valid_email


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

st.markdown("#### Team Registration")

st.markdown("Register your team to participate in the *Challenges of Trustworthy AI in Distribution Shifts and Algorithmic Fairness 2024*. Each team consists of at least one captain and up to five other members. Each team will be assigned **a unique team ID** as the sole identifier for submissions, so please refrain from disclosing your team ID to others to avoid unnecessary complications.")

st.markdown("If you have already registered, please do not register again and ignore this page. Please note that each team leader can only form one team.")

# 如果没有input的内容，获取到的是空字符串''
leader_name = st.text_input("Leader's name (required):", '')
leader_email = st.text_input("Leader's email address (required):", '')
leader_affiliation = st.text_input("Leader's affiliation (required):", '')
team_name = st.text_input("Team's name (required):", '')
members_name = st.text_input("Other team members' name. Please list members separated by commas.", '')
members_email = st.text_input("Other team members' email address. Please list members separated by commas.", '')
members_affiliation = st.text_input("Other team members' affiliation. Please list members separated by commas.", '')
st.markdown("*Note that the information of other team members should correspond one-to-one.")


if st.button('Register'):
    conn = st.connection('bigdatacupdb', type='sql')
    val_flag = 1
    # 判断必填项
    if len(leader_name) != 0 and len(leader_email) != 0 and len(leader_affiliation) != 0 and len(team_name) != 0:
        # 判断邮箱格式是否正确
        if is_valid_email(leader_email):
            # 判断队长是否已经注册过team
            is_reg = conn.query(f"select count(*) from teamsForCup where leader_name='{leader_name}' and leader_email='{leader_email}';",ttl=2)
            if is_reg.iloc[0, 0] == 0:
                # 判断队伍名是否已被注册
                team_name_df = conn.query(f"select team_name from teamsForCup;",ttl=2)
                team_name_list = team_name_df['team_name'].to_list()
                # st.write(team_name_list)
                if team_name not in team_name_list:
                    # 计算其他队员的数量
                    num1 = -1 if len(members_name)==0 else members_name.count(",")
                    num1 += 1
                    num2 = -1 if len(members_email)==0 else members_email.count(",")
                    num2 += 1
                    num3 = -1 if len(members_affiliation)==0 else members_affiliation.count(",")
                    num3 += 1
                    # 判断三个input中的数量是否一致
                    if num1==num2 and num1==num3:
                        # 判断队员数量是否符合要求（至多五名）
                        if num1 <= 5:
                            other_members_num = num1
                            # 判断队员的邮箱格式是否正确
                            members_emails_list = members_email.split(",")
                            if num1 != 0:
                                for email in members_emails_list:
                                    if not is_valid_email(email):
                                        val_flag = 0
                                        break
                            if val_flag == 1:
                                # 通过验证，队伍注册成功，生成队伍id并入库
                                team_id = generate_random_string()
                                
                                team_num = conn.query('select count(*) from teamsForCup;',ttl=2)
                                try:
                                    with conn.session as s:
                                        try:
                                            s.execute(
                                                text(f"""INSERT INTO teamsForCup (id, team_id, leader_name, leader_email, leader_affiliation, team_name, 
                                                other_members_num, other_members_name, other_members_email, other_members_affiliation) 
                                                VALUES ({team_num.iloc[0, 0]+1},'{team_id}','{leader_name}','{leader_email}','{leader_affiliation}','{team_name}',
                                                {other_members_num},'{members_name}','{members_email}','{members_affiliation}');""")
                                            )
                                            s.commit()

                                            st.success(f'Registration successful, your team ID is {team_id}. Do not disclose your team ID to others!', icon="✅")
                                            conn = st.connection('bigdatacupdb', type='sql')
                                        except sqlalchemy.exc.SQLAlchemyError as e:
                                            # 在捕获到 SQLAlchemy 异常时进行回滚
                                            st.error(f'Dataset error: {e}.', icon="🚨")
                                            s.rollback()

                                except Exception as e:
                                    # 在捕获到其他异常时进行处理
                                    st.error(f'Dataset error: {e}.', icon="🚨")
                            else:
                                st.error('Registration failed: incorrect member email format.', icon="🚨")
                        else:
                            st.error('Registration failed: too many team members.', icon="🚨")
                    else:
                        st.error('Registration failed: the number of other team members filled in is inconsistent.', icon="🚨")
                else:
                    st.error('Registration failed: team name has been registered.', icon="🚨")
            else:
                st.error('Registration failed: the captain has already registered.', icon="🚨")
        else:
            st.error('Registration failed: incorrect leader email format.', icon="🚨")
    else:
        st.error('Registration failed: required fields cannot be empty.', icon="🚨")

