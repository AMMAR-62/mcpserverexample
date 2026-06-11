To use the `add_tool`, add the below mcp server to your client:
```json
{
	"servers": {
		"Add Numbers": {
			"command": "uvx",
			"args": [
				"--from",
				"git+https://github.com/AMMAR-62/mcpserverexample.git",
				"mcp-server"
			]
		}
	}
}
```
