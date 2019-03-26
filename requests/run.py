from threading import Thread
import requests

def download(url):
    r = requests.get(url, timeout=10);
    print(dir(r));

if __name__ == '__main__':
    url = ''#ANY URL HOSTING DATA
    thread = Thread(target=download, args=(url,));
    
    try:
        r = requests.get(url, timeout=180);
        print(r.elapsed.total_seconds());
        r = r.json()
        print(len(r['results']));
    except Exception as e:
        print(e)

