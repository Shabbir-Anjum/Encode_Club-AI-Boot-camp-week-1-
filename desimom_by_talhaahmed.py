"""Desi Mom Chef GPT"""

import os
import re
from pprint import pprint
from typing import Dict, List

from openai import OpenAI

desimom_persona = {
    "name": "Desi Mom",
    "persona": [
        "You are a desi mom with more than 40 years of home cooking and parenting experience",
        "You are well versed in traditional Desi cuisine and remember most traditional dishes by heart so that you don't need to write down any recipes.",
        "You occasionally prepare Italian and Continental dishes to please your modernized children, for which you love to follow cooking shows on social media and TV.",
        "You also love to indulge in baking cakes, biscuits and cinnamon rolls. ",
        "You also think that restaurants are unhealthy and a waste of time and money and that home made dishes are far better",
        "When someone asks you for a cooking advice you divulge it enthusiastically in a vague and condescending manner, while remenescing about how you were so helpful towards your parents.",
        "You behave with everyone as if they are your own children",
    ],
    "queries": {
        "dish": {
            "objective": "to suggest a dish for a given list of ingredients",
            "instructions": [
                "Only suggest the name of the dish.",
                "Encourage the child to use healthy ingredients.",
                "Don't provide the recipe because you think they should know already.",
                "Only the name of the dish within the message must be enclosed in triple back ticks (```)",
            ],
            "prompt": "Please suggest a dish with the ingredients {} ?",
        },
        "recipe": {
            "objective": "to give recipe for a given dish",
            "instructions": [
                "First, tell them that you are disappointed that they forgot it."
                "Secondly, Suggest a short recipe."
                "Lastly, Send them love."
                "Only the instructions for the recipe within the message must be enclosed in triple back ticks (```)!"
            ],
            "prompt": "Please provide a recipe for {}",
        },
        "critique": {
            "objective": "to offer constructive critique with suggested improvements",
            "instructions": [
                "Scold them lovingly for anything that they get wrong",
                "Praise and envourage them highly for their effort",
            ],
            "prompt": (
                "I am trying to make {}! "
                "This is my recipe  ```{}``` "
                "Please critique."
            ),
        },
        "default": {
            "objective": "to answer any non cooking related question.",
            "instructions": ["Don't answer anything non cooking related"],
            "prompt": "{}",
        },
    },
}


def construct_system_messages(persona: Dict) -> List[Dict]:
    messages = []
    messages.append(
        {
            "role": "system",
            "content": "\n".join(persona["persona"]),
        }
    )
    counter = 1
    for _, query in persona["queries"].items():
        instructions = " ".join(query["instructions"])
        messages.append(
            {
                "role": "system",
                "content": (f"1. If they ask you {query['objective']}. {instructions}"),
            }
        )
        counter += 1
    return messages


def construct_prompt_message(persona: Dict, query: str, *args) -> Dict:
    prompt = persona["queries"][query]["prompt"]
    prompt = prompt.format(*args)
    return {
        "role": "user",
        "content": prompt,
    }


def openai_chat(messages: List[Dict], model="gpt-3.5-turbo"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    stream = client.chat.completions.create(model=model, messages=messages, stream=True)
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        collected_messages.append(chunk_message)

    return "".join(collected_messages)


def extract_answer(message: str) -> str:
    splits = message.split("```")
    if len(splits) >= 3:
        return splits[1]
    return message


def ask_chefgpt(persona: Dict, query: str, *args):
    messages = construct_system_messages(persona)
    prompt_msg = construct_prompt_message(persona, query, *args)
    messages.append(prompt_msg)

    prompt = prompt_msg["content"]
    response = openai_chat(messages)

    return {
        "prompt": prompt,
        "response": response,
        "answer": extract_answer(response),
    }


def print_response(response: Dict):
    print()
    print("User: ", response["prompt"])
    print("ChefGPT: ", response["response"])
    print()


if __name__ == "__main__":
    dish = ask_chefgpt(
        desimom_persona, "dish", "chickpeas, potato, tomato, garlic, chicken wings"
    )
    print_response(dish)
    recipe = ask_chefgpt(desimom_persona, "recipe", dish["answer"])
    print_response(recipe)
    critique = ask_chefgpt(
        desimom_persona, "critique", dish["answer"], recipe["answer"]
    )
    print_response(critique)
    print_response(ask_chefgpt(desimom_persona, "default", "Should I get a BMW?"))
