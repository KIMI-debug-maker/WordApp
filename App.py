import pickle
import streamlit as st
import pandas as pd
import random
from datetime import datetime


n = 10
words_ = ['self-motivate', 'self-start', 'ambitious', 'results-driven', 'resourceful', 'solution-orient',
          'goal-oriented', 'proactive', 'performance-driven', 'persistent', 'deadline-driven', 'hardworking',
          'collaborative', 'multi-tasking', 'fact-pace', 'forward-thinking', 'motivation', 'strategically-important',
          'flexibleteam', 'self-start', 'fast-paced', 'customer-oriented', 'self-motivat', 'achiever',
          'rapidly-changing', 'business-savvy', 'excels', 'relentlessly', 'metrics-driven', 'achievement-oriented',
          'problem-solving', 'highly-driven', 'adapt', 'persevering', 'results', 'nimble', 'resilience', 'persevere',
          'influential', 'face-paced', 'problem-solvers', 'self-improve', 'matrixed', 'multiple-tasks',
          'self-initiates', 'selfmotivate', 'data-driven', 'goal-focused', 'execution-focused', 'self-reliance',
          'initiative', 'drivingresults', 'results-drive', 'career-oriented', 'hard-worker', 'impactful',
          'growth-focused', 'decisive', 'high-performing', 'accountability', 'strategic-thinker', 'quantifiable',
          'critical-thinking', 'excellence', 'integrity', 'success-centric', 'demanding', 'innovative', 'career-driven',
          'product-driven', 'overachieving', 'execution-oriented', 'delivery-centric', 'results-based', 'solvequotes',
          'integrity', 'hard-working', 'fast-learner', 'goalschampioning', 'hunger', 'change-oriented', 'organized',
          'dependable', 'enthusiasm', 'disciplined-but-entrepreneurial', 'high-pace', 'growth-mindset', 'excellen',
          'pressured', 'imaginative', 'quick-learner', 'desired', 'self-structure', 'tasksrequiring', 'resourcefulness',
          'over-achiever', 'quality-minded', 'quota-driven', 'motivated', 'detail-orientation', 'metric-driven',
          'organizational', 'goal-based', 'bottom-line', 'self-starter', 'self-reliant', 'drive', 'clearly',
          'tasks-strong', 'solutions', 'team-drive', 'entrepreneur-mind', 'quick-learning', 'goal-orientated',
          'performance', 'productive', 'assertiveness', 'mission-driven', 'victories', 'multitasking',
          'schedulemotivated', 'detailresults', 'leadership', 'experienceproactive', 'metrics-based', 'high-pressure',
          'over-achieving', 'high-performance', 'goal-setting', 'results-drivenenvironment', 'numbers-oriented',
          'prioritize', 'resultsmust', 'challenging', 'demonstratescost-effective', 'strategising', 'closingability',
          'challenge', 'team-centered', 'revenuefood', 'high-impact', 'goalsachieving', 'improvementgoals',
          'executionsupreme', 'straightforward']


@st.cache_data
def fetch_data():
    with open("data.json", "rb") as fp:
        data = pickle.load(fp)
    return data


watch_list_ = fetch_data()
option_ = st.selectbox('TOP 145 Words with stress', words_)

if option_:
    values = st.number_input("please choose a JD within " + str(n), min_value=0, max_value=min(n, len(watch_list_[option_]))-1, step=1)
    st.write(watch_list_[option_][values])

with st.sidebar:
    da = [{"Words": word, "Rating 1-5": 0, "is_chosen": False} for word in words_]
    df = pd.DataFrame(da)
    edited_df = st.experimental_data_editor(df)
    @st.cache_data
    def convert_df(df_):
        return df_.to_csv().encode('utf-8')
    current_time_str = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    csv = convert_df(edited_df)
    st.download_button(
        label="Download Rating Results as CSV",
        data=csv,
        file_name="Words_result_"+current_time_str+".csv",
        mime='text/csv',
    )

