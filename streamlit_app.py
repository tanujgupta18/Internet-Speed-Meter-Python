import streamlit as st
import speedtest

def speedcheck():
    st.write("Testing internet speed... Please wait.")
    sp = speedtest.Speedtest()
    sp.get_servers()
    download_speed = sp.download() / 1_000_000  # Convert to Mbps
    upload_speed = sp.upload() / 1_000_000  # Convert to Mbps
    st.write(f"Download Speed: {download_speed:.3f} Mbps")
    st.write(f"Upload Speed: {upload_speed:.3f} Mbps")

st.title("Internet Speed Test")
st.markdown("### Download and Upload Speed Test")

if st.button("Check Speed"):
    speedcheck()
