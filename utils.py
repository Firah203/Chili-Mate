# utils.py
import streamlit as st
import streamlit.components.v1 as components
import os

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "style.css")
    with open(css_path, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_filtered_products(products, search_query, category_filter, min_price, max_price):
    filtered_products = [
        product for product in products
        if (category_filter == "All" or product["category"] == category_filter) and
           (search_query.lower() in product["name"].lower())
    ]
    return filtered_products

def show_cart():
    import streamlit as st

    st.subheader("🛒 Keranjang Belanja")
    cart = st.session_state.get("cart", [])
    
    if not cart:
        st.info("Keranjang masih kosong.")
    else:
        for item in cart:
            st.markdown(f"- *{item['name']}* — Rp{item['price']:,}")

    