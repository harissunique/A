import streamlit as st
import streamlit.components.v1 as components

with open("a.html", "r") as f:
    html_content = f.read()

components.html(html_content, height=900)