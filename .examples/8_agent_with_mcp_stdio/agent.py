from google.adk.agents import Agent
from google.adk.models.gemma_llm import Gemma3Ollama
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import google_search  # Import the tool
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams, SseConnectionParams, StreamableHTTPConnectionParams
from mcp import StdioServerParameters

# 로컬 mcp서버
toolset = McpToolset(
         connection_params=StdioConnectionParams(
            server_params = StdioServerParameters(
               command = r"path\to\python.exe",
               args=[r"path\to\your_sample_mcp_server.py"]
               )
            ) 
         )

# sse mcp서버
sse_toolset = McpToolset(
   connection_params=SseConnectionParams(
      url=r"<<your-url>>"
      # 나머지 params.. Bearer 토큰 인증같은거 필요하면 headers 설정 등
   )
)

# http mcp 서버
streamable_http_toolset = McpToolset(
   connection_params=StreamableHTTPConnectionParams(
      url=r"<<your-url>>"
      # 나머지 params..
   )
)


root_agent = Agent(
   name="gpt5_agent",
   model=LiteLlm("openai/gpt-5-mini-2025-08-07"),
   description="gpt5 에이전트.",
   instruction="당신은 유용한 어시스턴트입니다. 간단한 덧셈 기능을 할 수 있습니다.",
   tools=[toolset]                                                              # toolset 하나를 tool 한개인 것처럼 인자로 넘기면 에이전트는 해당 mcp서버에서 제공하는 모든 tool에 접근 가능하다.
)