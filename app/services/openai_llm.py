import os
import logging
import asyncio
from langchain.schema import StrOutputParser  # Ensure this is the correct import

from langchain.chat_models import ChatOpenAI

from app.logger import setup_logger
from app.prompts.documentation_prompt import build_documentation_prompt
from app.prompts.test_prompt import build_test_prompt


logger = setup_logger(__name__, level=logging.DEBUG)

openai_api_key = os.getenv("OPENAI_API_KEY", None)


llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="deepseek/deepseek-chat:free",
    # model_name="meta-llama/llama-3.3-8b-instruct:free",
)


async def generate_docs_from_code(code: str, job_data: dict) -> tuple[str, str]:
    language = job_data["language"]
    doc_chat_prompt = build_documentation_prompt()
    test_chat_prompt = build_test_prompt()

    doc_chain = doc_chat_prompt | llm | StrOutputParser()
    test_chain = test_chat_prompt | llm | StrOutputParser()

    doc_response, test_response = await asyncio.gather(
        doc_chain.ainvoke({"code": code, "language": language}),
        test_chain.ainvoke({"code": code, "language": language}),
    )

    doc_response = (
        doc_response.content if hasattr(doc_response, "content") else str(doc_response)
    )

    test_response = (
        test_response.content
        if hasattr(test_response, "content")
        else str(test_response)
    )

    return doc_response, test_response
