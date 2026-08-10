import os
import logging
from dotenv import load_dotenv

try:
    from google import genai
    from google.genai import types
except ImportError:
    genai = None
    types = None

load_dotenv()

logger = logging.getLogger(__name__)

SUPPORTED_MODES = {"coach", "review", "hint", "interview"}
GEMINI_MODEL = "gemini-3.6-flash"
API_KEY = os.getenv("GEMINI_API_KEY", "").strip()


def _normalize_mode(mode: str) -> str:
    mode = (mode or "coach").strip().lower()
    return mode if mode in SUPPORTED_MODES else "coach"


def _build_prompt(message: str, mode: str) -> str:
    message_text = message.strip()
    if mode == "hint":
        return (
            "You are an expert data structures and algorithms coach. "
            "Provide 2-4 progressive hints for the problem below. "
            "Do not reveal the complete solution immediately. "
            "Explain the key observation and mention the likely data structure or algorithm. "
            "Keep the hints specific to the provided problem or code and avoid generic one-line advice.\n\n"
            f"Problem / code:\n{message_text}"
        )
    if mode == "review":
        return (
            "You are an expert algorithm and code reviewer. "
            "Review the submitted solution or approach below. "
            "Discuss correctness, bugs, edge cases, time complexity, space complexity, code quality, and optimization opportunities. "
            "Do not rewrite the entire solution; offer targeted improvements and potential pitfalls.\n\n"
            f"Submission:\n{message_text}"
        )
    if mode == "interview":
        return (
            "You are a coding interviewer guiding a candidate through an algorithm problem. "
            "Do not give the full solution right away. "
            "Ask useful follow-up questions, suggest the next steps, and point toward the right techniques. "
            "Keep your guidance specific to the problem or code below.\n\n"
            f"Problem / code:\n{message_text}"
        )
    return (
        "You are an expert data structures and algorithms coach. "
        "Analyze the problem or code below in a problem-specific way. "
        "Explain: 1) understanding and constraints, 2) the brute-force approach, 3) the key observation, "
        "4) the optimized approach, 5) the most suitable algorithm or data structure, and 6) time and space complexity.\n\n"
        f"Problem / code:\n{message_text}"
    )


def _fallback_response(mode: str) -> dict[str, str]:
    return {"mode": mode, "answer": "AI coaching is temporarily unavailable. Please try again shortly."}


def generate_ai_response(message: str, mode: str = "coach"):
    mode = _normalize_mode(mode)
    if not message or not message.strip():
        return {"mode": mode, "answer": "Please provide a problem statement, code, or question so I can help."}

    if not API_KEY:
        logger.warning("GEMINI_API_KEY is not configured; returning fallback AI response.")
        return _fallback_response(mode)

    prompt = _build_prompt(message, mode)

    if genai is None or types is None:
        logger.error("google-genai SDK is not installed or failed to import; returning fallback AI response.")
        return _fallback_response(mode)

    try:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.25,
                max_output_tokens=1000,
                top_p=0.95,
            ),
        )

        answer = getattr(response, "text", "") or ""
        answer = answer.strip()
        if not answer:
            logger.error("Gemini returned an empty response text.")
            return _fallback_response(mode)

        return {"mode": mode, "answer": answer}
    except Exception:
        logger.exception("Gemini API error; returning fallback AI response.")
        return _fallback_response(mode)
