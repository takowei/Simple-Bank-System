"""
History Module
歷史記錄模組 - 管理所有交易記錄

[實作 40% / 留白 60%]
負責人：組員 C

職責：
1. 記錄交易
2. 查詢交易記錄
3. 按類型查詢
"""

from datetime import datetime
from typing import List, Dict, Optional


class HistoryModule:
    """歷史記錄模組"""
    
    def __init__(self, data_manager):
        """
        初始化歷史記錄模組
        
        [已實作] 由整合者提供
        
        參數：
            data_manager: DataManager 實例
        """
        self.data_manager = data_manager
    
    def log_transaction(self, account_id: str, transaction_type: str, 
                       amount: float, balance_after: float, 
                       related_account: Optional[str] = None) -> str:
        """
        記錄交易
        
        [已實作 100%] 完整範例
        
        輸入：
            account_id (str): 帳號 ID
            transaction_type (str): 交易類型 (DEPOSIT, WITHDRAW, TRANSFER_OUT, TRANSFER_IN)
            amount (float): 交易金額
            balance_after (float): 交易後餘額
            related_account (str, optional): 關聯帳號（轉帳時使用）
        
        輸出：
            str: 交易 ID (例如: "TXN0001")
        
        [設計決策]
        - 交易 ID 格式：TXN + 4位數字
        - 記錄時間戳記
        - 轉帳時可記錄對方帳號
        
        使用範例：
            txn_id = history.log_transaction(
                account_id="ACC0001",
                transaction_type="DEPOSIT",
                amount=500.0,
                balance_after=1500.0
            )
        """
        # Step 1: 載入現有交易記錄
        transactions = self.data_manager.load_transactions()
        
        # Step 2: 生成交易 ID
        next_id = self.data_manager.get_next_transaction_id()
        transaction_id = f"TXN{next_id:04d}"
        
        # Step 3: 建立交易記錄
        transaction = {
            "transaction_id": transaction_id,
            "account_id": account_id,
            "type": transaction_type,
            "amount": float(amount),
            "balance_after": float(balance_after),
            "timestamp": datetime.now().isoformat()
        }
        
        # 如果有關聯帳號（轉帳時）
        if related_account:
            transaction["related_account"] = related_account
        
        # Step 4: 加入列表
        transactions.append(transaction)
        
        # Step 5: 儲存
        self.data_manager.save_transactions(transactions)
        self.data_manager.increment_transaction_id()
        
        return transaction_id
    
    def get_history(self, account_id: str, limit: int = 10) -> List[Dict]:
        """
        查詢帳戶的交易記錄
        
        [已實作 60% / 留白 40%]
        
        輸入：
            account_id (str): 帳號 ID
            limit (int): 最多返回幾筆（預設 10）
        
        輸出：
            list: 交易記錄列表（最新的在前）
        
        [討論事項]
        1. 與組員B討論：
           - 需要支援哪些交易類型的篩選？
        
        2. 與團隊討論：
           - 如果 limit=0，是否返回全部？
           - 排序方式：最新在前還是最舊在前？
        
        [實作提示]
        - 需要篩選出屬於該帳戶的交易
        - 需要排序（按時間）
        - 需要限制返回筆數
        """
        # [已提供] 載入所有交易
        transactions = self.data_manager.load_transactions()
        
        # [已提供] 篩選該帳戶的交易
        account_transactions = [
            txn for txn in transactions 
            if txn.get("account_id") == account_id
        ]
        
        # ========== [留白區域 1] 排序 ==========
        # TODO: 按時間排序（約 1-2 行）
        #
        # [需要討論]
        # 1. 最新的在前還是最舊的在前？
        #    建議：最新的在前（使用者通常想看最近的交易）
        #
        # 2. 如何排序？
        #    提示：使用 sorted() 函數
        #    提示：key=lambda x: x['timestamp']
        #    提示：reverse=True 代表降序（新→舊）
        #
        # [參考實作]
        # account_transactions = sorted(
        #     account_transactions,
        #     key=lambda x: x['timestamp'],
        #     reverse=True
        # )
        
        
        
        # ========== [留白區域 2] 限制筆數 ==========
        # TODO: 只返回前 limit 筆（約 1 行）
        #
        # [需要考慮]
        # 1. 如果 limit=0，要返回全部還是空列表？
        #    建議：返回全部
        #
        # 2. 如何切片？
        #    提示：使用列表切片 [:limit]
        #    提示：如果 limit=0，可以特別處理
        #
        # [參考實作]
        # if limit > 0:
        #     account_transactions = account_transactions[:limit]
        
        
        
        return account_transactions
    
    def get_history_by_type(self, account_id: str, transaction_type: str, 
                           limit: int = 10) -> List[Dict]:
        """
        查詢特定類型的交易記錄
        
        [留白 100%] 請自行實作
        
        輸入：
            account_id (str): 帳號 ID
            transaction_type (str): 交易類型 (DEPOSIT, WITHDRAW, TRANSFER_OUT, TRANSFER_IN)
            limit (int): 最多返回幾筆
        
        輸出：
            list: 符合條件的交易記錄
        
        [討論事項]
        1. 與組員B討論：
           - 有哪些交易類型？需要定義常數嗎？
           - 例如：TRANSACTION_TYPES = ["DEPOSIT", "WITHDRAW", ...]
        
        2. 與團隊討論：
           - 如果 transaction_type 不合法，要拋例外還是返回空列表？
        
        [實作提示]
        這個函數可以重用 get_history() 的邏輯：
        
        方法1（簡單但效能較差）：
            # 先取得所有交易
            all_history = self.get_history(account_id, limit=0)
            # 再篩選類型
            filtered = [txn for txn in all_history if txn['type'] == transaction_type]
            # 限制筆數
            return filtered[:limit]
        
        方法2（推薦，效能較好）：
            # 載入所有交易
            transactions = self.data_manager.load_transactions()
            # 一次篩選帳號和類型
            filtered = [
                txn for txn in transactions
                if txn['account_id'] == account_id and txn['type'] == transaction_type
            ]
            # 排序
            # 限制筆數
            # 返回
        
        預計 10-15 行
        """
        pass  # TODO: 請實作
    
    def get_all_transactions(self) -> List[Dict]:
        """
        取得所有交易記錄（管理員功能）
        
        [留白 100%] 選擇性實作
        
        輸出：
            list: 所有交易記錄
        
        [實作提示]
        這是最簡單的函數，只需要：
        1. 載入 transactions
        2. 回傳
        
        預計 2 行
        """
        pass  # TODO: 選擇性實作