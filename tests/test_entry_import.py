from __future__ import annotations

import main


def test_entry_module_imports() -> None:
    """
    宿主加载入口走 import 链路；SDK 路径漂移（如 ECL.plugin_api 旧路径）必须在本仓库 CI 被拦截。
    """
    assert main.Plugin.__name__ == "Plugin"
