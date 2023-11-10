import asyncio
from funcchain import achain, settings
from langchain.pydantic_v1 import BaseModel

settings.MODEL_TEMPERATURE = 1


class StartupConcept(BaseModel):
    name: str
    description: str
    

async def startup_generator(topic: str) -> StartupConcept:
    """
    Generate a random startup for the given topic.
    """
    return await achain()


async def generate_random_startups(topic: str, amount: int = 3) -> list[StartupConcept]:
    return await asyncio.gather(
        *[
            startup_generator(topic)
            for _ in range(amount)
        ]
    )

if __name__ == "__main__":
    topic = "AI generated Vegan Recipes"
    
    startups = asyncio.run(generate_random_startups(topic))

    for startup in startups:
        print("name:", startup.name)
        print("concept:", startup.description)
