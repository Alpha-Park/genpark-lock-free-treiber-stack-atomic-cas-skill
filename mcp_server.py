"""MCP Server for Treiber Stack Skill."""
import json
import sys
from client import TreiberStack

def main():
    stack = TreiberStack()
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [
                            {
                                "name": "push_stack",
                                "description": "Push value to lock-free stack",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {"value": {}},
                                    "required": ["value"]
                                }
                            },
                            {
                                "name": "pop_stack",
                                "description": "Pop value from lock-free stack",
                                "inputSchema": {"type": "object"}
                            }
                        ]
                    }
                }
            elif method == "tools/call":
                name = params.get("name")
                args = params.get("arguments", {})
                if name == "push_stack":
                    stack.push(args["value"])
                    out = {"status": "pushed", "size": stack.size}
                else:
                    val = stack.pop()
                    out = {"popped": val, "size": stack.size}
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(out)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
