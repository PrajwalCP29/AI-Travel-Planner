# 🌍 AI Travel Planner

# 📌 Project Description
AI Travel Planner is a Streamlit-based web app that helps users generate personalized travel itineraries using Google Gemini AI. Users can input their location, destination, budget, and trip duration to receive a detailed AI-generated travel plan that includes activities, food, and transport suggestions.

# 🚀 Features
🏖️ AI-generated trip plans based on user preferences
🗺️ User-friendly interface built with Streamlit
📥 Downloadable itinerary as a text file
🎨 Modern UI with custom styling
🔐 Secure API key management (via .env file)

# 🛠️ Installation & Setup
1. Clone the repository:
   git clone https://github.com/PrajwalCP29/AI-Travel-Planner.git
   cd AI-Travel-Planner
2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
3. Install dependencies:
   pip install -r requirements.txt
4. Set up API keys securely:
   Create a .env file in the root directory and add your API key:
   GOOGLE_API_KEY=your_google_api_key
   Load this key in your code using:
   from dotenv import load_dotenv
   import os
   load_dotenv()
   api_key = os.getenv("GOOGLE_API_KEY")
5. Run the app:
   streamlit run app.py

# 🚀 Deployment on Streamlit Cloud
   1.Push your code to GitHub.
   2.Go to Streamlit Cloud and connect your repo.
   3.Specify requirements.txt in the setup.
   4.Deploy & enjoy! 🎉

# 📧 Contact
For any issues or improvements, feel free to raise an issue or reach out at prajwalparihar292003@gmail.com
