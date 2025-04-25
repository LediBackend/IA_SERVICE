from openai import OpenAI
from src.config.env import TOKEN,ENDPOINT,MODEL



def retrieveDocs(query, fVector, bookName=None):
    
    docs = fVector.similarity_search(query, k=10)

    if bookName:
        normalized_book_name = bookName.strip().lower()
        
        docs = [
        
            doc for doc in docs 
        
            if doc.metadata.get("book_name", "").strip().lower().startswith(normalized_book_name)
        
        ]
    return docs

#falta ampliar la lógica pra tener memoria de cada usuario 
def responseGenerator(question,template):    
    token = TOKEN
    endpoint = ENDPOINT
    model = MODEL

    
    client = OpenAI(
        base_url = endpoint,
        api_key = token,
    )

    response = client.chat.completions.create(
    
        messages=[
            {
                "role": "system",
                "content": template,
            },
            {
                "role": "user",
                "content": question,
            }
        ],
        temperature = 1.0,
        top_p = 1.0,
        model = model
    )

    res = response.choices[0].message.content
    
    return res

