from bardapi import BardCookies
import streamlit as st

# Set up the BardCookies instance with your predefined cookie_dict
cookie_dict = {
    "__Secure-1PSID": "Enter your Bardapi cookies here",
    "__Secure-1PSIDTS": "Enter your Bardapi cookies here",
    "__Secure-1PSIDCC": "Enter your Bardapi cookies here"
}

bard = BardCookies(cookie_dict=cookie_dict)

# Streamlit web interface
st.title("Automated Code Review tool")

# User input
query = st.text_area("Enter your query:", height=100)

# Button to trigger the answer retrieval
if st.button("Get Answer"):
    with st.spinner("Fetching answer..."):
        reply = bard.get_answer(query)['content']
        st.success("Answer received!")
        st.write(reply)

# Additional Streamlit functions for a more appealing interface
st.markdown("---")
st.subheader("Additional Options")

# Checkbox to show/hide cookie information
show_cookies = st.checkbox("Show Cookie Information", value=False)
if show_cookies:
    st.write("Cookies Information:")
    st.write(cookie_dict)

# Slider for adjusting the font size of the answer
font_size = st.slider("Adjust Font Size", min_value=8, max_value=24, value=12, step=2)
st.markdown(f"<style>div.stButton > button {{ font-size: {font_size}px; }}</style>", unsafe_allow_html=True)
