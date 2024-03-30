import pickle
import streamlit as st
import pandas as pd
import random
from datetime import datetime


n = 100
words_ = ['self-motivate', 'self-starter', 'ambitious', 'assertive', 'driven', 'results-driven', 'tenacious',
          'resourceful', 'solution-orientation', 'goal-oriented', 'forward-thinking', 'motivation',
          'strategically-important', 'flexible', 'client-service', 'self-start', 'customer-oriented', 'achiever',
          'business-savvy', 'metrics-driven', 'solution-development', 'achievement-oriented', 'problem-solving',
          'results', 'focused', 'resilience', 'influential', 'nimble', 'approachable', 'communicator', 'self-improve',
          'references', 'multiple-tasks', 'self-initiates', 'data-driven', 'solutions-focus', 'execution-focused',
          'accountability', 'initiative', 'results-driven', 'career-oriented', 'hard-worker', 'impactful',
          'growth-focused', 'decisive', 'high-performing', 'strategic-thinker', 'quantifiable', 'critical-thinking',
          'achievement-focused', 'demanding', 'innovative', 'career-driven', 'product-driven', 'change-driver',
          'overachieving', 'execution-oriented', 'impact-driven', 'results-based', 'delivery-centric', 'risk-takers',
          'mission-driven', 'integrity', 'hard-working', 'fast-learner', 'goalschampioning', 'influence', 'dependable',
          'exceptional', 'enthusiasm', 'disciplined-but-entrepreneurial', 'growth-mindset', 'demonstrable',
          'results-orient', 'desired', 'self-structure', 'tasksrequiring', 'resourcefulness', 'over-achiever',
          'environmentwilling', 'quota-driven', 'quality-minded', 'metric-driven', 'goal-based', 'self-starter',
          'self-reliant', 'drive', 'solutions-orientation', 'team-drive', 'high-valuecommunications', 'quick-learning',
          'goal-oriented', 'performance-driven', 'productive', 'victories', 'multitasking', 'schedulemotivated',
          'detailresults', 'followership', 'high-pressure', 'high-performance', 'proactive', 'metrics-based',
          'goal-setting', 'results-driven', 'self-motivated', 'entrepreneurial', 'numbers-oriented', 'nimbleness',
          'challenging', 'expertise-based', 'persistence', 'inspiring', 'demonstratescost-effective', 'boldmark',
          'closingability', 'partnersdemonstrated', 'strategic',
          'sales-tax-manager-for-leading-sales-tax-consulting-firm', 'entrepreneurially', 'challenge', 'high-impact',
          'improvementgoals']


@st.cache_data
def fetch_data():
    with open("data.json", "rb") as fp:
        data = pickle.load(fp)
    sampled_data = {}
    for key, value in data.items():
        sampled_data[key] = random.sample(value, min(n, len(value)))
    del data
    return sampled_data


watch_list_ = fetch_data()
option_ = st.selectbox('TOP 123 Words with stress', words_)

if option_:
    values = st.number_input("please choose a JD within " + str(n), min_value=0, max_value=n-1, step=1)
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

