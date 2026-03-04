import streamlit as st

st.set_page_config(page_title="Revenue-Intelligence-Platform-Suite", layout="wide")

st.title("Revenue-Intelligence-Platform-Suite")
st.caption("Unified portal for Revenue + Retention decision systems.")

st.markdown(
    """
### What You Can Access Here
- Executive KPI board with real integrated module data
- Direct links to all module repositories inside the monorepo
- Direct links to available public demos
"""
)

st.info(
    "Use the left sidebar pages to navigate: `Executive KPI Board` and `Modules Access`."
)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Primary Navigation")
    st.page_link("pages/1_Executive_KPI_Board.py", label="Open Executive KPI Board")
    st.page_link("pages/2_Modules_Access.py", label="Open Modules Access")

with col2:
    st.subheader("Public Demos")
    st.markdown(
        """
- Revenue Intelligence: https://revenue-intelligence-platform.streamlit.app/
- Data Senior Analytics: https://data-analytics-sr.streamlit.app
- Sales Analytics: https://analys-vendas-python.streamlit.app/
"""
    )

st.markdown("---")
st.subheader("Purpose")
st.write(
    "This flagship app is the access layer that unifies all modules into one platform "
    "experience, with business decision support as the core outcome."
)
