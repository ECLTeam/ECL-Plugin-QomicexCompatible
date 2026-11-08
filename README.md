# ECL-Plugin-QomicexCompatible

EuoraCraft Launcher（ECL）的 Qomicex 兼容插件：读取 Qomicex 模组导出的角色存档，在启动器与游戏存档之间传输角色数据。

本插件自主仓库 `EuoraCraft-Launcher` 的 `external_plugins/qomicex_compatible` 迁出，现为独立仓库。

## 安装

在 EuoraCraft Launcher 的插件页面从发布渠道安装，或手动安装 `.eclplugin` 归档。

## 开发

```bash
# 运行测试
pip install pytest pydantic
python -m pytest --tb=short

# 代码检查（与主仓库同一套规则）
pip install ruff==0.16.10
ruff check .
ruff format --check .
```

目录结构：

- `main.py` — 插件入口，注册命令与事件
- `transfer.py` — 角色数据读取、转换与写入
- `plugin.json` — 插件清单（名称、权限、入口）
- `tests/` — 迁移自主仓库的行为测试

## 规范

插件标识为 `ECL-Plugin-QomicexCompatible`。修改 `plugin.json` 的 `name` 等于改变已安装插件的身份，会影响权限授权与设置迁移，须谨慎评估。代码风格遵循 `pyproject.toml` 中的 Ruff 配置。

## 许可证

GPL-3.0，见 `LICENSE`。
