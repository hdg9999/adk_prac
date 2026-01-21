# 랭체인 연동
## 1. Tool로써 연동
LangchainTool 이라는 래퍼 클래스 제공됨. Langchain에 내장된 tool 클래스나 아니면 Langchain 규격으로 작성된 커스텀 툴(langchain.tools.base.BasTool클래스 상속)의 경우 이걸로 감싸서 사용 가능.

### 예제
GPT와 덕덕고 검색을 연동하기

```python
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.langchain_tool import LangchainTool
from langchain.tools.ddg_search import DuckDuckGoSearchRun
from langchain.tools.base import BaseTool

# LangchainTool 이라는 래퍼 클래스 제공됨. Langchain에 내장된 tool 클래스나 아니면 Langchain 규격으로 작성된 커스텀 툴(langchain.tools.base.BasTool클래스 상속)의 경우 이걸로 감싸서 사용 가능
root_agent = LlmAgent(
    model=LiteLlm(model="openai/gpt-5-mini-2025-08-07"), # LiteLLM model string format
    name="openai_agent",
    instruction="You are a helpful assistant powered by GPT-5-mini. You are provided with search tool.",
    tools=[LangchainTool(DuckDuckGoSearchRun())]
    # ... other agent parameters
)
```

## 2. 랭그래프 워크플로우 연동
LangGraph로 작성된 그래프를 에이전트로 가져와서 사용가능.

```python
```

