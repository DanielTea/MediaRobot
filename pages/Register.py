import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

import streamlit as st

st.set_page_config(
    page_title="Register",
    page_icon="👋",
)


with open('./mediarobot/authentication/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


try:
    if authenticator.register_user('Register user', preauthorization=False):

        with open('./mediarobot/authentication/config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)

        st.success('User registered successfully')
except Exception as e:
    st.error(e)
