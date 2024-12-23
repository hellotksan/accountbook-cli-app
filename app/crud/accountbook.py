import app.crud.accountbook_register as accountbook_register
import app.crud.accountbook_list as accountbook_list
import app.crud.accountbook_update as accountbook_update
import app.crud.accountbook_delete as accountbook_delete
import app.crud.input_utils as input_utils


def print_menu():
    print("1. 帳簿登録")
    print("2. 帳簿⼀覧")
    print("3. 帳簿更新")
    print("4. 帳簿削除")
    print("5. 終了")


def main():
    print("=== 帳簿 メニュー ===")

    print_menu()

    while True:
        no = input_utils.validate_int("メニューを選択してください : ")

        if no == 1:
            accountbook_register.main()
        elif no == 2:
            accountbook_list.main()
        elif no == 3:
            accountbook_update.main()
        elif no == 4:
            accountbook_delete.main()
        elif no == 5:
            print("終了します")
            break
        else:
            print("無効な値です")
            print_menu()


if __name__ == "__main__":
    main()
