# 11 — Port forwarding and internal network pivots

**Outcome:** draw which host listens, which host connects, and which service
is reached before starting a tunnel. Only route traffic to in-scope systems.

## Tutorial

A local SSH forward places a listener on your machine and forwards to a
service reachable from the SSH server:

```sh
ssh -N -L 127.0.0.1:18080:10.10.20.5:80 user@bastion
curl -i http://127.0.0.1:18080/
```

The `10.10.20.5` address is an example inside an authorized lab. `-N`
requests no shell, and binding the listener to `127.0.0.1` prevents other
machines from using it. For a SOCKS route, `ssh -N -D 127.0.0.1:1080
user@bastion` creates a local proxy; verify that the application actually
uses it. A remote forward (`-R`) reverses listener placement. `socat`,
Chisel and Ligolo-ng provide other route shapes; each needs a port diagram
and a teardown step. Never assume a tunnel gives you DNS resolution or
authorization for every reachable subnet.

Worked route:

```text
Kali:127.0.0.1:18080 --SSH--> bastion --TCP--> internal:80
```

If `curl` fails, check the SSH session, bind address, bastion reachability,
and service port separately. A connection failure is not proof the internal
service is absent.

## Challenge

Draw a route for an HTTP service reachable only from an authorized bastion.
Then write the exact forward and teardown commands. In a disposable SSH lab,
verify with `ss -ltn` that the listener binds only to loopback.

<details><summary>Hint 1</summary>`-L local_bind:local_port:remote_host:remote_port` creates the local listener.</details>
<details><summary>Hint 2</summary>The SSH server resolves/reaches `remote_host`; the browser connects to `local_bind:local_port`.</details>
<details><summary>Check</summary>The route diagram must show both TCP legs and the process to stop. If the listener is `0.0.0.0`, explain why that is wider exposure than intended.</details>
