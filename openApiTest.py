from openai import OpenAI
import base64
import mimetypes
from PIL import Image


image_name = str(input("Enter image name.exe: "))

with open(image_name, "rb") as f:
    image_bytes = f.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

mime_type = mimetypes.guess_type(image_name)[0] or "image/jpeg"

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="nvidia/nemotron-nano-12b-v2-vl:free",
   messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "extract the text from the image"
        },
        {
          "type": "image_url",
          "image_url": {
             "url": f"data:{mime_type};base64,{image_base64}"
          }
        }
      ]
    }
  ]
)
print(completion.choices[0].message.content)

if completion and completion.choices:
        print(completion.choices[0].message.content)
else:
        print("⚠️ No response content received from model.")
        print(completion)



#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