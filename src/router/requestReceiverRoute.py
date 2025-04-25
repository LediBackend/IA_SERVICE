from fastapi import APIRouter
from src.utils.requestProcessingUtilities import retrieveDocs,responseGenerator
from pydantic import BaseModel
from src.components.classEmbeddings import vector_store

requestReceiverRoute = APIRouter()

class QueryRequest(BaseModel):
    question: str
    book_name: str | None = None  

@requestReceiverRoute.post('/request')
async def requestReceiver(request:QueryRequest):

     RelatedDocs = retrieveDocs(request.question,vector_store,request.book_name)

     context = "\n".join(doc.page_content for doc in RelatedDocs) if RelatedDocs else "No se encontró suficiente contexto."

     res = responseGenerator(context,request.question)

     return { 'answer': res  }
     