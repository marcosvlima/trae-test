# trae-test
(DEMO) Just a weather rest API built with trae agent

## Prerequisites

- Python 3.7 or higher
- WeatherAPI.com API key (get it from [WeatherAPI.com](https://www.weatherapi.com/))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/trae-test.git
cd trae-test
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your WeatherAPI.com API key as follows:
     ```
     WEATHERAPI_KEY=your_api_key_here
     ```

## Running the Application

Start the server with:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Usage

### Get Weather Information

```bash
curl http://localhost:8000/weather/{city}
```

Replace `{city}` with the name of the city you want to get weather information for.

Example response:
```json
{
    "city": "London",
    "temperature": 15.6,
    "humidity": 75,
    "description": "Partly cloudy",
    "feels_like": 14.8
}
```
