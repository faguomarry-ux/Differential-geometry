# 图示来源与参考画法

本目录的几何坐标、曲线方程、标签和模块代码由本工程编写。下列网站用于参考构图及TikZ通用画法；本轮没有复制其完整图形或专用宏。网页的作品许可不能自动扩展为本仓库的许可证。

| 参考 | 作者与页面 | 本工程采用的思路 | 代码关系 |
|---|---|---|---|
| 密切圆 | Efraín Soto Apolinar：[Osculating Circle](https://tikz.net/osculating-circle/) | 曲线、切向量、主法向和密切圆分层标注 | 独立绘制平面抛物线，使用原点曲率显式计算圆心及半径；未使用网页的三维曲线及宏。网页代码注明CC BY-NC-SA 4.0，故不将其代码混入本模块 |
| 坐标和曲面向量 | Izaak Neutelings：[3D coordinate systems](https://tikz.net/axis3d/) | 坐标轴、虚线投影、参数网格及不同语义向量分层 | 使用固定线性斜投影重新绘制抛物面网格；未引入网页的physics、contour及专用命令 |
| 平滑边界的可选画法 | Jake：[Easy curves](https://tikz.net/easy-curves/) | 对无方程边界，可用smooth cycle组织控制点 | 本轮数学曲线优先使用解析参数方程；本页仅为后续模块开发参考，没有移植其图形 |

原有 `subspace-topology` 继续登记为参照梁灿彬、周彬上册第二版图1-4（印刷页7，PDF第23页）的改绘；其来源不能因为模块化而改成原创。原有立体投影、Frenet标架、鞍面法截面、极坐标基及阅读路线图保留原创性质。

本轮新增9幅原创/参考主题后重新构图的示意：`compact-cover`、`implicit-graph`、`exterior-area`、`osculating-parabola`、`surface-patch`、`atlas-transition`、`tangent-equivalence`、`tangent-map`、`bundle-trivialization`。图中条件、比例及局部/全局适用范围分别写在正文图注中。

网站核对日期：2026-10-28。参数变化时应重新检查几何意义；例如极坐标角度以度输入PGF，但正文的角坐标导数仍使用通常弧度定义，绘图角度仅控制所画的点。

## 第5章新增（2026-10-29）

`flow-box`：原创，按 X=∂x+x∂y 的精确流与 (s,z)=(x,y−x²/2) 坐标构造；`bracket-loop`：原创，按 X=∂x、Y=∂y+x∂z 的四段流计算各端点；`integral-plaques`：原创，按 z−xy=c 的解析曲面及其拉直坐标构造。三图均非原书图改绘，未复制新的网页代码，方向、比例和局部含义写入正文图注；沿用既有语义样式与局部调用接口。

## 第6章新增（2026-10-29）

`tensor-universal` 为原创泛性质交换图；`bundle-cocycle` 为原创同一纤维三套坐标的过渡相容图，矩阵次序按实际坐标变换定义；`mobius-gluing` 为原创反号拼接基本域示意，曲线按 a(t)=cos(t/2) 计算，端点及中点值与正文一致。三图无原书图号，没有复制新网页代码；均通过统一注册与局部调用接口提供，实现在新增的 `modules/tensor-bundles.tex` 中。

## 第7章新增（2026-10-30）

`forms-pullback` 为原创自然性交换图；`radial-homotopy` 为原创星形域收缩示意，使用同一比例绘出v与tv；`angular-obstruction` 为原创穿孔平面的闭而不恰当形式示意，圆周箭头为逆时针，原点以空圈标识。无原书图号，没有复制网页代码，实现在新增 `modules/forms.tex` 中，沿用统一注册、语义样式和局部分组接口。

## 第8章新增（2026-11-01）

`partition-unity` 为三角恒等式构造的三个非负权函数示意，和恒为1；不声称图中函数紧支从属于任意开覆盖。`boundary-orientation` 为圆环的原创定向图，外圆逆时针、内圆顺时针，外向横截向量均指向区域外部。`stokes-halfspace` 按二维r≥0模型绘制局部Stokes边界符号。三图无原书图号、未复制网页代码；在 `modules/integration.tex` 中沿用统一注册及局部调用接口。

## 第9章新增（2026-11-01）

`radial-retract` 根据正半径插值公式原创绘制，内外点的轨迹均避开删点。`mv-connecting` 画出提升、微分、限制三个操作，连接映射只定义在上同调类上；不把局部数据任意延拓画成天然映射。`sphere-mv-cover` 为二维球面示意，覆盖成员各删一个极点，交叠删去两极并收缩到赤道；未把闭半球用作开覆盖。三图在 `modules/cohomology.tex` 中沿用统一接口，无原书图号、未复制外部图形或网页代码。

## 第10章新增（2026-11-01）

`connection-frame-change` 为同一截面系数与协变导数的换基交换图，使用e′=eG、s′=G⁻¹s。`parallel-transport` 用两条纤维示意沿曲线的线性同构，几何向量长度没有度量含义。`connection-loop` 按常矩阵模型的四段线性方程画出移动次序，乘积从右向左作用，二阶项为−εδ[A,B]。三图原创，无原书图号，未复制网页代码；实现在 `modules/connections.tex`，沿用统一注册与局部分组接口。

## 第11章新增（2026-11-01）

`metric-unit-balls` 在同一坐标比例绘制I与diag(4,1)的单位圆/椭圆；`metric-transport` 用两套正交归一表示中的单位圆与两向量演示等距移动，未声称端点无关；`sectional-trace` 在投影切空间画包含同一单位方向的两个截面，三维Ricci值为两项之和。三图原创，无原书图号，未复制网页代码；实现位于 `modules/riemannian.tex`，沿用注册、语义样式及局部分组接口。

## 第12章新增（2026-11-01）

`gauss-radial` 在切空间的v点画径向/角向输入，再在q=exp(v)的切空间画微分像；径向长度一致，角向长度有意不同，微分均在v处取值。`hopf-rinow-step` 仅表示小球面取子列和距离等号延伸，虚线不是预设存在的最短线。`jacobi-models` 按sin(t)、t、sinh(t)解析函数绘制，两个面板横轴同为[0,π]，负曲率面板纵轴独立缩放并标刻度。三图原创，非梁书原图改绘，无原图号、未复制网页代码；在 `modules/geodesics.tex` 沿用统一接口。

## 第13章新增（2026-11-01）

`submanifold-acceleration`以F(u)=(u,u²/2)、u(t)=t+t²/2在t=0的精确加速度(1,1)作切法分解，两个轴采用相同比例；非梁书图4-7改绘。`adapted-frame-block`为适配联络矩阵的原创结构示意，箭头表示切法混合求导，不是逐纤维联络映射。`mean-curvature-balance`在一个法空间内平移排列两个主方向的法向弯曲向量，用两个同号和两个异号的例子说明平均，不将逐点零迹当作全曲面极小。三图在`modules/submanifold-geometry.tex`中沿用公共接口，均无原书图号，不复制网页图形代码。

## 第14章新增（2026-11-01）

`hodge-star-plane`在同一定向欧氏平面中画dx→dy→-dx，箭头使用内积识别，不将星说成坐标换基。`hodge-decomposition`为L²正交直和的有限维投影模型，不声明形式逐点正交。`gauss-bonnet-octant`以沿(1,1,1)方向的等比例正投影绘制三个参数大圆弧，三个内角从实际球面切向量计算，图上投影角不直接量作直角；面积和角超均有解析值。三图原创，在`modules/hodge-gauss-bonnet.tex`中沿用公共接口，无原书图号，未复制网页图形代码。

## 第15章新增（2026-11-01）

`lie-left-flow`的交换图同时显示固定g的左平移与固定t的右平移流，正文明确乘法次序。`quotient-slice`是局部坐标盒：竖向Y改变时exp(X)exp(Y)留在同一左陪集，未把全群画作全局直积。`symmetric-reflection`在同一测地线上交换±t点，箭头与法坐标v→-v一致；法坐标图式不表示任意一般流形都存在全局反射。三图原创，模块`modules/lie-groups.tex`，无原书图号或网页图代码。

## 第16章新增（2026-11-01）

`associated-coordinates`显示同一相伴元素在两截面中的表示，右乘g与系数乘ρ(g)^-1配合。`principal-horizontal`位于同一切空间，竖直向量平移排列成分解图，斜水平补空间不表示任何天然正交。`hopf-potentials`取单位球面沿正交投影(X,Y,Z)→(X,(Y+√3 Z)/2)，整体放大2倍，纬线ϑ=75°；箭头由参数φ增加给出，两个势的符号与s_S=s_N exp(-iφ)一致。球面显示为投影示意，未复制原书或网页图形代码。三图原创，模块`modules/principal-bundles.tex`，无原图号。

## 第17章复几何三图（v0.18）

`complex-types`、`projective-potentials`、`complex-conditions`均为原创TikZ组织，模块为`modules/complex-kahler.tex`，无原书图号。分别表示复线性特征分解/反线性共轭、局部势经i∂bar∂后的相容性、以及有明确外引边界的条件关系。图中不是实切空间直和、等距射影平面或NN定理证明；相应限制在正文图注中说明。

## 第18章示性类三图（v0.19）

`characteristic-descent`、`connection-transgression`、`characteristic-limits`均为原创TikZ组织，位于`modules/characteristic-classes.tex`。分别表示不变曲率多项式的基本性/闭性、联络仿射线段和全局相对传递、四维示性数检测与七维消失的局限。四维数值取复定向；图不代表分类空间、整数提升或怪球构造证明，无原书图号。

## 第19章（v0.20）

`spin-half-angle`、`spin-transition-sign`、`calibration-phase`均为原创TikZ示意，不改绘原书图。分别表示Spin2半角参数、三重交集提升符号、对角Lagrange平面的复相位；不把参数圆当作切向量，不把模2提升障碍当实曲率，不把虚部零与正定向校准等同。正文证明和来源核对见第19章自查记录。

## 第20章（v0.21）

fredholm-splitting、yang-mills-bound、gauge-moduli-boundary为原创TikZ示意，位于modules/index-gauge.tex，无原书图号。分别表达有限维缺陷与同构块、固定正k下的能量恒等式、从线性Fredholm到非线性及全局构造的依赖。能量图横坐标为自对偶曲率的平方范数，不表示可实现参数的全集；依赖图不声称本书已完成模空间或不变量。
