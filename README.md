Google ADK 스터디용 자료

## Quick Setting
이 git 소스를 내려받고(git clone 하거나 다운로드)\
```uv sync``` \
이거 한번에 세팅 끝.


## Adk 기본 명령어
1) 디버깅용 채팅 화면(dev-ui)가 포함된 api 서버 실행\
`adk web <폴더경로>`
2) 디버깅 화면 빼고 순수 api서버로만 실행\
`adk api_server`

## 커스텀 실행
별도의 실행용 파이썬 파일을 작성. 실행용 파일 내 코드는 대략적으로 다음 흐름으로 작성하면 된다.
1) `get_fast_api_app` 함수를 임포트하여 ADK에서 만들어주는 FastAPI 앱 객체를 생성
2) Uvicorn이나 Gunicorn 실행 방법에 따라 해당 객체를 바라보게 명령어 지정하여 실행\
ex) 프로젝트 루트 경로에 main.py를 만들고 `app`이라는 변수명으로 FastAPI 객체를 생성 하여 uvicorn으로 실행하는 경우\
```uvicorn main:app <<uvicorn 실행 옵션 ... >>```\
내부 코드 샘플은 main.py 참고.\

## API 레퍼런스 페이지
FastAPI 앱 형태로 실행되므로 FastAPI에서 자동으로 만들어주는 API 문서 페이지(Swagger, ReDoc)도 당연히 사용 가능함. ->  `/docs`,`/redoc`

그런데 현재 버그가 있어서 `adk web`같이 adk 기본 명령어로 서버를 실행하는 경우 오류페이지가 나옴.

버그 픽스된 버전이 출시 전까지 꼭 스웨거 등이 꼭 필요한 경우에는 `main.py` 같은 실행파일에 `get_fast_api_app` 함수 호출 전 다음 몽키패치 코드를 추가하여 커스텀 실행 방법을 사용해야 함.
```python
from fastapi import FastAPI
from pydantic.json_schema import GenerateJsonSchema
from pydantic._internal._generate_schema import GenerateSchema
from pydantic_core import core_schema

# Patch 1: Handle invalid JSON schema types
def _patched_handle_invalid(self, schema, error_info):
    return {'type': 'object', 'description': f'Unserializable type: {error_info}'}
GenerateJsonSchema.handle_invalid_for_json_schema = _patched_handle_invalid

# Patch 2: Handle unknown types during schema generation
def _patched_unknown_type_schema(self, obj):
    return core_schema.any_schema()
GenerateSchema._unknown_type_schema = _patched_unknown_type_schema
```