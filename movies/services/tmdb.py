import requests
from django.conf import settings


class TMDbAPIError(Exception):
    """Custom exception for TMDb API errors."""


def fetch_from_tmdb(endpoint, params=None):
    """
    Generic TMDb fetcher with error handling.
    """
    url = f"{settings.TMDB_BASE_URL}/{endpoint}"
    params = params or {}
    params["api_key"] = settings.TMDB_API_KEY

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "results" in data:
            return data["results"]
        return data
    except requests.exceptions.RequestException as e:
        raise TMDbAPIError(f"TMDb API request failed: {str(e)}")
    except ValueError:
        raise TMDbAPIError("Invalid JSON response from TMDb API")
