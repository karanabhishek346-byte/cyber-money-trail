import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

st.set_page_config(page_title="CyberCell Trail Pro", layout="wide")
st.title("🛡️ Advanced Money Trail Analyzer")

# File Uploader for CSV and Excel
uploaded_file = st.file_uploader("Upload Bank Statement (CSV ya Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Check file type and load data
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.write("### Data Preview", df.head())

    # Column Selection (User khud select karega kaunsa column Sender hai aur kaunsa Receiver)
    columns = df.columns.tolist()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        sender_col = st.selectbox("Sender Account Column", columns)
    with col2:
        receiver_col = st.selectbox("Receiver Account Column", columns)
    with col3:
        amount_col = st.selectbox("Amount Column", columns)

    if st.button("Generate Trail Graph"):
        net = Network(height="600px", width="100%", bgcolor="#f4f4f4", font_color="black", directed=True)
        
        # Build the graph
        for index, row in df.iterrows():
            s = str(row[sender_col])
            r = str(row[receiver_col])
            a = str(row[amount_col])
            
            net.add_node(s, label=s, color="#FF5733", title="Sender")
            net.add_node(r, label=r, color="#2ECC71", title="Receiver")
            net.add_edge(s, r, value=float(a) if a.isdigit() else 1, title=f"Amount: {a}")

        # Save and Show
        net.save_graph("trail.html")
        with open("trail.html", 'r', encoding='utf-8') as f:
            components.html(f.read(), height=700)
            
        st.success("Analysis Complete!")import streamlit as st
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
