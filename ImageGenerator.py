import base64
import time
from together import Together

# Initialize the Together client with your API key
client = Together(api_key="72d44deceac5d1158f9a08a5773fcb873e1dbf6e3b2fc12272ea96232180beea")

# List of 50 prompts for cartoon-style human faces with diverse demographics
prompts = [
    # "A cartoon of a young male from Japan with a friendly smile, wearing a traditional kimono",
    # "A cartoon of a female from India with long black hair, wearing a colorful saree",
    # "A cartoon of a middle-aged male from Germany with glasses, wearing a formal suit",
    # "A cartoon of a young female from Brazil with curly hair, wearing a casual summer dress",
    # "A cartoon of a senior male from Nigeria with a traditional agbada outfit and a warm smile",
    # "A cartoon of a young female from the United States with blonde hair, wearing a modern business suit",
    # "A cartoon of a male from China with short black hair, wearing a casual t-shirt and jeans",
    # "A cartoon of a female from Russia with light brown hair, wearing a winter coat and scarf",
    # "A cartoon of a male from Mexico with a mustache, wearing a traditional charro outfit",
    # "A cartoon of a female from France with short hair, wearing a stylish beret and a striped shirt",
    # "A cartoon of a male from South Korea with a trendy hairstyle, wearing a casual hoodie",
    # "A cartoon of a female from Italy with dark brown hair, wearing a fashionable dress",
    # "A cartoon of a male from Canada with a beard, wearing a flannel shirt and jeans",
    # "A cartoon of a female from Australia with wavy blonde hair, wearing a summer hat",
    # "A cartoon of a male from South Africa with a shaved head, wearing a casual polo shirt",
    # "A cartoon of a female from Egypt with a hijab, wearing a traditional dress",
    # "A cartoon of a male from Saudi Arabia with a keffiyeh, wearing a white thobe",
    # "A cartoon of a female from Spain with long black hair, wearing a flamenco dress",
    # "A cartoon of a male from the United Kingdom with a bowler hat, wearing a formal coat",
    # "A cartoon of a female from Argentina with braided hair, wearing a casual outfit",
    # "A cartoon of a male from Turkey with a mustache, wearing a traditional fez and suit",
    # "A cartoon of a female from Sweden with blonde hair, wearing a knitted sweater",
    # "A cartoon of a male from Kenya with a bright smile, wearing a traditional Maasai shuka",
    # "A cartoon of a female from Thailand with long black hair, wearing a traditional Thai dress",
    # "A cartoon of a male from Greece with a beard, wearing a casual shirt and jeans",
    # "A cartoon of a female from Vietnam with a conical hat, wearing a traditional áo dài",
    # "A cartoon of a male from the Philippines with short black hair, wearing a barong tagalog",
    # "A cartoon of a female from Indonesia with a hijab, wearing a batik dress",
    # "A cartoon of a male from Peru with a poncho, wearing a traditional hat",
    # "A cartoon of a female from Norway with light brown hair, wearing a winter jacket",
    # "A cartoon of a male from Ethiopia with a traditional shamma, smiling warmly",
    # "A cartoon of a female from South Korea with a hanbok, standing gracefully",
    # "A cartoon of a male from Scotland with a kilt, holding bagpipes",
    # "A cartoon of a female from Morocco with a colorful kaftan, wearing traditional jewelry",
    # "A cartoon of a male from the United States with a cowboy hat, wearing a plaid shirt",
    # "A cartoon of a female from Brazil with carnival makeup, wearing a vibrant costume",
    # "A cartoon of a male from Russia with a fur hat, wearing a heavy winter coat",
    # "A cartoon of a female from Japan with a geisha outfit, holding a paper fan",
    # "A cartoon of a male from India with a turban, wearing a traditional sherwani",
    # "A cartoon of a female from China with a qipao, standing in a serene garden",
    # "A cartoon of a male from France with a beret, holding a baguette",
    # "A cartoon of a female from Mexico with a traditional embroidered dress, smiling brightly",
    # "A cartoon of a male from Canada with a lumberjack outfit, holding an axe",
    # "A cartoon of a female from Nigeria with a gele headwrap, wearing a colorful dress",
    # "A cartoon of a male from Italy with a chef's hat, holding a pizza",
    # "A cartoon of a female from Greece with a traditional peplos, standing near ancient ruins",
    # "A cartoon of a male from Thailand with a traditional chang kben, smiling warmly",
    # "A cartoon of a female from the Netherlands with blonde hair, wearing a traditional Dutch bonnet",
    # "A cartoon of a male from Iceland with a thick wool sweater, standing near a glacier",
    # "A cartoon of a female from Malaysia with a baju kurung, standing in a tropical setting"
    "Create an Gibli image of Salman Khan"
]

# Iterate through the list of prompts
for i, prompt in enumerate(prompts):
    print(f"Generating image for prompt {i + 1}: {prompt}")
    response = client.images.generate(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell-Free",
        width=1024,
        height=768,
        steps=4,
        n=1,
        response_format="b64_json",
        stop=[]
    )

    # Decode the base64 image data and save it as an image file
    image_data = response.data[0].b64_json
    image_bytes = base64.b64decode(image_data)

    # Save the image with a unique filename
    filename = f"generated_cartoon_image_{i + 1}.png"
    with open(filename, "wb") as image_file:
        image_file.write(image_bytes)

    print(f"Image saved as '{filename}'")

    # Wait for 10 seconds before generating the next image
    time.sleep(10)