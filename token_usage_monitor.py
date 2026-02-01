#!/usr/bin/env python3
"""
Offline & Office GitHub Token Usage Monitor
離線與辦公 Token 使用量監控器

Monitors GitHub API Rate Limits, PAT usage, and token efficiency for office environments.
"""

import json
import os
import urllib.request
import sys

def check_token_status():
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
    headers = {
        "User-Agent": "Antigravity-Token-Monitor/2026",
        "Accept": "application/vnd.github.v3+json"
    }
    
    if token:
        headers["Authorization"] = f"token {token}"
        print("[INFO] Using authenticated GitHub Token / 使用已驗證之 Token")
    else:
        print("[INFO] No Token found in environment. Testing unauthenticated rate limit / 未發現 Token，測試匿名連線")

    url = "https://api.github.com/rate_limit"
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            core = data.get("resources", {}).get("core", {})
            limit = core.get("limit", 0)
            remaining = core.get("remaining", 0)
            reset_ts = core.get("reset", 0)
            
            print("==================================================")
            print("📊 GitHub Token / API Usage Status (Token 使用量報告)")
            print("==================================================")
            print(f"Total Hourly Quota (總額度):      {limit}")
            print(f"Remaining Quota (剩餘額度):       {remaining}")
            print(f"Used Quota (已使用額度):          {limit - remaining}")
            print(f"Usage Percentage (使用率):        {((limit - remaining)/limit * 100):.2f}%" if limit > 0 else "N/A")
            print("==================================================")
            
            return {
                "limit": limit,
                "remaining": remaining,
                "used": limit - remaining
            }
    except Exception as e:
        print(f"[WARN] Unable to reach GitHub API directly (Offline/Network restricted): {e}")
        print("[INFO] Offline Mode Active / 離線模式生效：使用 SSH Key 與本地鏡像緩存即可，無需耗費 API Token。")
        return None

if __name__ == "__main__":
    check_token_status()
