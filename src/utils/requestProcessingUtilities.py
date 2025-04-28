from openai import OpenAI
# from src.config.env import TOKEN_DE_TATI
from src.config.env import TOKEN_DE_SELENE
# 
from src.config.env import ENDPOINT,MODEL



def retrieveDocs(query, fVector, bookName=None):
    
    docs = fVector.similarity_search(query, k=10)

    if bookName:
        normalized_book_name = bookName.strip().lower()
        
        docs = [
        
            doc for doc in docs 
        
            if doc.metadata.get("book_name", "").strip().lower().startswith(normalized_book_name)
        
        ]
    return docs


def retrieveDocsForCategory(fVector, preference, k=10):
    categories = [cat.lower().strip() for cat in preference.get('category', [])]
    language = preference.get('lenguaje', '').lower().strip()
    docs_test = fVector.similarity_search("", k=5)
    for doc in docs_test:
        print(doc.metadata)  # Ver qué datos realmente están almacenados



    # Buscar todos los documentos en el vector store
    docs = fVector.similarity_search("", k=k)  # Búsqueda vacía para obtener documentos

    # Filtrar por categorías y lenguaje
    docs = [
        doc for doc in docs
        if doc.metadata.get("language", "").lower().strip() == language and
           doc.metadata.get("category", "").lower().strip() in categories
    ]

    return docs


def responseGenerator(question,template):    
    token = TOKEN_DE_SELENE
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

