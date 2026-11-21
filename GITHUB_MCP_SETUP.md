# Set Up GitHub MCP in Codex CLI

These instructions use Bash and a GitHub personal access token (PAT). They apply to a Codex CLI version that supports `--no-daemon`; check `codex --help` on other installations.

## 1. Create a GitHub token

Create a PAT in [GitHub token settings](https://github.com/settings/personal-access-tokens). Limit its repository access and permissions to the operations you need, and choose an expiration date.

Keep the token private. Never paste it into chat, commit it, or put its value in the commands below. Revoke and replace any token that has been exposed.

## 2. Register the server once

Run in your regular terminal:

```bash
codex mcp add github \
  --url https://api.githubcopilot.com/mcp/ \
  --bearer-token-env-var GITHUB_MCP_TOKEN

codex mcp list
```

The **Bearer Token Env Var** column must show `GITHUB_MCP_TOKEN`, not your token. If the existing entry is incorrect, run `codex mcp remove github` and then repeat the add command.

The corresponding entry in `~/.codex/config.toml` is:

```toml
[mcp_servers.github]
url = "https://api.githubcopilot.com/mcp/"
bearer_token_env_var = "GITHUB_MCP_TOKEN"
```

This PAT setup does not require `codex mcp login github`.

## 3. Load the token before starting Codex

Run in the same Bash terminal you will use to launch Codex:

```bash
read -rsp "GitHub PAT: " GITHUB_MCP_TOKEN
echo
export GITHUB_MCP_TOKEN
codex
```

Paste the token at the prompt; input stays hidden. The token remains available in this shell until you unset it or close the shell. Repeat this step in a new terminal or after rebooting; registering the server again is unnecessary.

## 4. Restart the Codex server if necessary

**The shared Codex background server may need restarting after you export or replace the token.** Closing and reopening the Codex interface can reuse that existing server.

An already-running server does not receive environment variables exported afterward. Restart it using the server-management mechanism supported by your installed version, and ensure the replacement server starts from the terminal where you exported the token. Restart commands vary; this guide does not assume one.

Alternatively, bypass the shared server:

```bash
codex --no-daemon
```

This starts without the shared background server and inherits the launching terminal's exported token. After a laptop restart, try ordinary `codex` after loading the token; `--no-daemon` is useful if another process has already started a server without it.

## 5. Verify inside Codex

Enter `/mcp` directly in the Codex interface, not in Bash. GitHub should show as connected with available tools. Try: `Show my GitHub profile.`

If startup reports that the variable is missing, check in the launching terminal without displaying the token:

```bash
if [ -n "${GITHUB_MCP_TOKEN:-}" ]; then
  echo "Token is set"
else
  echo "Token is missing"
fi
```

If it is set, revisit the background-server step. Other authentication failures may require checking token expiration, permissions, or organization approval.

## Reference

[GitHub's official Codex MCP installation guide](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-codex.md)
