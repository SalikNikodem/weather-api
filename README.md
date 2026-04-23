# weather-api
Weather API that fetches and returns weather data from a 3rd party API. 

A RESTful API that fetches weather data from a 3rd party service (Visual Crossing) and uses Redis for caching to improve performance and reduce API calls.

This project demonstrates how to work with external APIs, implement in-memory caching, and manage environment variables.

Features
Weather Fetching: Get current weather data for any city.

Redis Caching: Results are cached for 12 hours to speed up subsequent requests.

Error Handling: Graceful management of invalid city names or API failures.

Rate Limiting: Prevents abuse by limiting the number of requests per user.
