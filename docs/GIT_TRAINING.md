# Git 訓練教材 - 三週課程

本文檔提供完整的 Git 訓練內容

---

## 📅 Week 1: Git 基礎操作

### Day 1-2: 基本指令訓練

#### 🎯 學習目標
- 理解 Git 的基本概念
- 熟悉常用指令
- 能夠進行基本的版本控制

#### 📝 訓練內容

##### 1. Git 設定
```bash
# 設定使用者資訊
git config --global user.name "你的名字"
git config --global user.email "your.email@example.com"

# 檢查設定
git config --list
```

##### 2. Clone 專案
```bash
# 複製遠端 repository
git clone <repository-url>

# 進入專案目錄
cd simple-bank-system

# 查看遠端連結
git remote -v
```

##### 3. 查看狀態與歷史
```bash
# 查看目前狀態
git status

# 查看提交歷史
git log

# 查看簡短歷史
git log --oneline

# 查看分支圖
git log --oneline --graph --all
```

##### 4. 基本工作流程
```bash
# 1. 切換到自己的分支
git checkout feature/your-module

# 2. 修改檔案（用編輯器）
vim modules/account.py

# 3. 查看修改內容
git diff

# 4. 加入暫存區
git add modules/account.py

# 或加入所有修改
git add .

# 5. 提交
git commit -m "feat: add create_account function"

# 6. 推送到遠端
git push origin feature/your-module
```

#### 🏋️ 練習任務

**練習 1：基本流程**
1. Clone 專案
2. 切換到你的分支
3. 修改 README.md，加入你的名字
4. 提交並推送

**練習 2：多次提交**
1. 建立一個新檔案 `test.txt`
2. 寫入一些內容，提交
3. 修改內容，再次提交
4. 查看提交歷史

#### ✅ 檢查點

- [ ] 能夠 clone 專案
- [ ] 能夠查看狀態和歷史
- [ ] 能夠 add, commit, push
- [ ] 理解暫存區的概念

---

### Day 3-5: 分支操作

#### 🎯 學習目標
- 理解分支的概念
- 能夠建立和切換分支
- 理解如何同步遠端更新

#### 📝 訓練內容

##### 1. 分支基本操作
```bash
# 查看所有分支
git branch -a

# 建立新分支
git branch feature/test

# 切換分支
git checkout feature/test

# 建立並切換（快捷方式）
git checkout -b feature/test

# 刪除分支
git branch -d feature/test
```

##### 2. 同步遠端更新
```bash
# 查看遠端分支
git branch -r

# 拉取遠端更新（不合併）
git fetch origin

# 拉取並合併
git pull origin main

# 完整流程：同步主分支的更新到自己的分支
git checkout main           # 切換到 main
git pull origin main        # 拉取最新更新
git checkout feature/xxx    # 切回自己的分支
git merge main              # 合併 main 的更新
```

##### 3. 查看差異
```bash
# 查看工作區與暫存區的差異
git diff

# 查看暫存區與上次提交的差異
git diff --staged

# 查看兩個分支的差異
git diff main feature/your-branch

# 查看特定檔案的差異
git diff modules/account.py
```

#### 🏋️ 練習任務

**練習 3：分支操作**
1. 建立一個測試分支 `test/practice`
2. 在測試分支新增一個檔案
3. 提交後切回原本的分支
4. 觀察檔案不見了（因為在不同分支）
5. 刪除測試分支

**練習 4：同步練習**
1. 整合者會修改 main 分支
2. 你要同步這些更新到你的分支
3. 確認成功合併

#### ✅ 檢查點

- [ ] 能夠建立和切換分支
- [ ] 理解分支的獨立性
- [ ] 能夠同步遠端更新
- [ ] 能夠查看差異

---

## 📅 Week 2: 協作流程

### Day 1-3: Pull Request 流程

#### 🎯 學習目標
- 理解 Pull Request 的流程
- 能夠提交 PR
- 能夠進行 Code Review

#### 📝 訓練內容

##### 1. 提交 Pull Request

**步驟：**

1. **確保程式碼在最新版本上**
```bash
git checkout main
git pull origin main
git checkout feature/your-branch
git merge main
```

2. **推送到遠端**
```bash
git push origin feature/your-branch
```

3. **在 GitHub 上建立 PR**
   - 前往 Repository 頁面
   - 點擊 "Pull requests" 標籤
   - 點擊 "New pull request"
   - 選擇分支：`feature/your-branch` → `main`
   - 填寫 PR 模板
   - 指定 Reviewers
   - 點擊 "Create pull request"

##### 2. Code Review

**作為 Reviewer：**

1. **查看 PR**
   - 進入 PR 頁面
   - 點擊 "Files changed"

2. **留下評論**
   - 在程式碼行號旁點 "+"
   - 寫下評論
   - 選擇 "Add single comment" 或 "Start a review"

3. **完成 Review**
   - 填寫 Review 檢查清單
   - 選擇：
     - ✅ Approve
     - 🔄 Request changes
     - 💬 Comment

**作為 PR 作者：**

1. **回應評論**
   - 看到評論後，回覆說明
   - 或直接修改程式碼

2. **更新 PR**
```bash
# 修改程式碼
vim modules/account.py

# 提交
git add .
git commit -m "fix: address review comments"

# 推送（自動更新 PR）
git push origin feature/your-branch
```

3. **標記為已解決**
   - 在 GitHub 上點 "Resolve conversation"

#### 🏋️ 練習任務

**練習 5：完整 PR 流程**
1. 完成一個小功能（例如：新增一個函數）
2. 提交 PR
3. 指定其他兩位組員為 Reviewers
4. 等待 Review
5. 根據意見修改
6. 等待合併

**練習 6：Review 別人的 PR**
1. 收到 Review 請求後
2. 仔細閱讀程式碼
3. 使用 Code Review 檢查清單
4. 留下至少 2 個有意義的評論
5. 做出 Review 決定

#### ✅ 檢查點

- [ ] 能夠建立 PR
- [ ] 能夠填寫完整的 PR 描述
- [ ] 能夠進行 Code Review
- [ ] 能夠回應 Review 意見
- [ ] 理解 PR 的完整流程

---

### Day 4-7: 衝突處理

#### 🎯 學習目標
- 理解衝突產生的原因
- 能夠解決簡單衝突
- 能夠解決程式碼衝突

#### 📝 訓練內容

##### 1. 理解衝突

**什麼時候會產生衝突？**
- 兩個人修改了同一個檔案的同一行
- 一個人刪除了檔案，另一個人修改了它
- 兩個分支對同一個地方做了不同的修改

**衝突的標記：**
````
<<<<<<< HEAD
你的程式碼
=======
別人的程式碼（或 main 的程式碼）
>>>>>>> main