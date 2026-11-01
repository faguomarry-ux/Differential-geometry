# 现代微分几何与广义相对论

使用 LaTeX 编写的中文学习整理工程，入口为 [`main.tex`](main.tex)，内容集中在 [`course-study/`](course-study/)。目标是用统一符号、完整证明、可复现的 TikZ 图及配套习题串起现代微分几何与广义相对论。

**当前为 v0.14 子流形几何与活动标架初稿，不是完整教材。** 已建立五部分、23章及两个附录的写作目录。第一部分（第1–2章）已写入拓扑、欧氏分析、对偶与外代数预备，以及曲线曲面、Frenet标架、基本形式、形算子和Gauss内蕴曲率的正文与证明；第1章保留梁书16题并新增6道原创补充题，第2章配8道原创题，均有解答及来源说明。第3章已有流形基础及6题解答；第4章现已补入曲线与导子模型、坐标变换、切映射与拉回、切丛及余切丛的正文证明和8题解答。第5章已补入子流形与正则值、ODE局部理论、极大局部流与流盒、李括号与流交换、Frobenius局部坐标证明及8道习题解答。第6章已补入张量积泛性质、混合型张量与缩并、外代数及阶乘约定、向量丛拼接及运算、Möbius线丛与常秩子丛证明，配3道梁书改述题和5道原创题及解答。第7章已补入微分形式局部表示、外微分构造与唯一性、拉回自然性、Cartan公式与交换关系、同伦算子及星形域Poincare引理，配8题解答和局部/全局反例。第8章已补入紧耗尽与单位分解、带边流形与外向首位定向、紧支顶次形式积分、换卡及选择无关性、Stokes局部证明与拼接，配8题解答及3幅原创图。第9章已补入de Rham上同调代数、光滑同伦不变性、Mayer–Vietoris连接映射及长正合性、圆周周期和所有球面计算，配8题解答及3幅原创图。第10章已补入一般联络及其换标架、平行移动与测地线初值、挠率与曲率、结构方程和含挠Bianchi、局部平坦性及张量丛诱导联络，配8题解答和3幅原创图。第11章已补入黎曼度量存在、Koszul与Levi–Civita基本定理、等距移动、曲率对称性、截面/Ricci/标量及缩并Bianchi和Schur引理，配8题详解及3幅原创图。第12章已补入指数映射/法坐标、Gauss引理与径向最短性、长度距离与第一变分、Hopf–Rinow完整等价、Jacobi场/共轭点、第二变分及指标引理，配8题详解与3幅原创图。第13章已补入法丛/第二基本形式、Gauss–Weingarten及Gauss–Codazzi–Ricci方程、活动标架与局部欧氏浸入重建、体积第一变分、极小图像及8题详解和3幅图。现有内容已配42个可复用TikZ图（含阅读路线），提供独立图册。第14–23章仍为写作计划。正文尚待独立数学审阅与补充来源逐页核对；第2章曲线重建、全局叶理论及高级分析工具仍待完成。编译成功不代表数学审稿通过。覆盖状态见 [PROGRESS](docs/PROGRESS.md)，下一步见 [TODO](docs/TODO.md)，变更见 [工作记录](docs/WORKLOG.md)。

## 主参考与范围

选用**周建伟《微分几何讲义》**作为中文主参考，按流形、形式、联络、黎曼几何、李群和丛理论展开，并为原书后半部的复几何、示性类、旋量和指标理论保留独立章节。经典曲线曲面作为直觉桥梁；广义相对论作为后续应用。

主参考的结构以[科学出版社目录及试读](https://www.ecsponline.com/goods.php?id=20199)核实。本地 DjVu 尚需解码核对版次。另两书用于交叉核对与相对论补充：“陈省身等著” PDF 实为 Chern、Chen、Lam 的英文书；梁灿彬、周彬 PDF 首页标注上册第二版，后续覆盖范围待核实。具体记录与文件校验值见 [参考书登记](references/README.md)。

三本参考书按原名纳入仓库。使用者已确认上传授权；该确认不代表向访问者授予任意转载许可。

## 目录

| 部分 | 章节 | 主要内容 |
|---|---|---|
| I | 1–2 | 分析、代数、拓扑；曲线曲面 |
| II | 3–9 | 流形、切空间、子流形、张量、形式、积分与上同调 |
| III | 10–14 | 联络、曲率、测地线、子流形几何、Hodge与Gauss–Bonnet |
| IV | 15–20 | 李群、丛、复几何、示性类、旋量、指标与规范场 |
| V | 21–23 | Lorentz几何、Einstein方程、典型时空 |

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

第13章另提供可选的具体模型符号核算；使用含SymPy的Python环境执行 `python scripts/check-submanifold-models.py`。它核对余维二图像、法曲率、螺旋面、Clifford环面及图像变分等恒等式，不能替代一般证明或独立数学审阅；普通构建不依赖SymPy。

## TikZ模块与图册

统一入口为 `course-study/figures/dg-diagrams.tex`，支持 `\DGDiagram[局部选项]{图名}`，正文仍可输入一图一个 `.tex` 文件。42幅默认图的注册信息、参数、语义样式、新增方式及迁移说明见 [绘图模块文档](course-study/figures/README.md)，参考来源见 [图示来源](course-study/figures/SOURCES.md)。

```powershell
python scripts/build-figures.py
# 或一并构建主书与图册
powershell -ExecutionPolicy Bypass -File scripts/build.ps1 -WithFigureGallery
```

图册输出为 `build/figures-gallery.pdf`，包含42幅默认图和5个参数变体，并检查调用间参数隔离。无需书籍模板、外部图片或shell-escape；修改后仍须查看正文页面和图册，不能仅凭编译判断图形正确。

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
