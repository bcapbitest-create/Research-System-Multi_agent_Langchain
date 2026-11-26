from langchain.tools import tool
import requests
from dotenv  import load_dotenv
import os
from tavily import TavilyClient
from rich import print
from bs4 import BeautifulSoup
from readability import Document 
import trafilatura
import re
#load your environment object
load_dotenv() 

# load the tavily object
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# create the web_search function and transform as a tool( use @tool decorator)

@tool
def web_search(query : str) -> str:
    """
    Searches the web for recent and reliables information on a topic.
    Returnes the title, the URL and the results of the search.
    """
    results = tavily.search(query=query, max_results = 5)

    
    out = []

    for r in results['results']:
        out.append(
            f"Title:{r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )

    return "\n----\n".join(out)

@tool
def web_scraper(url: str) -> str:
    """
    Scrapes the content of a webpage using its URL.

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        The webpage title and extracted text content.
    """

    try:
        # Validate URL
        if not url.startswith(("http://", "https://")):
            return "Error: Please provide a valid HTTP or HTTPS URL."

        # Send HTTP request
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        # Parse webpage
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract webpage title
        title = soup.title.get_text(strip=True) if soup.title else "No title found"

        # Remove unnecessary HTML elements
        for element in soup([
            "script",
            "style",
            "header",
            "footer",
            "nav",
            "noscript",
            "iframe"
        ]):
            element.decompose()

        # Extract readable text
        content = soup.get_text(separator=" ", strip=True)

        # Clean excessive whitespace
        content = " ".join(content.split())

        # Limit extracted content
        content = content[:12000]

        return f"""
        Webpage Title: {title}

        URL: {url}

        Extracted Content:
        {content}
        """

    except requests.exceptions.Timeout:
        return "Error: The webpage took too long to respond."

    except requests.exceptions.RequestException as e:
        return f"Error fetching webpage: {str(e)}"

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

