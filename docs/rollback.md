# 异常处理与回滚说明

覆盖条目作废、替换、版本回退，以及台账与文件不一致时的处理流程。

## 1. 条目作废（deprecate）

1. 在主清单台账 `templates/index.manifest.json` 中把该条目的 `status` 由 `active` 改为 `deprecated`，
   并在 `version` 后追加 `-deprecated`（如 `2.0-deprecated`）。
2. 运行 `python scripts/build_ledger.py` 重建 `docs/CATALOG.md` / `catalog.csv`，使台账同步。
3. 文件**不立即删除**，保留一个大版本周期，便于引用回滚；在 `docs/CATALOG.md` 中以「已作废」维度可检索。
4. 若确认永久移除：`git rm templates/<分类>/<文件>` 后提交（保留提交历史可回溯）。

## 2. 条目替换（replace）

1. 新条目沿用原编号，`version` 递增（如 `2.0 → 2.1`），`updated` 改为当天。
2. 覆盖写入同名文件；因为所有模板都是**可重建的纯生成物**，替换等价于重新生成。
3. 重跑 `build_ledger.py` 与 `build_site.py`，提交并在 commit message 注明「替换 SF-0XX」。

## 3. 版本回退（rollback）

模板是纯生成物，任意版本都可还原：

```bash
git checkout <commit> -- templates        # 还原某一版的全部模板
python generator/validate.py templates    # 复核
python scripts/build_ledger.py            # 台账同步
git commit -m "rollback: 回退到 <commit> 的模板集"
```

生成器回退同理：`git revert <commit>` 回退 `generator/` 与产物，然后重跑
`build.py → validate.py → build_ledger.py → build_site.py → build_readme.py`。

### 已实际演练的回退（证据）

- 演练场景：把 `templates/01-teaching-programming-courseware/01__build.pptx` 故意改坏一页后回退。
- 执行：`git checkout HEAD -- templates/01-teaching-programming-courseware/01__build.pptx`
- 结果：文件与 HEAD 一致（`git status` 干净），`validate.py` 复核该套页数与形状数恢复正常。
- 结论：回退流程可执行、可复现。

## 4. 台账与文件不一致

| 不一致类型 | 检测 | 处理 |
|---|---|---|
| 有文件无台账记录 | `validate.py` 文件数 > `index.manifest.json` 条目数 | 运行 `build.py` 重新生成（会重建台账） |
| 有台账无文件 | 打开台账内文件路径报不存在 | 重跑 `build.py`；或将该条目标记 `status=missing` 待修复 |
| 页数与台账不符 | `qa_check.py` 的 `slides_match=✗` | 重新生成该套；复查生成器版本 |
| 编号重复 | 台账 `id` 列出现重复 | 重新生成（编号由 `build.py` 按序生成，天然唯一） |

一致性自检命令：

```bash
python generator/validate.py templates     # 文件侧统计 + 可打开性
python scripts/qa_check.py                 # 抽检 + 台账对照
python scripts/build_ledger.py             # 台账侧统计
```

## 5. 发布异常回滚

- Pages 部署失败：Actions 里重跑最近一次成功 run，或 `git revert` 到上一个绿色提交后 `git push`。
- 误推敏感信息：立即 `git revert` 该提交并 `git push --force-with-lease`（需评估），随后轮换可能泄露的凭据；
  本项目已在推送前执行 `git grep` 排查（见 `docs/handoff-ops.md`）。
