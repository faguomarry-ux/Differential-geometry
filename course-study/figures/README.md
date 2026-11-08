# 可复用TikZ模块 v1.0

本目录为第1–20章及前言提供63幅命名图。正文保留一图一个 `.tex` 入口；几何实现集中在十八个模块中。统一加载文件是 `dg-diagrams.tex`，图目录为 `catalog.json`，来源说明为 [SOURCES.md](SOURCES.md)。

## 加载与调用

从仓库根目录编译。主书已在 `course-study/config/course-config.tex` 中加载一次：

```tex
\input{course-study/figures/dg-diagrams}
```

正文可保持原有插图方式，图注和标签归正文管理：

```tex
\begin{figure}[htbp]
  \centering
  \input{course-study/figures/tangent-equivalence}
  \caption{两条同速曲线代表同一切向量。}
  \label{fig:my-tangent-example}
\end{figure}
```

也可直接使用命名接口，局部修改参数：

```tex
\DGDiagram[scale=1.1,/dg/polar radius=1.4,/dg/polar angle=30]{polar-tangent}
\DGDiagram[/dg/parabola curvature=1.25]{osculating-parabola}
\DGDiagram{polar-tangent} % 本次恢复默认半径2、角度0
```

每次调用有独立TeX分组，参数、坐标名和局部样式不向下一幅图泄漏。缩放默认只作用于几何坐标，字体保持统一；不建议用 `transform shape` 同时缩小文字。未知图名与重复注册会产生明确的编译错误。

半径、曲率、区间数量的基本合法性和投影点远离北极的条件也会在绘图入口检查；这些检查不代替版面检查。

独立编译的最小文档如下，不需要书籍模板、外部图片、Python库、网络请求、shell-escape或外部化缓存：

```tex
\documentclass[UTF8]{ctexart}
\input{course-study/figures/dg-diagrams}
\begin{document}
\begin{center}
  \DGDiagram{surface-patch}
\end{center}
\end{document}
```

需要XeLaTeX/TeX Live、CTeX、TikZ及AMS数学包。CTeX只负责图中的中文；模块本身自动加载TikZ、AMS及所需库，并为 `\dd` 提供后备定义。迁移到其他项目时保留 `course-study/figures/` 的目录层级，或统一调整该入口文件中十八个模块的相对路径。所有输入路径均为项目根目录相对路径，不包含本机绝对路径。

## 目录与参数

| 模块 | 图名 |
|---|---|
| `modules/topology-analysis.tex` | `subspace-topology`、`compact-cover`、`implicit-graph`、`exterior-area` |
| `modules/curves-surfaces.tex` | `frenet-circle`、`normal-sections`、`osculating-parabola`、`surface-patch` |
| `modules/manifolds-tangent.tex` | `atlas-transition`、`stereographic`、`tangent-equivalence`、`polar-tangent`、`tangent-map`、`bundle-trivialization`、`roadmap`、`flow-box`、`bracket-loop`、`integral-plaques` |
| `modules/tensor-bundles.tex` | `tensor-universal`、`bundle-cocycle`、`mobius-gluing` |
| `modules/forms.tex` | `forms-pullback`、`radial-homotopy`、`angular-obstruction` |
| `modules/integration.tex` | `partition-unity`、`boundary-orientation`、`stokes-halfspace` |
| `modules/cohomology.tex` | `radial-retract`、`mv-connecting`、`sphere-mv-cover` |
| `modules/connections.tex` | `connection-frame-change`、`parallel-transport`、`connection-loop` |
| `modules/riemannian.tex` | `metric-unit-balls`、`metric-transport`、`sectional-trace` |
| `modules/geodesics.tex` | `gauss-radial`、`hopf-rinow-step`、`jacobi-models` |
| `modules/submanifold-geometry.tex` | `submanifold-acceleration`、`adapted-frame-block`、`mean-curvature-balance` |
| `modules/hodge-gauss-bonnet.tex` | `hodge-star-plane`、`hodge-decomposition`、`gauss-bonnet-octant` |
| `modules/lie-groups.tex` | `lie-left-flow`、`quotient-slice`、`symmetric-reflection` |
| `modules/principal-bundles.tex` | `associated-coordinates`、`principal-horizontal`、`hopf-potentials` |
| `modules/complex-kahler.tex` | `complex-types`、`projective-potentials`、`complex-conditions` |
| `modules/characteristic-classes.tex` | `characteristic-descent`、`connection-transgression`、`characteristic-limits` |
| `modules/spin-calibrations.tex` | `spin-half-angle`、`spin-transition-sign`、`calibration-phase` |

| 参数 | 默认值 | 含义与使用条件 | 图册验证值 |
|---|---|---|---|
| `/dg/circle radius` | `1.65` | Frenet圆半径，正数；箭头表示标架方向 | `1.2` |
| `/dg/polar radius` | `2` | 所画点的极径，正数；角向坐标向量长度随之变化 | `1.4` |
| `/dg/polar angle` | `0` | 所画点的角度，单位为PGF绘图度数 | `30` |
| `/dg/stereo angle` | `36.8699` | 单位圆上投影点的极角，单位为度；选第一象限且远离北极以保持版面有限 | `20` |
| `/dg/parabola curvature` | `1` | 抛物线在原点的正曲率，自动计算圆心高度和半径 `1/κ` | `1.25` |
| `/dg/compact intervals` | `3` | 有限子覆盖的区间数量，使用正整数；数量过多需另调标签布局 | `4` |

以上是少量有明确几何意义的接口，不是任意曲线的自动排版器。改变数值后，必须同步相应图注并检查标签布局。实际验证覆盖默认值和表中变体；不宣称极端参数也能自动保持版面。正文默认极坐标图取 `r=2, θ=0`，正文默认密切圆图取 `κ=1`。

图册只改变绘图点的角度；数学上的角向坐标导数仍用弧度定义，不能将PGF角度参数误解为重新定义 `∂/∂θ`。

## 样式与基础图元

统一的语义样式包括 `dg/axis`（灰色坐标轴）、`dg/curve`（蓝色主曲线）、`dg/secondary`（橙色辅助对象）、`dg/vector`（切向量）、`dg/normal`（绿色法向/辅助方向）、`dg/guide`（虚线）、`dg/patch`、`dg/grid`、`dg/fiber`、`dg/map` 和 `dg/box`。它们在TikZ名字空间下，不修改全局 `every picture` 或 `every path`；`dg/base` 的节点设置仅在当前绘图分组中生效。

局部覆写示例：

```tex
\DGDiagram[dg/curve/.append style={draw=black},dg/secondary/.append style={dashed}]
  {osculating-parabola}
```

可在新模块中使用两个基础图元：

```tex
\DGAxes{-1}{2}{-1}{2}{$x$}{$y$} % xmin,xmax,ymin,ymax,两个轴标签
\DGPoint[below left]{0,0}{$p$}  % 节点选项、坐标内容、标签
```

`\DGPoint` 的坐标参数也可为已有坐标名。默认点径固定为1.4pt；图元不会自行改变整体坐标比例。等长、正交等几何性质若依赖空间度量，应由解析公式保证，投影示意须在图注说明。

## 新增与维护

1. 在对应 `modules/*.tex` 中用 `\DGDeclareDiagram{new-name}{...}` 注册图体。图体只放路径、坐标、节点、局部scope及局部计算，不再嵌套 `tikzpicture`，不写figure、caption、label或全局字体配置。
2. 新建 `new-name.tex`，默认内容为 `\DGDiagram{new-name}`；将名称、标题、正文归属和来源性质加入 `catalog.json`。
3. 在正文插入入口文件，并写明图形所表达的命题、方向、比例/投影和局部/全局边界。改绘保留原书页码与图号，参考画法登记作者和链接。
4. 构建独立图册与全书，查看新增图和受影响正文页面。新增参数应加入图册变体与隔离断言，避免下一幅图继承上次设置。

## 构建与回归验收

```powershell
python scripts/build-figures.py --check-only
python scripts/build-figures.py
python scripts/check-sources.py
latexmk -r latexmkrc main.tex
```

Python不在PATH时，用主书构建说明中的Python可执行文件路径调用同一脚本。脚本只依赖Python标准库和PATH中的latexmk。

输出为 `build/figures-gallery.pdf`：63个默认图和5个变体，每图一页，A5横向。该图册使用独立CTeX文档，不加载 `maki-notes`，同时验证模块能脱离书籍模板编译。生成的TeX、PDF、日志均在忽略目录 `build/` 下，不作为源文件提交。

脚本检查目录/注册/入口一致性、重复名称及未知名称；编译日志出现LaTeX警告、缺字或Overfull/Underfull时失败；编译末尾检查参数是否泄漏。它不能自动判断标签重叠、图形遮挡或数学意义，仍须实际查看图册和正文PDF。当前验收记录见 [图示模块验收](../../docs/REVIEW-DIAGRAMS.md)。

主书的 `check-sources.py` 已接入图目录校验。PowerShell可用 `scripts/build.ps1 -WithFigureGallery` 一并构建两份PDF；CI也已配置图册构建和双PDF artifact上传，是否在远端成功须另行核查对应提交的运行结果。
