import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from miniweb import make_server


class MiniwebTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = make_server(0)
        cls.base = "http://127.0.0.1:" + str(cls.server.server_port)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_loopback_and_health(self):
        self.assertEqual(self.server.server_address[0], "127.0.0.1")
        with urlopen(self.base + "/health") as response:
            self.assertEqual(json.load(response), {"status": "ok"})

    def test_cookie_boundary(self):
        with self.assertRaises(HTTPError) as denied:
            urlopen(self.base + "/admin")
        self.assertEqual(denied.exception.code, 403)
        denied.exception.close()
        with urlopen(Request(self.base + "/admin", headers={"Cookie": "role=admin"})) as response:
            self.assertEqual(response.status, 200)

    def test_traversal_is_bounded_to_lab(self):
        with urlopen(self.base + "/files?" + urlencode({"name": "../hidden/ops.txt"})) as response:
            self.assertIn("Synthetic hidden document", response.read().decode())
        with self.assertRaises(HTTPError) as denied:
            urlopen(self.base + "/files?" + urlencode({"name": "/etc/passwd"}))
        self.assertEqual(denied.exception.code, 403)
        denied.exception.close()

    def test_boolean_sqli(self):
        def search(q):
            with urlopen(self.base + "/search?" + urlencode({"q": q})) as response:
                return json.load(response)
        self.assertEqual(len(search("x' OR 1=1 -- ")), 3)
        self.assertEqual(len(search("x' OR 1=2 -- ")), 0)


if __name__ == "__main__":
    unittest.main()
