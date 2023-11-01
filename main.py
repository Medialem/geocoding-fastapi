from typing import Optional
from fastapi import FastAPI
from utils import google_map_geocoding
import requests
import subprocess
app = FastAPI()




@app.get("/geocoding")
def geocoding(query: str, token: str):
    data = google_map_geocoding(query, token)
    print(f'>>>>>> {data}')
    return data


@app.get("/download")
def geocoding():
    try:
        print("Start cmd")
        url = "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_1.bin"
        file_name = 'llama-2-7b-chat.ggmlv3.q4_1.bin'
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        print("Download successful.")
        return {'status': 200}
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return {'status': 500, 'error': e}


@app.get("/cmd")
def geocoding(query: str):
    # Execute the command and capture the output
    try:
        result = subprocess.run(query, capture_output=True, text=True, shell=True)
        print(result.stdout)
        return { 'status': 200, 'result': result}
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return { 'status': 500, 'error': e}

