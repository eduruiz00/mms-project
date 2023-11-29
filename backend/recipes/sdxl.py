from diffusers import DiffusionPipeline, AutoPipelineForText2Image
import torch
import matplotlib.pyplot as plt

def create_image(title, description):
    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", 
                                            torch_dtype=torch.float16,
                                            use_safetensors=True, 
                                            variant="fp16")

    pipe.to("cuda")

    final_prompt = f"""
        Generate a high-definition image representing the dish {title} with the following description: {description}. 
        Ensure the image captures the essence, appearance, and details of the dish, including color, texture, and plating.
    """

    image = pipe(prompt=final_prompt).images[0]
    return image

def create_image_turbo(title, description):
    pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
    pipe.to("cuda")

    final_prompt = f"""
        Generate a high-definition image representing the dish {title} with the following description: {description}. 
        Ensure the image captures the essence, appearance, and details of the dish, including color, texture, and plating.
    """


    image = pipe(prompt=final_prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
    return image