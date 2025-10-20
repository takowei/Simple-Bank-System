# Git 工作流程指南

本文檔說明專案的 Git 協作流程

---

## 🌳 分支策略
```
main (受保護，只能透過 PR 合併)
  ├─ feature/account-module (組員 A)
  ├─ feature/transaction-module (組員 B)
  └─ feature/history-module (組員 C)
```

---

## 📝 基本流程

### 1. Clone 專案
```bash
git clone <repository-url>
cd simple-bank-system
```

### 2. 切換到自己的分支
```bash
# 查看所有分支
git branch -a

# 切換到自己的分支
git checkout feature/account-module
```

### 3. 開發功能
```bash
# 修改程式碼...

# 查看修改狀態
git status

# 加入變更
git add modules/account.py

# 提交
git commit -m "feat: add create_account function"
```

### 4. 推送到遠端
```bash
git push origin feature/account-module
```

### 5. 提交 Pull Request

1. 前往 GitHub Repository
2. 點擊 "New Pull Request"
3. 選擇分支: `feature/account-module` → `main`
4. 填寫 PR 模板
5. 指定 Reviewers
6. 提交

---

## 🔄 同步主分支的更新
```bash
# 切換到 main
git checkout main

# 拉取最新更新
git pull origin main

# 切回自己的分支
git checkout feature/account-module

# 合併 main 的更新
git merge main

# 如果有衝突，解決後：
git add .
git commit -m "merge: sync with main"
git push
```

---

## ⚠️ 解決衝突

### 當遇到衝突時：

1. **不要慌張！** 這是正常的

2. **查看衝突檔案**
```bash
git status
```

3. **打開衝突檔案，會看到：**
```python
<<<<<<< HEAD
你的程式碼
=======
別人的程式碼
>>>>>>> main
```

4. **手動編輯，保留正確的版本**

5. **標記為已解決**
```bash
git add <檔案名稱>
git commit -m "fix: resolve merge conflict"
git push
```

6. **如果不確定，請找整合者或相關組員討論**

---

## 📋 Commit Message 規範

### 格式：
```
<type>: <description>

[optional body]
```

### Type 類型：
- `feat`: 新增功能
- `fix`: 修正錯誤
- `docs`: 更新文檔
- `test`: 新增/修改測試
- `refactor`: 重構程式碼
- `style`: 格式調整（不影響功能）

### 範例：
```bash
git commit -m "feat: add deposit function"
git commit -m "fix: handle negative balance in withdraw"
git commit -m "docs: update API_ACCOUNT.md"
git commit -m "test: add test for transfer function"
```

---

## 🚫 注意事項

### ❌ 不要做的事：

1. **不要直接 push 到 main**
```bash
git push origin main  # ❌ 禁止！
```

2. **不要 force push 到共享分支**
```bash
git push -f  # ❌ 危險！
```

3. **不要提交 test_data/ 目錄**
（已在 .gitignore 中）

### ✅ 建議做的事：

1. **經常 commit**（但每個 commit 要有意義）

2. **經常 pull**（保持同步）

3. **寫清楚的 commit message**

4. **遇到問題立刻溝通**

---

## 🆘 常見問題

### Q: 我不小心 commit 錯了怎麼辦？

A: 使用 reset（只在還沒 push 時）
```bash
git reset HEAD~1  # 撤銷最後一次 commit（保留修改）
```

### Q: 我 push 後發現錯誤怎麼辦？

A: 修正後再 commit 一次
```bash
git add .
git commit -m "fix: correct previous commit"
git push
```

### Q: 我的分支落後 main 很多怎麼辦？

A: 參考「同步主分支的更新」section

---

## 📞 需要幫助？

- 查看此文檔
- 詢問整合者
- 建立 GitHub Issue
- 團隊群組討論