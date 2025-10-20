"""
Account Module
帳戶模組 - 管理帳戶的基本資料

[實作 40% / 留白 60%]
負責人：組員 A

職責：
1. 建立新帳戶
2. 查詢帳戶資訊
3. 更新帳戶餘額
4. 刪除帳戶
"""

from datetime import datetime
from typing import Dict, Optional


class AccountModule:
    """帳戶模組"""
    
    def __init__(self, data_manager):
        """
        初始化帳戶模組
        
        [已實作] 由整合者提供
        
        參數：
            data_manager: DataManager 實例（依賴注入）
        """
        self.data_manager = data_manager
    
    def create_account(self, name: str, initial_balance: float) -> str:
        """
        建立新帳戶
        
        [已實作 100%] 這是完整範例，請參考此寫法完成其他函數
        
        輸入：
            name (str): 帳戶名稱
            initial_balance (float): 初始餘額
        
        輸出：
            str: 帳號 ID (例如: "ACC0001")
        
        例外：
            ValueError: 如果名稱為空或餘額 < 0
        
        [設計決策]
        - 帳號格式：ACC + 4位數字 (ACC0001)
        - 初始餘額必須 >= 0
        - 建立後自動遞增帳號流水號
        """
        # Step 1: 驗證輸入
        if not name or name.strip() == "":
            raise ValueError("帳戶名稱不能為空")
        if initial_balance < 0:
            raise ValueError("初始餘額不能為負數")
        
        # Step 2: 載入現有帳戶
        accounts = self.data_manager.load_accounts()
        
        # Step 3: 生成新帳號 ID
        next_id = self.data_manager.get_next_account_id()
        account_id = f"ACC{next_id:04d}"
        
        # Step 4: 建立帳戶資料
        accounts[account_id] = {
            "name": name.strip(),
            "balance": float(initial_balance),
            "created_date": datetime.now().isoformat()
        }
        
        # Step 5: 儲存回檔案
        self.data_manager.save_accounts(accounts)
        self.data_manager.increment_account_id()
        
        return account_id
    
    def get_account(self, account_id: str) -> Optional[Dict]:
        """
        查詢帳戶資訊
        
        [已實作 100%] 完整範例
        
        輸入：
            account_id (str): 帳號 ID
        
        輸出：
            dict: {
                "name": "張三",
                "balance": 1000.0,
                "created_date": "2025-10-20T10:30:00"
            }
            或 None (如果帳戶不存在)
        
        使用範例：
            account = account_module.get_account("ACC0001")
            if account:
                print(f"餘額: {account['balance']}")
            else:
                print("帳戶不存在")
        """
        accounts = self.data_manager.load_accounts()
        return accounts.get(account_id)
    
    def update_balance(self, account_id: str, new_balance: float) -> bool:
        """
        更新帳戶餘額
        
        [已實作 70% / 留白 30%]
        
        輸入：
            account_id (str): 帳號 ID
            new_balance (float): 新餘額
        
        輸出：
            bool: True=成功, False=失敗
        
        [討論事項]
        1. 與團隊討論：
           Q: 餘額可以是負數嗎？（透支功能）
           A: 目前設計不允許，但可以討論是否開放
        
        2. 與組員C討論：
           Q: 更新餘額時是否要記錄到交易歷史？
           A: 不用，因為交易由 Transaction Module 處理
        
        [實作提示]
        - 參考 create_account() 的流程
        - 需要先檢查帳戶是否存在
        - 需要驗證 new_balance 是否合理
        """
        # [已提供] 載入帳戶
        accounts = self.data_manager.load_accounts()
        
        # [已提供] 檢查帳戶存在
        if account_id not in accounts:
            return False
        
        # ========== [留白區域] 驗證新餘額 ==========
        # TODO: 請實作餘額驗證（約 2-3 行）
        #
        # [需要考慮]
        # 1. new_balance 可以是負數嗎？
        #    - 目前團隊決議：不允許負數
        #    - 如果要改變，請在 Week 1 討論會議提出
        #
        # 2. 是否有最大餘額限制？
        #    - 例如：不能超過 1,000,000
        #    - 這個可以作為進階功能
        #
        # [參考實作]
        # if new_balance < 0:
        #     return False
        
        
        
        # [已提供] 更新餘額
        accounts[account_id]["balance"] = float(new_balance)
        
        # [已提供] 儲存
        return self.data_manager.save_accounts(accounts)
    
    def account_exists(self, account_id: str) -> bool:
        """
        檢查帳戶是否存在
        
        [留白 100%] 請自行實作
        
        輸入：
            account_id (str): 帳號 ID
        
        輸出：
            bool: True=存在, False=不存在
        
        [實作提示]
        這是最簡單的函數，只需要：
        1. 載入 accounts
        2. 檢查 account_id 是否在 accounts 裡
        3. 回傳 True 或 False
        
        [參考]
        - 可以用 `account_id in accounts`
        - 或用 `accounts.get(account_id) is not None`
        
        預計 3-5 行即可完成
        """
        pass  # TODO: 請實作
    
    def delete_account(self, account_id: str) -> bool:
        """
        刪除帳戶
        
        [留白 100%] 請自行實作
        
        輸入：
            account_id (str): 帳號 ID
        
        輸出：
            bool: True=成功, False=失敗
        
        [討論事項]
        1. 與團隊討論：
           Q: 如果帳戶餘額 > 0，可以刪除嗎？
           Q: 刪除後交易記錄要一起刪除嗎？
        
        2. 與組員C討論：
           Q: 是否要記錄「刪除帳戶」這個動作到歷史？
        
        [實作提示]
        Step 1: 載入 accounts
        Step 2: 檢查帳戶是否存在
        Step 3: (選擇性) 檢查餘額是否為 0
        Step 4: 使用 del accounts[account_id] 刪除
        Step 5: 儲存
        
        預計 10-15 行
        """
        pass  # TODO: 請實作