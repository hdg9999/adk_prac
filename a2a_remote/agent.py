import os
from google.adk.agents import Agent, LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a

os.environ.setdefault("GOOGLE_API_KEY", "AIzaSyBEexEwzOe0RHzYaCrY1QroiBYC4o9g-7I")

# A2A 프로토콜을 준수하는 에이전트 서빙
# root_agent를 to_a2a함수의 인자로 담으면 끝.

root_agent = LlmAgent(
   name="basic_llm_agent",
   model='gemini-2.5-flash',
   description="Gemini agent",
   instruction="You are a helpful assistant."
)

a2a_app = to_a2a(root_agent, port=8001)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(a2a_app, port=8001)

