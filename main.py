import uvicorn
from fastapi import FastAPI
from routers import class_routes, student_routes, users_route
from db.database import initialize_database


async def lifespan(app: FastAPI):
    """
    Lifespan function for handling startup and shutdown events.
    """
    print("Startup event triggered")
    try:
        initialize_database()  # Initialize database tables
    except Exception as e:
        print("Exception occurred during database initialization:", e)

    yield  # Indicates startup has completed

    print("Shutdown event triggered")



# Use Lifespan for application lifecycle events
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    """
    Root endpoint for the application.
    """
    return {"message": "Hello! Welcome to Our Qook-Qloud"}

# Include class and student routes
app.include_router(class_routes.router)
app.include_router(student_routes.router)
app.include_router(users_route.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)