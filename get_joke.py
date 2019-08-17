# Import the library
import requests

def main():
    # Get the API endpoint
    URL = "https://api.chucknorris.io/jokes/random"

    # Store the result here
    result = requests.get(url = URL)

    # Convert the result to json format
    json_data = result.json()
    json_joke_value = json_data["value"]

    # Display the joke
    print (json_joke_value)

if __name__ == "__main__":
    main()