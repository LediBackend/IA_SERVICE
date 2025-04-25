from fastapi import APIRouter
from pydantic import BaseModel
from src.utils.requestProcessingUtilities import responseGenerator
from src.templates.templateContainer import getTemplateQuiz
from src.utils.databaseUtilities import get_document,insert_document

questionnaireCreationRoutes = APIRouter()

class Record(BaseModel):
     userId:str
     bookName:str
     

@questionnaireCreationRoutes.get('/quiz',tags=['Quiz'])
def questionnaireCreation(req:Record):
     
     isPlayers = get_document('Games','Puzzle',{"userId": req.userId})

     if not isPlayers:
          insert_document('Games','Puzzle',{'userId':req.userId,'plays':[]})

     

     quiz = responseGenerator('pregúntame',getTemplateQuiz())