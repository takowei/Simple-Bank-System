"""
Transaction Module
交易模組 - 處理所有金流操作

[實作 40% / 留白 60%]
負責人：組員 B

職責：
1. 存款
2. 提款
3. 轉帳
4. 呼叫其他模組更新餘額和記錄
"""

from datetime import datetime
from typing import Dict


class TransactionModule:
    """交易模組"""
    
    def __init__(self, account_module, history_module):
        """
        初始化交易模組
        
        [已實作] 由整合者提供
        
        [設計模式說明]
        這裡使用「依賴注入」：
        - 不在這裡 import AccountModule
        - 而是透過參數傳入
        - 好處：方便測試、降低耦合
        
        參數：
            account_module: AccountModule 實例
            history_module: HistoryModule 實例
        """
        self.account = account_module
        self.history = history_module
    
    def deposit(self, account_id: str, amount: float) -> Dict:
        """
        存款功能
        
        [已實作 100%] 完整範例，請參考此實作完成其他函數
        
        輸入：
            account_id (str): 帳號 ID
            amount (float): 存款金額
        
        輸出：
            dict: {
                "success": True,
                "new_balance": 1500.0,
                "transaction_id": "TXN0001"
            }
        
        例外：
            ValueError: 帳戶不存在或金額無效
        
        [設計決策]
        - 存款金額必須 > 0
        - 使用例外處理錯誤情況
        - 成功後記錄到交易歷史
        """
        # Step 1: 驗證金額
        if amount <= 0:
            raise ValueError("存款金額必須大於 0")
        
        # Step 2: 取得帳戶
        account = self.account.get_account(account_id)
        if account is None:
            raise ValueError(f"帳戶不存在: {account_id}")
        
        # Step 3: 計算新餘額
        new_balance = account['balance'] + amount
        
        # Step 4: 更新餘額
        self.account.update_balance(account_id, new_balance)
        
        # Step 5: 記錄交易
        transaction_id = self.history.log_transaction(
            account_id=account_id,
            transaction_type="DEPOSIT",
            amount=amount,
            balance_after=new_balance
        )
        
        # Step 6: 回傳結果
        return {
            "success": True,
            "new_balance": new_balance,
            "transaction_id": transaction_id
        }
    
    def withdraw(self, account_id: str, amount: float) -> Dict:
        """
        提款功能
        
        [已實作 40% / 留白 60%]
        
        輸入：
            account_id (str): 帳號 ID
            amount (float): 提款金額
        
        輸出：
            dict: {
                "success": True,
                "new_balance": 500.0,
                "transaction_id": "TXN0002"
            }
        
        [討論事項]
        1. 與組員A討論：
           - get_account() 如果失敗會回傳什麼？
        
        2. 與組員C討論：
           - log_transaction() 的參數格式？
           - transaction_type 用 "WITHDRAW" 還是 "WITHDRAWAL"？
        
        [實作提示]
        參考 deposit() 的流程，差別在於：
        - 需要多檢查餘額是否足夠
        - 新餘額是減法而非加法
        """
        # [已提供] Step 1: 驗證金額
        if amount <= 0:
            raise ValueError("提款金額必須大於 0")
        
        # [已提供] Step 2: 取得帳戶
        account = self.account.get_account(account_id)
        if account is None:
            raise ValueError(f"帳戶不存在: {account_id}")
        
        # ========== [留白區域 1] 驗證餘額 ==========
        # TODO: 檢查餘額是否足夠（約 2-3 行）
        #
        # [需要檢查]
        # 如果 amount > account['balance']:
        #     應該拋出 ValueError("餘額不足")
        #
        # [進階思考]
        # - 是否要保留最低餘額？
        # - 例如：至少要留 100 元
        
        
        
        # [已提供] Step 3: 計算新餘額
        new_balance = account['balance'] - amount
        
        # [已提供] Step 4: 更新餘額
        self.account.update_balance(account_id, new_balance)
        
        # ========== [留白區域 2] 記錄交易 ==========
        # TODO: 呼叫 history.log_transaction()（約 2-5 行）
        #
        # [需要與組員C確認]
        # 1. 函數名稱：log_transaction 還是 add_transaction？
        # 2. 參數順序：先 account_id 還是先 type？
        # 3. transaction_type 用什麼字串？
        #
        # [參考 deposit() 的寫法]
        # transaction_id = self.history.log_transaction(...)
        
        transaction_id = None  # TODO: 替換這行
        
        # [已提供] Step 5: 回傳結果
        return {
            "success": True,
            "new_balance": new_balance,
            "transaction_id": transaction_id
        }
    
    def transfer(self, from_account_id: str, to_account_id: str, amount: float) -> Dict:
        """
        轉帳功能
        
        [留白 100%] 最複雜的功能，請完整實作
        
        輸入：
            from_account_id (str): 轉出帳號
            to_account_id (str): 轉入帳號
            amount (float): 轉帳金額
        
        輸出：
            dict: {
                "success": True,
                "from_balance": 700.0,
                "to_balance": 800.0,
                "transaction_id": "TXN0003"
            }
        
        [討論事項]
        1. 與團隊討論：
           - 可以轉帳給自己嗎？
           - 轉帳金額上下限？
           - 是否需要手續費？
        
        2. 與組員C討論：
           - 要記錄幾筆交易？（轉出 + 轉入 = 2筆）
           - transaction_type 用什麼？
             * "TRANSFER_OUT" / "TRANSFER_IN"？
             * 還是統一用 "TRANSFER"？
           - 兩筆交易要有關聯嗎？
        
        [實作提示 - 建議步驟]
        
        Step 1: 驗證金額
            if amount <= 0:
                raise ValueError("轉帳金額必須大於 0")
        
        Step 2: 驗證不能轉給自己
            if from_account_id == to_account_id:
                raise ValueError("不能轉帳給自己")
        
        Step 3: 取得兩個帳戶
            from_account = self.account.get_account(from_account_id)
            to_account = self.account.get_account(to_account_id)
            
            if from_account is None:
                raise ValueError("轉出帳戶不存在")
            if to_account is None:
                raise ValueError("轉入帳戶不存在")
        
        Step 4: 檢查轉出帳戶餘額
            if amount > from_account['balance']:
                raise ValueError("餘額不足")
        
        Step 5: 計算新餘額
            from_new_balance = from_account['balance'] - amount
            to_new_balance = to_account['balance'] + amount
        
        Step 6: 更新兩個帳戶
            self.account.update_balance(from_account_id, from_new_balance)
            self.account.update_balance(to_account_id, to_new_balance)
        
        Step 7: 記錄兩筆交易
            txn_out = self.history.log_transaction(
                account_id=from_account_id,
                transaction_type="TRANSFER_OUT",
                amount=amount,
                balance_after=from_new_balance
            )
            
            txn_in = self.history.log_transaction(
                account_id=to_account_id,
                transaction_type="TRANSFER_IN",
                amount=amount,
                balance_after=to_new_balance
            )
        
        Step 8: 回傳結果
            return {
                "success": True,
                "from_balance": from_new_balance,
                "to_balance": to_new_balance,
                "transaction_id": txn_out
            }
        
        [⚠️ 進階挑戰]
        思考：如果第一個 update_balance 成功，但第二個失敗怎麼辦？
        - 目前簡單做法：不處理
        - 未來改進：加入回滾機制
        """
        pass  # TODO: 請實作（預計 30-40行程式碼