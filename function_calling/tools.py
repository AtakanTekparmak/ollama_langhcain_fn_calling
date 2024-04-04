import random

from math import sqrt
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain.chains import create_extraction_chain

def return_random_number() -> int:
    """Return a random number."""
    return 313131

def return_random_city() -> str:
    """Return a random city."""
    cities = ["San Francisco", "New York", "Boston", "Los Angeles", "Chicago", "Seattle"]
    return random.choice(cities)

def get_current_weather(location: str) -> str:
    """
    Get the weather in a given location.
    
    Args:
        location (str): The city, e.g. San Francisco.
    """
    mock_data_dict = {
        "Boston": "The weather in Boston is sunny and 53 degrees fahrenheit.",
        "San Francisco": "The weather in San Francisco is foggy and 60 degrees fahrenheit.",
        "New York": "The weather in New York is cloudy and 45 degrees fahrenheit.",
    }
    return mock_data_dict[location]