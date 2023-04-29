import streamlit as st
from components.sidebar import sidebar
import prompts
from mediarobot.openai_functions import ask
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

 
import openai
import os
import dotenv

import replicate
import base64

dotenv.load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
REPLICATE_API_TOKEN  = os.environ["REPLICATE_API_TOKEN"]
GPT_MODEL = "gpt-3.5-turbo"

st.set_page_config(page_title="MediaRobot", 
                   page_icon="♥", 
                #    layout="wide",
                #    initial_sidebar_state="expanded",
                   )

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# css_path = os.path.join("static", "styles.css")

load_css("./static/styles.css")

def generate_social_media_content(media_name: str, media_prompt:str, general_description:str, picture_description:str, video_description:str):
        # Generate Twitter content using the ask function
        description = general_description + picture_description +video_description
        print(description)
        response = ask(message=description, prompt=media_prompt, model=GPT_MODEL)
        st.session_state[media_name] = response
        st.experimental_rerun()



def app():

    st.title("MediaRobot")

    # with open('./mediarobot/authentication/config.yaml') as file:
    #     config = yaml.load(file, Loader=SafeLoader)

    # authenticator = stauth.Authenticate(
    #     config['credentials'],
    #     config['cookie']['name'],
    #     config['cookie']['key'],
    #     config['cookie']['expiry_days'],
    #     config['preauthorized']
    # )

    # name, authentication_status, username = authenticator.login('Login', 'main')

    # if authentication_status:

        # sidebar(authenticator)

    sidebar()

    if "image" not in st.session_state:
        st.session_state["image"] = ""
    if "video" not in st.session_state:
        st.session_state["video"] = ""


    uploaded_image = st.file_uploader('Upload Image', type=['png', 'jpg'], accept_multiple_files=False, key=None, help=None, on_change=None, disabled=False, label_visibility="visible")

    if uploaded_image is not None:
        image_bytes_data = uploaded_image.getvalue()
        
        # Convert the image bytes to a base64 encoded string
        image_base64_str = base64.b64encode(image_bytes_data).decode('utf-8')

        # Determine the image format (either 'png' or 'jpg')
        image_format = 'png' if uploaded_image.type == 'image/png' else 'jpg'

        # Create a data URI
        image_data_uri = f"data:image/{image_format};base64,{image_base64_str}"
        
        description = replicate.run(
            "rmokady/clip_prefix_caption:9a34a6339872a03f45236f114321fb51fc7aa8269d38ae0ce5334969981e4cd8",
            use_beam_search=True,
            input={"image": image_data_uri}
        )

        st.session_state["image"] = description
        print(description)
        st.image(image_bytes_data, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    # uploaded_video = st.file_uploader('Upload Video *mp4 only!*', 
    #                                   type=['mp4'], 
    #                                   accept_multiple_files=False, 
    #                                   key=None, 
    #                                   help=None, 
    #                                   on_change=None, 
    #                                   disabled=False, 
    #                                   label_visibility="visible",
    #                                   )
    
    # if uploaded_video is not None:
    #     video_bytes_data = uploaded_video.getvalue()
    #     st.video(video_bytes_data, format="video/mp4", start_time=0)

    st.markdown("---")

    # Create description textfield
    st.write("General Description:")
    general_description = st.text_area("", height=200, value=prompts.general_description, key="general_desc")

    if uploaded_image is not None:
        # Create description textfield
        st.write("Picture Description:")
        picture_description = st.text_area("", height=200, value=prompts.picture_description.format(description=description), key="pic_desc")
        # st.experimental_rerun()
    else: 
        picture_description = ""

    # if uploaded_video is not None:
    #     # Create description textfield
    #     st.write("Video Description:")
    #     video_description = st.text_area("", height=200, value=prompts.video_description, key="vid_desc")
    # else:
    #     video_description = ""

    st.markdown("---")

    # Create social media textfields
    st.write("Social Media:")

    if "twitter" not in st.session_state:
        st.session_state["twitter"] = ""
    if "linkedin" not in st.session_state:
        st.session_state["linkedin"] = ""
    if "instagram" not in st.session_state:
        st.session_state["instagram"] = ""
    if "facebook" not in st.session_state:
        st.session_state["facebook"] = ""
    if "tiktok" not in st.session_state:
        st.session_state["tiktok"] = ""
    if "newsletter" not in st.session_state:
        st.session_state["newsletter"] = ""

    col1, col2, col3 = st.columns(3)
    with col1:
        twitter = st.text_area("Twitter", height=400, value=st.session_state["twitter"])
        twitter_create = st.button("Create Twitter Content")
    with col2:
        linkedin = st.text_area("LinkedIn", height=400, value=st.session_state["linkedin"])
        linkedin_create = st.button("Create LinkedIn Content")
    with col3:
        instagram = st.text_area("Instagram", height=400, value=st.session_state["instagram"])
        instagram_create = st.button("Create Instagram Content")

    col4, col5, col6 = st.columns(3)
    with col4:
        facebook = st.text_area("Facebook", height=400, value=st.session_state["facebook"])
        facebook_create = st.button("Create Facebook Content")
    with col5:
        tiktok = st.text_area("TikTok", height=400, value=st.session_state["tiktok"])
        tiktok_create = st.button("Create TikTok Content")
    with col6:
        newsletter = st.text_area("E-Mail Newsletter", height=400, value=st.session_state["newsletter"])
        newsletter_create = st.button("Create Newsletter Content")

    # Handle button clicks
    if twitter_create:
        # Generate Twitter content using the ask function
        generate_social_media_content(media_name ="twitter", 
                                        media_prompt=prompts.twitter_prompt, 
                                        general_description=general_description, 
                                        picture_description=st.session_state["image"], 
                                        video_description=st.session_state["video"])

    if linkedin_create:
        # Generate LinkedIn content using the ask function
        generate_social_media_content(media_name ="linkedin", 
                                        media_prompt=prompts.linkedin_prompt, 
                                        general_description=general_description, 
                                        picture_description=st.session_state["image"], 
                                        video_description=st.session_state["video"])

    if instagram_create:
        # Generate Instagram content using the ask function
        generate_social_media_content(media_name ="instagram", 
                                        media_prompt=prompts.instagram_prompt, 
                                        general_description=general_description, 
                                        picture_description=st.session_state["image"], 
                                        video_description=st.session_state["video"])

    # Handle button clicks
    if facebook_create:
        # Generate Twitter content using the ask function
        generate_social_media_content(media_name ="facebook", 
                                        media_prompt=prompts.facebook_prompt, 
                                        general_description=general_description, 
                                        picture_description=st.session_state["image"], 
                                        video_description=st.session_state["video"])

    if tiktok_create:
        # Generate LinkedIn content using the ask function
        generate_social_media_content(media_name ="tiktok", 
                                        media_prompt=prompts.tiktok_prompt, 
                                        general_description=general_description, 
                                        picture_description=picture_description, 
                                        video_description=st.session_state["video"])

    if newsletter_create:
        # Generate Instagram content using the ask function
        generate_social_media_content(media_name ="newsletter", 
                                        media_prompt=prompts.newsletter_prompt, 
                                        general_description=general_description, 
                                        picture_description=st.session_state["image"], 
                                        video_description=st.session_state["video"])

    # elif authentication_status is False:
    #     st.error('Username/password is incorrect')
    # elif authentication_status is None:
    #     st.warning('Please enter your username and password')


if __name__ == "__main__":

    app()
