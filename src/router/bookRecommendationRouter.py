from fastapi import APIRouter

bookRecommendationRouter =APIRouter()

@bookRecommendationRouter.get('/recommendations',tags=['bookRecommendation'])
def bookRecommendation():
     return 'hello world'