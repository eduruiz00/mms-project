from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import re

def extract_recipe_info(input_string):
    assistant_info = {}
    parts = re.split("### Assistant:", input_string)[-1]
    title = re.search(r'Title: "([^"]+)"', parts).group(1)
    assistant_info['Title'] = title

    # Extract Quantities Required
    quantities_match = re.search(r'Quantities Required:\n(([^\n]+:[^\n]+\n)+)', parts)
    if quantities_match:
        quantities_section = quantities_match.group(1)
        quantities = {}
        quantity_lines = quantities_section.strip().split('\n')
        for line in quantity_lines:
            line = re.sub('"',"", line)
            ingredient, amount = line.split(':')
            quantities[ingredient.strip()] = amount
        assistant_info['Quantities Required'] = quantities

    # Extract Description
    description_match = re.search(r'Description: "([^"]+)"', parts)
    if description_match:
        assistant_info['Description'] = description_match.group(1)
    else:
        description_match = re.search(r'Description: ([^"]+)', parts)
        if description_match:
            assistant_info['Description'] = description_match.group(1)

    # Extract Instructions
    instructions_match = re.search(r'Instructions:(.*)<\/s>', parts, re.DOTALL)
    if instructions_match:
        assistant_info['Instructions'] = instructions_match.group(1)

    return assistant_info

def generate_recipe(ingredients, num_people, cooking_time, all_ingr=True, model=True):
    model_name_or_path = "TheBloke/sheep-duck-llama-2-13B-GPTQ"
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                                device_map="auto",
                                                trust_remote_code=False,
                                                revision="main")

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

    if all_ingr:
        all_ingr = "You have to use all the ingredients from the list above."
    else: 
        all_ingr = "You have to use some of the ingredients from the list abve."

    sample_prompt = f"""
        Create a recipe that serves {num_people} people in under {cooking_time} minutes, using the following ingredients:

        Ingredients:
        {ingredients}

        {all_ingr} 

        ---

        Title: "dish name. Write it in quotes"

        Quantities Required:
        "write the ingredients and the quantity of each one in this format ingredient: quantity"

        Description: "dish description that will be used to create an image of it. Write it in quotes"

        Instructions:

        "Enumerate the steps to cook the recipe."
    """

    system_message = "You are a professional chef. Everything expressed in quotes has to be replaced with that information."

    prompt_template=f'''### System:
    {system_message}

    ### User:
    {sample_prompt}

    ### Assistant:
    '''

    if model:
        input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
        output = model.generate(inputs=input_ids, temperature=0.7, do_sample=True, top_p=0.95, top_k=40, max_new_tokens=1024)

        out_model = tokenizer.decode(output[0])
        return out_model
    
    else:
        # Inference can also be done using transformers' pipeline

        # print("*** Pipeline:")
        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=1024,
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
            top_k=40,
            repetition_penalty=1.1
        )

        out_pipe = pipe(prompt_template)[0]['generated_text']
        return out_pipe
