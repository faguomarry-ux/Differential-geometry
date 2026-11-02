# 第18章初稿自查与验收

日期：2026-11-02（Asia/Shanghai）；版本：v0.19 示性类与Chern–Weil理论初稿。入口`course-study/chapters/18-characteristic/chapter.tex`，装配invariants、chern、real、transgression、secondary、numbers、exotic、exercises八个正文文件。

本记录区分作者自查、来源核对、具体模型和版面验收，不是独立数学审阅或形式化证明。第1–18章为draft，第19–23章仍为planned。

## 数学主线、约定与依赖边界

| 项目 | 本章自查 |
|---|---|
| 极化与不变性 | 约定P(X,…,X)=p(X)，极化只除一次k!，曲率代入不再重复除。要求全群Ad不变；不连通群不能仅查无穷小条件 |
| 次数与迹 | 曲率为偶次；矩阵值形式使用带次数循环律及带减号的分次交换子，不无符号移动一次形式 |
| Chern–Weil | 水平等变曲率经不变多项式成为basic形式，沿局部截面下降；逐项证明协变微分的联络项抵消，再用Bianchi证明闭性、自然性及乘法 |
| Chern与特征 | c=det(I+iF/(2π))，ch=tr exp(iF/(2π))；证明酉联络给实形式、Whitney、对偶/共轭、行列式及张量公式，不预用分裂原理。不同Hermite度量间通过复联络路径及传递形式实部比较实类 |
| Pontryagin | p_k(V)=(-1)^k c_2k(V_C)，p1=−trΩ²/(8π²)，验证实化p1=c1²−2c2；奇次Chern项由实反对称曲率消失 |
| Euler/Pfaffian | Pfaffian在SO下不变，定向反转变号；用正定平方根把不同度量的正交标架丛对应。证明乘积、p_r=e²及非零截面障碍 |
| 实化定向 | 采用交错实基(u1,iu1,…)，酉对角化的实块为[[0,−λ],[λ,0]]，由Pf=det(iX)得e(E_R)=顶Chern；不混用分块排序的定向 |
| 球面 | 直接代入圆球曲率并计算Pfaffian及体积，得到偶维圆球Euler积分2；由非零截面障碍推毛球结论。稳定平凡推出球面正次Pontryagin类消失，不调用一般CGB |
| 相对传递 | ω_t=ω0+t a，dotΩ_t=D_t a；T=k∫P(a,Ω_t,…)，dT=cw1−cw0。差形式水平，故T全局下降；圆柱曲率含dt∧a |
| 两参数路径 | 固定端点时T_path1−T_path0=−k(k−1)d∫∫P(a,b,Ω^(k−2))；k=1另算。拼接给模恰当可加，不冒充所有代表逐形式相等 |
| 局部CS3 | CS3(A)=tr(A dA+2A³/3)，dCS3=trF²。局部零势的选择不能代替全局相对形式；纯规范CS3=−tr(g⁻¹dg)³/3，SU2给非零例子，整数跳变未证 |
| 平坦反例 | 实Möbius线丛结构群O1的李代数为零，正次Chern–Weil形式消失而丛仍非平凡；不据此断言任意复线丛分类 |
| 射影积分 | x=[ωFS/(2π)]，重言线丛c1=−x；显式径向积分算∫x^m=1。由Hom(L,Q)得到切丛Euler短正合列并取光滑分裂，c(TCPm)=(1+x)^(m+1)，不假设整上同调环已构造 |
| 示性数比较 | CP2的c1²/c2/p1/e为9/3/3/3；CP1×CP1为8/4/0/4。两者即使允许定向反转，p1积分仍不相等。可延拓形式用Stokes给边界消失；切丛Pontryagin可稳定限制，Euler不能类推（S2边界反例） |
| 怪球 | Milnor存在性和相对整拓扑不变量为外引。仅说明七维实偶次类检测的局限，不以类消失推微分同胚；仅有同胚时的de Rham比较亦显式外引 |

依赖链：第7–10、16章形式/曲率/Bianchi → 不变多项式闭形式 → 全局相对传递与联络无关 → 实示性类及性质 → 第8章积分/Stokes和第17章射影FS模型 → 显式示性数。一般整类比较、Euler零点指标/CGB、签名定理、微分特征及怪球完整构造分类均未证明。

## 来源与习题

- Freed《Geometry of Dirac Operators》约1987年初稿，[Harvard托管PDF](https://abel.math.harvard.edu/~dafr/DiracNotes.pdf)，122个物理页。渲染并读取印刷92/PDF94的6.1.13、6.1.15、6.1.16；18.1–18.3分别改述并扩展。来源页的分次交换子号及曲率幂次排印处已校正；其exp(−F)约定未照录，正文统一iF/(2π)归一化。后续扩展不归给原题。
- Meinrenken《Group actions on manifolds》Spring 2003，[Toronto作者讲义](https://www.math.toronto.edu/mein/teaching/LectureNotes/action.pdf)，62页；核对第5节43–48页，定理5.1在44页、命题5.10在47页。按本书右主作用重写，未把讲义的Weil代数或分类空间比较当成本书已证。
- Milnor《On manifolds homeomorphic to the 7-sphere》，Annals of Mathematics 64(2), 399–405 (1956)，[DOI](https://doi.org/10.2307/1969983)及[Rutgers托管原文扫描](https://sites.math.rutgers.edu/~feehan/teaching/math866/milnor7sphere.pdf)。渲染核对印刷399/PDF2的相对配对及定理1：λ=2q−σ模7。整相对上同调、填充、签名和其独立性保持外引；没有逐步核验全文怪球构造。
- 18.4–18.8为原创补充，标准结论不宣称首次发现。8题均配详细解答；映射见`references/EXERCISES.md`。周书本地DjVu及梁书对应题页码仍待核对，不虚构来源编号。

## 具体模型与图示

`scripts/check-characteristic-models.py`的131项精确模型恒等式通过：五维非交换矩阵值形式的Bianchi及非顶次闭性、曲率插值/传递及两参数负号、CS3、规范协变及带次数迹；一般四阶反对称Pfaffian/定向、u2实化及p1/顶Chern；Pauli交换子和三次迹；偶维球面及射影径向积分、CP2及乘积示性数。核算仅验证具体模型，不替代一般证明；普通构建不依赖SymPy。

新增第16组模块`course-study/figures/modules/characteristic-classes.tex`，三幅原创图为`characteristic-descent`、`connection-transgression`、`characteristic-limits`。图注区分闭性/联络无关、局部/全局及示性检测局限。

## 本地构建、页面与链接

- 主书352页，第18章PDF物理页312–330（19页，印刷301–319）；独立图册62页。源码检查通过（23章、201个可达TeX文件，57图、16模块），图目录和参数隔离通过；两份最终日志无警告、缺字、未定义引用或溢出。第18章23个具名目标页码一致，全书333个内部链接有效，131项精确模型核算通过。普通构建不依赖SymPy。
- 渲染并查看本章全部页面及前后衔接、封面/前言/完整目录、附录和参考文献；最终渲染页为[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352]，图册55–57页另行查看。图示方向、定向及适用范围与图注一致。
- 首轮发现两参数传递证明一处长行，将两个推导公式独立成行；下降图的不变多项式标签移到边框上方，避免贴框。示性数图注补明确复定向。修改后重建并复查全部新章页及相关变动页。
- 本章23个具名目标页码一致，报告`tmp/ch18-qa/report.json`的errors为空；第17章24个具名目标在当前PDF也通过复核。4个新增来源URI与PDF注释一致；两章各8题对应8份解答。本章无PlannedSection占位、替换字符或行尾空白，`git diff --check`通过。
- 最终构建日志为忽略目录`tmp/ch18-final-build.log`；整页渲染、联系表及链接报告位于`tmp/ch18-qa/`。上述均为本地验收材料，不作为独立数学审阅。

## Git及保留范围

第17–18章正文、图示、习题、脚本及记录将随本次README与任务清单整理一并提交推送；生成PDF、日志及临时材料继续忽略。远端CI须按实际提交单独核实。独立数学审阅未完成，第19–23章仍为计划，下一章为Clifford代数与旋量几何。
