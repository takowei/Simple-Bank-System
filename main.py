"""
Simple Bank System - 主程式
命令列介面

[實作 80% / 留白 20%]
負責人：整合者
"""

import sys
from modules.data_manager import DataManager
from modules.account import AccountModule
from modules.history import HistoryModule
from modules.transaction import TransactionModule


class BankSystem:
    """銀行系統主程式"""
    
    def __init__(self):
        """初始化系統"""
        self.data_manager = DataManager()
        self.account_module = AccountModule(self.data_manager)
        self.history_module = HistoryModule(self.data_manager)
        self.transaction_module = TransactionModule(
            self.account_module, 
            self.history_module
        )
    
    def show_menu(self):
        """顯示主選單"""
        print("\n" + "=" * 50)
        print("🏦  Simple Bank System")
        print("=" * 50)
        print("1. 建立帳戶")
        print("2. 查詢帳戶")
        print("3. 存款")
        print("4. 提款")
        print("5. 轉帳")
        print("6. 查詢交易記錄")
        print("7. 系統統計")
        print("0. 離開")
        print("=" * 50)
    
    def create_account_ui(self):
        """建立帳戶 UI"""
        print("\n--- 建立帳戶 ---")
        try:
            name = input("請輸入帳戶名稱: ").strip()
            balance = float(input("請輸入初始餘額: "))
            
            account_id = self.account_module.create_account(name, balance)
            print(f"✅ 帳戶建立成功！")
            print(f"   帳號: {account_id}")
            print(f"   名稱: {name}")
            print(f"   餘額: ${balance:.2f}")
        except ValueError as e:
            print(f"❌ 建立失敗: {e}")
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")
    
    def query_account_ui(self):
        """查詢帳戶 UI"""
        print("\n--- 查詢帳戶 ---")
        account_id = input("請輸入帳號: ").strip()
        
        account = self.account_module.get_account(account_id)
        if account:
            print(f"✅ 帳戶資訊:")
            print(f"   帳號: {account_id}")
            print(f"   名稱: {account['name']}")
            print(f"   餘額: ${account['balance']:.2f}")
            print(f"   建立日期: {account['created_date']}")
        else:
            print(f"❌ 帳戶不存在: {account_id}")
    
    def deposit_ui(self):
        """存款 UI"""
        print("\n--- 存款 ---")
        try:
            account_id = input("請輸入帳號: ").strip()
            amount = float(input("請輸入存款金額: "))
            
            result = self.transaction_module.deposit(account_id, amount)
            print(f"✅ 存款成功！")
            print(f"   交易編號: {result['transaction_id']}")
            print(f"   新餘額: ${result['new_balance']:.2f}")
        except ValueError as e:
            print(f"❌ 存款失敗: {e}")
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")
    
    def withdraw_ui(self):
        """提款 UI"""
        print("\n--- 提款 ---")
        try:
            account_id = input("請輸入帳號: ").strip()
            amount = float(input("請輸入提款金額: "))
            
            result = self.transaction_module.withdraw(account_id, amount)
            print(f"✅ 提款成功！")
            print(f"   交易編號: {result['transaction_id']}")
            print(f"   新餘額: ${result['new_balance']:.2f}")
        except ValueError as e:
            print(f"❌ 提款失敗: {e}")
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")
    
    def transfer_ui(self):
        """轉帳 UI"""
        print("\n--- 轉帳 ---")
        try:
            from_id = input("請輸入轉出帳號: ").strip()
            to_id = input("請輸入轉入帳號: ").strip()
            amount = float(input("請輸入轉帳金額: "))
            
            result = self.transaction_module.transfer(from_id, to_id, amount)
            print(f"✅ 轉帳成功！")
            print(f"   交易編號: {result['transaction_id']}")
            print(f"   {from_id} 餘額: ${result['from_balance']:.2f}")
            print(f"   {to_id} 餘額: ${result['to_balance']:.2f}")
        except ValueError as e:
            print(f"❌ 轉帳失敗: {e}")
        except Exception as e:
            print(f"❌ 發生錯誤: {e}")
    
    def query_history_ui(self):
        """查詢交易記錄 UI"""
        print("\n--- 查詢交易記錄 ---")
        account_id = input("請輸入帳號: ").strip()
        
        try:
            limit_str = input("顯示筆數 (按Enter顯示全部): ").strip()
            limit = int(limit_str) if limit_str else 0
            
            history = self.history_module.get_history(account_id, limit)
            
            if not history:
                print(f"❌ 無交易記錄")
                return
            
            print(f"\n✅ 交易記錄 (共 {len(history)} 筆):")
            print("-" * 80)
            print(f"{'交易編號':<12} {'類型':<15} {'金額':<12} {'餘額':<12} {'時間'}")
            print("-" * 80)
            
            for txn in history:
                print(f"{txn['transaction_id']:<12} "
                      f"{txn['type']:<15} "
                      f"${txn['amount']:<11.2f} "
                      f"${txn['balance_after']:<11.2f} "
                      f"{txn['timestamp'][:19]}")
        except Exception as e:
            print(f"❌ 查詢失敗: {e}")
    
    def show_stats_ui(self):
        """顯示系統統計 UI"""
        print("\n--- 系統統計 ---")
        try:
            stats = self.data_manager.get_stats()
            print(f"帳戶總數: {stats['total_accounts']}")
            print(f"交易總數: {stats['total_transactions']}")
            print(f"總餘額: ${stats['total_balance']:.2f}")
        except Exception as e:
            print(f"❌ 查詢失敗: {e}")
    
    # ========== [留白區域] 請組員協助補充功能 ==========
    
    def list_all_accounts_ui(self):
        """
        [留白] TODO: 列出所有帳戶
        
        功能需求：
        1. 顯示所有帳戶的列表
        2. 包含帳號、名稱、餘額
        3. 以表格形式呈現
        
        討論事項：
        - 需要與組員A討論如何實作 AccountModule.list_all_accounts()
        - 或直接使用 data_manager.load_accounts()
        
        實作提示：
        accounts = self.data_manager.load_accounts()
        for account_id, info in accounts.items():
            print(f"{account_id}  {info['name']}  ${info['balance']}")
        """
        print("\n--- 所有帳戶列表 ---")
        print("⚠️ 此功能尚未實作")
        # TODO: 請實作
    
    def delete_account_ui(self):
        """
        [留白] TODO: 刪除帳戶
        
        功能需求：
        1. 輸入帳號
        2. 確認刪除
        3. 呼叫 account_module.delete_account()
        
        討論事項：
        - 刪除前是否需要二次確認？
        - 如何提示用戶這是危險操作？
        """
        print("\n--- 刪除帳戶 ---")
        print("⚠️ 此功能尚未實作")
        # TODO: 請實作
    
    # =================================================
    
    def run(self):
        """執行主程式"""
        print("\n歡迎使用 Simple Bank System！")
        
        while True:
            self.show_menu()
            choice = input("\n請選擇功能 (0-7): ").strip()
            
            if choice == "1":
                self.create_account_ui()
            elif choice == "2":
                self.query_account_ui()
            elif choice == "3":
                self.deposit_ui()
            elif choice == "4":
                self.withdraw_ui()
            elif choice == "5":
                self.transfer_ui()
            elif choice == "6":
                self.query_history_ui()
            elif choice == "7":
                self.show_stats_ui()
            elif choice == "0":
                print("\n感謝使用！再見！👋")
                break
            else:
                print("❌ 無效的選項，請重新選擇")
            
            input("\n按 Enter 繼續...")


if __name__ == "__main__":
    try:
        system = BankSystem()
        system.run()
    except KeyboardInterrupt:
        print("\n\n程式已中斷")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 系統錯誤: {e}")
        sys.exit(1)