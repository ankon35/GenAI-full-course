# Import necessary libraries

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI


load_dotenv()  

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)


while True:
    query = input("You: ")

    if query.lower() in ['exit']:
        print("Bye!")
        break


    res = llm.invoke(query)
    print("Bot:", res.content)




