from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key="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", model_name="llama-3.2-90b-text-preview")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)





