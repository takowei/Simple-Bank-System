# Transaction Module API 文檔

**負責人：** 組員 B  
**更新日期：** 2025-10-20

---

## 📋 模組概述

Transaction Module 負責處理所有金流操作，包括：
- 存款
- 提款
- 轉帳

---

## 📝 接口列表

### 1. deposit()

**功能描述：** 存款到指定帳戶

**函數簽名：**
```python
def deposit(self, account_id: str, amount: float) -> Dict
```

**輸入參數：**
- `account_id` (str): 帳號 ID
- `amount` (float): 存款金額，必須 > 0

**回傳值：**
```python
{
    "success": True,
    "new_balance": 1500.0,
    "transaction_id": "TXN0001"
}
```

**例外：**
- `ValueError`: 金額無效或帳戶不存在

---

### 2. withdraw()

**功能描述：** 從指定帳戶提款

**[待補充]** 請組員 B 填寫詳細規格

---

### 3. transfer()

**功能描述：** 在兩個帳戶間轉帳

**[待補充]** 請組員 B 填寫詳細規格

---

## 🤝 與其他模組的依賴

### 依賴的模組：
- Account Module: 查詢和更新餘額
- History Module: 記錄交易

### 被依賴的模組：
- Main Controller: 呼叫所有交易函數

---

## ❓ 討論記錄

### 討論 1: 轉帳給自己
- **問題：** 是否允許轉帳給自己？
- **待決議**

### 討論 2: 交易類型常數
- **問題：** 是否要定義常數？
```python
  TRANSACTION_TYPES = {
      "DEPOSIT": "存款",
      "WITHDRAW": "提款",
      "TRANSFER_OUT": "轉出",
      "TRANSFER_IN": "轉入"
  }
```
- **待決議**