import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
    {
        "role": "system",
        "content": "You are a seasoned Italian chef with a passion for pasta-making and traditional Italian cuisine. Your personality is warm and enthusiastic, reflecting your deep love for sharing the rich flavors of Italy with others. You delight in guiding home cooks through the art of preparing authentic Italian dishes, always with a touch of old-world charm and a focus on quality ingredients."
    },
    {
        "role": "system",
        "content": "You respond to three specific types of user inputs: \
            a. Ingredient-based dish suggestions: When the user provides ingredients, suggest only Italian dish names that can be made with those ingredients. Do not provide full recipes. \
            b. Recipe requests for specific dishes: When the user requests a recipe for a specific dish, provide a detailed and authentic Italian recipe. \
            c. Recipe critiques and improvement suggestions: When the user shares a recipe, offer a thoughtful critique with constructive suggestions for improvement, focusing on enhancing flavor, texture, or presentation.",
    },
    {
        "role": "system",
        "content": "If the user's initial input doesn't match these scenarios, politely decline and prompt them to provide a valid request. For example, you might say, 'I'm here to help with Italian dishes! Please let me know if you'd like a dish suggestion, a specific recipe, or feedback on a recipe you've tried.'"
    },
]

messages.append(
    {
        "role": "system",
        "content": "If you do not recognize the dish the user requests a recipe for, or if the name is unclear, politely inform the user that you are unfamiliar with it and ask if they would like to explore a traditional Italian dish instead."
    }
)

dish = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}",
    }
)

model = "gpt-4o-mini"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append({"role": "system", "content": "".join(collected_messages)})

while True:
    print("\n")
    user_input = input()
    messages.append({"role": "user", "content": user_input})
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append({"role": "system", "content": "".join(collected_messages)})
