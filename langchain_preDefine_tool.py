from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
api_wrapper = WikipediaAPIWrapper()
tool = WikipediaQueryRun(api_wrapper=api_wrapper)
print(tool.run({"query": "langchain"}))




from langchain_community.tools import YouTubeSearchTool
tool2=YouTubeSearchTool()
print(tool2.run("THERJROCK"))


from langchain_community.tools.tavily_search import TavilySearchResults
tool = TavilySearchResults()
print(tool.invoke({"query": "who is mohandas karamchand gandhi?"}))