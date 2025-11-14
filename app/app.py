from fastapi import FastAPI, HTTPException, Form, UploadFile, Depends, File
from .db import Post, create_db_and_tables, get_async_session
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session)
):
    post = Post(
        caption=caption,
        url="dummy url",
        file_type="photo",
        file_name="dummy name"
    )

    session.add(post)
    await session.commit()
    await session.refresh(post)
    return {
        "id": str(post.id),
        "caption": post.caption,
        "url": post.url,
        "file_type": post.file_type,
        "file_name": post.file_name,
        "created_at": post.created_at.isoformat()
    }


