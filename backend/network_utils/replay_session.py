from requests import Session

class LoggedSession(Session):
    def __init__(self):
        super().__init__()

    # Overriding 'send' catches all methods (.get, .post, .put, etc.) 
    def send(self, request, **kwargs):
        # .path_url gives you just the path (e.g., /api/data), .url gives the full string

        print(f"Making {request.method} request to: {request.url}")
        # Call the parent class to actually execute the request
        return super().send(request, **kwargs)

if __name__ == '__main__':
    sess = LoggedSession()
    payload = {
        "project": "Proyecto-TALIA",
        "status" : "testing"
    }

    # httpbin.org is a free service that echoes your request back to you
    response = sess.post("https://httpbin.org/post", json=payload)

    print("Status Code:", response.status_code)
    print("Echoed Body:", response.json().get("json"))