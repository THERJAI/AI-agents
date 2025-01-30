from langchain.agents import tool
import urllib.parse

@tool
def linkedin_search(query: str) -> str:
    """
    Search for profiles, companies, or topics on LinkedIn.
    
    Args:
        query (str): The search term to look for on LinkedIn.
    
    Returns:
        str: The LinkedIn search URL based on the input query.
    """
    base_url = "https://www.linkedin.com/search/results/all/?keywords="
    search_url = base_url + urllib.parse.quote(query)

    return f"Click here to search on LinkedIn: {search_url}"

# Example Usage
user=input("enter something to searrch")
result = linkedin_search.run(user)
print(result)
