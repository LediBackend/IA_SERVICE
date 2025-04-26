from fastapi import FastAPI
from src.router.bookReceiveRouter import bookReceiveRouter
from src.router.requestReceiverRouter import requestReceiverRouter
from src.router.questionnaireCreationRouter import questionnaireCreationRouter
from src.router.bookRecommendationRouter import bookRecommendationRouter
app = FastAPI()

app.include_router(router=bookReceiveRouter)
app.include_router(router=requestReceiverRouter)
app.include_router(router=questionnaireCreationRouter)
app.include_router(router=bookRecommendationRouter)

