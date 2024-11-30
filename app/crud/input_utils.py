import datetime


def validate_int(prompt: str, max_num: int = 4294967295):
    """入力される値がint型になるかをチェックする関数

    Args:
        prompt (str): inputするときに表示する文字
        max_price(int): 最大の数字の指定。デフォルトは4294967295。データベースに登録するときにINT型の最大整数。

    Returns:
        num(int): int型に変換した返り値
    """
    while True:
        num = input(prompt)

        try:
            num = int(num)

            if num < 0:
                print("[Error!] 無効な整数値です。0以上の整数を入力してください。")
                continue
            if num > max_num:
                print(f"[Error!] 無効な整数値です。{max_num}以下の整数を入力してください。")
                continue
            return num

        except ValueError:
            print("[Error!] 無効な値です。整数を入力してください。")
            continue


def validate_type(prompt: str) -> str:
    """入力される値を収入か支出に変換する関数

    Args:
        prompt (str): inputするときに表示する文字列

    Returns:
        type(str): 変換された収支の文字列。デフォルトは空文字。
    """
    while True:
        str = input(prompt)

        try:
            str = int(str)
            type = ""

            if str != 1 and str != 2:
                print("[Error!] 無効な整数値です。1か2を入力してください。")
                continue
            if str == 1:
                type = "収入"
            elif str == 2:
                type = "支出"
            return type

        except ValueError:
            print("[Error!] 無効な値です。1か2を入力してください。")
            continue


def validate_date(prompt: str, show_check: bool = False) -> datetime.date:
    """入力される値がdatetime.date型になるかをチェックする関数

    Args:
        prompt (str): inputするときに表示する文字
        show_check (bool, optional): 年月のみをチェックしたいときにTrueにしておく。
        デフォルトはFalse。
    """
    while True:
        str = input(prompt)

        try:
            if show_check:
                datetime.datetime.strptime(str, "%Y-%m")
            else:
                datetime.datetime.strptime(str, "%Y-%m-%d")
            return str
        except ValueError:
            print("[Error!] 無効な値です。日付を入力してください [%Y-%m-%d]")
            continue


def validate_len(prompt: str, length: int = 100) -> str:
    """入力される文字列が指定した長さになるかをチェックする関数

    Args:
        prompt (str): inputするときに表示する文字
        length (int): 指定した長さ。デフォルトは100。
    """
    while True:
        str = input(prompt)

        if len(str) > length:
            print(f"[Error!] 無効な文字数です。{length}文字以内で入力してください。")
            continue
        break

    return str


def confirm(prompt: str) -> bool:
    """削除するときに確認する関数

    Args:
        prompt (str): inputするときに表示する文字

    Returns:
        result(bool): yが入力されたらTrue、nが入力されたらFalseを返す。デフォルトはFalse。
    """
    while True:
        str = input(prompt)
        str = str.lower()
        result = False

        if str == "y":
            result = True
        elif str == "n":
            result = False
        else:
            print("[Error!] 無効な値です。yかnを入力してください")
            continue
        return result
