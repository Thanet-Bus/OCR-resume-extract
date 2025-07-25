import os
import instructor
from dotenv import load_dotenv
from pydantic import BaseModel

# NOTE: Make sure that the model you're using has support for Tool Calling and/or Structured Outputs
load_dotenv()
model = "deepseek/deepseek-chat-v3-0324:free"

class ResumeLLMExtraction(BaseModel):
    name: str
    lname: str
    introduce: str
    additional_skill: str
    email: str

client = instructor.from_provider(
    model=model,
    base_url="https://openrouter.ai/api/v1",
    api_key= os.getenv('API_KEY'),
)

def send_to_ai(resume):
    response = client.chat.completions.create(
        model = model,
        messages= [
            {
                "role" : "system",
                "content" : "you are a experienced HR who is similiar with resume extraction. When reading resume,\
                    you usually pick up name even if it's place in incorrect order due to mistake in ocr (in Thai if available)\
                    and do short summary into thai language with precise, name/surname corrected order and corrected wording.\
                    You will be given unstructured text and should convert it into the given structure."
            },
            {
                "role": "user",
                "content": f"{resume}"
            }
            ],
            response_model = ResumeLLMExtraction,
            extra_body={"provider": {"require_parameters": True}},
            )
    return response