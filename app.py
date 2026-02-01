import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

st.set_page_config(page_title="CyberCell Money Trail", layout="wide")
st.title("🛡️ Financial Fraud Money Trail Analyzer")

uploaded_file = st.file_uploader("NCRP ya Bank Statement CSV Upload Karein", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Maan lijiye CSV mein 'From_Acc' aur 'To_Acc' columns hain
    st.write("### Raw Data Preview", df.head())

    # Network Graph Banayein
    net = Network(height="500px", width="100%", bgcolor="#ffffff", font_color="black", directed=True)
    
    for index, row in df.iterrows():
        net.add_node(row['From_Acc'], label=str(row['From_Acc']), color="#FF5733")
        net.add_node(row['To_Acc'], label=str(row['To_Acc']), color="#2ECC71")
        net.add_edge(row['From_Acc'], row['To_Acc'], value=row['Amount'], title=f"Amt: {row['Amount']}")

    # Visualization Save aur Show karein
    net.save_graph("trail.html")
    HtmlFile = open("trail.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height=600)
    
    st.success("Money Trail Graph Taiyaar Hai!")
