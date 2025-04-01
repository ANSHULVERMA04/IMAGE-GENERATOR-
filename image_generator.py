from PIL import Image, ImageDraw, ImageFont
import random


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_image_based_on_prompt(prompt, image_name="generated_image.png", width=800, height=600):
    # Create a blank image with a white background
    image = Image.new('RGB', (width, height), "white")
    draw = ImageDraw.Draw(image)


    if "sun" in prompt.lower():
       
        draw.ellipse((width // 4, height // 4, width // 4 + 100, height // 4 + 100), fill="yellow")
        for i in range(8):
            angle = i * 45  
            x1 = (width // 4 + 50) + 120 * (random.uniform(-1, 1))  
            y1 = (height // 4 + 50) + 120 * (random.uniform(-1, 1))
            draw.line((width // 4 + 50, height // 4 + 50, x1, y1), fill="orange", width=3)

    elif "mountain" in prompt.lower():
      
        draw.polygon([(0, height), (width // 2, height // 3), (width, height)], fill="gray")
        draw.polygon([(width // 4, height), (width // 2, height // 2), (3 * width // 4, height)], fill="darkgray")

    elif "tree" in prompt.lower():
      
        draw.rectangle((width // 2 - 15, height - 100, width // 2 + 15, height), fill="saddlebrown")
        draw.ellipse((width // 2 - 50, height - 150, width // 2 + 50, height - 100), fill="forestgreen")

    else:
      
        for _ in range(5):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            draw.rectangle([x1, y1, x2, y2], fill=random_color())

 
    image.save(image_name)
    print(f"Image saved as {image_name}")


    image.show()

user_prompt = input("Enter a prompt for the image (e.g., sun, mountain, tree): ")
draw_image_based_on_prompt(prompt=user_prompt, image_name="generated_image.png")
