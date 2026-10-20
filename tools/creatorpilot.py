#!/usr/bin/env python3
"""Dependency-free local utilities for YouTube Creator Agent — CreatorPilot AI."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CONCRETE_RE = re.compile(r"\b\d+\b|%|\$|₹|\b(days?|weeks?|months?|hours?|minutes?|years?|steps?|mistakes?|ways?)\b", re.I)
TENSION_WORDS = {"wrong", "mistake", "secret", "surprising", "instead", "stop", "avoid", "never", "why", "truth", "problem", "hidden", "fail", "failed"}
AUDIENCE_WORDS = {"you", "your", "beginner", "beginners", "creator", "creators", "student", "students", "developer", "developers", "everyone"}
FILLER_STARTS = ("welcome back", "hey guys", "hello everyone", "in this video", "today we are going to")


def score_hook(text: str) -> dict:
    """Return a transparent heuristic score and explainable feedback."""
    clean = " ".join(text.split())
    words = re.findall(r"\b[\w'-]+\b", clean.lower())
    if not words:
        return {"score": 0, "signals": [], "advice": ["Add a specific opening line to evaluate."], "word_count": 0}

    points = 0
    signals, advice = [], []
    if CONCRETE_RE.search(clean):
        points += 25
        signals.append("Has a concrete detail")
    else:
        advice.append("Add a concrete detail, example, number, or outcome.")

    if any(w in TENSION_WORDS for w in words):
        points += 25
        signals.append("Contains a curiosity or tension cue")
    else:
        advice.append("Introduce a real question, contrast, mistake, or unresolved problem.")

    if any(w in AUDIENCE_WORDS for w in words):
        points += 20
        signals.append("Signals an audience or direct relevance")
    else:
        advice.append("Make the intended audience or personal relevance clearer.")

    if 7 <= len(words) <= 24:
        points += 20
        signals.append("Opening is a concise spoken length")
    elif len(words) < 7:
        points += 10
        advice.append("Consider adding enough context to make the promise clear.")
    else:
        advice.append("Trim the opening; try to communicate one idea in 7–24 words.")

    if not clean.endswith("?") and any(w in {"because", "but", "until", "without", "before"} for w in words):
        points += 10
        signals.append("Sets up a contrast or reason")
    elif clean.endswith("?"):
        points += 10
        signals.append("Uses a direct question")
    else:
        advice.append("Consider a meaningful contrast or question, if it fits the content.")

    if clean.lower().startswith(FILLER_STARTS):
        points = max(0, points - 10)
        advice.append("Remove the generic greeting and lead with the viewer's problem or payoff.")

    return {"score": min(100, points), "signals": signals, "advice": advice, "word_count": len(words)}


def check_title(title: str, thumbnail: str = "") -> dict:
    """Lint title and thumbnail text; no external performance claims."""
    title = " ".join(title.split())
    thumbnail = " ".join(thumbnail.split())
    issues, strengths = [], []
    words = re.findall(r"\b[\w'-]+\b", title)
    if not title:
        issues.append("Title is empty.")
    if len(title) > 70:
        issues.append(f"Title is {len(title)} characters; consider shortening it (heuristic threshold: 70).")
    elif title:
        strengths.append("Title length is within the 70-character heuristic.")
    letters = [c for c in title if c.isalpha()]
    if len(letters) >= 8 and sum(c.isupper() for c in letters) / len(letters) > 0.7:
        issues.append("Most letters are uppercase; use capitalization intentionally.")
    vague = {"amazing", "crazy", "awesome", "best", "incredible", "unbelievable"}
    if any(w.lower() in vague for w in words):
        issues.append("Contains a generic hype word; replace it with a specific benefit or claim.")
    if len(words) < 4 and title:
        issues.append("Very short title: check that the topic and viewer payoff are still clear.")
    if thumbnail:
        t_words = {w.lower() for w in re.findall(r"\b[\w'-]+\b", title)}
        th_words = {w.lower() for w in re.findall(r"\b[\w'-]+\b", thumbnail)}
        overlap = t_words & th_words
        meaningful = overlap - {"the", "a", "an", "to", "of", "and", "in", "for", "with", "how"}
        if meaningful and len(meaningful) / max(1, len(th_words)) >= 0.5:
            issues.append("Title and thumbnail text repeat much of the same wording; let them complement each other.")
        else:
            strengths.append("Title and thumbnail wording have some separation.")
    if title and not re.search(r"\b(why|how|what|when|mistake|guide|build|learn|fix|without|vs\.?)\b", title, re.I):
        issues.append("Check whether the title communicates a clear question, action, contrast, or specific topic.")
    return {"title": title, "thumbnail": thumbnail, "issues": issues, "strengths": strengths}


TIMESTAMP_RE = re.compile(r"(?P<time>(?:\d{1,2}:)?\d{1,2}:\d{2}(?:[.,]\d{1,3})?)")


def to_seconds(timestamp: str) -> float:
    timestamp = timestamp.replace(",", ".")
    parts = timestamp.split(":")
    if len(parts) == 2:
        minutes, seconds = parts
        return int(minutes) * 60 + float(seconds)
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    raise ValueError(f"Unsupported timestamp: {timestamp}")


def transcript_moments(text: str, limit: int = 5) -> list[dict]:
    """Parse timestamped lines and rank candidate moments with transparent text cues."""
    rows = []
    for line in text.splitlines():
        match = TIMESTAMP_RE.search(line)
        if not match:
            continue
        stamp = match.group("time")
        remainder = (line[:match.start()] + line[match.end():]).strip(" \t-:|")
        if not remainder:
            continue
        lower = remainder.lower()
        cues = ["surprising", "mistake", "secret", "key", "fix", "problem", "because", "instead", "lesson", "save", "important", "never"]
        score = min(10, sum(1 for cue in cues if cue in lower) * 2 + (2 if "?" in remainder else 0) + (1 if re.search(r"\d", remainder) else 0))
        rows.append({"timestamp": stamp, "seconds": to_seconds(stamp), "text": remainder, "score": score})
    rows.sort(key=lambda item: (-item["score"], item["seconds"]))
    return rows[:max(0, limit)]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="creatorpilot", description="Local-first YouTube creator helpers.")
    sub = parser.add_subparsers(dest="command", required=True)
    hook = sub.add_parser("hook", help="Score an opening line with transparent heuristics.")
    hook.add_argument("text", help="Opening line")
    title = sub.add_parser("title", help="Lint title and optional thumbnail text.")
    title.add_argument("text", help="Video title")
    title.add_argument("--thumbnail", default="", help="Thumbnail text, if any")
    clips = sub.add_parser("clips", help="Rank candidate moments in a timestamped transcript.")
    clips.add_argument("file", type=Path, help="Text file with timestamps at line level")
    clips.add_argument("--limit", type=int, default=5)
    args = parser.parse_args(argv)

    if args.command == "hook":
        result = score_hook(args.text)
        print(f"Hook score: {result['score']}/100 (heuristic, not a virality prediction)")
        print(f"Word count: {result['word_count']}")
        for item in result["signals"]:
            print(f"  + {item}")
        for item in result["advice"]:
            print(f"  - {item}")
        return 0
    if args.command == "title":
        result = check_title(args.text, args.thumbnail)
        print(f"Title: {result['title']}")
        if result["thumbnail"]:
            print(f"Thumbnail text: {result['thumbnail']}")
        for item in result["strengths"]:
            print(f"  + {item}")
        for item in result["issues"]:
            print(f"  ! {item}")
        if not result["issues"]:
            print("No heuristic issues found. Human review is still recommended.")
        return 0
    if args.command == "clips":
        try:
            content = args.file.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"Could not read transcript: {exc}", file=sys.stderr)
            return 2
        moments = transcript_moments(content, args.limit)
        if not moments:
            print("No timestamped transcript lines found. Use lines such as 00:01:23.400 Your transcript text.")
            return 0
        for index, item in enumerate(moments, 1):
            print(f"{index}. [{item['timestamp']}] heuristic score {item['score']}/10")
            print(f"   {item['text']}")
        print("These are editing candidates, not rendered clips. Verify context and timestamps manually.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
