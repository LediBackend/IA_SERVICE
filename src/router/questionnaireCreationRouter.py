from fastapi import APIRouter
from pydantic import BaseModel
from src.utils.requestProcessingUtilities import responseGenerator
from src.templates.templateContainer import getTemplateQuiz
from src.utils.databaseUtilities import get_document,insert_document,append_to_array,get_document_by_id
from src.components.classEmbeddings import vector_store
from src.utils.requestProcessingUtilities import retrieveDocs

questionnaireCreationRouter = APIRouter()

class Record(BaseModel):
     userId:str
     bookName:str
     

@questionnaireCreationRouter.get('/quiz',tags=['Quiz'])
async def questionnaireCreation(req:Record):
     
     user = get_document_by_id('userService','users',req.userId)

     isPlayers = get_document('Games','Puzzle',{"userId": user['_id']})
     
     if not isPlayers:
          insert_document('Games','Puzzle',{'userId':user['_id'],'plays':[]})

     puzzles = isPlayers['plays'] if isPlayers else []

     formatted_string = "\n\n".join(f"Pregunta: {entry['question']}\nRespuestas: {', '.join(entry['answers'])}" for entry in puzzles)

     RelatedDocs = retrieveDocs('',vector_store,req.bookName)

     context = "\n".join(doc.page_content for doc in RelatedDocs) if RelatedDocs else "No se encontró suficiente contexto."

     quiz = responseGenerator('',getTemplateQuiz(context,formatted_string))

     test = quiz.split('\n')
     
     append_to_array('Games','Puzzle',{'userId':user['_id']},'plays',{'question':test[4],'answers':test[:4]})

     
     return test