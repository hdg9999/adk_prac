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
LangGraph로 작성된 그래프를 에이전트로 가져와서 사용가능.\
ADK에서는 LangGraphAgent라는 LangGraph로 작성된 워크플로우를 전체를 하나의 에이전트로 사용할 수 있는 래퍼 클래스가 제공됨. 
- 아직은 실험적인 기능이라고 적혀 있어서 실제 사용 전에 먼저 공식 문서의 업데이트 내역을 참고하는 것을 권장함.

```python
from typing_extensions import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from google.adk.agents.langgraph_agent import LangGraphAgent

# 예제 그래프 - 사용자 입력을 받아서 단순 문자열 출력하는 싱글 노드 그래프
# 1) LangGraph state 정의
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], lambda x, y: x + y]

# 2) LangGraph node 정의 - 사용자 인풋을 단순 echoing 하는 간단한 노드
def echo_node(state: AgentState):
    last = state["messages"][-1]
    if isinstance(last, HumanMessage):
        return {"messages": [AIMessage(content=f"{last.content}에 대한 처리를 시작합니다.")]}
    return {"messages": []}

# 3) 그래프 구성 + compile - echo노드 달랑 하나만 추가하고 종료 노드로 직행 
builder = StateGraph(AgentState)
builder.add_node("echo", echo_node)
builder.set_entry_point("echo")     # 그래프의 시작점 노드 지정
builder.add_edge("echo", END)

graph = builder.compile(checkpointer=MemorySaver())

# 4) LangGraph -> ADK Agent로 랩핑해서 root_agent로 공개
start_notice_agent = LangGraphAgent(
    name="my_langgraph_agent",
    graph=graph,
    instruction="You are a helpful assistant powered by LangGraph.",
)

from google.adk.agents import SequentialAgent

root_agent = SequentialAgent(
    name="랭그래프에이전트",
    description="사용자 인풋 한번 복명복창 한뒤 덕덕고 검색 가능한 gpt 에이전트에게 처리를 떠넘기는 에이전트",
    sub_agents=[start_notice_agent, llm_agent]    
)
```

