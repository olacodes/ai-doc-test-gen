from langchain_core.prompts import ChatPromptTemplate


def build_test_prompt() -> ChatPromptTemplate:
    system_message = """
    You are a highly experienced Senior Backend Engineer renowned for your expertise in writing robust, maintainable, and idiomatic test suites. 
    Your role is to author unit and integration tests that exemplify industry best practices, ensuring confidence, stability, and long-term maintainability of software systems.
    """.strip()

    human_template = """
    Analyze the following source code and develop a comprehensive test suite encompassing both unit and integration tests:

    ```{language}
    {code}
    ```

    🧪 **Objective**:
    - Design test cases that thoroughly validate the intended behavior of the code.
    - Include edge cases, error scenarios, and interactions with external dependencies.
    - Apply mocking or test doubles where appropriate to isolate functionality and ensure test reliability.

    ---

    📋 **Output Requirements**:
    - Organize tests into logical groups or test classes/modules.
    - Use clear, behavior-driven naming conventions for test functions and methods.
    - Mock or stub I/O, external services, databases, and other side effects.
    - Cover both success paths ("happy paths") and failure modes ("unhappy paths").

    ---

    ✅ **Best Practice Guidelines**:
    - Follow idiomatic patterns and conventions for the target language and framework (e.g., `pytest` for Python, `JUnit` for Java).
    - Assume standard fixtures, mocks, or dependency injection setups (e.g., `conftest.py` for Pytest).
    - Prioritize testing observable behavior over implementation details.
    - Ensure tests are deterministic, fast, and easy to maintain.
    - Consider separation of concerns: test logic independently of orchestration.

    Approach this task with the same precision and care you would bring to production-quality code. Your ability to craft thoughtful, effective, and maintainable tests reflects your commitment to engineering excellence and long-term software quality.
    """.strip()

    return ChatPromptTemplate.from_messages(
        [("system", system_message), ("human", human_template)]
    )
