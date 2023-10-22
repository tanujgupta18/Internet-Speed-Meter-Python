import streamlit as st
import speedtest
import time

def speedcheck():
    st.write("Testing your internet speed. Please wait...")
    sp = speedtest.Speedtest()
    download_speed = sp.download()
    upload_speed = sp.upload()
    
    st.write("Download Speed: {:.2f} Mbps".format(download_speed / 10**6))
    st.write("Upload Speed: {:.2f} Mbps".format(upload_speed / 10**6))

st.title("Internet Speed Test")

st.markdown("### Download and Upload Speed Test")

if st.button("Check Speed"):
    speedcheck()
