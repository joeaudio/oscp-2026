import unittest

from check_public import problem


class PublicGuardTest(unittest.TestCase):
    def test_blocks_private_paths_and_tokens(self):
        self.assertIsNotNone(problem("oscp-work/targets/box/notes.md", b"clean"))
        self.assertIsNotNone(problem("notes.md", b"ghp_" + b"A" * 25))
        self.assertIsNotNone(problem("notes.md", b"-----BEGIN " + b"PRIVATE KEY-----"))

    def test_allows_public_text(self):
        self.assertIsNone(problem("oscp-notes/01-workflow.md", b"A synthetic lesson."))


if __name__ == "__main__":
    unittest.main()
