# mcp 연동
google.adk.tools.mcp_tool 에 McpToolset 클래스가 제공됨. 이 클래스 인스턴스를 tools 인자로 넘겨주면 됨.
mcp 서버 유형에 따라 connection_params를 다르게 가져가야 하는데, 
로컬 mcp 서버인 경우 StdioConnectionParams 클래스로 커넥션 설정하면 됨.
원격 mcp 서버인 경우 통신 방식에 따라 SseConnectionParams과 StreamableHTTPConnectionParams를 사용하면 된다.

### 예제

```python
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
   )
)

# http mcp 서버
streamable_http_toolset = McpToolset(
   connection_params=StreamableHTTPConnectionParams(
      url=r"<<your-url>>"
   )
)


root_agent = Agent(
   name="gpt5_agent",
   model=LiteLlm("openai/gpt-5-mini-2025-08-07"),
   description="gpt5 에이전트.",
   instruction="당신은 유용한 어시스턴트입니다. 간단한 덧셈 기능을 할 수 있습니다.",
   tools=[toolset]                                                              # toolset 하나를 tool 한개인 것처럼 인자로 넘기면 에이전트는 해당 mcp서버에서 제공하는 모든 tool에 접근 가능하다.
)
```

