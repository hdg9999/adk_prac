from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH

# A2A 원격 서버 호출하는 컨슈머 에이전트
# URL의 에이전트 카드의 정보를 읽어서 a2a 규격의 원격 에이전트를 호출함

root_agent = RemoteA2aAgent(
   name="remote_agent",
   description="Remote A2A agent",
   agent_card=f"http://localhost:8011/{AGENT_CARD_WELL_KNOWN_PATH}"  # 디폴트의 경우 AGENT_CARD_WELL_KNOWN_PATH 상수를 사용하면 편함
)