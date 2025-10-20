# History Module API 文檔

**負責人：** 組員 C  
**更新日期：** 2025-10-20

---

## 📋 模組概述

History Module 負責管理交易記錄，包括：
- 記錄交易
- 查詢交易記錄
- 按類型篩選

---

## 📝 接口列表

### 1. log_transaction()

**功能描述：** 記錄一筆交易

**函數簽名：**
```python
def log_transaction(self, account_id: str, transaction_type: str, 
                   amount: float, balance_after: float, 
                   related_account: Optional[str] = None) -> str
```

**輸入參數：**
- `account_id` (str): 帳號 ID
- `transaction_type` (str): 交易類型
- `amount` (float): 交易金額
- `balance_after` (float): 交易後餘額
- `related_account` (str, optional): 關聯帳號（轉帳用）

**回傳值：**
- `str`: 交易 ID（格式：TXN0001）

---

### 2. get_history()

**功能描述：** 查詢帳戶的交易記錄

**[待補充]** 請組員 C 填寫詳細規格

---

### 3. get_history_by_type()

**功能描述：** 查詢特定類型的交易

**[待補充]** 請組員 C 填寫詳細規格

---

## 📊 資料格式

### 交易記錄結構（transactions.json）：
```json
[
  {
    "transaction_id": "TXN0001",
    "account_id": "ACC0001",
    "type": "DEPOSIT",
    "amount": 500.0,
    "balance_after": 1500.0,
    "timestamp": "2025-10-20T12:00:00.123456"
  },
  {
    "transaction_id": "TXN0002",
    "account_id": "ACC0001",
    "type": "TRANSFER_OUT",
    "amount": 300.0,
    "balance_after": 1200.0,
    "related_account": "ACC0002",
    "timestamp": "2025-10-20T12:30:00.654321"
  }
]
```