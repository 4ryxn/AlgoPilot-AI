import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

URL = "https://leetcode.com/graphql"
HEADERS = {
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com/",
    "User-Agent": "AlgoPilot-AI/1.0 (+https://algo-pilot-ai.vercel.app/)",
}
REQUEST_TIMEOUT = (5, 25)
RETRY_STATUS_CODES = (429, 500, 502, 503, 504)


class LeetCodeError(Exception):
    pass


class LeetCodeUserNotFound(LeetCodeError):
    pass


class LeetCodeUnavailable(LeetCodeError):
    pass


def _build_session() -> requests.Session:
    retry = Retry(
        total=2,
        connect=2,
        read=2,
        status=2,
        backoff_factor=0.75,
        status_forcelist=RETRY_STATUS_CODES,
        allowed_methods=frozenset(["POST"]),
        respect_retry_after_header=True,
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session = requests.Session()
    session.headers.update(HEADERS)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


SESSION = _build_session()


def _post_graphql(query: str, variables: dict):
    try:
        response = SESSION.post(
            URL,
            json={"query": query, "variables": variables},
            timeout=REQUEST_TIMEOUT,
        )
    except (requests.Timeout, requests.ConnectionError) as exc:
        raise LeetCodeUnavailable("LeetCode data is temporarily unavailable. Please try again later.") from exc
    except requests.RequestException as exc:
        raise LeetCodeUnavailable("LeetCode data is temporarily unavailable. Please try again later.") from exc

    if response.status_code in RETRY_STATUS_CODES or response.status_code >= 500:
        raise LeetCodeUnavailable("LeetCode data is temporarily unavailable. Please try again later.")
    if response.status_code >= 400:
        raise LeetCodeUnavailable("LeetCode data is temporarily unavailable. Please try again later.")

    try:
        payload = response.json()
    except ValueError as exc:
        raise LeetCodeUnavailable("LeetCode data is temporarily unavailable. Please try again later.") from exc

    if payload.get("errors"):
        raise LeetCodeUnavailable("LeetCode data is temporarily unavailable. Please try again later.")

    return payload

def fetch_profile(username: str):
    query = """
    query userPublicProfile($username: String!) {
      matchedUser(username: $username) {
        username
        profile {
          realName
          userAvatar
          aboutMe
          school
          websites
          countryName
          ranking
        }
        submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
            submissions
          }
        }
      }
    }
    """
    user = _post_graphql(query, {"username": username}).get("data", {}).get("matchedUser")
    if not user:
        raise LeetCodeUserNotFound("LeetCode user not found.")
    return user

def fetch_calendar(username: str, year=None):
    query = """
    query userProfileCalendar($username: String!, $year: Int) {
      matchedUser(username: $username) {
        userCalendar(year: $year) {
          activeYears
          streak
          totalActiveDays
          submissionCalendar
        }
      }
    }
    """
    user = _post_graphql(query, {"username": username, "year": year}).get("data", {}).get("matchedUser")
    if not user:
        raise LeetCodeUserNotFound("LeetCode user not found.")
    return user.get("userCalendar")
