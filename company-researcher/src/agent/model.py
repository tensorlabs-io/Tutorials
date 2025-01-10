from langchain_openai import AzureChatOpenAI
from langchain_core.rate_limiters import InMemoryRateLimiter
from agent.config import settings 
# LLMs

rate_limiter = InMemoryRateLimiter(
    requests_per_second=4,
    check_every_n_seconds=0.1,
    max_bucket_size=10,  # Controls the maximum burst size.
)

chat_gpt_model = AzureChatOpenAI(
                model_name=settings.AZURE_MODEL_NAME_4O_MINI,
                openai_api_key=settings.AZURE_OPENAI_API_KEY_4O_MINI,
                azure_endpoint=settings.AZURE_OPENAI_ENDPOINT_4O_MINI,
                deployment_name=settings.AZURE_ENGINE_4O_MINI,
                api_version=settings.AZURE_OPENAI_API_VERSION_4O_MINI,
                temperature=0,
                rate_limiter=rate_limiter
            )