import streamlit as st
import speedtest

@st.cache(ttl=300)  #timeout for 300 seconds (5 minutes)
def get_speed():
    st.text("Checking speed...")
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10**6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10**6), 3)) + " Mbps"
    st.text("Speed check complete.") 
    return down, up

st.title("Internet Speed Test")

# Download Speed Section
st.subheader("Download Speed")
lab_down = st.empty()

# Upload Speed Section
st.subheader("Upload Speed")
lab_up = st.empty()

# Check Speed Button
if st.button("Check Speed"):
    down, up = get_speed()
    lab_down.text(down)
    lab_up.text(up)
