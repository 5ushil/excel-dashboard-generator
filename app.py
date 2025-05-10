# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os

st.set_page_config(page_title="Excel Data Presenter", layout="wide")
st.title("Excel to Professional Dashboard & Report Generator")

# Upload Excel File
uploaded_file = st.file_uploader("Upload your Excel file (.xlsx)", type=["xlsx"])

if uploaded_file:
    try:
        # Load all sheets into a dictionary
        xls = pd.ExcelFile(uploaded_file)
        sheet_names = xls.sheet_names
        selected_sheet = st.selectbox("Select Sheet", sheet_names)
        df = pd.read_excel(xls, sheet_name=selected_sheet)

        st.subheader("Raw Data")
        st.dataframe(df)

        # Detect numerical and categorical columns
        num_cols = df.select_dtypes(include=['number']).columns.tolist()
        cat_cols = df.select_dtypes(exclude=['number']).columns.tolist()

        # Automatic Visualization
        if len(num_cols) >= 1:
            st.subheader("Numeric Column Trends")
            x_col = st.selectbox("Select X-axis (Optional)", ["Index"] + num_cols)
            y_col = st.selectbox("Select Y-axis", num_cols)

            if x_col == "Index":
                fig = px.line(df, y=y_col, title=f"{y_col} Over Index")
            else:
                fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")

            st.plotly_chart(fig)

        if len(cat_cols) >= 1 and len(num_cols) >= 1:
            st.subheader("Categorical vs Numeric Comparison")
            cat_col = st.selectbox("Select Category", cat_cols)
            val_col = st.selectbox("Select Value", num_cols)
            fig = px.bar(df.groupby(cat_col)[val_col].mean().reset_index(),
                         x=cat_col, y=val_col, title=f"Average {val_col} by {cat_col}")
            st.plotly_chart(fig)

        # Generate Summary Statistics
        summary = df.describe(include='all').to_html()

        # Save Report
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('report.html')
        html_out = template.render(
            title="Automated Data Report",
            date=datetime.now().strftime("%Y-%m-%d"),
            table=df.head().to_html(classes='table'),
            summary=summary,
            chart1=fig.to_html(full_html=False, include_plotlyjs='cdn')
        )

        # Save HTML Report with UTF-8 encoding
        report_path = os.path.join("reports", "generated_report.html")
        os.makedirs("reports", exist_ok=True)
        with open(report_path, "w", encoding='utf-8') as f:
            f.write(html_out)

        st.success("✅ Report Generated!")
        with open(report_path, "r", encoding='utf-8') as f:
            btn = st.download_button("Download HTML Report", f, file_name="data_report.html")

    except Exception as e:
        st.error(f"Error: {e}")