"""
History Module 測試
負責人：組員 C

測試涵蓋：
- 記錄交易
- 查詢交易記錄
- 按類型查詢
- 限制筆數
"""

import os
import shutil
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.data_manager import DataManager
from modules.history import HistoryModule


def setup_test_env():
    """建立測試環境"""
    test_dir = "test_data_history"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    data_manager = DataManager(data_dir=test_dir)
    history_mod = HistoryModule(data_manager)
    return history_mod, test_dir


def cleanup_test_env(test_dir):
    """清理測試環境"""
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)


# ==================== 測試案例 ====================

def test_log_transaction():
    """測試：記錄交易"""
    print("測試：記錄交易...")
    history_mod, test_dir = setup_test_env()
    
    # 執行
    txn_id = history_mod.log_transaction(
        account_id="ACC0001",
        transaction_type="DEPOSIT",
        amount=500.0,
        balance_after=1500.0
    )
    
    # 驗證
    assert txn_id is not None, "❌ 交易ID不應為空"
    assert txn_id.startswith("TXN"), "❌ 交易ID格式錯誤"
    
    print(f"✅ 測試通過 (交易ID: {txn_id})")
    cleanup_test_env(test_dir)


def test_get_history():
    """測試：查詢交易記錄"""
    print("測試：查詢交易記錄...")
    history_mod, test_dir = setup_test_env()
    
    # 準備：記錄3筆交易
    history_mod.log_transaction("ACC0001", "DEPOSIT", 500.0, 1500.0)
    history_mod.log_transaction("ACC0001", "WITHDRAW", 200.0, 1300.0)
    history_mod.log_transaction("ACC0002", "DEPOSIT", 1000.0, 2000.0)
    
    # 執行：查詢 ACC0001 的記錄
    history = history_mod.get_history("ACC0001")
    
    # 驗證
    assert len(history) == 2, f"❌ 應該有2筆記錄，實際: {len(history)}"
    
    print("✅ 測試通過")
    cleanup_test_env(test_dir)


# ========== [留白] 請組員C補充以下測試 ==========

def test_get_history_with_limit():
    """
    [留白] TODO: 請實作此測試
    
    測試目標：
    1. 記錄 5 筆交易到同一個帳戶
    2. 使用 get_history(account_id, limit=3)
    3. 驗證只返回 3 筆
    4. 驗證返回的是最新的 3 筆
    """
    print("測試：限制返回筆數...")
    # TODO: 請實作
    pass


def test_get_history_empty():
    """
    [留白] TODO: 請實作此測試
    
    測試目標：
    1. 查詢一個沒有任何交易的帳戶
    2. 應該返回空列表
    """
    print("測試：查詢空記錄...")
    # TODO: 請實作
    pass


def test_get_history_by_type():
    """
    [留白] TODO: 請實作此測試
    
    測試目標：
    1. 記錄多種類型的交易（DEPOSIT, WITHDRAW等）
    2. 使用 get_history_by_type() 只查詢 DEPOSIT
    3. 驗證返回的都是 DEPOSIT 類型
    """
    print("測試：按類型查詢...")
    # TODO: 請實作
    pass


# ==================== 執行所有測試 ====================

if __name__ == "__main__":
    print("=" * 50)
    print("開始測試 History Module")
    print("=" * 50)
    print()
    
    # 已提供的測試
    test_log_transaction()
    test_get_history()
    
    # 留白的測試（組員補充）
    # test_get_history_with_limit()
    # test_get_history_empty()
    # test_get_history_by_type()
    
    print()
    print("=" * 50)
    print("測試完成！")
    print("=" * 50)