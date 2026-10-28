# 内容目录

全书入口是根目录 `main.tex`，章节统一由 `contents.tex` 接入。`chapters.json` 是目录和进度登记表；`chapters/<编号-主题>/chapter.tex` 放正文；`figures/` 放 TikZ；`appendices/` 放全书约定；`reference/` 放书内参考说明。

不要恢复旧 `modules/` 的重复骨架，也不要添加第二个独立全书入口。新增正文同步更新 `chapters.json`、`COVERAGE.md` 与 `../docs/PROGRESS.md`。框架章节允许存在，但必须保留待写标记。
