import asyncio
import pydantic
from baml_client.async_client import b
from baml_client.types import Response



async def loop():
    print("MuzzleGPT: What can I help you with?")
    while True:
        prompt = input(">")
        print("\n")
        first_word = await b.Genesis(request=prompt, limit=100)
        generated = first_word.word
        for i in range(50, 1, -1):
            next_word = await b.Output(request=prompt, limit=i, generated=generated)
            generated += " " + next_word.word 
        print(generated)
        print(len(generated.split(" ")))
if __name__ == "__main__":
    asyncio.run(loop())

