# AI and GPT Bootcamp - Week 1 Homework

## Introduction
In this repository, you will find the code and documentation for the homework assigned in Week 1 of the Encode Club AI and GPT Bootcamp Q3 2024. The main objective of this assignment is to utilize the OpenAI API to create a simulated cooking assistant.

The author of this project, **Shabbir Anjum**, is a proud participant of **Group 6**.

### Exercise Statement
The exercise statement can be found in the Weekend Project section at the end of Lesson 4. You can refer to the detailed instructions [here](https://github.com/Encode-Club-AI-Bootcamp/Generative-AI-Applications/blob/main/Lesson-04/exercises/07-Chef-GPT.md).

The base code for this project is located in the `ChefGPT.py` file.

---

## Project Overview

### ChefGPT - Your Friendly Pakistani Cooking Assistant

ChefGPT is a Python script that simulates an interactive cooking assistant, **Chef Shabbir**, who specializes in traditional Pakistani cuisine. Users can ask for dish suggestions based on ingredients, request detailed recipes, or seek feedback on dishes they've already cooked. Chef Shabbir responds with helpful advice, recipes, and constructive feedback.

---

## How It Works

The ChefGPT project utilizes OpenAI's API to create an interactive assistant. The assistant is trained to respond based on the following scenarios:

1. **Ingredient-Based Queries:** The assistant suggests dishes based on the ingredients provided by the user, without giving full recipes.
2. **Recipe Requests:** Users can ask for a detailed recipe, and the assistant provides step-by-step instructions along with ingredients.
3. **Recipe Critiques:** The assistant offers constructive feedback on a user's attempt at a recipe, suggesting improvements while maintaining a respectful and friendly tone.

### Detailed Workflow:
1. **User Input:** The user enters a query regarding Pakistani cuisine, such as asking for a recipe, suggesting a dish based on ingredients, or seeking feedback on a dish they've prepared.
2. **System Message:** A predefined system message introduces Chef Shabbir's personality and expertise.
3. **API Call:** The user query and system message are sent to OpenAI's GPT-3.5 model to generate a response.
4. **Response:** The assistant provides a response based on the user's query.
5. **Interactive Loop:** The script continues to prompt the user for more queries until they decide to exit by typing 'quit'.

---

## How to Use Chef Shabbir

You can ask Chef Shabbir questions like:
- What can I make with [ingredients]?
- Can you give me a recipe for [dish]?
- I made [dish] with [ingredients]. What could I improve?

Type `quit` to exit the conversation.

## Example Interactions

### Example 1: Ingredient-Based Query

# User Input
What can I make with chicken, rice, and yogurt?
```python
# Chef Shabbir's Response
With the ingredients you have - chicken, rice, and yogurt, I would suggest making Chicken Biryani, a popular and aromatic Pakistani dish. Here's a simplified recipe for you:

Ingredients:
- 500g chicken, cut into pieces
- 2 cups basmati rice
- 2 cups plain yogurt
- 2 onions, thinly sliced
- 2 tbsp garlic paste
- 2 tbsp ginger paste
- 2 tbsp red chili powder
- 1 tbsp coriander powder
- 1 tbsp cumin powder
- 2 tsp turmeric powder
- 4 cardamom pods
- 2 cinnamon sticks
- 2 bay leaves
- Salt to taste
- 4 tbsp vegetable oil
- 2 tbsp butter
- Fresh coriander and mint leaves for garnish
- Fried onions for garnish

Instructions:
1. Wash and soak the basmati rice for 30 minutes. Drain and set aside.
2. In a large pan, heat oil and butter over medium heat. Add cinnamon sticks, cardamom pods, and bay leaves, followed by sliced onions. Sauté until golden brown.
3. Add garlic and ginger paste, stirring until fragrant.
4. Add chicken pieces and stir well, ensuring they're coated with the onion mixture. Cook until chicken is half done.
5. Add coriander powder, cumin powder, turmeric powder, red chili powder, and salt. Mix well.
6. Stir in the yogurt and cook for 5-7 minutes until the chicken is fully cooked and the sauce thickens.
7. In a separate large pot, boil the soaked rice with a pinch of salt and 2 whole cinnamon sticks. Cook until the rice is 80% done. Drain and set aside.
8. Layer the rice over the chicken mixture in the pan, ensuring an even layer.
9. Cover the pan with a tight lid and cook over low heat for 10-15 minutes until the rice is fully cooked and the flavors are well combined.
10

Continue? (yes/no): yes
```
### Example 2: Recipe Request
# User Input
Can you give me a recipe for Chicken Biryani?
```python
# Chef Shabbir's Response
Of course! I'd be happy to share my Chicken Biryani recipe with you. Here it is:

Ingredients:
- 1 kg (2.2 lbs) basmati rice
- 1 kg (2.2 lbs) chicken, cut into pieces
- 2 cups yogurt
- 4 medium onions, thinly sliced
- 4 medium tomatoes, finely chopped
- 4 green chilies, finely chopped
- 1 tbsp ginger paste
- 1 tbsp garlic paste
- 2 tbsp lemon juice
- 1 tbsp red chili powder
- 1 tbsp coriander powder
- 1 tbsp cumin powder
- 1 tsp turmeric powder
- 2 tbsp biryani masala (available at most Indian/Pakistani grocery stores)
- 1 bunch fresh coriander, finely chopped
- 1 bunch fresh mint, finely chopped
- 1 cup ghee (clarified butter) or oil
- Salt to taste
- 4 cups water
- A few strands of saffron, soaked in 1/4 cup warm milk
- 1/2 cup fried onions for garnish (optional)

Instructions:

1. Wash the rice thoroughly and soak it in water for at least 30 minutes. Drain and set aside.

2. In a large bowl, mix the chicken pieces with yogurt, 1/2 of the sliced onions, 1/2 of the chopped tomatoes, green chilies, ginger paste, garlic paste, lemon juice, red chili powder, coriander powder, cumin powder, turmeric powder, biryani masala, and salt. Marinate for at least 2 hours or overnight.

3. Heat 1/2 of the ghee or oil in a large pan and fry the remaining sliced onions until golden brown. Remove and set aside.

4. In the same pan, add the marinated chicken and cook on medium heat until the chicken is half-cooked. Add the remaining chopped tomatoes, coriander, and mint. Cook for another 5 minutes

Continue? (yes/no): yes
```
### Example 3: Recipe Critique
# User Input
I made Chicken Karahi with chicken, tomatoes, ginger, garlic, and spices. What could I improve?
```python
# Chef Shabbir's Response
Hello! It's wonderful that you've tried your hand at Chicken Karahi, a beloved dish from the Punjab region of Pakistan. I'm more than happy to provide some constructive feedback to help enhance your cooking experience.

1. Marination: Marinating the chicken in a mixture of yogurt, lemon juice, and spices for at least 30 minutes can help tenderize the meat and impart a richer flavor.
2. Browning the chicken: Make sure to sear the chicken pieces on high heat until they are nicely browned. This step will add depth and complexity to the final dish.
3. Freshness of ingredients: Using the freshest possible ingredients, especially ginger, garlic, and tomatoes, can significantly improve the taste of your Chicken Karahi.
4. Balancing the spices: While Pakistani cuisine is known for its bold flavors, it's essential to balance the spices carefully. Feel free to adjust the quantities of individual spices according to your preference, ensuring that none overpowers the others.
5. Garnish: Don't forget to garnish your Chicken Karahi with fresh coriander leaves and a squeeze of lemon juice just before serving. These finishing touches can elevate the presentation and enhance the overall taste.

Keep practicing and experimenting with these tips, and I'm sure you'll continue to create delicious Pakistani dishes. Happy cooking!

Continue? (yes/no): no
Thank you for visiting Chef Shabbir kitchen. Allah Hafiz!
```
#How to Run the Project
###Clone the Repository
```python 
git clone git@github.com:Shabbir-Anjum/Encode_Club-AI-Boot-camp-week-1-.git
```
###Setup API Key: Ensure that you have your OpenAI API key securely prompted in the environment
```python
openai.api_key = userdata.get('OPENAI_API_KEY')
```

