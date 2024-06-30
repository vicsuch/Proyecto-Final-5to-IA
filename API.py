from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import io
from PIL import Image
from Readfiles import Clasify

app = FastAPI()

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Read image file
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Process the image (for demonstration purposes, we'll just get its format)
        image_format = Clasify(image)
        
        # Return a string response
        return JSONResponse(content={"message": f"{image_format}"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    #uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)