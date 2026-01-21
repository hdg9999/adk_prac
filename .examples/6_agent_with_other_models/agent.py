from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

# lite llm 래퍼 클래스가 제공됨. lite llm은 여러가지 다양한 플랫폼의 모델을 갈아끼기 쉽게 해주는 플랫폼 프레임워크임.
# 기본적으로 model에 제미나이 모델명이 아닌 LiteLlm 클래스 변수를 넘기면 됨.
# 모델 서비스 제공자 별로 알맞는 이름으로 환경변수 등록해야함.
# 타모델의 경우 adk에서 제공하는 tool은 사용이 대체로 사용이 안되니 참고.
# 앤스로픽 모델의 경우 별도 클래스가 제공되므로 클로드를 쓴다면 해당 클래스를 사용하는것도 고려.

def add(num1:int, num2:int) -> int:
    """숫자 두 개 덧셈"""
    return num1 + num2

# OpenAI모델
root_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-5-mini-2025-08-07"), # LiteLLM model string format
    name="openai_agent",
    instruction="You are a helpful assistant powered by GPT-5-mini. You are provided with google_search tool.",
    tools=[add]
    # ... other agent parameters
)


# 앤스로픽 클로드 계열
agent_claude_direct = LlmAgent(
    model=LiteLlm(model="anthropic/claude-3-haiku-20240307"),
    name="claude_direct_agent",
    instruction="You are an assistant powered by Claude Haiku.",
    # ... other agent parameters
)