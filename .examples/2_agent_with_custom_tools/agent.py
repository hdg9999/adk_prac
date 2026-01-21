from google.adk.agents import Agent, LlmAgent

# 파이썬 함수를 에이전트의 tool로 등록할 수 있음
# 도구 사용을 해야하는지 추론할 때, 타입 힌트와 함수 주석(def 바로 밑에 문자열 """""")을 에이전트가 참고함.
# 타입 힌트와 주석을 자세히 적을 수록 LLM이 도구 추론을 정확하게 함
def add(num_1:int, num_2:int) -> int:
   """덧셈 수행"""
   return num_1 + num_2


root_agent = Agent(   
   name="덧셈에이전트",                                           
   model='gemini-2.5-flash',                                      
   description="숫자 두 개 더해주는 계산기 에이전트",  
   instruction="사용자가 덧셈 물어보면 계산해주는 에이전트", 
   tools=[add]                   
)
