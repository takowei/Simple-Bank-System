"""
整合測試
負責人：整合者

測試完整的業務流程
"""

import os
import shutil
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.data_manager import DataManager
from modules.account import AccountModule
from modules.history import HistoryModule
from modules.transaction import TransactionModule


def setup_integration_test():
    """建立整合測試環境"""
    test_dir = "integration_test_data"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    # 初始化所有模組
    dm = DataManager(data_dir=test_dir)
    account_mod = AccountModule(dm)
    history_mod = HistoryModule(dm)
    transaction_mod = TransactionModule(account_mod, history_mod)
    
    return transaction_mod, account_mod, history_mod, test_dir


def cleanup(test_dir):
    """清理測試環境"""
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)


# ==================== 整合測試案例 ====================

def test_complete_workflow():
    """測試：完整業務流程"""
    print("測試：完整業務流程...")
    transaction_mod, account_mod, history_mod, test_dir = setup_integration_test()
    
    # 1. 建立兩個帳戶
    acc1 = account_mod.create_account("用戶A", 1000.0)
    acc2 = account_mod.create_account("用戶B", 500.0)
    print(f"  ✓ 建立帳戶: {acc1}, {acc2}")
    
    # 2. 用戶A 存款 500
    result = transaction_mod.deposit(acc1, 500.0)
    assert result["new_balance"] == 1500.0
    print(f"  ✓ 存款成功，新餘額: {result['new_balance']}")
    
    # 3. 用戶A 轉帳 300 給用戶B
    result = transaction_mod.transfer(acc1, acc2, 300.0)
    assert result["from_balance"] == 1200.0
    assert result["to_balance"] == 800.0
    print(f"  ✓ 轉帳成功")
    
    # 4. 驗證交易記錄
    history_a = history_mod.get_history(acc1)
    history_b = history_mod.get_history(acc2)
    assert len(history_a) >= 2  # 存款 + 轉出
    assert len(history_b) >= 1  # 轉入
    print(f"  ✓ 交易記錄正確")
    
    print("✅ 測試通過")
    cleanup(test_dir)


def test_insufficient_balance_workflow():
    """測試：餘額不足的情境"""
    print("測試：餘額不足情境...")
    transaction_mod, account_mod, _, test_dir = setup_integration_test()
    
    # 1. 建立帳戶，餘額 100
    acc = account_mod.create_account("用戶", 100.0)
    
    # 2. 嘗試提款 200（應失敗）
    try:
        transaction_mod.withdraw(acc, 200.0)
        assert False, "❌ 應該拋出例外"
    except ValueError as e:
        assert "餘額" in str(e)
        print(f"  ✓ 正確處理餘額不足")
    # 3. 驗證帳戶餘額沒有變動
    account = account_mod.get_account(acc)
    assert account["balance"] == 100.0, "❌ 餘額不應改變"
    print(f"  ✓ 餘額未被錯誤修改")
    
    print("✅ 測試通過")
    cleanup(test_dir)


# ==================== 執行所有測試 ====================

if __name__ == "__main__":
    print("=" * 50)
    print("開始整合測試")
    print("=" * 50)
    print()
    
    test_complete_workflow()
    test_insufficient_balance_workflow()
    
    print()
    print("=" * 50)
    print("整合測試完成！")
    print("=" * 50)