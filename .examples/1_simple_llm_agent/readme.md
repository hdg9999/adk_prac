# 기초 
- 진입점 역할을 하는 agent파일은 `__init__.py`와 같은 위치에 존재해야함.
- 진입점 역할을 하는 agent파일에는 "root_agent"라는 변수명으로 에이전트 클래스를 생성해야함(변수명 정확하게 맞춰야 함). \
root_agent가 input을 받아들이고 최종 response를 뱉어내는 핵심 역할임.


### 구글 제미나이 API를 사용하는 경우 가장 기본 Agent 클래스 혹은 LlmAgent 클래스를 사용.

```python
from google.adk.agents import Agent, LlmAgent

root_agent = Agent(   
   name="basic_search_agent",                                     # 에이전트 이름      
   model='gemini-2.5-flash',                                      # 모델명 - https://google.github.io/adk-docs/get-started/streaming/quickstart-streaming/#supported-models 여기 참고.
   description="helpful assistant",  # 에이전트 역할 설명
   instruction="You are a helpful assistant.",                    # 시스템 프롬프트
)
```

## 주의
adk에서 Gemini 사용시 API키 다음 KEY값을 환경변수로 등록해야함.
- GOOGLE_GENAI_USE_VERTEXAI : LLM을 Vertex AI 쪽 서비스를 사용한다면 1, 일반 구글 AI 스튜디오 쪽 API 사용한다면 0.
- GOOGLE_API_KEY : 제미나이 API 키