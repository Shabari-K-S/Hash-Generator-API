# 🔐 Universal Hash Generator API

A fast and flexible API for generating cryptographic hashes using various popular algorithms like **SHA256**, **SHA3**, **MD5**, **BLAKE2**, and more. Designed for developers who need secure, consistent hashing in a lightweight, RESTful interface.

---

## 🚀 Features

* ✅ Supports multiple hash algorithms (MD5, SHA1, SHA2, SHA3, BLAKE2, SHAKE)
* 📦 Simple `POST` request with flexible JSON body
* 🔄 Dynamic algorithm support with optional output length (for SHAKE)
* 🧪 Includes endpoint to list all supported algorithms
* ⚡ Built using **FastAPI** – blazing fast and easy to deploy

---

## 📬 API Endpoints

### `POST /generate-hash`

Generate a hash from a string using the selected algorithm.

#### Request Body

```json
{
  "data": "Hello World",
  "algorithm": "SHA256"
}
```

If using `SHAKE_128` or `SHAKE_256`, include `length`:

```json
{
  "data": "Hello World",
  "algorithm": "SHAKE_256",
  "length": 64
}
```

#### Response

```json
{
  "original_data": "Hello World",
  "algorithm": "SHA256",
  "hash_value": "a591a6d40bf420404a011733cfb7b190..."
}
```

---

### `GET /supported-algorithms`

Returns a list of all supported hashing algorithms.

#### Response

```json
{
  "algorithms": [
    "MD5",
    "SHA1",
    "SHA256",
    "SHA3_512",
    "SHAKE_128",
    ...
  ]
}
```

---

## 🧪 Supported Algorithms

* **MD5**
* **SHA1**, **SHA224**, **SHA256**, **SHA384**, **SHA512**
* **SHA3\_224**, **SHA3\_256**, **SHA3\_384**, **SHA3\_512**
* **BLAKE2B**, **BLAKE2S**
* **SHAKE\_128**, **SHAKE\_256** (require length)

---

## 🛠️ Running Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/Shabari-K-S/Hash-Generator-API.git
   cd Hash-Generator-API
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

4. Visit the docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧠 Use Cases

* Hashing user passwords
* Data verification & integrity
* Token generation
* Content fingerprinting
* Cryptographic research
