# 现代微分几何与广义相对论

使用 LaTeX 编写的中文学习整理工程，入口为 [`main.tex`](main.tex)，内容集中在 [`course-study/`](course-study/)。目标是用统一符号、完整证明、可复现的 TikZ 图及配套习题串起现代微分几何与广义相对论。

**当前版本：v0.21 指标与规范场初稿。** 已建立五部分、23章和两个附录；第1–20章已有正文初稿，第21–23章仍为写作计划。独立数学审阅与部分来源核对尚未完成。

[详细进度](docs/PROGRESS.md) · [完整任务清单](docs/TODO.md) · [内容覆盖](course-study/COVERAGE.md) · [工作记录](docs/WORKLOG.md) · [写作约定](CONTRIBUTING.md)

## 当前验收快照

以下为2026-11-09的本地验收结果；远端构建以对应提交的[GitHub Actions](https://github.com/faguomarry-ux/Differential-geometry/actions/workflows/build.yml)为准。

| 项目 | 当前结果 |
|---|---|
| 正文状态 | 第1–20章初稿；第21–23章待写 |
| 任务归档 | 49项已完成、31项待办；按工作记录条目统计，不代表数学内容完成率 |
| 主书 | 387页；第20章为PDF物理页351–367，共17页 |
| 图示 | 63幅默认图（62幅正文图及1幅阅读路线图），18组可复用TikZ模块 |
| 独立图册 | 68页，含63幅默认图及5个参数变体 |
| 源码与构建 | 23章、225个可达TeX文件；主书及图册日志无警告、缺字、未定义引用或溢出 |
| 第20章核查 | 8题详解、3幅原创图；76项模型核算通过，21个具名目标页码一致 |
| 全书链接 | 389个内部链接有效；图模块参数隔离检查通过 |

具体验收与证明边界见[第20章自查记录](docs/REVIEW-CHAPTER-20.md)。源码检查、符号核算和编译通过均不代替独立数学审阅，也不表示全书证明已完整。

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
| 第17章 | 复图册/类型、Hermite/Kahler、FS势、Chern/Ricci、非可积反例及球面边界；8题详解及3图 | [自查与依赖边界](docs/REVIEW-CHAPTER-17.md) |
| 第18章 | 不变曲率多项式、实Chern/Pontryagin/Euler、联络无关性与传递、局部CS3、射影示性数及怪球边界；8题详解及3图 | [自查与依赖边界](docs/REVIEW-CHAPTER-18.md) |
| 第19章 | Clifford/复表示、Spin双覆盖、给定覆盖的符号提升障碍、旋量联络/Dirac及Lichnerowicz平方公式、曲率消失、校准；8题详解及3图 | [自查与依赖边界](docs/REVIEW-CHAPTER-19.md) |
| 第20章 | Dirac型Fredholm/指标稳定、外引AS及条件推论、Yang–Mills变分/四维能量界、ASD规范固定符号、给定Spin-c方程/消失；8题详解及3图 | [自查与依赖边界](docs/REVIEW-CHAPTER-20.md) |
| 图示与来源登记 | 统一TikZ接口、图册及参数隔离检查；习题逐题区分改述、扩展和原创，图示单独登记来源 | [图示文档](course-study/figures/README.md) · [习题来源](references/EXERCISES.md) |

## 待办与下一步

- [ ] **下一写作章：第21章Lorentz几何与因果结构。** 先核对梁书本地上下册覆盖及主题来源，再展开度量号差、因果向量、时间定向与局部模型，配题解及图示。
- [ ] 第22–23章：核对资料覆盖后，写作Einstein方程和典型时空。
- [ ] 补齐已有章节的证明缺口与推广，包括第2章曲线重建、第5章全局叶理论、第19章提升障碍与拓扑w2的比较，第20章AS完整证明、Spin-c拓扑与非线性模空间构造，以及全局比较和非紧算子分析；具体未证范围按章登记。
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
| IV | 15–20 | 李群、丛、复几何、示性类、旋量、指标与规范场 | 第15–20章初稿 |
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

输出 `build/main.pdf`。也可以在根目录对 `main.tex` 直接运行 XeLaTeX 至交叉引用稳定。根目录旧 `main.pdf` 是历史产物，不代表最新构建。

GitHub Actions 会编译主书与图册。在对应提交成功的 `Build book` 运行页面下载 `differential-geometry-book` artifact，即可获取两份PDF。生成PDF不纳入源码提交；远端验收须查看对应提交的运行结果，不以push成功代替CI成功。当前不自动创建Release。

若 Python 不在 PATH 中，PowerShell 脚本支持 `-PythonCommand 'Python可执行文件的绝对路径'`。本机验证使用此参数调用已安装的 Python 运行时。

第13–20章另提供可选的具体模型核算。使用含SymPy的Python环境执行相应脚本；普通构建不依赖SymPy。这些核算检查具体例子，不替代一般证明或独立审阅。

| 章节 | 命令 | 本地核算 |
|---|---|---|
| 第13章 | `python scripts/check-submanifold-models.py` | 46项：余维二图像、法曲率、螺旋面、Clifford环面及变分 |
| 第14章 | `python scripts/check-hodge-models.py` | 110项：Hodge星/主符号、Fourier分解、边界号及四维Pfaffian |
| 第15章 | `python scripts/check-lie-group-models.py` | 84项：左右场、指数/伴随/Killing、Koszul曲率及球面反射 |
| 第16章 | `python scripts/check-principal-bundle-models.py` | 44项：规范协变、水平括号、Hopf局部势/曲率周期 |
| 第17章 | `python scripts/check-complex-kahler-models.py` | 60项：FS/Ricci、Chern协变、实CP1尺度、Hopf势及非可积括号 |
| 第18章 | `python scripts/check-characteristic-models.py` | 131项：五维非交换联络/传递、CS3、Pfaffian/定向、球面及射影归一化 |
| 第19章 | `python scripts/check-spin-models.py` | 174项：Fock/手征、Spin半角/微分、四维曲率缩并、圆球/扭Dirac、环面符号与校准相位 |
| 第20章 | `python scripts/check-index-gauge-models.py` | 76项：ASD符号、非交换曲率变分/能量、A-hat展开、Spin-c/Fock及SW规范尺度 |

## TikZ模块与图册

统一入口为 `course-study/figures/dg-diagrams.tex`，支持 `\DGDiagram[局部选项]{图名}`，正文仍可输入一图一个 `.tex` 文件。63幅默认图的注册信息、参数、语义样式、新增方式及迁移说明见 [绘图模块文档](course-study/figures/README.md)，参考来源见 [图示来源](course-study/figures/SOURCES.md)。

```powershell
python scripts/build-figures.py
# 或一并构建主书与图册
powershell -ExecutionPolicy Bypass -File scripts/build.ps1 -WithFigureGallery
```

图册输出为 `build/figures-gallery.pdf`，包含63幅默认图和5个参数变体，并检查调用间参数隔离。无需书籍模板、外部图片或shell-escape；修改后仍须查看正文页面和图册，不能仅凭编译判断图形正确。

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
