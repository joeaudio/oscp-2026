# 05 — Manual SQL injection

**Outcome:** prove a query changes because of input, then describe the data
boundary and fix. The local lab stores invented rows in memory only.

## Tutorial

The toy search route builds SQL by joining text into a query. Compare a normal
search with an input containing a quote:

```sh
BASE=http://127.0.0.1:8765
curl -G --data-urlencode 'q=guide' "$BASE/search"
curl -G --data-urlencode "q='" "$BASE/search"
```

An error after a quote is a clue, not sufficient proof. Try one controlled
boolean pair and compare row counts:

```sh
curl -G --data-urlencode "q=x' OR 1=1 -- " "$BASE/search"
curl -G --data-urlencode "q=x' OR 1=2 -- " "$BASE/search"
```

`-- ` begins a SQL comment in this SQLite example. The `x` makes the normal
title match false, so the two predicates can be compared. If the first
returns rows and the second does not, the input affects query logic. Other DBs
use different syntax. A `UNION` attempt needs matching column count and
compatible types; never assume a copied payload will work. Error-based and
blind SQLi require comparing controlled true/false or timing outcomes.

The fix is a parameterized query, not stripping quotes:

```python
db.execute("SELECT title FROM docs WHERE title LIKE ?", ("%" + q + "%",))
```

The PEN-200 syllabus discusses SQLmap, but the current OSCP+ exam guide
prohibits automatic exploitation tools including SQLmap. Practice manual
reasoning and verify the live policy before an exam.

## Challenge

Without opening `miniweb.py`, find the number of searchable documents and
write a two-request proof of injection. State one alternative explanation
you ruled out. Then inspect the code and point to the unsafe concatenation.

<details><summary>Hint 1</summary>Use URL encoding; a literal space and quote may otherwise be altered by the shell or URL parser.</details>
<details><summary>Hint 2</summary>Start both inputs with `x' OR`; compare only `1=1` versus `1=2`.</details>
<details><summary>Check</summary>The true predicate returns all toy docs; the false predicate returns none. The contrast supports SQLi. The parameterized rewrite keeps user input as data.</details>
