import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from creatorpilot import score_hook, check_title, to_seconds, transcript_moments


class HookTests(unittest.TestCase):
    def test_empty_hook(self):
        self.assertEqual(score_hook(" ")["score"], 0)

    def test_specific_hook_scores_above_empty(self):
        self.assertGreater(score_hook("I made 3 mistakes, but you can avoid them in 7 days.")["score"], 0)

    def test_score_is_bounded(self):
        self.assertLessEqual(score_hook("You should never make this mistake in 10 days because it is surprising")["score"], 100)


class TitleTests(unittest.TestCase):
    def test_long_title_flagged(self):
        result = check_title("A" * 75 + " how to build a useful project")
        self.assertTrue(any("shortening" in issue for issue in result["issues"]))

    def test_overlap_flagged(self):
        result = check_title("Python mistakes beginners should avoid", "Python mistakes")
        self.assertTrue(any("repeat" in issue for issue in result["issues"]))

    def test_blank_title(self):
        self.assertIn("Title is empty.", check_title("")["issues"])


class TranscriptTests(unittest.TestCase):
    def test_timestamp_conversion(self):
        self.assertEqual(to_seconds("01:02:03.500"), 3723.5)
        self.assertEqual(to_seconds("02:03"), 123.0)

    def test_candidate_order(self):
        result = transcript_moments("00:00:01 First ordinary line\n00:00:05 Here is the surprising mistake and the key fix.")
        self.assertEqual(result[0]["timestamp"], "00:00:05")

    def test_no_timestamps(self):
        self.assertEqual(transcript_moments("plain text only"), [])


if __name__ == "__main__":
    unittest.main()
