import streamlit as st
from streamlit_option_menu import option_menu
import residoodle
import about
import feedback

st.set_page_config(
    page_title = 'Residoodle',
    page_icon = '🦝'
)

title_cols = st.columns([1, 5])
with title_cols[0]:
    st.image('raccoon.png', width=100)
with title_cols[1]:
    st.title('ResiDoodle')
    st.caption("It's a doodle poll that fills itself out!")

selected = option_menu(None, ["Home", "About", "Feedback"], 
    icons=['house', 'question-circle', "chat-left-text"], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected == 'Home':
    residoodle.run()
elif selected == 'About':
    about.run()
elif selected == 'Feedback':
    feedback.run()