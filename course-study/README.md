# 内容目录

全书入口是根目录 `main.tex`，章节统一由 `contents.tex` 接入。`chapters.json` 是目录和进度登记表；`chapters/<编号-主题>/chapter.tex` 放正文；`figures/` 放 TikZ；`appendices/` 放全书约定；`reference/` 放书内参考说明。

不要恢复旧 `modules/` 的重复骨架，也不要添加第二个独立全书入口。新增正文同步更新 `chapters.json`、`COVERAGE.md` 与 `../docs/PROGRESS.md`。框架章节允许存在，但必须保留待写标记。

v0.17于2026-11-02完成第16章续接本地验收：主书317页，本章PDF272–293页，图册56页；完整记录见[第16章自查与验收](../docs/REVIEW-CHAPTER-16.md)。下一章为第17章复流形与Kahler几何。

绘图模块位于 `figures/modules/`，与已废弃的课程内容 `modules/` 不同。统一接口、图目录和独立图册构建说明见 [figures/README](figures/README.md)；只需调用 `\DGDiagram{图名}` 或输入对应图文件，无需在每章重复配置样式。

当前正文初稿推进至第16章，新增拉回/商丛、标架主丛/相伴丛、主联络与全路径水平提升、曲率与局部平坦、规范变换及Hopf丛计算。第17章以后保留明确计划标记；分类空间、一般示性类及完整holonomy理论未证明。第15章的Lie第三定理、完整BCH/分类及等距群Lie结构仍未证明。第14章曲面剖分存在/拓扑比较及高维整体公式仍保持原范围。逐章自查与依赖边界见 `../docs/REVIEW-CHAPTER-05.md`、`../docs/REVIEW-CHAPTER-06.md`、`../docs/REVIEW-CHAPTER-07.md`、`../docs/REVIEW-CHAPTER-08.md`、`../docs/REVIEW-CHAPTER-09.md`、`../docs/REVIEW-CHAPTER-10.md`、`../docs/REVIEW-CHAPTER-11.md`、`../docs/REVIEW-CHAPTER-12.md`、`../docs/REVIEW-CHAPTER-13.md`、`../docs/REVIEW-CHAPTER-14.md`、`../docs/REVIEW-CHAPTER-15.md`、`../docs/REVIEW-CHAPTER-16.md`。
