import streamlit as st
import speedtest

def speedcheck():
    st.sidebar.text("Checking speed...")
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10**6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10**6), 3)) + " Mbps"
    lab_down.text(down)
    lab_up.text(up)
    st.sidebar.text("Speed check complete.")

st.title("Internet Speed Test")

st.subheader("Download Speed")
lab_down = st.empty()

# Upload Speed Section
st.subheader("Upload Speed")
lab_up = st.empty()

# Check Speed Button
if st.button("Check Speed"):
    speedcheck()
