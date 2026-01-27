from google.adk.agents import Agent, LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a


# A2A 프로토콜을 준수하는 에이전트 서빙
# root_agent를 to_a2a함수의 인자로 담으면 끝.

root_agent = LlmAgent(
   name="basic_llm_agent",
   model='gemini-2.5-flash',
   description="Gemini agent",
   instruction="You are a helpful assistant."
)

a2a_app = to_a2a(root_agent, port=8011)


# 직접 A2A 에이전트 카드 작성하는 경우 아래 참고.
# from google.adk.a2a.utils.agent_to_a2a import to_a2a
# from a2a.types import AgentCard

# my_agent_card = AgentCard(
#     "name": "file_agent",
#     "url": "http://example.com",
#     "description": "Test agent from file",
#     "version": "1.0.0",
#     "capabilities": {},
#     "skills": [],
#     "defaultInputModes": ["text/plain"],
#     "defaultOutputModes": ["text/plain"],
#     "supportsAuthenticatedExtendedCard": False,
# )
# a2a_app = to_a2a(root_agent, port=8001, agent_card=my_agent_card)