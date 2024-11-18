from requests import get, Response

class RequestHandler:
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"

    @staticmethod
    def make_request(url: str) -> Response:
        headers = {"User-Agent": RequestHandler.USER_AGENT}
        
        resp = get(url, headers=headers)
        
        if resp.status_code != 200:
            raise Exception(f"Error getting response. Status code: {resp.status_code}")
        return resp