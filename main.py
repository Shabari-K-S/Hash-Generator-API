from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI(title="Universal Hash Generator API")

# Supported hash algorithms from hashlib
SUPPORTED_ALGORITHMS = {
    algo.upper(): getattr(hashlib, algo)
    for algo in hashlib.algorithms_available
    if callable(getattr(hashlib, algo, None))
}

# SHAKE algorithms require a length
SHAKE_ALGOS = {"SHAKE_128", "SHAKE_256"}

class HashRequest(BaseModel):
    data: str
    algorithm: str = "SHA256"
    length: int | None = None  # Optional, only needed for SHAKE

class HashResponse(BaseModel):
    original_data: str
    algorithm: str
    hash_value: str

@app.post("/generate-hash", response_model=HashResponse)
def generate_hash(request: HashRequest):
    algo_upper = request.algorithm.upper()

    if algo_upper not in SUPPORTED_ALGORITHMS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported algorithm '{request.algorithm}'. Supported: {', '.join(SUPPORTED_ALGORITHMS)}"
        )

    hasher = SUPPORTED_ALGORITHMS[algo_upper]()
    hasher.update(request.data.encode("utf-8"))

    if algo_upper in SHAKE_ALGOS:
        if not request.length:
            raise HTTPException(
                status_code=400,
                detail=f"{algo_upper} requires 'length' field in request (number of hex digits to return)."
            )
        hash_value = hasher.hexdigest(request.length)
    else:
        hash_value = hasher.hexdigest()

    return HashResponse(
        original_data=request.data,
        algorithm=algo_upper,
        hash_value=hash_value
    )

@app.get("/supported-algorithms")
def get_supported_algorithms():
    return {"supported_algorithms": list(SUPPORTED_ALGORITHMS.keys())}


@app.get("/ping")
def ping():
    return {"message": "pong"}