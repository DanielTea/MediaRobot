import streamlit as st

def sidebar(authenticator):
    with st.sidebar:
        
        # st.markdown("---")

        # Add login buttons for social media sites
        # st.markdown("# Social Media Logins")
        # twitter_login = st.button("Login to Twitter")
        # linkedin_login = st.button("Login to LinkedIn")
        # instagram_login = st.button("Login to Instagram")

        # TODO: Add logic to handle button clicks and log in the user
        
        st.markdown("Made by Daniel Tremer [LinkedIn](https://www.linkedin.com/in/daniel-tremer/) [GitHub](https://github.com/DanielTea)")
        st.markdown("---")
        authenticator.logout('Logout', 'main')

