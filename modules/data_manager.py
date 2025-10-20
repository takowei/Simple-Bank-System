"""
Data Manager Module
資料存取層 - 統一管理所有 JSON 檔案的讀寫操作

[完整實作 100%] 由整合者提供，組員直接使用
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any


class DataManager:
    """資料管理器 - 負責所有資料檔案的讀寫操作"""
    
    def __init__(self, data_dir: str = "data"):
        """初始化 DataManager"""
        self.data_dir = data_dir
        self.accounts_file = os.path.join(data_dir, "accounts.json")
        self.transactions_file = os.path.join(data_dir, "transactions.json")
        self.config_file = os.path.join(data_dir, "config.json")
        
        os.makedirs(data_dir, exist_ok=True)
        self._init_files()
    
    def _init_files(self):
        """初始化所有資料檔案"""
        if not os.path.exists(self.accounts_file):
            self._save_json(self.accounts_file, {})
        if not os.path.exists(self.transactions_file):
            self._save_json(self.transactions_file, [])
        if not os.path.exists(self.config_file):
            self._save_json(self.config_file, {
                "next_account_id": 1,
                "next_transaction_id": 1,
                "created_at": datetime.now().isoformat()
            })
    
    def _load_json(self, filepath: str) -> Any:
        """讀取 JSON 檔案"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"檔案不存在: {filepath}")
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON 格式錯誤: {filepath}")
    
    def _save_json(self, filepath: str, data: Any) -> bool:
        """儲存資料到 JSON 檔案"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"[Error] 儲存失敗: {e}")
            return False
    
    # ==================== 帳戶操作 ====================
    
    def load_accounts(self) -> Dict[str, Dict]:
        """載入所有帳戶資料"""
        return self._load_json(self.accounts_file)
    
    def save_accounts(self, accounts: Dict) -> bool:
        """儲存帳戶資料"""
        return self._save_json(self.accounts_file, accounts)
    
    # ==================== 交易記錄操作 ====================
    
    def load_transactions(self) -> List[Dict]:
        """載入所有交易記錄"""
        return self._load_json(self.transactions_file)
    
    def save_transactions(self, transactions: List) -> bool:
        """儲存交易記錄"""
        return self._save_json(self.transactions_file, transactions)
    
    # ==================== 設定檔操作 ====================
    
    def get_next_account_id(self) -> int:
        """取得下一個帳號 ID"""
        config = self._load_json(self.config_file)
        return config.get("next_account_id", 1)
    
    def increment_account_id(self) -> bool:
        """遞增帳號 ID"""
        config = self._load_json(self.config_file)
        config["next_account_id"] += 1
        return self._save_json(self.config_file, config)
    
    def get_next_transaction_id(self) -> int:
        """取得下一個交易 ID"""
        config = self._load_json(self.config_file)
        return config.get("next_transaction_id", 1)
    
    def increment_transaction_id(self) -> bool:
        """遞增交易 ID"""
        config = self._load_json(self.config_file)
        config["next_transaction_id"] += 1
        return self._save_json(self.config_file, config)
    
    def clear_all_data(self):
        """清空所有資料（測試用）"""
        self._save_json(self.accounts_file, {})
        self._save_json(self.transactions_file, [])
        self._save_json(self.config_file, {
            "next_account_id": 1,
            "next_transaction_id": 1
        })