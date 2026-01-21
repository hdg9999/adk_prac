# 타 모델 연동
타 모델 연동은 lite_llm 래퍼 클래스가 제공됨. 이를 사용하는 것이 가장 간편. \
lite llm은 여러가지 다양한 모델 서비스 제공자의 모델들을 갈아끼기 쉽게 해주는 프레임워크/라이브러리. \
모델 제공자 별로 해당하는 API 키 값은 환경변수로 등록해야함 (OpenAI의 경우 OPENAI_API_KEY) \
LlmAgent 클래스에서 모델 인자값을 제미나이 모델명 string이 아니라 LiteLlm 클래스로 넘기면 간편하게 연동된다.
참고 링크 : https://docs.litellm.ai/docs/#litellm-python-sdk


## 예제

```python
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import google_search

# tool calling이 지원되는 모델이라면 이런 파이썬 함수로 만든 커스텀 tool도 잘 호출한다.
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
```
