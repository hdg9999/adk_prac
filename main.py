### 현재 버그가 있어서 swagger가 안됨.
### 아래는 swagger를 사용하기 위한 몽키 패치. swagger 안써도 된다면 기존의 cli 명령어 쓰는데 문제는 없음.

from fastapi import FastAPI
from pydantic.json_schema import GenerateJsonSchema
from pydantic._internal._generate_schema import GenerateSchema
from pydantic_core import core_schema
from fastapi.responses import PlainTextResponse
from google.adk.cli.fast_api import get_fast_api_app

# Patch 1: Handle invalid JSON schema types
def _patched_handle_invalid(self, schema, error_info):
    return {'type': 'object', 'description': f'Unserializable type: {error_info}'}
GenerateJsonSchema.handle_invalid_for_json_schema = _patched_handle_invalid

# Patch 2: Handle unknown types during schema generation
def _patched_unknown_type_schema(self, obj):
    return core_schema.any_schema()
GenerateSchema._unknown_type_schema = _patched_unknown_type_schema

# Then import and run ADK



# 버그 픽스 되면 여기 이하부터만 사용하면 됨.

## 프로덕션 배포를 위한 api 문서 페이지 및 dev-ui 비활성화
def get_app(agents_dir:str, is_prod:bool) -> FastAPI:
    adk_app = get_fast_api_app(agents_dir=agents_dir, web=not is_prod)
    # 운영환경일 경우 swagger 등 api 문서 페이지 라우트 제거
    if is_prod: 
        blocked = {"/docs", "/redoc", "/openapi.json", "/docs/oauth2-redirect"}
        adk_app.router.routes = [
            r for r in adk_app.router.routes
            if getattr(r, "path", None) not in blocked
        ]
    return adk_app

app = get_app(agents_dir="./agents", is_prod=False)         # web=True인 경우 디버깅용 채팅화면이 오픈되고 '/' 요청시 채팅화면 '/dev-ui'로 리다이렉트 되도록 설정됨



