"""
Author: Bisnu Ray
https://t.me/itsSmartDev
"""

import requests
import json
import re

# Function to load cookies from a file
def load_cookies(file_path):
    with open(file_path, 'r') as file:
        cookies_raw = json.load(file)
        if isinstance(cookies_raw, dict):
            return cookies_raw
        elif isinstance(cookies_raw, list):
            cookies = {}
            for cookie in cookies_raw:
                if 'name' in cookie and 'value' in cookie:
                    cookies[cookie['name']] = cookie['value']
            return cookies
        else:
            raise ValueError("Cookies are in an unsupported format.")

# Function to extract URL ID from the main Unsplash URL
def extract_url_id(url):
    return url[-11:]

# Unsplash downloader function
def get_unsplash_download_link(input_url):
    # Extract url_id from input_url
    url_id = extract_url_id(input_url)
    cookies_file = 'cookie.json'  # Ensure this is the correct path to your cookies file
    url = f'https://unsplash.com/photos/{url_id}/download?force=true'  # Correctly formatted URL
    cookies = load_cookies(cookies_file)
    
    # Send GET request with the loaded cookies
    response = requests.get(url, cookies=cookies, allow_redirects=False)
    
    # Check if the 'Location' header exists
    if 'Location' in response.headers:
        return response.headers['Location']
    else:
        return "Unable to retrieve the download link."

# Main function to run the script
def main():
    input_url = input("Please enter an Unsplash photo URL: ")
    try:
        download_link = get_unsplash_download_link(input_url)
        print(f"Download Link: {download_link}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
