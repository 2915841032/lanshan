from gevent import pool, monkey
monkey.patch_all()
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time
import requests
from curl_cffi import requests as cffi_requests
from gevent.lock import RLock

key_lock = RLock()
key = 0


def get_key():
    global key
    key_lock.acquire()
    key += 1
    key_lock.release()
    return key

def test_request():
    print("start ")
    time.sleep(2)
    print(get_key())
    session = cffi_requests.Session(thread='gevent')
    response = session.get('https://www.baidu.com', verify=False, timeout=10)
    print(response.status_code, response.url)
    time.sleep(3)
    print('end')


if __name__ == "__main__":
    n = 3
    gevent_poll = pool.Pool(n)
    jobs = []
    for i in range(n):
        job = gevent_poll.spawn(test_request)
        jobs.append(job)
    gevent.joinall(jobs)