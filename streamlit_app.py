import streamlit as st
import speedtest

@st.cache(ttl=300)  # Set a timeout for 300 seconds (5 minutes)
def get_speed():
    st.text("Checking speed...")  # Show a message in the sidebar while checking speed
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10**6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10**6), 3)) + " Mbps"
    st.text("Speed check complete.")  # Show a message in the sidebar after checking speed
    return down, up

# Streamlit UI
st.title("Internet Speed Test")

# Download Speed Section
st.subheader("Download Speed")
lab_down = st.empty()  # Create a placeholder for download speed

# Upload Speed Section
st.subheader("Upload Speed")
lab_up = st.empty()  # Create a placeholder for upload speed

# Check Speed Button
if st.button("Check Speed"):
    down, up = get_speed()  # Call the get_speed function when the button is clicked
    lab_down.text(down)
    lab_up.text(up)
