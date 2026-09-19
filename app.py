"""SN Cloud acceptance fixture — generic Python (DEC-001 AC-01).

No Dockerfile and no provider configuration: the repository is a plain Python web app
(requirements.txt + app.py) and must deploy because the platform can detect it.
"""
import os

from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return {
        "fixture": "sncloud-fixture-python",
        "framework": "python",
        "path": "/",
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
