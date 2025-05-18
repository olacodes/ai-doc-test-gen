from langchain_core.prompts import ChatPromptTemplate


def build_documentation_prompt() -> ChatPromptTemplate:
    system_message = """
    You are a distinguished Software Architect and Senior Technical Writer, celebrated for producing industry-grade documentation that is precise, comprehensive, and elegantly structured.
    Your work consistently demonstrates a deep understanding of system design, engineering best practices, and effective communication for technical and non-technical stakeholders.
    """.strip()

    human_template = """
    Carefully review and analyze the following code. Your task is to produce high-quality technical documentation that reflects best practices in software architecture and technical writing.

    ```{language}
    {code}
    ```

    The documentation must include the following sections:

    1. **Project Overview** – A concise yet thorough description of the project's purpose, goals, and context.
    2. **Architecture Diagram (Mermaid Syntax)** – Illustrate the system's architecture using appropriate Mermaid diagrams (e.g., sequence, component, or flow diagrams).
    3. **Core Components** – Describe the major modules, classes, or services, detailing their responsibilities and how they interact.
    4. **API Specifications** – Clearly document any exposed endpoints, including HTTP methods, request/response formats, authentication, and relevant headers or query parameters.
    5. **Error Handling** – Explain the strategy for managing errors, including known exceptions, fallback mechanisms, and any custom error models.
    6. **Deployment Guide** – Provide step-by-step instructions for building, configuring, and deploying the application, including any environment variables or infrastructure dependencies.

    **Documentation Guidelines**:
    - Adhere to standard Markdown formatting conventions.
    - Provide illustrative code snippets and examples where relevant.
    - Maintain a consistent level of technical depth and clarity across all sections.
    - Emphasize key architectural decisions and trade-offs where applicable.

    Approach this task with the highest standards of craftsmanship. Deliver work that reflects excellence, clarity, and a strong sense of ownership. Your attention to detail and pride in execution are what set you apart.
    """.strip()

    return ChatPromptTemplate.from_messages(
        [("system", system_message), ("human", human_template)]
    )
