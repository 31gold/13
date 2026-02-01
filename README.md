# 31Gold Repo 13 - Cyber Time Capsule & Token Usage Monitor / 賽博時光膠囊與 Token 監控

[![GitHub 31gold/13](https://img.shields.io/badge/GitHub-31gold%2F13-181717?style=flat&logo=github)](https://github.com/31gold/13)
[![Time Capsule](https://img.shields.io/badge/Time--Capsule-2031--03--01-brightgreen)](#)

[English] Official repository **13** for user **31gold** showcasing Git history timestamp spoofing, Co-authored-by integration with tech leaders, GitHub Contribution Graph Art ("31"), Cyber Time Capsule workflows, and Offline Office Token Usage Monitoring.

[繁體中文] 本倉庫為 **31gold/13** 官方專案，展示 Git 提交時間偽造、行業大佬聯合署名 (Co-authored-by)、GitHub 貢獻牆點陣藝術 ("31")、賽博時光膠囊機制，以及辦公/離線 Token 使用量監控系統。

---

## 1. Git Timestamp Spoofing / 偽造 Git 提交時間

- **Target Repository / 目標倉庫**: `https://github.com/31gold/13`
- **Target Timestamp / 目標時間**: `1970-01-01 00:00:01`
- **Author Email / 作者郵箱**: `31@A31Z.com`

### Command Block / 命令行控制台
```bash
# 1. First commit with content "1"
echo "1" > index.html
git add index.html
GIT_AUTHOR_DATE="1970-01-01T00:00:01" GIT_COMMITTER_DATE="1970-01-01T00:00:01" git commit -m "First commit"

# 2. Second commit with content "31" & Co-authors
echo "31" > index.html
git add index.html

commit_msg=$(cat << 'EOF'
Update content to 31

Co-authored-by: David Heinemeier Hansson <dhh@hey.com>
Co-authored-by: David Heinemeier Hansson <world@hey.com>
Co-authored-by: David Heinemeier Hansson <david@loudthinking.com>
Co-authored-by: David Heinemeier Hansson <dhh@basecamp.com>
Co-authored-by: David Heinemeier Hansson <dhh@37signals.com>
Co-authored-by: Linus Torvalds <torvalds@linux-foundation.org>
Co-authored-by: Linus Torvalds <torvalds@transmeta.com>
Co-authored-by: Linus Torvalds <torvalds@osdl.org>
EOF
)

GIT_AUTHOR_DATE="1970-01-01T00:00:01" GIT_COMMITTER_DATE="1970-01-01T00:00:01" git commit -m "$commit_msg"
```

---

## 2. Offline Token & Office Token Usage Monitoring / 離線辦公 Token 監控

Run `token_usage_monitor.py` to audit GitHub API rate limits, PAT usage, and token efficiency for office environments:

```bash
python3 token_usage_monitor.py
```

### 2026 Office Token Best Practices / 2026 辦公 Token 規範
- Store PAT tokens securely in `/mnt/data3/configs/` or environment variable `GH_TOKEN`.
- Use SSH keys (`ssh -T git@github.com`) for git operations to achieve zero token consumption for push/pull.
- Leverage local cache (`/mnt/data3/repository/`) to save API calls and bandwidth.

---

## 3. Contribution Graph Art ("31") / 綠色貢獻牆藝術

```bash
python3 generate_31_art.py --dry-run
python3 generate_31_art.py --commits-per-pixel 10
```

---

## 4. Cyber Time Capsule / 賽博時光膠囊 (2031-03-01)

Managed via `.github/workflows/time_capsule.yml`.
