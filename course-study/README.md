# 内容目录

全书入口是根目录 `main.tex`，章节统一由 `contents.tex` 接入。`chapters.json` 是目录和进度登记表；`chapters/<编号-主题>/chapter.tex` 放正文；`figures/` 放 TikZ；`appendices/` 放全书约定；`reference/` 放书内参考说明。

不要恢复旧 `modules/` 的重复骨架，也不要添加第二个独立全书入口。新增正文同步更新 `chapters.json`、`COVERAGE.md` 与 `../docs/PROGRESS.md`。框架章节允许存在，但必须保留待写标记。

v0.19续写第18章示性类与Chern–Weil理论，完整记录见[第18章自查与验收](../docs/REVIEW-CHAPTER-18.md)。本轮主书352页，第18章PDF312–330页；独立图册62页，结构/日志/页面及链接验收通过。下一章为第19章Clifford代数与旋量几何。

绘图模块位于 `figures/modules/`，与已废弃的课程内容 `modules/` 不同。统一接口、图目录和独立图册构建说明见 [figures/README](figures/README.md)；只需调用 `\DGDiagram{图名}` 或输入对应图文件，无需在每章重复配置样式。

当前正文初稿推进至第18章，新增Chern–Weil闭性/联络无关性、实示性类/特征、相对传递/局部CS3、射影示性数及怪球检测边界，配8题详解和3图。第19章以后保留明确计划标记；一般整类比较/CGB/签名/怪球完整构造分类未证；NN充分性、一般局部势和2026球面构造完整证明未核验；分类空间与完整holonomy理论未证明。第15章的Lie第三定理、完整BCH/分类及等距群Lie结构仍未证明。第14章曲面剖分存在/拓扑比较及高维整体公式仍保持原范围。逐章自查与依赖边界见[进度总表](../docs/PROGRESS.md)及[第17章](../docs/REVIEW-CHAPTER-17.md)、[第18章自查记录](../docs/REVIEW-CHAPTER-18.md)。
