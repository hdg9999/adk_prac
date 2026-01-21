# 커스텀 에이전트

ADK에서 제공하는 기본 워크플로우 클래스는 Sequential, Loop, Parallel밖에 없음.
복잡한 조건부 분기 처리 로직 등이 필요하거나, LLM 추론에 의한 tool calling이 아니라 프로세스 상 무조건 실행해야하는 커스텀 코드 등이 필요한 경우에는 커스텀 에이전트 클래스를 직접 생성할 수 있다.

## 기본 구현 방법
BaseAgent클래스를 상속받은 커스텀 클래스를 생성하고,
_run_async_impl 함수를 구현하면 된다.
(아래는 임의의 llm 에이전트를 따로 하나 받아서 내부에서 실행하는 에이전트 예제)
```python
import logging
from typing import overload, override, AsyncGenerator
from google.adk.agents import BaseAgent, LlmAgent, Agent
from google.adk.tools import google_search 
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
# from pydantic import Field


class CustomAgent(BaseAgent): 
   ## 클래스 생성시 내부적으로 Pydantic을 사용해서 검증하므로 인스턴스 변수에 대한 타입 힌트 명확히 작성 필수
   your_agent: LlmAgent
   
   # 인스턴스 변수에 str, int가 아닌데 Pydantic 모델도 아닌 변수 사용하는 경우 이 값을 작성해주어야 함
   model_config = {"arbitrary_types_allowed":True}    
   
   def __init__(self, your_agent:LlmAgent, **kwargs):
      super().__init__(**kwargs, your_agent=your_agent)     # 인스턴스 변수로 생성할 값을 부모 생성자호출 할때도 넘겨줘야 pydantic 오류 안남
      self.sub_agents = [your_agent]                        # 명시적으로 하위 에이전트의 동작을 확인하려면 sub_agents 라는 속성으로 리스트 넘기면 됨. - adk web에서 하위 에이전트 호출하는지 확인 할 수 있음.
      self.your_agent = your_agent                          # 본인에 커스텀 로직에 필요한건 별도 인스턴스 변수로 등록

   # 이 함수를 커스터마이징해서 실제 실행 로직 커스터마이징 하면 됨.
   @override
   async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
      logger = logging.getLogger('custom_agent')
      logger.info(f"[{self.name}] Running Your agent...")
      # 특정 하위 에이전트를 호출해서 작업을 시킬 때는 <에이전트 객체>.run_async(ctx) 함수를 async for 구문으로 호출하고 , yield event를 해야한다.
      async for event in self.your_agent.run_async(ctx):                                                                      
         logger.info(f"[{self.name}] Event from Your Agent: {event.model_dump_json(indent=2, exclude_none=True)}")
         yield event

sub_agent = Agent(
   name="효과음에이전트",
   model='gemini-3-flash-preview',
   description="찰싹찰싹 소리내는 에이전트",
)

root_agent = CustomAgent(
   name="프론트에이전트",
   description="지정된 서브 에이전트 대행",
   your_agent=sub_agent
)
```