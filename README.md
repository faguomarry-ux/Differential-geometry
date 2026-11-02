# 现代微分几何与广义相对论

使用 LaTeX 编写的中文学习整理工程，入口为 [`main.tex`](main.tex)，内容集中在 [`course-study/`](course-study/)。目标是用统一符号、完整证明、可复现的 TikZ 图及配套习题串起现代微分几何与广义相对论。

**当前版本：v0.17 主丛与丛联络初稿。** 已建立五部分、23章和两个附录；第1–16章已有正文初稿，第17–23章仍为写作计划。独立数学审阅与部分来源核对尚未完成。

[详细进度](docs/PROGRESS.md) · [完整任务清单](docs/TODO.md) · [内容覆盖](course-study/COVERAGE.md) · [工作记录](docs/WORKLOG.md) · [写作约定](CONTRIBUTING.md)

## 当前验收快照

以下为2026-11-02的本地验收结果；远端构建以对应提交的[GitHub Actions](https://github.com/faguomarry-ux/Differential-geometry/actions/workflows/build.yml)为准。

| 项目 | 当前结果 |
|---|---|
| 正文状态 | 第1–16章初稿；第17–23章待写 |
| 主书 | 317页；第16章为PDF物理页272–293，共22页 |
| 图示 | 51幅默认图（50幅正文图及1幅阅读路线图），14组可复用TikZ模块 |
| 独立图册 | 56页，含51幅默认图及5个参数变体 |
| 源码与构建 | 23章、177个可达TeX文件；主书及图册日志无警告、缺字、未定义引用或溢出 |
| 第16章核查 | 8题详解、3幅原创图、44项具体模型恒等式、44个具名目标页码一致 |
| 全书链接 | 286个内部链接有效；图模块参数隔离检查通过 |

具体验收与证明边界见[第16章自查记录](docs/REVIEW-CHAPTER-16.md)。源码检查、符号核算和编译通过均不代替独立数学审阅，也不表示全书证明已完整。

## 已完成任务

这里的“完成”指对应内容已形成初稿或完成本地验收；各章仍保留独立审阅及来源补核任务。

| 章节或工作 | 已写入内容 | 记录 |
|---|---|---|
| 工程框架 | 唯一入口、五部分23章、两个附录、章节登记、构建脚本和双PDF CI流程 | [章节清单](course-study/chapters.json) |
| 第1–2章 | 拓扑、欧氏分析、对偶与外代数、曲线曲面及Gauss内蕴曲率；第1章梁书16题及6道补充题，第2章8题，均配解答 | [第一部分自查](docs/REVIEW-PART-I.md) |
| 第3–4章 | 光滑流形与映射、切空间曲线/导子模型、切映射、切丛和余切丛；分别配6题和8题解答 | [第4章自查](docs/REVIEW-CHAPTER-04.md) |
| 第5–9章 | 子流形/局部流/Frobenius、张量与向量丛、微分形式、积分与Stokes、de Rham上同调及Mayer–Vietoris；每章8题解答及3幅新图 | [详细进度](docs/PROGRESS.md) |
| 第10–13章 | 一般联络与曲率、Levi–Civita、测地线与Hopf–Rinow/Jacobi、子流形相容方程和极小图像；每章8题详解及3幅新图 | [内容覆盖](course-study/COVERAGE.md) |
| 第14章 | Hodge星/余微分、Sobolev与椭圆工具、Hodge分解/对偶、有限兼容剖分下的曲面Gauss–Bonnet；8题详解及3图 | [自查与依赖边界](docs/REVIEW-CHAPTER-14.md) |
| 第15章 | 李群/指数/伴随/Killing、闭子群与商流形、不变度量和对称空间；8题详解及3图 | [自查与依赖边界](docs/REVIEW-CHAPTER-15.md) |
| 第16章 | 拉回/商丛、主丛/相伴丛、主联络与水平提升、曲率/Bianchi、规范变换和Hopf丛；8题详解及3图，完成续接验收 | [自查与验收](docs/REVIEW-CHAPTER-16.md) |
| 图示与来源登记 | 统一TikZ接口、图册及参数隔离检查；习题逐题区分改述、扩展和原创，图示单独登记来源 | [图示文档](course-study/figures/README.md) · [习题来源](references/EXERCISES.md) |

## 待办与下一步

- [ ] **下一写作章：第17章复流形与Kahler几何。** 补写复结构/全纯坐标、Hermite与Kahler形式、复联络与曲率，明确可积性定理及球面复结构问题的边界，配习题解答和图示。
- [ ] 第18–20章：示性类与Chern–Weil、Clifford/旋量、指标与规范场；逐项列出证明依赖。
- [ ] 第21–23章：核对资料覆盖后，写作Lorentz几何、Einstein方程和典型时空。
- [ ] 补齐已有章节的证明缺口与推广，包括第2章曲线重建、第5章全局叶理论，以及后续全局比较和高级分析工具；具体未证范围按章登记。
- [ ] 解码并核对周书DjVu版次/页码，核对梁书上下册覆盖，继续补齐参考书、习题和图示的逐项来源映射。
- [ ] 对已有初稿进行独立数学审阅，复核定理假设、符号、证明依赖及习题解答；新增或修订内容继续进行页面和链接验收。
- [ ] 正文达到可发布标准后创建教材Release。

逐章未完成项和已完成任务归档见[完整任务清单](docs/TODO.md)。

## 主参考与范围

选用**周建伟《微分几何讲义》**作为中文主参考，按流形、形式、联络、黎曼几何、李群和丛理论展开，并为原书后半部的复几何、示性类、旋量和指标理论保留独立章节。经典曲线曲面作为直觉桥梁；广义相对论作为后续应用。

主参考的结构以[科学出版社目录及试读](https://www.ecsponline.com/goods.php?id=20199)核实。本地 DjVu 尚需解码核对版次。另两书用于交叉核对与相对论补充：“陈省身等著” PDF 实为 Chern、Chen、Lam 的英文书；梁灿彬、周彬 PDF 首页标注上册第二版，后续覆盖范围待核实。具体记录与文件校验值见 [参考书登记](references/README.md)。

三本参考书按原名纳入仓库。使用者已确认上传授权；该确认不代表向访问者授予任意转载许可。

## 目录

| 部分 | 章节 | 主要内容 | 当前状态 |
|---|---|---|---|
| I | 1–2 | 分析、代数、拓扑；曲线曲面 | 初稿 |
| II | 3–9 | 流形、切空间、子流形、张量、形式、积分与上同调 | 初稿 |
| III | 10–14 | 联络、曲率、测地线、子流形几何、Hodge与Gauss–Bonnet | 初稿 |
| IV | 15–20 | 李群、丛、复几何、示性类、旋量、指标与规范场 | 第15–16章初稿；第17–20章待写 |
| V | 21–23 | Lorentz几何、Einstein方程、典型时空 | 待写 |

各章细分节、参考范围和进度由 [`chapters.json`](course-study/chapters.json) 登记；详细映射见 [COVERAGE](course-study/COVERAGE.md)。高阶专题也必须列明证明依赖，不能以专题简介替代完整证明。

## 构建

依赖 Python 3、TeX Live（建议完整安装）、XeLaTeX、latexmk。使用 TeX Live 自带的 Fandol 与 TeX Gyre 字体，无需上传本地 `fonts/`。从仓库根目录执行：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build.ps1
```

跨平台命令：

```sh
python scripts/check-sources.py
latexmk -r latexmkrc main.tex
```

输出 `build/main.pdf`。也可以在根目录对 `main.tex` 直接运行 XeLaTeX 至交叉引用稳定。根目录旧 `main.pdf` 是历史产物，不代表最新构建。GitHub Actions 已配置编译主书和图册并上传双 PDF artifact；是否成功须查看对应提交的运行结果，不以 push 成功代替 CI 成功。当前不自动创建 Release。

若 Python 不在 PATH 中，PowerShell 脚本支持 `-PythonCommand 'Python可执行文件的绝对路径'`。本机验证使用此参数调用已安装的 Python 运行时。

第13–16章另提供可选的具体模型核算。使用含SymPy的Python环境执行相应脚本；普通构建不依赖SymPy。这些核算检查具体例子，不替代一般证明或独立审阅。

| 章节 | 命令 | 本地核算 |
|---|---|---|
| 第13章 | `python scripts/check-submanifold-models.py` | 46项：余维二图像、法曲率、螺旋面、Clifford环面及变分 |
| 第14章 | `python scripts/check-hodge-models.py` | 110项：Hodge星/主符号、Fourier分解、边界号及四维Pfaffian |
| 第15章 | `python scripts/check-lie-group-models.py` | 84项：左右场、指数/伴随/Killing、Koszul曲率及球面反射 |
| 第16章 | `python scripts/check-principal-bundle-models.py` | 44项：规范协变、水平括号、Hopf局部势/曲率周期 |

## TikZ模块与图册

统一入口为 `course-study/figures/dg-diagrams.tex`，支持 `\DGDiagram[局部选项]{图名}`，正文仍可输入一图一个 `.tex` 文件。51幅默认图的注册信息、参数、语义样式、新增方式及迁移说明见 [绘图模块文档](course-study/figures/README.md)，参考来源见 [图示来源](course-study/figures/SOURCES.md)。

```powershell
python scripts/build-figures.py
# 或一并构建主书与图册
powershell -ExecutionPolicy Bypass -File scripts/build.ps1 -WithFigureGallery
```

图册输出为 `build/figures-gallery.pdf`，包含51幅默认图和5个参数变体，并检查调用间参数隔离。无需书籍模板、外部图片或shell-escape；修改后仍须查看正文页面和图册，不能仅凭编译判断图形正确。

## 工程结构

```text
main.tex                       唯一全书入口
maki-notes.cls / .sty           现有书籍排版模板
course-study/config/           元信息、宏及状态提示
course-study/contents.tex       章节装配与分部
course-study/chapters/          一章一目录
course-study/figures/           原创或注明出处的 TikZ 源码
course-study/appendices/        符号与证明依赖
course-study/reference/         书内参考说明
docs/                          写作规范、待办、进度与记录
references/                    原书登记、校验值与授权记录
scripts/                       源码检查和构建
```

旧课程模块和模板展示型 README 已从正式工程移除；本地备份在忽略目录 `tmp/legacy-course-study/` 与 `tmp/legacy-README.md`，不上传。现有字体及历史编译产物保留在本地并忽略。

## 写作与审阅

遵循 [CONTRIBUTING](CONTRIBUTING.md)。每节由动机、定义、精确命题、详细证明、例子与反例、必要插图、习题及解答组成。**习题重点参考梁灿彬、周彬《微分几何入门与广义相对论》**，逐题标明原题号、印刷页和PDF页，并提供证明或求解；来源明细见 [习题来源映射](references/EXERCISES.md)。原书有助于理解的图应重新用 TikZ 绘制并注明出处，难点可增加原创图。所有待写项和外引结果须显式标注，数学审阅、来源核对和编译版面检查分别记录。
