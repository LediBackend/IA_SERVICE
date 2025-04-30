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


def retrieveDocsForCategory(fVector, preference, k=10, fetch_size=100):
    categories = [cat.lower().strip() for cat in preference.get('category', [])]
    language = preference.get('language', '').lower().strip()

    try:
        docs = fVector.similarity_search("", k=fetch_size)
        
        filtered_docs = []
        for doc in docs:
            doc_lang = doc.metadata.get("language", "").lower().strip()
            doc_cat = doc.metadata.get("category", "").lower().strip()
                        
            if doc_lang == language and doc_cat in categories:
                filtered_docs.append(doc)

        return filtered_docs[:k]

    except Exception as e:
        print(f"[retrieveDocsForCategory] Error: {e}")
        return []


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

