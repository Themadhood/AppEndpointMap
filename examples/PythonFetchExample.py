import json
import urllib.request
import os
from datetime import datetime, timedelta

URL = "https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/endpoints.json"
CACHE_FILE = "endpoint_cache.json"
REFRESH_DAYS = 365


def fetch_remote():
    with urllib.request.urlopen(URL, timeout=5) as response:
        data = response.read()
        return json.loads(data.decode("utf-8"))


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return None

    with open(CACHE_FILE, "r") as f:
        return json.load(f)


def save_cache(data):
    payload = {
        "fetched_at": datetime.utcnow().isoformat(),
        "map": data
    }

    with open(CACHE_FILE, "w") as f:
        json.dump(payload, f, indent=4)


def is_expired(cache):
    fetched = datetime.fromisoformat(cache["fetched_at"])
    return datetime.utcnow() - fetched > timedelta(days=REFRESH_DAYS)


def get_endpoint_map():
    cache = load_cache()

    # 1. No cache → fetch
    if cache is None:
        data = fetch_remote()
        save_cache(data)
        return data

    # 2. Expired → refresh
    if is_expired(cache):
        try:
            data = fetch_remote()
            save_cache(data)
            return data
        except:
            return cache["map"]

    # 3. Use cache
    return cache["map"]