# Streaming video with FastAPI

Read the blog post: [Streaming video with FastAPI](https://stribny.name/blog/fastapi-video).

You will need a video in the video format that is supported by your browser. Place it in the root folder as `video.mp4` or modify the video path in the source code.

To run the example, install Poetry and then execute:

```bash
poetry install && poetry shell
uvicorn main:app --reload
```

Then just navigate to the main page at `http://127.0.0.1:8000/` and the video should be streamed.