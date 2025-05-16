from app.logger import setup_logger
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
import logging
from app.prompts.documentation import documentation_prompt


logger = setup_logger(__name__, level=logging.DEBUG)

openai_api_key = os.getenv("OPENAI_API_KEY", None)


llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="deepseek/deepseek-chat:free",
    # model_name="meta-llama/llama-3.3-8b-instruct:free",
)


async def generate_docs_from_code(code: str, job_data: dict) -> tuple[str, str]:
    documentation_prompt = documentation_prompt(code, job_data)
    prompt = ChatPromptTemplate.from_template(
        """
        You're a senior software engineer.

        Given this {language} code:
        ```{code}```

        1. Write clean documentation in Markdown format.
        2. Then write corresponding unit tests (using mocks if needed).
        
        Return:
        ---
        [DOCUMENTATION]
        ...
        [TESTS]
        ...
        """
    )
    chain = prompt | llm
    response = await chain.ainvoke({"code": code, "language": job_data["language"]})

    response = response.content if hasattr(response, "content") else str(response)

    logger.info(f"=========Response ========={response}")

    # Extract sections
    doc_part = response.split("[DOCUMENTATION]")[-1].split("[TESTS]")[0].strip()
    test_part = response.split("[TESTS]")[-1].strip()

    logger.info(f"=========Doc Part ========={doc_part}")
    logger.info(f"=========Test Part ========={test_part}")
    return doc_part, test_part
