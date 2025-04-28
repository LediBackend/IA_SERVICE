from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.utils.databaseUtilities import get_document_by_id
from src.utils.requestProcessingUtilities import responseGenerator,retrieveDocsForCategory
from src.components.classEmbeddings import vector_store


bookRecommendationRouter =APIRouter()

class DataUser(BaseModel):
     userId: str

@bookRecommendationRouter.get('/recommendations',tags=['bookRecommendation'])
def bookRecommendation(req:DataUser):
     user = get_document_by_id('userService','users',req.userId)

     if not user:
          return JSONResponse({'msg':'usuario no registrado'},status_code=404)

     preference = user['preference']

     searchedBooks = retrieveDocsForCategory(vector_store,preference)

     print(searchedBooks)

     return 'hola'

