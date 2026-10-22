"""支付模块测试用例：等价类划分 + 边界值分析。"""

MIN_AMOUNT = 0.01
MAX_AMOUNT = 50000.0


def validate_amount(amount: float) -> str:
    """被测函数：校验支付金额是否合法。"""
    if amount is None:
        return "金额不能为空"
    if not isinstance(amount, (int, float)):
        return "金额必须为数字"
    if amount < MIN_AMOUNT:
        return "金额低于最小支付限额"
    if amount > MAX_AMOUNT:
        return "金额超过单笔支付上限"
    return "校验通过"


def test_valid_amount():
    assert validate_amount(0.01) == "校验通过"
    assert validate_amount(100.0) == "校验通过"
    assert validate_amount(50000.0) == "校验通过"


def test_boundary_amount():
    assert validate_amount(0.0) == "金额低于最小支付限额"
    assert validate_amount(50000.01) == "金额超过单笔支付上限"


def test_invalid_type():
    assert validate_amount("100") == "金额必须为数字"
    assert validate_amount(None) == "金额不能为空"
