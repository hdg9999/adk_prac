## * 주의
아직 A2A 관련 기능은 실험적 기능이므로 버그가 있거나 업데이트 이후 대폭 수정될 가능성이 있어 프로덕션 환경에서 사용은 권장하지 않음.

## A2A 프로토콜을 준수하는 에이전트 서빙
root_agent를 to_a2a 함수로 감싸기만 하면 알아서 A2A 프로토콜을 준수하는 에이전트 서빙이 됨.

```python
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
```

#### 직접 A2A 에이전트 카드 작성하는 경우
```python
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from a2a.types import AgentCard

## 1) AgentCard 클래스를 사용하여 수동 작성
my_agent_card = AgentCard(
    "name": "file_agent",
    "url": "http://example.com",
    "description": "Test agent from file",
    "version": "1.0.0",
    "capabilities": {},
    "skills": [],
    "defaultInputModes": ["text/plain"],
    "defaultOutputModes": ["text/plain"],
    "supportsAuthenticatedExtendedCard": False,
)
# to_a2a 함수의 agent_card 인자에 AgentCard 객체를 직접 전달하면 자동 생성 대신 사용자 지정 에이전트 카드가 적용됨.
a2a_app = to_a2a(root_agent, port=8001, agent_card=my_agent_card)

## 2) json 파일로 에이전트 카드 작성
## json 파일 경로만 던지면 됨
a2a_app = to_a2a(root_agent, port=8001, agent_card="/path/to/your_agent_card.json")

```

## A2A 에이전트 서버 실행
to_a2a함수로 생성한 app 객체를 uvicorn으로 실행하면 됨.\
cli : `uvicorn agent:a2a_app --port 8001`\
python : 
```python
uvicorn.run(a2a_app, port=8001)
```


## A2A 에이전트 호출
a2a 원격 에이전트가 실행되어 있는 상태에서 RemoteA2aAgent 클래스를 사용하여 아래와 같이 사용할 수 있음.
```python
from google.adk.agents import RemoteA2aAgent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH

# A2A 원격 서버 호출하는 컨슈머 에이전트
# URL의 에이전트 카드의 정보를 읽어서 a2a 규격의 원격 에이전트를 호출할 때 참고하므로 agent_card url을 정확히 넘겨야 한다.

root_agent = RemoteA2aAgent(
   name="remote_agent",
   description="Remote A2A agent",
   agent_card=f"http://localhost:8001/{AGENT_CARD_WELL_KNOWN_PATH}"
)
```
* 디폴트의 경우 AGENT_CARD_WELL_KNOWN_PATH 상수를 사용하면 편함
* 실행 위치에 따라 host와 well_known_path 사이에 추가 path가 필요할 수 있음.\
-> `http://localhost:8001/<<parent_folder>>/<<your_agent_folder>>/{AGENT_CARD_WELL_KNOWN_PATH}`