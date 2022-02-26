from pathlib import Path
from fastapi import FastAPI
from fastapi import Request, Response
from fastapi import Header
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")
CHUNK_SIZE = 1024*1024
video_path = Path("video.mp4")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.htm", context={"request": request})


@app.get("/video")
async def video_endpoint(range: str = Header(None)):
    start, end = range.replace("bytes=", "").split("-")
    start = int(start)
    length = int(end) - start if end else CHUNK_SIZE
    end = start + length - 1
    with open(video_path, "rb") as video:
        video.seek(start)
        data = video.read(length)
        total = video_path.stat().st_size
        if end > total - 1:
            end = total - 1
        headers = {
            "Content-Range": f"bytes {start}-{end}/{total}",
            "Accept-Ranges": "bytes"
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")
