from fastapi import APIRouter

questionnaireCreationRoutes = APIRouter()

@questionnaireCreationRoutes.get('/quiz')
def questionnaireCreation():
     return 'hello'