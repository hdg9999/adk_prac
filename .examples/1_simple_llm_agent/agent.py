from google.adk.agents import Agent, LlmAgent

# 공통 
# - 진입점 역할을 하는 agent파일은 __init__.py와 같은 위치에 존재해야함.
# - 진입점 역할을 하는 agent파일에는 "root_agent"라는 변수명으로 에이전트 클래스를 생성해야함(변수명 정확하게 맞춰야 함). 
# 이 클래스가 input을 받아들이고 최종 response를 뱉어내는 핵심 역할임.


# 구글 제미나이 API를 사용하는 경우 가장 기본 Agent 클래스 혹은 LlmAgent 클래스를 사용하면 됨.


root_agent = Agent(   
   name="basic_agent",                                            # 에이전트 이름 (내부 시스템 프롬프트에 영향을 줌. 공백 사용 불가.)      
   model='gemini-2.5-flash',                                      # 모델명 - https://google.github.io/adk-docs/get-started/streaming/quickstart-streaming/#supported-models 여기 참고.
   description="Agent to answer questions using Google Search.",  # 에이전트 역할 설명
   instruction="You are a helpful assistant.",                    # 시스템 프롬프트
)

root_agent = LlmAgent(
   name="basic_llm_agent",
   model='gemini-2.5-flash',
   description="Agent to answer questions using Google Search.",
   instruction="You are a helpful assistant."
)