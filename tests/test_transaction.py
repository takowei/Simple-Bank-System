"""
Transaction Module 測試
負責人：組員 B

測試涵蓋：
- 存款
- 提款
- 轉帳
- 錯誤處理
"""

import os
import shutil
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.data_manager import DataManager
from modules.account import AccountModule
from modules.history import HistoryModule
from modules.transaction import TransactionModule


def setup_test_env():
    """建立測試環境"""
    test_dir = "test_data_transaction"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    data_manager = DataManager(data_dir=test_dir)
    account_mod = AccountModule(data_manager)
    history_mod = HistoryModule(data_manager)
    transaction_mod = TransactionModule(account_mod, history_mod)
    
    return transaction_mod, account_mod, history_mod, test_dir


def cleanup_test_env(test_dir):
    """清理測試環境"""
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)


# ==================== 測試案例 ====================

def test_deposit():
    """測試：存款成功"""
    print("測試：存款...")
    transaction_mod, account_mod, history_mod, test_dir = setup_test_env()
    
    # 準備：建立帳戶
    account_id = account_mod.create_account("測試用戶", 1000.0)
    
    # 執行：存款 500
    result = transaction_mod.deposit(account_id, 500.0)
    
    # 驗證
    assert result["success"] is True, "❌ 存款應該成功"
    assert result["new_balance"] == 1500.0, "❌ 餘額計算錯誤"
    assert result["transaction_id"].startswith("TXN"), "❌ 交易ID格式錯誤"
    
    # 驗證帳戶餘額
    account = account_mod.get_account(account_id)
    assert account["balance"] == 1500.0, "❌ 帳戶餘額未更新"
    
    # 驗證交易記錄
    history = history_mod.get_history(account_id)
    assert len(history) >= 1, "❌ 應該有交易記錄"
    
    print("✅ 測試通過")
    cleanup_test_env(test_dir)


def test_deposit_invalid_amount():
    """測試：存款負數金額應失敗"""
    print("測試：存款負數金額...")
    transaction_mod, account_mod, _, test_dir = setup_test_env()
    
    account_id = account_mod.create_account("測試用戶", 1000.0)
    
    try:
        transaction_mod.deposit(account_id, -100.0)
        assert False, "❌ 應該拋出 ValueError"
    except ValueError:
        print("✅ 測試通過（正確拋出例外）")
    
    cleanup_test_env(test_dir)


# ========== [留白] 請組員B補充以下測試 ==========

def test_withdraw():
    """
    [留白] TODO: 請實作此測試
    
    測試目標：
    1. 建立帳戶，餘額 1000
    2. 提款 300
    3. 驗證餘額變成 700
    4. 驗證有交易記錄
    """
    print("測試：提款...")
    # TODO: 請實作
    pass


def test_withdraw_insufficient_balance():
    """
    [留白] TODO: 請實作此測試
    
    測試目標：
    1. 建立帳戶，餘額 500
    2. 嘗試提款 1000
    3. 應該拋出 ValueError（餘額不足）
    """
    print("測試：提款餘額不足...")
    # TODO: 請實作
    pass


def test_transfer():
    """
    [留白] TODO: 請實作此測試
    
    測試目標：
    1. 建立兩個帳戶 A(1000) 和 B(500)
    2. 從 A 轉 300 到 B
    3. 驗證 A 餘額變成 700
    4. 驗證 B 餘額變成 800
    5. 驗證兩邊都有交易記錄
    """
    print("測試：轉帳...")
    # TODO: 請實作
    pass


def test_transfer_to_self():
    """
    [留白] TODO: 請實作此測試
    
    測試目標：
    1. 建立帳戶 A
    2. 嘗試從 A 轉帳到 A
    3. 應該失敗（不能轉給自己）
    """
    print("測試：轉帳給自己...")
    # TODO: 請實作
    pass


# ==================== 執行所有測試 ====================

if __name__ == "__main__":
    print("=" * 50)
    print("開始測試 Transaction Module")
    print("=" * 50)
    print()
    
    # 已提供的測試
    test_deposit()
    test_deposit_invalid_amount()
    
    # 留白的測試（組員補充）
    # test_withdraw()
    # test_withdraw_insufficient_balance()
    # test_transfer()
    # test_transfer_to_self()
    
    print()
    print("=" * 50)
    print("測試完成！")
    print("=" * 50)