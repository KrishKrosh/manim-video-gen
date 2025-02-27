import dotenv
dotenv.load_dotenv()
import os

llm_client_choice = os.getenv("LLM_CLIENT")


if llm_client_choice == "groq":
    from groq import AsyncGroq
    client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

elif llm_client_choice == "anthropic":
    from anthropic import AsyncAnthropic
    class AsyncAnthropicClient:
        def __init__(self, api_key: str):
            self.chat = AsyncAnthropic(api_key=api_key)
    client = AsyncAnthropicClient(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
    )

elif llm_client_choice == "gemini":
    
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=os.getenv("GEMINI_API_KEY"),
                             base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
    
elif llm_client_choice == "openai":
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

else:
    print("No LLM client chosen, using DeepSeek")
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com/v1")
