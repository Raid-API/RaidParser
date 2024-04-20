import requests
import re
from bs4 import BeautifulSoup
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def parse_website_view(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the URL from the POST request form
        url = request.POST.get('url')

        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check the success of the request
        if response.status_code == 200:
            # Create a BeautifulSoup object to parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the title tag and extract the title text
            title = soup.title.text.strip()

            # Assume the price is in a tag with class "price"
            # Extract the price text
            price_tags = soup.find(class_=re.compile(r'\bprice\b.{0,11}\b'))

            prices = []
            for tag in price_tags:
                text = tag.get_text(strip=True)
                print(text)
                clean_text = re.sub(r'\s+', ' ', text)
                prices.append(clean_text)

            # Pass the title and price to the template for rendering
            return render(request, 'result.html', {'title': title, 'prices': prices})
        else:
            # If the request fails, display an error message
            error_message = f"Error retrieving the page: {response.status_code}"
            return render(request, 'error.html', {'error_message': error_message})
    else:
        # If the request is not POST, return an empty form
        return render(request, 'form.html')

