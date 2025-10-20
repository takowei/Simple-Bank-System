"""
Account Module 測試
負責人：組員 A

測試涵蓋：
- 建立帳戶
- 查詢帳戶
- 更新餘額
- 刪除帳戶
- 帳戶存在性檢查
"""

import os
import shutil
import sys

# 加入父目錄到路徑
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.data_manager import DataManager
from modules.account import AccountModule


def setup_test_env():
    """建立測試環境"""
    test_dir = "test_data_account"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    data_manager = DataManager(data_dir=test_dir)
    account_module = AccountModule(data_manager)
    return account_module, test_dir


def cleanup_test_env(test_dir):
    """清理測試環境"""
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)


# ==================== 測試案例 ====================

def test_create_account():
    """測試：建立帳戶成功"""
    print("測試：建立帳戶...")
    account_module, test_dir = setup_test_env()
    
    # 執行
    account_id = account_module.create_account("張三", 1000.0)
    
    # 驗證
    assert account_id is not None, "❌ 帳號ID不應為空"
    assert account_id.startswith("ACC"), "❌ 帳號格式錯誤"
    
    # 驗證帳戶資料
    account = account_module.get_account(account_id)
    assert account is not None, "❌ 應該能查詢到帳戶"
    assert account["name"] == "張三", "❌ 姓名不符"
    assert account["balance"] == 1000.0, "❌ 餘額不符"
    
    print(f"✅ 測試通過 (帳號: {account_id})")
    cleanup_test_env(test_dir)


def test_create_account_with_empty_name():
    """測試：空名稱應該失敗"""
    print("測試：空名稱建立帳戶...")
    account_module, test_dir = setup_test_env()
    
    try:
        account_module.create_account("", 1000.0)
        assert False, "❌ 應該拋出 ValueError"
    except ValueError as e:
        assert "名稱" in str(e), "❌ 錯誤訊息應提及名稱"
        print("✅ 測試通過（正確拋出例外）")
    
    cleanup_test_env(test_dir)


def test_create_account_with_negative_balance():
    """測試：負數餘額應該失敗"""
    print("測試：負數餘額...")
    account_module, test_dir = setup_test_env()
    
    try:
        account_module.create_account("李四", -100.0)
        assert False, "❌ 應該拋出 ValueError"
    except ValueError as e:
        assert "負數" in str(e) or "餘額" in str(e), "❌ 錯誤訊息應提及負數或餘額"
        print("✅ 測試通過（正確拋出例外）")
    
    cleanup_test_env(test_dir)


def test_get_nonexistent_account():
    """測試：查詢不存在的帳戶"""
    print("測試：查詢不存在的帳戶...")
    account_module, test_dir = setup_test_env()
    
    # 執行
    account = account_module.get_account("ACC9999")
    
    # 驗證
    assert account is None, "❌ 不存在的帳戶應返回 None"
    
    print("✅ 測試通過")
    cleanup_test_env(test_dir)


def test_update_balance():
    """測試：更新餘額"""
    print("測試：更新餘額...")
    account_module, test_dir = setup_test_env()
    
    # 準備
    account_id = account_module.create_account("王五", 500.0)
    
    # 執行
    success = account_module.update_balance(account_id, 1500.0)
    
    # 驗證
    assert success is True, "❌ 更新應該成功"
    account = account_module.get_account(account_id)
    assert account["balance"] == 1500.0, "❌ 餘額未正確更新"
    
    print("✅ 測試通過")
    cleanup_test_env(test_dir)


# ========== [留白] 請組員A補充以下測試 ==========

def test_account_exists():
    """
    [留白] TODO: 請實作此測試
    
    測試目標：
    1. 建立一個帳戶
    2. 使用 account_exists() 檢查應該返回 True
    3. 檢查不存在的帳號應該返回 False
    """
    print("測試：帳戶存在性檢查...")
    # TODO: 請實作
    pass


def test_delete_account():
    """
    [留白] TODO: 請實作此測試
    
    測試目標：
    1. 建立一個帳戶
    2. 刪除該帳戶
    3. 驗證刪除成功
    4. 驗證刪除後無法查詢到
    """
    print("測試：刪除帳戶...")
    # TODO: 請實作
    pass


# ==================== 執行所有測試 ====================

if __name__ == "__main__":
    print("=" * 50)
    print("開始測試 Account Module")
    print("=" * 50)
    print()
    
    # 已提供的測試
    test_create_account()
    test_create_account_with_empty_name()
    test_create_account_with_negative_balance()
    test_get_nonexistent_account()
    test_update_balance()
    
    # 留白的測試（組員補充）
    # test_account_exists()
    # test_delete_account()
    
    print()
    print("=" * 50)
    print("測試完成！")
    print("=" * 50)