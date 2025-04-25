from fastapi import FastAPI
from src.router.bookReceiveRouter import bookReceiveRouter
from src.router.requestReceiverRoute import requestReceiverRoute
from src.router.questionnaireCreationRoutes import questionnaireCreationRoutes
app = FastAPI()

app.include_router(router=bookReceiveRouter)
app.include_router(router=requestReceiverRoute)
app.include_router(router=questionnaireCreationRoutes)

