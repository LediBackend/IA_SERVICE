from fastapi import APIRouter

bookRecommendationRouter =APIRouter()

@bookRecommendationRouter.get('/',tags=['bookRecommendation'])
def bookRecommendation():
     return 'hello world'