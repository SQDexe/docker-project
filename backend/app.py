from routes.main import router as main_router
from routes.adoptions import router as adoptions_router
from routes.animals import router as animals_router
from routes.donations import router as donations_router
from routes.workers import router as workers_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(redoc_url=None)

origins = ('*', )

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=('*', ),
    allow_headers=('*', ),
    )

app.include_router(main_router)
app.include_router(adoptions_router)
app.include_router(animals_router)
app.include_router(donations_router)
app.include_router(workers_router)