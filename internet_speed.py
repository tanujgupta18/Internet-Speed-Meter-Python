import streamlit as st
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    st.write("Getting the closest servers...")
    sp.get_best_server()
    st.write("Testing download speed...")
    download_speed = round(sp.download() / (10 ** 6), 3)
    st.write(f"Download Speed: {download_speed} Mbps")
    st.write("Testing upload speed...")
    upload_speed = round(sp.upload() / (10 ** 6), 3)
    st.write(f"Upload Speed: {upload_speed} Mbps")

st.title("Internet Speed Test")

st.markdown("### Download and Upload Speed Test")

if st.button("Check Speed"):
    speedcheck()
