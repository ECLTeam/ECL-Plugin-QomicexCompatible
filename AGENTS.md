# ECL-Plugin-QomicexCompatible 变更规范

本仓库是 EuoraCraft Launcher 的 Qomicex 兼容插件，自主仓库 `external_plugins/qomicex_compatible` 迁出。规则从简，优先参考主仓库 `AGENTS.md` 的精神。

## 强制约定

1. **插件身份不可随意变更**：`plugin.json` 的 `name` 是已安装插件的识别标识，改动会影响权限授权、设置迁移与插件目录名；变更须在 PR 中单独说明理由。
2. **Python 文件**：UTF-8、`from __future__ import annotations`、模块级 docstring、Google 风格 docstring；公共函数须带参数与返回说明。
3. **提交**：使用 `feat:` / `fix:` / `docs:` / `test:` / `chore:` 前缀；提交前运行 `ruff check .`、`ruff format --check .` 与 `python -m pytest --tb=short`。
4. **权限**：只申请 `plugin.json` 中声明的能力，新增能力须说明用途并在 PR 描述中列明。
5. **测试**：行为变更须有对应测试；`tests/` 内的测试不依赖宿主仓库，保持这一点。

## 文件职责

- `main.py` — 插件入口与命令注册
- `transfer.py` — 角色数据的读取、转换与写入
- `plugin.json` — 插件清单
