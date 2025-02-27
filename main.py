from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import requests
import os
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Weather API",
    description="A simple API to get weather information for any city",
    version="1.0.0"
)

# Get API key from environment variable
API_KEY = os.getenv("WEATHERAPI_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

@app.get("/weather/{city}")
async def get_weather(city: str):
    """Get weather information for a specific city.

    Args:
        city (str): Name of the city

    Returns:
        dict: Weather information including temperature, humidity, and description
    """
    try:
        # Make request to WeatherAPI
        params = {
            "key": API_KEY,
            "q": city
        }
        
        # Get weather data
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        logger.info(f">>>> debug: {data}")
        # Extract relevant weather information
        current = data["current"]
        weather_info = {
            "city": data["location"]["name"],
            "temperature": current["temp_c"],
            "humidity": current["humidity"],
            "description": current["condition"]["text"],
            "feels_like": current["feelslike_c"]
        }
        
        logger.info(f"Successfully retrieved weather data for {city}")
        return weather_info
        
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred while fetching weather data for {city}: {str(e)}")
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail=f"City '{city}' not found. Please check the city name and try again."
            )
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch weather data. Please try again with a valid city name."
        )
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Failed to fetch weather data")
    except KeyError as e:
        raise HTTPException(status_code=404, detail="City not found")

@app.get("/")
async def root():
    """Root endpoint that provides API information."""
    return {
        "message": "Welcome to the Weather API",
        "usage": "Make a GET request to /weather/{city} to get weather information"
    }