from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)

system_message = SystemMessage(content="""
You are a virtual assistant that can only answer using the following information:
- Opening hours: Monday to Friday from 9 a.m. to 6 p.m.
- Shipping: Free for orders over €50
- Customer service: contacto@tiendaejemplo.com
- Delivery time: Between 2 and 5 business days
- Payment methods: Credit card, PayPal, and Bizum
- We do not offer international shipping
""")

print("Asistente IAGENZ")

while True:
    pregunta = input("How can I help you?")
    if pregunta.lower() == "exit":
        print("See you later.")
        break

    human_message = HumanMessage(content=pregunta)
    respuesta = llm.invoke([system_message, human_message])
    print(respuesta.content)