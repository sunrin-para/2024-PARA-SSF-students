import os
import openai
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Query

from service import path
from service.chatting import load_log, load_feature
from service.save import log_save

load_dotenv()  # .env 파일을 불러옵니다.

router = APIRouter(
    prefix="/chat",
    tags=["GPT"],
)

# AI와 대화하기 위한 필수 설정입니다.
openai.api_key = os.getenv("OPENAI_KEY")
model_name = os.getenv("MODEL_NAME")


# 채팅 내용을 AI에게 전송합니다.
async def api_request(prompt: str, max_tokens: int = 256):
    try:
        message = # 기존 대화 기록을 추가합니다. # 빈칸을 채워주세요.
        message = message + #특징을 불러옵니다. # #빈칸을 채워주세요.
        message.append({"role": "user", "content": prompt})

        new_chat = openai.chat.completions.create(
            model=model_name,# 사용할 인공지능 이름입니다.
            messages=,# 빈칸을 채워주세요.
            max_tokens=max_tokens,# 인공지능이 말할 수 있는 최대 길이입니다.
            temperature=0.8, # 인공지능의 창의성을 조절합니다.
        )
        response = new_chat.choices[0].# 나머지 부분을 완성해주세요
        message.append({"role": "assistant", "content": response})
        log_save(message, path.get_log_path())

        return response

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


# AI에게 대화 내용을 전송하고, 답변을 받아옵니다.
@router.get("/send")
async def chat(
        prompt: str = Query(None, title="Prompt")
):
    try:
        response = await api_request() # 빈칸을 채워주세요.
        return {"response": } # 빈칸을 채워주세요.

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
