import unittest
from text_analyzer.analyzer import analyze_text

class TestTextAnalyzer(unittest.TestCase):
    def test_analyze_text(self):
        text = "Hello world! This is a simple text for analysis."
        result = analyze_text(text)

        self.assertEqual(result["word_count"], 8)
        self.assertEqual(result["char_count"], 43)
        self.assertIn("analysis", result["keywords"])

if __name__ == "__main__":
    unittest.main()
