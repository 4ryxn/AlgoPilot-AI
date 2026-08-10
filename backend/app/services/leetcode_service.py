import requests

URL = "https://leetcode.com/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com/",
    "User-Agent": "Mozilla/5.0",
}

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
    r = requests.post(
        URL,
        json={"query": query, "variables": {"username": username}},
        headers=HEADERS,
        timeout=15,
    )
    r.raise_for_status()
    user = r.json().get("data", {}).get("matchedUser")
    if not user:
        raise ValueError("LeetCode user not found")
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
    r = requests.post(
        URL,
        json={"query": query, "variables": {"username": username, "year": year}},
        headers=HEADERS,
        timeout=15,
    )
    r.raise_for_status()
    return r.json().get("data", {}).get("matchedUser", {}).get("userCalendar")
