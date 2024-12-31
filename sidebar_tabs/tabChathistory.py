import streamlit as st
import os
import ijson


def render_chathistory():
    chathistory_navication = []
    with open("chathistory.json", "rb") as f:
        for item in ijson.items(f, 'item'):
            chathistory_navication.append({
                "uuid": item["uuid"],
                "timestamp": item["timestamp"],
                "title": item["title"]
            })

    st.sidebar.markdown("""
    <style>        
    .stEmotionCache-1qdyr5 {
        padding: 1rem 1rem 3rem;
    }
    
    .stRadio > div {
        gap: 0;
    }
    .stRadio > div > label {
        # border-radius: 20px;
        cursor: pointer;
        width: 100%;
    }              
    .stRadio > div > label > div:first-child {
        display: none;
    }
    .stRadio > div > label > input[type="radio"]:not(:checked) + div:hover {
        border-radius: 10px;      
        background-color: #f0f0f0;
        width: 100%;
    }
    .stRadio > div > label > input[type="radio"]:checked + div {
        border-radius: 10px;      
        background-color: #c8cad9;
        width: 100%;
    } 
    </style>
    """, unsafe_allow_html=True)

    selected_history = st.radio(label="chatNavicator", options=chathistory_navication, format_func=lambda x: x["title"], captions=[
                                x["timestamp"] for x in chathistory_navication], label_visibility="collapsed", key="chatNavicator")
