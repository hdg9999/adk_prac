from google.adk.agents import SequentialAgent, Agent
from google.adk.tools import google_search

## Workflow Agent 클래스들은 LLM 없이 하위 에이전트 들을 특정 순서대로 호출만 해주는 클래스.
## SequentialAgent는 sub_agents 인자에 하위 에이전트 클래스들을 리스트로 던져주면 리스트 안에 에이전트들을 앞에서부터 순차적으로 호출함.

google_search_agent = Agent(
   name="구글검색에이전트",
   model='gemini-2.5-flash',
   description="구글 검색을 할 줄 아는 조사원",
   instruction="사용자 입력이 들어오면 구글 검색을 활용해 해당 주제와 관련된 시장 동향을 조사하세요.",
   tools=[google_search],
   output_key="search_result"                                                             # 다음 에이전트에게 결과값을 전달하기 위한 key값
)

summary_agent = Agent(
   name="요약에이전트",
   model='gemini-2.5-flash',
   description="조사 결과를 요약 정리하는 에이전트",
   instruction="다음은 조사원이 조사해온 시장 동향 정보입니다. 보고서 느낌으로 요약하세요. ##시장 동향 관련 자료\n{search_result}",
   tools=[],
   output_key="summary_result"  
)

marketer_agent = Agent(
   name="마케터에이전트",
   model='gemini-2.5-flash',
   description="요약된 자료를 바탕으로 마케팅 전략을 구상하는 에이전트",
   instruction="마케터에이전트가 가져온 보고서를 바탕으로 마케팅 전략을 제시하세요.\n ##보고서\n{summary_result}",
   tools=[]  
)

### 서브 에이전트들을 무조건 순차적으로 호출하여 작업을 처리하는 에이전트 클래스
root_agent = SequentialAgent(   
   name="마케팅팀장",                                                                             
   description="구글 검색을 활용하는 마케팅 연구 팀장. 검색, 요약, 전략 제시 단계 순으로 작업 수행.",  
   sub_agents=[google_search_agent,                               # 하위 에이전트들
               summary_agent, 
               marketer_agent
               ]
)