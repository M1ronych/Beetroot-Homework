import requests
import json
import time
from multiprocessing import Pool,cpu_count

BASE_URL = "https://api.pushshift.io/reddit/comment/search/"
SUBREDDIT ="python"
LIMIT = 100

def fetch_comments(after):
    params = {
        "subreddit":SUBREDDIT,
        "size":LIMIT,
        "after":after,
        "sort":"asc",
        "sort_type":"created_utc"
    }

    headers = {
        "User-Agent":"python-homework-script/1.0"
    }

    response = requests.get(BASE_URL,params=params,headers=headers,timeout=10)
    if response.status_code==403:
        print("403 Forbidden - Pushshift відмовив")
        return []

    if response.status_code != 200:
        print("HTTP error:",response.status_code)
        return []

    try:
        return response.json().get("data",[])
    except ValueError:
        print("Answer is not JSON")
        return []
    
    #response.raise_for_status()
    #data = response.json()["data"]

    #return data

def fetch_range(start_after,max_requests=50):
    all_comments = []
    after = start_after

    for _ in range(max_requests):
        comments = fetch_comments(after)
        if not comments:
            break

        all_comments.extend(comments)
        after = comments[-1]["created_utc"]
        time.sleep(0.5)

    return all_comments

def main():
    data = fetch_range(0,max_requests=5)
    print(len(data))

   # start_times = [0,1_000_000_000,1_300_000_000,1_600_000_000]
   # with Pool(processes=cpu_count()) as pool:
   #     results = pool.map(fetch_range,start_times)

    #all_comments = []
   # for part in results:
   #     all_comments.extend(part)

   # all_comments.sort(key=lambda x: x["created_utc"])

    #with open("comments.json","w",encoding="utf-8") as f:
    #    json.dump(all_comments,f,ensure_ascii=False,indent=2)

if __name__ == "__main__":
    main()
