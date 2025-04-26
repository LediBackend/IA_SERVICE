from fastapi import APIRouter
from src.utils.requestProcessingUtilities import retrieveDocs,responseGenerator
from pydantic import BaseModel
from src.components.classEmbeddings import vector_store
from src.utils.databaseUtilities import get_document,insert_document,append_to_array,get_document_by_id
from src.templates.templateContainer import getTemplateChatBot

requestReceiverRouter = APIRouter()

class QueryRequest(BaseModel):
    question: str | None = None
    book_name: str | None = None
    userId:str

@requestReceiverRouter.post('/request',tags=['ChatBot'])

async def requestReceiver(request:QueryRequest):

    RelatedDocs = retrieveDocs(request.question,vector_store,request.book_name)

    context = "\n".join(doc.page_content for doc in RelatedDocs) if RelatedDocs else "No se encontró suficiente contexto."

    user = get_document_by_id('userService','users',request.userId)

    historial = get_document('Historial','Chats',{"userId":user['_id']})

    if not historial:
        insert_document('Historial','Chats',{'userId':user['_id'],"chats":[]})

    if historial and "chats" in historial:
        historial_formateado = "\n".join([f"- {chat['question']}\n  👉 {chat['response']}" for chat in historial["chats"]])
        
    res = responseGenerator(request.question,getTemplateChatBot(context,user['name'],historial_formateado))
        
    append_to_array('Historial','Chats',{'userId':user['_id']},'chats',{'question':request.question, 'response': res})

    return { 'answer': res  }
     