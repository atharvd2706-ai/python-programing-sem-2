import streamlit as st

st.title("🛒 Grocery Bill Calculator")

st.write("Add your grocery items:")

# Initialize session state
if "items" not in st.session_state:
    st.session_state.items = []

# Add new item
if st.button("➕ Add Item"):
    st.session_state.items.append({"name": "", "price": 0.0, "qty": 1})

total = 0

# Display items
for i, item in enumerate(st.session_state.items):
    st.subheader(f"Item {i+1}")
    
    col1, col2, col3 = st.columns(3)
    
    item["name"] = col1.text_input("Name", value=item["name"], key=f"name_{i}")
    item["price"] = col2.number_input("Price", min_value=0.0, value=item["price"], key=f"price_{i}")
    item["qty"] = col3.number_input("Qty", min_value=1, value=item["qty"], key=f"qty_{i}")
    
    item_total = item["price"] * item["qty"]
    total += item_total
    
    st.write(f"Subtotal: ₹{round(item_total, 2)}")

st.write("---")

# Discount
discount = st.number_input("Discount (%)", min_value=0.0, max_value=100.0)

discount_amount = total * (discount / 100)
final_total = total - discount_amount

# Output
st.subheader("🧾 Final Bill")

st.write(f"Total: ₹{round(total, 2)}")
st.write(f"Discount: ₹{round(discount_amount, 2)}")
st.success(f"Final Amount to Pay: ₹{round(final_total, 2)}")