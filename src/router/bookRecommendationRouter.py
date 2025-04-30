from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.utils.databaseUtilities import get_document_by_id
from src.utils.requestProcessingUtilities import responseGenerator,retrieveDocsForCategory
from src.components.classEmbeddings import vector_store
from src.templates.templateContainer import getRecommendationTemplates


bookRecommendationRouter =APIRouter()

class DataUser(BaseModel):
     userId: str

@bookRecommendationRouter.get('/recommendations',tags=['bookRecommendation'])
def bookRecommendation(req:DataUser):
     user = get_document_by_id('userService','users',req.userId)

     if not user:
          return JSONResponse({'msg':'usuario no registrado'},status_code=404)

     preferences = user['preference']

     try:
          searchedBooks = retrieveDocsForCategory(vector_store,preferences)
     except Exception as error:
          print(f"Error al recuperar libros: {error}")
          return JSONResponse({'msg': 'Error al recuperar libros'}, status_code=500)

     context = "\n".join([doc.page_content for doc in searchedBooks])
     
     res = responseGenerator('',getRecommendationTemplates(context))

     return JSONResponse({'response':res})

