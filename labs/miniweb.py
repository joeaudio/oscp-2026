#!/usr/bin/env python3
"""Intentionally weak, loopback-only web lab with synthetic data."""

import json
import sqlite3
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit


DATA = Path(__file__).resolve().parent / "data"


class Handler(BaseHTTPRequestHandler):
    def send(self, status, body, content_type="text/plain; charset=utf-8"):
        content = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        url = urlsplit(self.path)
        args = parse_qs(url.query, keep_blank_values=True)

        if url.path == "/":
            self.send(200, '<h1>Miniweb</h1><a href="/files?name=readme.txt">files</a> '
                      '<a href="/search?q=guide">search</a>', "text/html; charset=utf-8")
        elif url.path == "/health":
            self.send(200, '{"status":"ok"}', "application/json")
        elif url.path == "/robots.txt":
            self.send(200, "User-agent: *\nDisallow: /admin\n")
        elif url.path == "/admin":
            cookie = SimpleCookie()
            cookie.load(self.headers.get("Cookie", ""))
            if cookie.get("role") and cookie["role"].value == "admin":
                self.send(200, "Synthetic admin page. No real credentials here.\n")
            else:
                self.send(403, "Forbidden\n")
        elif url.path == "/files":
            name = args.get("name", [""])[0]
            chosen = (DATA / "public" / name).resolve()
            # Deliberate lesson bug: confines reads to data/, not public/.
            if not chosen.is_relative_to(DATA):
                self.send(403, "Outside lab data root\n")
            elif not chosen.is_file():
                self.send(404, "Not found\n")
            else:
                self.send(200, chosen.read_text(encoding="utf-8"))
        elif url.path == "/search":
            q = args.get("q", [""])[0]
            with sqlite3.connect(":memory:") as db:
                db.executescript("""
                    CREATE TABLE docs (title TEXT, summary TEXT);
                    INSERT INTO docs VALUES ('guide', 'Start with scope and notes');
                    INSERT INTO docs VALUES ('web', 'Compare requests and responses');
                    INSERT INTO docs VALUES ('report', 'Reproduce every claim');
                """)
                try:
                    # Deliberate lesson bug: input changes SQL syntax.
                    rows = db.execute(
                        "SELECT title, summary FROM docs WHERE title LIKE '%" + q + "%'"
                    ).fetchall()
                except sqlite3.Error:
                    self.send(400, "Query error\n")
                    return
            self.send(200, json.dumps(rows), "application/json")
        else:
            self.send(404, "Not found\n")


def make_server(port=8765):
    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


if __name__ == "__main__":
    server = make_server()
    print("Miniweb lab: http://127.0.0.1:8765 (Ctrl-C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
