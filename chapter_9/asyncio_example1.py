# Import the asyncio module for asynchronous programming
import asyncio

# Import the aiohttp module for making HTTP requests asynchronously
import aiohttp

# Import the pprint module for pretty-printing data structures
from pprint import pprint


# Define an asynchronous function to fetch data from a given URL
async def fetch_data(url):
    print(f"Fetching data from {url}")

    # Create an aiohttp ClientSession
    async with aiohttp.ClientSession() as session:

        # Send a GET request to the URL
        async with session.get(url) as response:

            # Check if the response status is 200 (OK)
            if response.status == 200:

                # Parse the JSON response
                data = await response.json()

                print(f"Data fetched from {url}")

                # Return the fetched data
                return data
            else:
                print(
                    f"Failed to fetch data from {url}, status code: {response.status}"
                )

                # Return None if the fetch failed
                return None


# Define the main asynchronous function
async def main():
    # List of URLs to fetch data from
    urls = [
        "https://catfact.ninja/fact",  # URL for fetching a cat fact
        "https://api.chucknorris.io/jokes/random",  # URL for fetching a Chuck Norris joke
    ]

    # Create a list of tasks to fetch data from each URL
    tasks = [fetch_data(url) for url in urls]

    # Execute all tasks concurrently and gather the results
    results = await asyncio.gather(*tasks)

    # Iterate over the results
    for result in results:

        # Pretty-print each result
        pprint(result)


# Run the main function using asyncio.run
asyncio.run(main())
