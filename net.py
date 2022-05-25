import requests
from exceptions import BadServerResponseCode, LoginError
from bs4 import BeautifulSoup
# https://www.reduc.edu.cu/
def login(user: str, passw: str, redirect: str = "https://google.com") -> None:
    """
    Tries to login in WiFi UC Cautive Portal
    :return None
    """
    # data json
    data = {"zone": "wifinodo", "auth_user": user,
            "auth_pass": passw, "accept": "Login", "rediurl": redirect}
    # post data
    req = requests.post(
        "https://hotspot.reduc.edu.cu:8003/index.php", data=data, timeout=10, verify=False)
    if req.status_code == 200:
        # parse response html
        print("[OK] Successfully connection")
        bs = BeautifulSoup(req.text)
        # check for an error
        error = bs.find("div", {"id": "error-message"})
        if error is not None and error:
            print(f"[ERROR] {error}")
            raise LoginError(error.text.strip())
        # everything is ok
        print(f"{user} is Connected")
    else:
        raise BadServerResponseCode(req.status_code)