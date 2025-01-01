from requests import get, Response
import random
from time import sleep

class RequestHandler:
    USER_AGENT = [
        # Chrome
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.62 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.62 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.62 Mobile Safari/537.36",
        # Firefox
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:118.0) Gecko/20100101 Firefox/118.0",
        "Mozilla/5.0 (Android 13; Mobile; rv:118.0) Gecko/20100101 Firefox/118.0",
        # Safari
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        # Edge
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.62 Safari/537.36 Edg/117.0.2045.43",
        # Opera
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.62 Safari/537.36 OPR/92.0.4561.33",
        # Generic Mobile
        "Mozilla/5.0 (Linux; U; Android 13; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36",
    ]
    
    DELAYS = [0, 1, 2, 3, 4, 5, 6]

    @staticmethod
    def make_request(url: str) -> Response:
        # delay randomly
        sleep(random.choice(RequestHandler.DELAYS))
        
        # get a random user agent
        headers = {"User-Agent": random.choice(RequestHandler.USER_AGENT)}

        resp = get(url, headers=headers)

        if resp.status_code != 200:
            raise Exception(f"Error getting response. Status code: {resp.status_code}")
        
        return resp
