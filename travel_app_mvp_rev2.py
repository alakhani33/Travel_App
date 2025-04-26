# travel_app_mvp_rev2.py

import streamlit as st
import requests
import os
import random

GEOAPIFY_API_KEY = st.secrets["GEOAPIFY_API_KEY"]
OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]

# API keys from environment variables
# OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
# GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")

# Base URLs
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
GEOAPIFY_URL = "https://api.geoapify.com/v2/places"
GEOCODE_URL = "https://api.geoapify.com/v1/geocode/search"

# Sample cities mapped by month (same as before)
MONTH_CITIES = {
    "january": [{"city": "Sydney", "country": "Australia", "lat": -33.8688, "lon": 151.2093, "cost": 140}],
    "february": [{"city": "Rio de Janeiro", "country": "Brazil", "lat": -22.9068, "lon": -43.1729, "cost": 120}],
    "march": [{"city": "Tokyo", "country": "Japan", "lat": 35.6762, "lon": 139.6503, "cost": 170}],
    "april": [{"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041, "cost": 140}],
    "may": [{"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964, "cost": 160}],
    "june": [{"city": "Reykjavik", "country": "Iceland", "lat": 64.1355, "lon": -21.8954, "cost": 180}],
    "july": [{"city": "Vancouver", "country": "Canada", "lat": 49.2827, "lon": -123.1207, "cost": 150}],
    "august": [{"city": "Edinburgh", "country": "Scotland", "lat": 55.9533, "lon": -3.1883, "cost": 130}],
    "september": [{"city": "Munich", "country": "Germany", "lat": 48.1351, "lon": 11.5820, "cost": 140}],
    "october": [{"city": "New York City", "country": "USA", "lat": 40.7128, "lon": -74.0060, "cost": 200}],
    "november": [{"city": "Dubai", "country": "UAE", "lat": 25.276987, "lon": 55.296249, "cost": 190}],
    "december": [{"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738, "cost": 130}]
}

# Interesting facts for landmarks
LANDMARK_FACTS = {
    "eiffel tower": [
        "Built for the 1889 World's Fair",
        "Was initially considered an eyesore",
        "Receives over 7 million visitors each year"
    ],
    "machu picchu": [
        "Rediscovered by Hiram Bingham in 1911",
        "Believed to be an estate for Incan emperors",
        "One of the New Seven Wonders of the World"
    ],
    "statue of liberty": [
        "Gifted by France in 1886",
        "Designed by Frédéric Auguste Bartholdi",
        "Symbolizes freedom and democracy"
    ],
    "great wall of china": [
        "Over 13,000 miles long",
        "Construction began as early as the 7th century BC",
        "Built to protect Chinese states against invasions"
    ],
    "taj mahal": [
        "Built by Emperor Shah Jahan in memory of his wife",
        "Considered the jewel of Muslim art in India",
        "Attracts millions of visitors annually"
    ]
}

# Sample cities mapped by regions
REGION_CITIES = {
    "europe": [
        {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522, "cost": 160},
        {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964, "cost": 150}
    ],
    "asia": [
        {"city": "Tokyo", "country": "Japan", "lat": 35.6762, "lon": 139.6503, "cost": 170},
        {"city": "Bangkok", "country": "Thailand", "lat": 13.7563, "lon": 100.5018, "cost": 90}
    ],
    "north america": [
        {"city": "New York City", "country": "USA", "lat": 40.7128, "lon": -74.0060, "cost": 200},
        {"city": "Toronto", "country": "Canada", "lat": 43.651070, "lon": -79.347015, "cost": 150}
    ],
    "south america": [
        {"city": "Buenos Aires", "country": "Argentina", "lat": -34.6037, "lon": -58.3816, "cost": 100},
        {"city": "Lima", "country": "Peru", "lat": -12.0464, "lon": -77.0428, "cost": 80}
    ],
    "africa": [
        {"city": "Cape Town", "country": "South Africa", "lat": -33.9249, "lon": 18.4241, "cost": 110},
        {"city": "Marrakech", "country": "Morocco", "lat": 31.6295, "lon": -7.9811, "cost": 90}
    ],
    "australia": [
        {"city": "Sydney", "country": "Australia", "lat": -33.8688, "lon": 151.2093, "cost": 140}
    ],
    "antarctica": [
        {"city": "McMurdo Station", "country": "Antarctica", "lat": -77.8419, "lon": 166.6863, "cost": 300}
    ]
}

# Fun facts for regions
REGION_FACTS = {
    "europe": ["Home to 44 countries", "Birthplace of Western civilization", "Host of many historic landmarks like the Colosseum and Eiffel Tower"],
    "asia": ["Largest and most populous continent", "Home to Mount Everest and the Great Wall of China", "Diverse cultures and cuisines"],
    "north america": ["Includes USA, Canada, and Mexico", "Home to Grand Canyon, Niagara Falls, and diverse cities", "Rich in cultural diversity"],
    "south america": ["Famous for Amazon Rainforest and Andes Mountains", "Birthplace of tango and samba", "Home to Machu Picchu and Christ the Redeemer"],
    "africa": ["Origin of human civilization", "Home to Sahara Desert and Serengeti", "Rich in wildlife and culture"],
    "australia": ["Smallest continent but vast in natural beauty", "Home to Great Barrier Reef and unique wildlife", "Known for beaches and the Outback"],
    "antarctica": ["Coldest and driest continent", "Home to vast ice sheets and penguins", "Research stations, not cities"]
}

# Streamlit interface
st.title("🌍 Travel Recommendation App")

query = st.text_input("Enter a month, landmark, or region:", "July")

if st.button("Get Recommendations"):
    st.write("Generating recommendations for:", query)

    query_lower = query.lower()
    if query_lower in MONTH_CITIES:
        st.info(f"Showing destinations ideal for {query.title()}:")
        for dest in MONTH_CITIES[query_lower]:
            st.markdown(f"### {dest['city']}, {dest['country']}")
            weather_params = {"lat": dest['lat'], "lon": dest['lon'], "appid": OPENWEATHER_API_KEY, "units": "metric"}
            weather_resp = requests.get(WEATHER_URL, params=weather_params).json()
            if "main" in weather_resp:
                temp = weather_resp["main"]["temp"]
                desc = weather_resp["weather"][0]["description"]
                st.write(f"🌤️ Current Weather: {temp}°C, {desc}")
            st.write(f"💸 Estimated Daily Cost: ${dest['cost']}")

            hotel_params = {
                "categories": "accommodation.hotel",
                "filter": f"circle:{dest['lon']},{dest['lat']},5000",
                "limit": 1,
                "apiKey": GEOAPIFY_API_KEY
            }
            hotel_resp = requests.get(GEOAPIFY_URL, params=hotel_params).json()
            for hotel in hotel_resp.get("features", []):
                props = hotel["properties"]
                st.write(f"🏨 Hotel Suggestion: {props['name']} – {props.get('address_line1', '')}")
            st.markdown("---")

    elif query_lower in LANDMARK_FACTS:
        st.info(f"Treating '{query}' as a landmark.")
        geo_url = f"{GEOCODE_URL}?text={query}&apiKey={GEOAPIFY_API_KEY}"
        response = requests.get(geo_url).json()
        if response['features']:
            coords = response['features'][0]['geometry']['coordinates']
            lon, lat = coords[0], coords[1]
            st.write(f"Located at: {lat:.2f}, {lon:.2f}")

            weather_params = {"lat": lat, "lon": lon, "appid": OPENWEATHER_API_KEY, "units": "metric"}
            weather_resp = requests.get(WEATHER_URL, params=weather_params).json()
            if "main" in weather_resp:
                temp = weather_resp["main"]["temp"]
                desc = weather_resp["weather"][0]["description"]
                st.success(f"Current weather: {temp}°C, {desc}")

            st.write("📚 Interesting Facts:")
            facts = LANDMARK_FACTS.get(query_lower, [])
            random.shuffle(facts)
            for fact in facts:
                st.write(f"- {fact}")

            hotel_params = {
                "categories": "accommodation.hotel",
                "filter": f"circle:{lon},{lat},5000",
                "limit": 3,
                "apiKey": GEOAPIFY_API_KEY
            }
            hotel_resp = requests.get(GEOAPIFY_URL, params=hotel_params).json()
            st.subheader("Nearby Hotels:")
            for hotel in hotel_resp.get("features", []):
                props = hotel["properties"]
                st.write(f"🏨 {props['name']} – {props.get('address_line1', '')}")
        else:
            st.warning("Couldn't geocode that landmark. Try another.")

    elif query_lower in REGION_CITIES:
        st.info(f"Showing popular destinations in {query.title()}:")
        st.write("📚 Interesting Facts:")
        facts = REGION_FACTS.get(query_lower, [])
        random.shuffle(facts)
        for fact in facts:
            st.write(f"- {fact}")

        for dest in REGION_CITIES[query_lower]:
            st.markdown(f"### {dest['city']}, {dest['country']}")
            weather_params = {"lat": dest['lat'], "lon": dest['lon'], "appid": OPENWEATHER_API_KEY, "units": "metric"}
            weather_resp = requests.get(WEATHER_URL, params=weather_params).json()
            if "main" in weather_resp:
                temp = weather_resp["main"]["temp"]
                desc = weather_resp["weather"][0]["description"]
                st.write(f"🌤️ Current Weather: {temp}°C, {desc}")
            st.write(f"💸 Estimated Daily Cost: ${dest['cost']}")

            hotel_params = {
                "categories": "accommodation.hotel",
                "filter": f"circle:{dest['lon']},{dest['lat']},5000",
                "limit": 1,
                "apiKey": GEOAPIFY_API_KEY
            }
            hotel_resp = requests.get(GEOAPIFY_URL, params=hotel_params).json()
            for hotel in hotel_resp.get("features", []):
                props = hotel["properties"]
                st.write(f"🏨 Hotel Suggestion: {props['name']} – {props.get('address_line1', '')}")
            st.markdown("---")

    else:
        st.warning("Query not recognized. Try a month, a famous landmark, or a continent like 'Europe'.")
