# 第14章初稿自查与验收

日期：2026-11-01（Asia/Shanghai）；版本：v0.15 Hodge与曲面Gauss–Bonnet初稿。入口`course-study/chapters/14-hodge-gauss-bonnet/chapter.tex`，装配star、analysis、elliptic、hodge、gauss-bonnet、exercises六个文件。

本轮为写作者的数学自查、来源核对及本地源码/版面/链接验收，不是独立数学审阅或形式化证明。Hodge主线给出分析论证；曲面定理明确以给定有限光滑兼容剖分为拓扑先修，高维整体等式仅陈述，不标为已证。

## 数学主线、符号与先修

| 项目 | 本轮逐项核查 |
|---|---|
| 外代数与星 | 递增指标外幂基正交归一；全指标分量保留1/k!；以楔积配对定义星，证明补指标符号、两次星、定向反转和共形缩放 |
| 联络与余微分 | 用Levi–Civita的度量相容及斜对称联络矩阵证明体积/星平行；Stokes推出δ=(-1)^{n(k+1)+1}*d*及能量恒等式 |
| Laplace号 | 非负Δ_H=dδ+δd在函数上为-Δ_g；第11章div grad保持原号；主符号使用∂↦iξ，楔积与插入反对易给正定符号 |
| Hilbert变分 | 中点/平行四边形证明闭子空间投影和Riesz；等价内积证明本章所需的对称强制变分引理；不预引一般Fredholm或谱定理 |
| Sobolev | 以Lebesgue积分、L²完备性为显式先修；Fejer核与平移连续性给Fourier完备，尾部估计证Rellich，Cauchy–Schwarz证嵌入，有限图卡和紧支单位分解拼接 |
| Garding | 冻结d+δ的一阶系数，以主符号控制全部一阶导数，小球吸收误差，零阶截断交换子拼成全局估计 |
| 弱解正则性 | 在局部正交丛标架写标量一致正定主部；测试-D_-h(η²D_hu)，控制系数差商/截断/低阶项，右端只需f∈L²；弱极限给H²，交换子降阶后归纳H^{s+2}及光滑性 |
| 核与可解性 | Rellich排除无限正交核序列；反证法给核外L²估计，合并Garding给H¹强制性；在H¹∩核正交补上解弱方程，再提升光滑 |
| Hodge分解 | 明确smooth形式的L²正交直和，分量唯一但势不唯一；闭形式余恰当分量为零，恰当调和形式必为零，因此每类有唯一代表 |
| 对偶 | 闭/恰当代表的积分由Stokes无关；非零调和h以*h配对得正范数；调和代表和星使用度量，积分配对本身不依赖度量 |
| 域与边界 | 非紧实线上x及dx、有边界区间给反例；未无条件推广到非紧、带边或非定向版本 |
| 曲面局部公式 | a=ω²_1，da=-K vol，kg=θ′+a(T)，正向边界区域在左；用参考三角形的GL⁺矩阵收缩证明角增量2π，不预设任意闭曲线绕数1 |
| 有限角点 | 在卡内截角/光滑化并取极限，将第8章光滑边界Stokes扩到本节二维有限角点；未预引一般角点流形理论 |
| 曲面全局求和 | 内部边kg反向相消，内点角和2π、边界角和β；3F=2E_i+E_b及E_b=V_b给完整边界/转角公式。剖分存在及Euler数与同调交错和比较仍为未证先修 |
| 高维范围 | 推导Pfaffian形式的辅助外代数表达、保向换基不变及四维三项展开；二维号和四维模型核对。Chern–Gauss–Bonnet整体比较没有在本章证明 |

解析依赖链：有限维外代数/第8章Stokes/第11章Levi–Civita → 星/δ/主符号 → Hilbert变分与Sobolev工具 → Garding及H¹弱解正则性 → 有限维核/核外强制性 → Green解/Hodge分解 → de Rham对偶。曲面链由第13章活动标架/曲率号 → 测地曲率/局部转角 → 有限兼容剖分求和；不借用高维Euler类或指标定理反证前面的结论。

原题与自编内容分开登记。环面习题特意用系数全环面平均计算调和投影；未闭的一形式不能从任意代表环路积分直接读出调和分量。二维共形一次形式的内积和星不变，二形式势则需相应缩放。

## 来源核对

- 放大查看梁书5.6印刷121–124/PDF137–140及习题页印刷130–131/PDF146–147。原题11指向两次星与三维grad/curl/div，原题12/13为笛卡儿及球坐标星，原题15为R³无旋/无散势；保留这些原号，正定与Lorentz号明确分开。三组改述扩展题加五题原创，均有解答；详见`references/EXERCISES.md`。
- 读取Donaldson 2020 [官方椭圆讲义](https://www.ma.imperial.ac.uk/~skdona/elliptic%20operators.pdf)2.1–2.2印刷/PDF5–10，核对Sobolev/Rellich及弱解提升；本书用对称变分和差商建立Hodge所需的版本，未采用一般参数子理论。其主符号未包含i因子的约定与本书不同，比较时分别说明。
- 从网页PDF文本核对Etnyre [官方Hodge讲义](https://etnyre.math.gatech.edu/class/8803Fall18/Hodge.pdf)1.1–1.4，重点为定理1.22和后续分析依赖。直接下载失败，未写成已缓存本地PDF；正文仍由本工程按既定符号组织证明。
- 读取Andrews [第20讲](https://maths-people.anu.edu.au/~andrews/DG/DG_chap20.pdf)印刷181–186/独立PDF1–6的联络形式与总曲率；本书采用参考三角片/有限剖分求和，并显式保留拓扑先修。另核对Donaldson 2019 [几何讲义](https://www.ma.imperial.ac.uk/~skdona/differentialgeometrynotes.pdf)第5节印刷/PDF12–14的高维范围，Pfaffian归一化由本书自行固定并核算，不照搬含范数约定差异的四维缩并式。
- 周4.6–4.7本地DjVu页码仍待核对。未声称三部原书逐页校勘完毕，也未以网页讲义替代独立数学审阅。

## 模型核算与原创图

新增可复现`scripts/check-hodge-models.py`（需SymPy），110项精确恒等式全部通过：1–5维对角度量的两次星、楔积/插入的主符号关系、非零Fourier模式的恰当/余恰当投影、共形标量Hodge号和二形式势、从Christoffel独立算出的共形Gauss曲率、从协变加速度独立算出的圆周测地曲率、圆环双边界相消、球面Poisson/极帽/角超，以及四维Pfaffian和保向换基不变。具体模型核算不代替一般证明。

新增第12组模块`figures/modules/hodge-gauss-bonnet.tex`，提供`hodge-star-plane`、`hodge-decomposition`、`gauss-bonnet-octant`三幅图；球面图按参数大圆弧作等比例正投影。总45默认图+5变体，图示来源和调用说明同步。

## 本地源码、版面及链接验收

- `scripts/check-sources.py`通过：23章、155个可达TeX文件，45个命名图、12组模块。该工具仅查结构，明确不检查数学正确性；`git diff --check`通过。
- 完整主书277页；第14章PDF物理页229–249（印刷220–240），共21页。第250页为第四部分分部页，未计入本章。独立图册45默认图+5变体，共50页；注册与`DG-PARAMETER-ISOLATION: PASS`通过。
- 主书及图册最终日志无LaTeX/Package/Class Warning、Overfull、Underfull、缺字、未定义引用或错误。先以`scripts/build.ps1 -PythonCommand <Python路径> -WithFigureGallery`构建全部；两处长式及附录分页修订后以`latexmk -r latexmkrc main.tex`完成重编译。
- 渲染查看主书物理页1–10、228–250、270–277，覆盖本章全部21页及封面/前言/目录/前后边界/附录/参考文献；另查看新增图册43–45页。拆分Pfaffian辅助形式及球面Poisson的行内长式，修复两处溢出；附录A.4预留空间，避免小节标题及短首段拆开。修订后再查看相关整页。
- 最终`tmp/qa_ch14.py`读取PDF、aux及注释；16个具名目标的实际目标页与排印页一致，全书235个内部链接解析到有效页，`tmp/ch14-qa/report.json`的`errors`为空。新增三个官方讲义URI在最终PDF中与来源登记一致。
- 110项模型恒等式通过；本轮未更改供给的maki类或样式文件。README、章节/覆盖、待办/进度、前言/附录、题图来源与自查记录同步。

## GitHub与保留范围

本轮复核上次提交6cadbe259838229e5a4071adb2c5ba2793acdd27的[Build book运行41287472834](https://github.com/faguomarry-ux/Differential-geometry/actions/runs/41287472834)：status=completed、conclusion=success；artifact `differential-geometry-book`（ID13076005776）已生成且复核时未过期。该成功只对应v0.14，不代表本轮第14章改动已通过远端CI。本轮新改动未提交或推送，未创建Release。

独立数学审阅未完成。保留分析先修Lebesgue/L²完备性；一般三角剖分存在、拓扑比较、非紧/边界Hodge、高维整体公式与一般Fredholm/谱理论未在本章证明。第15–23章仍为计划，下一章为李群、李代数与齐性空间。
