import asyncio
from typing import Union
from baml_client.async_client import b
from baml_client.types import Punctuate, SentenceResponse

async def looper():
    print("MuzzleGPT")
    print("What do you want to know today?")
    while True:
        prompt: str = input("> ")
        limit: int = 100
        first_sentence: SentenceResponse = await b. GenFirstSentence(request=prompt, limit=limit)
        generated: str = first_sentence.sentence
        limit -= word_count(generated)
        while limit > 0:
            next_sentence: Union[SentenceResponse, Punctuate] = await b.GenNextSentence(request=prompt, limit=limit, generated=generated)
            if hasattr(next_sentence, "sentence"):
                generated += " " + next_sentence.sentence
                limit -= word_count(next_sentence.sentence)
            else:
                break
        print(generated)
        print(f"The total word count of the message is: {word_count(generated)}")
    
def word_count(string: str) -> int:
    return len(string.split(" "))


if __name__ == "__main__":
    asyncio.run(looper())

