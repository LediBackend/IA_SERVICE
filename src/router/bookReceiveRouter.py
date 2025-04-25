from langchain.schema import Document
from fastapi import APIRouter,File,UploadFile
import os
from src.utils.processingUtilities import processedAndSaved,getFileHash,isPdfAlreadyIndexed,loadFile,textSplitter,indexDocs
from src.components.classEmbeddings import vector_store

bookReceiveRouter = APIRouter()

@bookReceiveRouter.post('/upload',tags=['Books'])
async def bookReceive(file:UploadFile = File(...)):

     UPLOAD_FOLDER = './src/uploads'
     
     os.makedirs(UPLOAD_FOLDER,exist_ok=True)

     FileName = file.filename
     
     FilePath = await processedAndSaved(UPLOAD_FOLDER,file,FileName)
     
     FileHash = getFileHash(FilePath)

     isAlready = isPdfAlreadyIndexed(FileHash,vector_store)

     if isAlready:
        
        return {"message": "Este libro ya ha sido indexado."}
     
     document = loadFile(FilePath)
     
     isInstance = isinstance(document, str)

     if isInstance:
         
         document = [Document(page_content=document)]

     ChunkedDocument = textSplitter(document)

     for doc in ChunkedDocument:
        
        doc.metadata["file_hash"] = FileHash
        
        doc.metadata["book_name"] = FileName

     indexDocs(ChunkedDocument,vector_store)

     return {"file_name": FileName, "status": "Libro subido y procesado correctamente"}
