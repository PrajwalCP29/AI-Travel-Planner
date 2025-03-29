import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["google"]["api_key"])

# Custom Page Config
st.set_page_config(page_title="AI Travel Planner", page_icon="🌍", layout="centered")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&display=swap');

    html[data-theme='light'] .title {
        color: #000000 !important; /* Black for Light Mode */
    }

    html[data-theme='dark'] .title {
        color: #FFFFFF !important; /* White for Dark Mode */
    }

    .title {
        text-align: center;
        font-size: 50px !important;
        font-weight: 900;
        font-family: 'Montserrat', sans-serif !important;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #555;
    }

    .stTextInput, .stNumberInput {
        border: 2px solid #FF5733 !important;
        border-radius: 10px;
    }

    .stButton > button {
        background-color: #FF5733 !important;
        color: white !important;
        font-size: 18px !important;
        border-radius: 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Header
st.markdown('<p class="title">🌍 AI Travel Planner</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Plan your perfect trip with AI! Enter your details below.</p>', unsafe_allow_html=True)

# Input Fields in a Grid Layout
col1, col2 = st.columns(2)

with col1:
    Your_Location = st.text_input("📍 Your Location", placeholder="e.g., Mumbai, Delhi, Hyderabad")
    days = st.number_input("📅 Number of Days", min_value=1, max_value=30, value=3)

with col2:
    destination = st.text_input("🌍 Destination", placeholder="e.g., Goa, Manali, Paris")
    budget = st.text_input("💰 Budget (INR)", placeholder="e.g., 5000, 10000")

# Generate Button with Animation
if st.button("✨ Generate Trip Plan"):
    if Your_Location and destination and days and budget:
        with st.spinner("Generating your travel itinerary... 🏖️"):
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            user_input = f"Plan a {days}-day trip from {Your_Location} to {destination} with a budget of {budget} INR. Include activities, food, and transport details."
            response = model.generate_content(user_input)
            trip_plan = response.text if hasattr(response, 'text') else "No response received."

            st.success("✅ Here is your personalized travel itinerary:")
            st.markdown(f"📌 **Trip Plan:**\n\n{trip_plan}")

            # Download Button
            st.download_button("📥 Download Itinerary", data=trip_plan, file_name="trip_plan.txt", mime="text/plain")

    else:
        st.warning("⚠️ Please fill in all fields before generating your plan.")
