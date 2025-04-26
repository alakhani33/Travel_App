
# 🌍 Travel Recommendation App

## Overview
This app helps users find the best cities to visit based on:
- A **month** (e.g., "July")
- A **landmark** (e.g., "Eiffel Tower")
- A **continent** or **region** (e.g., "Europe", "Asia")

It pulls real-time weather, suggests hotels, and shows estimated daily costs. It also provides interesting facts about destinations!

## Core Features
- 🌦️ Current Weather Summary
- 🏨 Nearby Hotel Suggestions
- 📚 Fun Facts about Locations
- 💸 Estimated Daily Costs
- 🗺️ Coverage for:
  - 12 Months (January - December)
  - Landmarks (Eiffel Tower, Machu Picchu, Statue of Liberty, etc.)
  - Regions (Continents like Europe, Asia, Africa, etc.)

## Technologies Used
- **Python** (backend logic)
- **Streamlit** (user interface)
- **OpenWeatherMap API** (weather data)
- **Geoapify Places API** (hotels and geocoding)
- **Pandas**, **Requests** (data handling)

## Project Structure
- `travel_app_mvp_rev2.py`: Main Streamlit app
- APIs are securely accessed through environment variables

## Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install streamlit requests
   ```
3. Set environment variables for API keys:
   ```bash
   export OPENWEATHER_API_KEY="your_openweather_api_key"
   export GEOAPIFY_API_KEY="your_geoapify_api_key"
   ```
4. Run the app:
   ```bash
   streamlit run travel_app_mvp_rev2.py
   ```

## Example Queries
- **Month**: `"July"` → Suggests cities like Vancouver, Barcelona, Cape Town
- **Landmark**: `"Eiffel Tower"` → Paris with weather and hotels
- **Region**: `"Europe"` → Recommends Paris, Rome, etc.

## Future Improvements
- Add image previews for cities and landmarks
- Allow user personalization (e.g., budget, activity preference)
- Expand city and attraction database
- Mobile app version (Flutter/React Native)

---

Made with ❤️ to inspire your next adventure!
