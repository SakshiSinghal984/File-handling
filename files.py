import streamlit as st
import pandas as pd

st.subheader("Loading the CSV file")
df = st.file_uploader("Upload the CSV file : ", type=["csv","xlsx"])
df = pd.read_csv("vgsales_cleaned.csv")
if df is not None:
    st.table(df.head(20))

st.subheader("Working with images")
img = st.file_uploader("Upload the image file : ", type=["png","jpg","jpeg"])
if img is not None:
    st.image(img)

st.subheader("Working with videos")
vid = st.file_uploader("Upload the video file : ", type=["mkv","mp4"])
if vid is not None:
    st.video(vid,start_time=0)

st.subheader("Working with audios")
aud = st.file_uploader("Upload the audio file : ", type=["wav","mp3"])
if aud is not None:
    st.audio(aud.read())




