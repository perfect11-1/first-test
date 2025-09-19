from importlib import util
from pathlib import Path
import sys


def load_logic_module():
    """
    通过文件路径加载 python-learning/the_11_逻辑运算.py，返回已加载的模块对象。
    由于目录名包含短横线，不能用常规 import 语法，只能用 importlib 按路径加载。
    """
    repo_root = Path(__file__).resolve().parents[1]  # 项目根目录
    file_path = repo_root / "python-learning" / "the_11_逻辑运算.py"
    if not file_path.exists():
        raise FileNotFoundError(f"未找到文件：{file_path}")

    spec = util.spec_from_file_location("logic_module", file_path)
    module = util.module_from_spec(spec)
    sys.modules["logic_module"] = module
    spec.loader.exec_module(module)
    return module


def test_walk_when_all_conditions_true(capsys):
    module = load_logic_module()
    # 清理导入时模块底部调用产生的输出
    capsys.readouterr()

    module.how_to_go(distance=2, time_abundant=30, weather_if_good=True)
    out = capsys.readouterr().out.strip()
    assert out == "步行去"


def test_drive_when_distance_too_far(capsys):
    module = load_logic_module()
    capsys.readouterr()

    module.how_to_go(distance=5, time_abundant=30, weather_if_good=True)
    out = capsys.readouterr().out.strip()
    assert out == "开车去"


def test_drive_when_time_not_enough(capsys):
    module = load_logic_module()
    capsys.readouterr()

    # 边界：time_abundant == 20，不满足 > 20
    module.how_to_go(distance=2, time_abundant=20, weather_if_good=True)
    out = capsys.readouterr().out.strip()
    assert out == "开车去"


def test_drive_when_weather_bad(capsys):
    module = load_logic_module()
    capsys.readouterr()

    module.how_to_go(distance=2, time_abundant=30, weather_if_good=False)
    out = capsys.readouterr().out.strip()
    assert out == "开车去"


def test_boundary_distance_equal_3(capsys):
    module = load_logic_module()
    capsys.readouterr()

    # 边界：distance == 3，不满足 < 3
    module.how_to_go(distance=3, time_abundant=30, weather_if_good=True)
    out = capsys.readouterr().out.strip()
    assert out == "开车去"


def test_boundary_time_equal_20(capsys):
    module = load_logic_module()
    capsys.readouterr()

    # 边界：time_abundant == 20，不满足 > 20
    module.how_to_go(distance=2, time_abundant=20, weather_if_good=True)
    out = capsys.readouterr().out.strip()
    assert out == "开车去"
