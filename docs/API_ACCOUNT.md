# Account Module API 文檔

**負責人：** 組員 A  
**更新日期：** 2025-10-20

---

## 📋 模組概述

Account Module 負責管理銀行帳戶的基本資料，包括：
- 建立新帳戶
- 查詢帳戶資訊
- 更新帳戶餘額
- 刪除帳戶
- 檢查帳戶是否存在

---

## 📝 接口列表

### 1. create_account()

**功能描述：** 建立新的銀行帳戶

**函數簽名：**
```python
def create_account(self, name: str, initial_balance: float) -> str
```

**輸入參數：**
- `name` (str): 帳戶名稱，不可為空
- `initial_balance` (float): 初始餘額，必須 >= 0

**回傳值：**
- `str`: 帳號 ID（格式：ACC0001）

**例外：**
- `ValueError`: 名稱為空或餘額為負數

**範例：**
```python
account_id = account_module.create_account("張三", 1000.0)
# 回傳: "ACC0001"
```

---

### 2. get_account()

**功能描述：** 查詢帳戶資訊

**函數簽名：**
```python
def get_account(self, account_id: str) -> Optional[Dict]
```

**輸入參數：**
- `account_id` (str): 帳號 ID

**回傳值：**
- `dict`: 帳戶資訊
```python
  {
      "name": "張三",
      "balance": 1000.0,
      "created_date": "2025-10-20T10:30:00"
  }
```
- `None`: 如果帳戶不存在

**範例：**
```python
account = account_module.get_account("ACC0001")
if account:
    print(f"餘額: {account['balance']}")
```

---

### 3. update_balance()

**功能描述：** 更新帳戶餘額

**函數簽名：**
```python
def update_balance(self, account_id: str, new_balance: float) -> bool
```

**輸入參數：**
- `account_id` (str): 帳號 ID
- `new_balance` (float): 新餘額

**回傳值：**
- `bool`: True=成功, False=失敗

**注意事項：**
- 此函數應由 Transaction Module 呼叫
- 不建議直接呼叫

---

### 4. account_exists()

**功能描述：** 檢查帳戶是否存在

**[待實作]** 請組員 A 填寫此部分

---

### 5. delete_account()

**功能描述：** 刪除帳戶

**[待實作]** 請組員 A 填寫此部分

---

## 🤝 與其他模組的依賴

### 依賴的模組：
- DataManager: 用於讀寫帳戶資料

### 被依賴的模組：
- Transaction Module: 呼叫 `get_account()`, `update_balance()`
- Main Controller: 呼叫所有函數

---

## 📊 資料格式

### 帳戶資料結構（accounts.json）：
```json
{
  "ACC0001": {
    "name": "張三",
    "balance": 1000.0,
    "created_date": "2025-10-20T10:30:00.123456"
  },
  "ACC0002": {
    "name": "李四",
    "balance": 2000.0,
    "created_date": "2025-10-20T11:00:00.654321"
  }
}
```

---

## ❓ 討論記錄

### 討論 1: 餘額可以為負數嗎？
- **日期：** 2025-10-XX
- **結論：** 不允許負數餘額
- **原因：** 目前不支援透支功能

### 討論 2: 刪除帳戶時的檢查
- **日期：** 待討論
- **問題：** 如果帳戶餘額 > 0，可以刪除嗎？
- **待決議**

---

## 📝 更新歷史

- 2025-10-20: 初始版本
- 待更新...