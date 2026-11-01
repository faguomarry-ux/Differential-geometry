# 第10章初稿自查与验收

日期：2026-11-01（Asia/Shanghai）；版本：v0.11 联络、平行移动与曲率初稿。入口为 `course-study/chapters/10-connections/chapter.tex`，装配 connection、transport、curvature、induced、exercises 五个文件。

以下为写作者的数学自查、来源核查及本地源码/版面/链接验收，不是另一位审阅者的独立数学审阅，也不是形式化验证。

## 数学主线及依赖

| 主线 | 本轮完成与核查重点 |
|---|---|
| 联络 | 一般向量丛上的函数规则、局部性、标架矩阵及换基；坐标系数含二阶换元项，不误作同一张量的坐标分量 |
| 存在与差 | 以从属单位分解拼接局部联络，Leibniz项由权重和1恢复；两联络之差为End(E)值一形式，说明仿射结构 |
| 沿曲线导数 | 按局部标架系数定义并验证换基相容，不依赖沿曲线截面能否延成邻域场；允许自交与驻点 |
| 平行移动 | 线性ODE局部解、Gronwall界和有限端点延拓；紧时间路径有限分块拼接，证明线性、逆向、拼接和重参数化；参数依赖限于有限维光滑族 |
| 测地线 | 二阶坐标方程变成TM上的光滑一阶系统，写出加速度变换式；证明初值/极大解、非零速度及仿射参数条件；不把沿给定路径可移动误认为测地线完备 |
| 挠率与曲率 | 逐项证明函数线性，明确方向和输出槽位；坐标括号为零与非坐标标架的结构系数分开 |
| 结构方程 | Ω=dω+ω∧ω，Θ=dθ+ω∧θ，固定矩阵乘法次序与换基公式；曲率对偶作用负号与本书号差一致 |
| Bianchi | 先独立证明DΘ=Ω∧θ、DΩ=0，再建立诱导张量联络并翻译成含∇T、T(T)、R(T,·)的完整循环式，不暗加无挠 |
| 局部平坦 | R=0时水平提升场交换，以局部交换流构造平行标架；切丛平行标架成为坐标基还需无挠；不预设全局闭路移动为恒等 |
| 诱导联络 | 对偶通过配对、张量积通过平衡关系定义，证明与置换/缩并/外幂相容；写出所有指标的协变导数和曲率作用 |
| 二阶导数 | 区分方向算子的交换子与完整Hessian，有挠时反对称部分为R−∇T；标量Hessian也有挠率修正 |
| 习题 | 8题及8份解答，涵盖非张量偏导、挠率Hessian、基本解矩阵、极坐标、平坦绕圈、矩阵曲率、有挠Bianchi和对偶缩并 |

固定约定：∇∂ᵢ∂ⱼ=Γᵏᵢⱼ∂ₖ，第一个下槽为方向；R(∂ᵢ,∂ⱼ)∂ₖ=Rˡₖᵢⱼ∂ₗ。标架e′=eG、系数s′=G⁻¹s；这与第6章按纤维坐标登记过渡矩阵的方式相容。仿射联络不默认无挠或度规相容，不使用尚待证明的Levi–Civita存在唯一性来构造本章联络。

依赖顺序：第4章局部截断、第5章ODE/局部流及交换流、第6章向量丛与外代数、第7章外微分、第8章单位分解 → 联络及移动 → 挠率/曲率与结构形式Bianchi → 诱导联络 → 张量形式Bianchi。平坦局部标架证明不依赖测地线法坐标或黎曼度量。测地线完备性、指数映射、变分、一般全局holonomy分类及路径同伦不变理论未纳入本轮。

## 来源核查及习题映射

- 查看梁上册第二版3.1–3.4相关扫描页，印刷55–82/PDF71–98；重点放大核对印刷57–59/PDF73–75的联络差与坐标系数，印刷61/PDF77的无挠括号关系，印刷67/PDF83的移动与导数，印刷69/PDF85的测地线参数，印刷77–78/PDF93–94的曲率定义及恒等式。
- 放大核对章末印刷84/PDF100、印刷85/PDF101：10.1改述原题2，10.2改述并扩展原题1(1)(2)，10.3合并原题6和8的分量公式/平行移动同构任务；原题号未另造。其余5题原创，全部解答由本工程重写，新增计算不冒作原书原题。
- 原书定义导数算符时默认无挠，且以余矢量交换导数定义曲率分量；本章显式允许挠率。无挠坐标方向下，原书R_abc^d对应本书−R^d_cab。梁书的度规相容与度规曲率对称性未因浏览而登记为本书已证明。
- 交叉核对Meinrenken, *Riemannian Geometry*, University of Toronto, Spring 2002：[公开讲义](https://www.math.toronto.edu/mein/teaching/LectureNotes/rieall.pdf)，15节页38–42、16节初值范围页43–44、18节页51–53及19节页53–58。重新组织一般联络、换基、存在/差、对偶及张量积；本章另行补写紧时间线性解延拓、含挠Bianchi及局部交换流构造。
- 该讲义18节先以存在平行坐标定义flat，本章明确采用R=0并将平行坐标等价加上无挠。其曲率输入分量排列也与本书不同，按定义比对，不直接抄写数组。
- 具体题号与双页码见 `../references/EXERCISES.md`。周书第3章本地DjVu页码仍待核对，不声称已覆盖梁书第3章全部习题。

## 例子核算与图示

一次性脚本 `tmp/math_ch10.py` 使用精确有理数及整数矩阵，对以下例子作计算核查；它不取代一般证明或独立审阅。

- 在4组有理数边长下验证习题10.6的矩形移动矩阵及行列式1，包含正、负及零边长；非交换乘积的作用次序与−εδ[A,B]的号一致。正文已用A²=B²=0直接相乘给出一般公式。
- 在3个正有理半径上验证极坐标曲率的导数项与矩阵交换子抵消；正文亦逐项手算两个基输入。
- 对习题10.7的常矩阵仿射联络计算第一Bianchi的曲率循环−e₃、协变挠率循环−2e₃及二次挠率循环+e₃，并核对完整第二Bianchi的修正循环为零。常系数张量的协变导数不被误设为零。

新增第8组模块 `figures/modules/connections.tex`，统一入口及局部分组不变；现33个命名图，图册含33默认图及5参数变体，共38页，注册与参数隔离检查通过。

| 图名 | 自查内容 |
|---|---|
| connection-frame-change | 同一基点的系数和协变导数都按G⁻¹变换，D与D′的关系包含非齐次项，不误画成沿曲线移动 |
| parallel-transport | 两条竖线为不同纤维，平行方程给线性同构；图中长度无已选度量含义 |
| connection-loop | 按+x,+y,−x,−y走矩形，总矩阵从右往左作用，返回项的号由方程与方向共同决定 |

三图均原创，无原书图号、未复制网页代码；默认入口、catalog和SOURCES同步，新增图册物理页31–33实际查看。

## 本地构建与页面验收

- `scripts/check-sources.py`通过：23章、118个可达TeX文件，33个命名图、8组模块。该程序仅作结构检查，其输出明确提示 `mathematical correctness not checked.`
- 主书以`latexmk -r latexmkrc main.tex`完成最终构建，共204页；第10章为PDF物理页153–171，即印刷页144–162，共19页。第11章从物理页172开始。
- `scripts/build-figures.py`生成38页独立图册，日志中的`DG-PARAMETER-ISOLATION: PASS`通过。主书和图册最终日志均无Warning、Overfull、Underfull、Missing character及未定义引用。
- 实际渲染并查看主书物理页1–10、152–172、200–204，覆盖本章全部19页及受影响的前言、目录、邻章、附录和参考文献；新增图册页31–33另行查看。修复四段长公式的排版、三个具名目标提前落在前页的问题，以及附录末尾短节的分页。
- `tmp/qa_ch10.py`读取最终PDF、辅助文件和注释，核对本章20个具名目标的实际目标页与排印页；全书222个内部链接均解析到有效页。报告`tmp/ch10-qa/report.json`的`errors`为空；补充讲义的外部URI与登记地址一致。这是目标页与地址核验，不宣称所有外站的持续可用性。
- `git -c core.safecrlf=false diff --check`通过。8个习题均有解答，正文无本章规划占位，新增源码无替换字符或行尾空白。

### 具名目标页码

| 标签 | PDF物理页 | 印刷页 |
|---|---:|---:|
| ch:10-connections | 153 | 144 |
| def:connection；prop:connection-local | 154 | 145 |
| prop:connection-change；thm:connection-affine | 155 | 146 |
| fig:connection-frame-change | 156 | 147 |
| def:derivative-along-curve；thm:parallel-transport | 157 | 148 |
| fig:parallel-transport | 158 | 149 |
| thm:affine-geodesics | 159 | 150 |
| def:torsion-curvature；prop:curvature-tensor | 160 | 151 |
| prop:cartan-structure | 161 | 152 |
| thm:bianchi-forms；thm:flat-parallel-frame | 162 | 153 |
| fig:connection-loop | 163 | 154 |
| thm:induced-connection | 164 | 155 |
| prop:tensor-covariant-derivative；prop:ricci-commutator | 165 | 156 |
| thm:bianchi-tensors | 166 | 157 |

### 复现与发布边界

在工程根目录运行以下命令，可完成结构检查、图册和主书构建（需本机TeX Live及Python）：

```powershell
./scripts/build.ps1 -PythonCommand 'C:/Users/Topmkter/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -WithFigureGallery
git -c core.safecrlf=false diff --check
```

`tmp/math_ch10.py`、`tmp/qa_ch10.py`及渲染图为本轮临时验收材料；数学假设、一般推导和验收结果已保留在正文及本记录中。本轮未修改提供的类文件，未提交或推送新的Git提交，也未核查新的远端CI、构建产物或Release。独立数学审阅仍未完成，第11–23章仍为写作计划。
