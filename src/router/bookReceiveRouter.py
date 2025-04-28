from langchain.schema import Document
from fastapi import APIRouter,File,UploadFile,Body
import os
from src.utils.processingUtilities import processedAndSaved,getFileHash,isPdfAlreadyIndexed,loadFile,textSplitter,indexDocs,translateToEnglish
from src.components.classEmbeddings import vector_store

bookReceiveRouter = APIRouter()


    

@bookReceiveRouter.post('/upload',tags=['Books'])
async def bookReceive(
    category: str = Body(...),
    language: str = Body(...),
    file: UploadFile = File(...),
):
    UPLOAD_FOLDER = "./src/uploads"
    
    try:
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        FileName = file.filename

        FilePath = await processedAndSaved(UPLOAD_FOLDER, file, FileName)
        FileHash = getFileHash(FilePath)

        if isPdfAlreadyIndexed(FileHash, vector_store):
            return {"message": "Este libro ya ha sido indexado."}

        document = loadFile(FilePath)

        if isinstance(document, str):
            document = [Document(page_content=document)]

        ChunkedDocument = textSplitter(document)

        for doc in ChunkedDocument:
            doc.metadata["file_hash"] = FileHash
            doc.metadata["book_name"] = FileName
            doc.metadata["language"] = language
            doc.metadata["category"] = translateToEnglish(category.lower())

        indexDocs(ChunkedDocument, vector_store)

        return {"file_name": FileName, "status": "Libro subido y procesado correctamente"}

    except Exception as e:
        print(e)
        return {"error": f"Ocurrió un error por favor intente de nuevo"}

