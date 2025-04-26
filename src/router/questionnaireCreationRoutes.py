from fastapi import APIRouter
from pydantic import BaseModel
from src.utils.requestProcessingUtilities import responseGenerator
from src.templates.templateContainer import getTemplateQuiz
from src.utils.databaseUtilities import get_document,insert_document,append_to_array,get_document_by_id
from src.components.classEmbeddings import vector_store
from src.utils.requestProcessingUtilities import retrieveDocs

questionnaireCreationRoutes = APIRouter()

class Record(BaseModel):
     userId:str
     bookName:str
     

@questionnaireCreationRoutes.get('/quiz',tags=['Quiz'])
async def questionnaireCreation(req:Record):
     
     isPlayers = get_document('Games','Puzzle',{"userId": req.userId})
     
     user = get_document_by_id('userService','users',req.userId)

     if not isPlayers:
          insert_document('Games','Puzzle',{'userId':user['_id'],'plays':[]})


     puzzle_data = get_document("Games", "Puzzle", {"userId": user['_id']})

     extracted_data = puzzle_data

     extracted_data = ''


     RelatedDocs = retrieveDocs('',vector_store,req.bookName)

     context = "\n".join(doc.page_content for doc in RelatedDocs) if RelatedDocs else "No se encontró suficiente contexto."

     quiz = responseGenerator('',getTemplateQuiz(context,extracted_data))

     test = quiz.split('\n')
     

     append_to_array('Games','Puzzle',user['_id'],'plays',{'question':test[4],'answers':test[:3]})
     
     return test