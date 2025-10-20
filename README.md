# 🏦 Simple Bank System

一個模擬銀行帳戶操作的多人協作學習專案

## 📋 專案資訊

- **專案目標：** 學習 Git/GitHub 協作與模組化開發
- **時程：** 3 週
- **團隊：** 4 人（3 開發者 + 1 整合者）
- **學習重點：** 溝通協作（70%）+ Git 操作（30%）

## 🎯 核心功能

- ✅ 建立銀行帳戶
- ✅ 存款
- ✅ 提款
- ✅ 轉帳
- ✅ 查詢帳戶餘額
- ✅ 查詢交易記錄
- ✅ 資料持久化（JSON）

## 👥 團隊分工

| 組員 | 負責模組 | 主要任務 |
|------|---------|---------|
| **組員 A** | Account Module | 帳戶的增刪查改 |
| **組員 B** | Transaction Module | 存款、提款、轉帳邏輯 |
| **組員 C** | History Module | 交易記錄管理 |
| **整合者** | Main + DataManager | 系統整合、資料存取 |

## 🚀 快速開始

### 1. Clone 專案
```bash
git clone <repository-url>
cd simple-bank-system
```

### 2. 切換到自己的分支
```bash
# 組員 A
git checkout feature/account-module

# 組員 B
git checkout feature/transaction-module

# 組員 C
git checkout feature/history-module
```

### 3. 執行測試
```bash
python tests/test_account.py
python main.py
```

## 📅 開發時程

### Week 1: 熟悉 + 設計
- Day 1-2: Kickoff + Git 基礎訓練
- Day 3-5: 接口設計討論
- Day 6-7: Review 討論結果

### Week 2: 開發 + 協作
- Day 1-3: 各自開發基礎功能
- Day 4-5: 第一次整合（PR + Review）
- Day 6-7: 修正問題

### Week 3: 整合 + 測試
- Day 1-3: 整合測試
- Day 4-5: 修正 Bug
- Day 6-7: 最終測試 + 回顧

## 📝 開發規範

### Commit Message 格式
```
feat: 新增功能
fix: 修正錯誤
docs: 更新文檔
test: 新增測試
refactor: 重構程式碼
```

### 程式碼風格
- 使用 4 空格縮排
- 函數名稱使用 snake_case
- 類別名稱使用 PascalCase
- 每個函數都要有 docstring

## ✅ 完成標準

### 個人
- [ ] 實作所有分配的函數
- [ ] 單元測試覆蓋率 > 80%
- [ ] 填寫接口設計討論表
- [ ] 至少 5 次有意義的 commit
- [ ] 參與至少 2 次 Code Review

### 團隊
- [ ] 所有核心功能正常運作
- [ ] 整合測試通過
- [ ] 資料持久化正常
- [ ] 所有 PR 都經過 Review

## 🎓 學習目標

完成此專案後，你將學會：

✅ Git 分支管理與 PR 流程  
✅ 模組化程式設計  
✅ 接口設計與團隊溝通  
✅ Code Review 技巧  
✅ 衝突解決方法  
✅ 協作開發流程  

**不要怕犯錯，錯誤是最好的老師！** 💪
```
