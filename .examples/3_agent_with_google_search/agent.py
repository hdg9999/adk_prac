from google.adk.agents import Agent, LlmAgent
from google.adk.tools import google_search # google.adk.tools에 adk에서 이미 만들어서 제공되는 tool들이 있음.

root_agent = Agent(   
   name="검색에이전트",                                           
   model='gemini-2.5-flash',                                      
   description="구글 검색을 활용하는 연구원",  
   instruction="사용자가 질문하면 객관적인 시각으로 사실만을 대답해주세요. 필요하면 구글 검색을 활용하세요.", 
   tools=[google_search]                   
)
