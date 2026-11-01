# 第12章初稿自查与验收

日期：2026-11-01（Asia/Shanghai）；版本：v0.13 测地线、完备性与变分初稿。入口`course-study/chapters/12-geodesics/chapter.tex`，装配exponential、variation、completeness、jacobi、exercises五个文件。

这是写作者的数学自查、来源核查及本地源码/版面/链接验收，不是另一位审阅者的独立数学审阅或形式化验证。

## 数学主线与证明依赖

| 主线 | 逐项核查 |
|---|---|
| 指数定义域 | 从第5/10章喷流的开流域定义时间1指数，不预设完备；初速度缩放证明星形，零点微分恒等，再用逆映射定理 |
| 法坐标 | 只拉直过中心的径向测地线；用无挠下槽对称极化得中心Γ=0，度量相容给中心一阶偏导零；不等同于邻域平坦 |
| 参数交换/Gauss | 在沿映射的系数中推导两条导数交换公式，不要求变分浸入；Gauss由D_tT=0及初速度能量求导得到径向正交 |
| 径向最短 | 极坐标分解给长度≥径向变差；中心/多次过中心用截断极限；选更大微分同胚闭球并以第一次出球排除全局捷径 |
| 长度距离 | 用分段光滑可达集的开闭性给有限性；紧坐标球的度量上下界及第一次出球给非退化与拓扑；不以一般度量空间的有界集紧当先验 |
| 第一变分 | 固定时间能量含1/2，保留一般边界项；长度需正则，驻定给弧长测地；端点零场由沿曲线指数实现，紧时间段统一参数 |
| 最短线正则性 | 分段正则时第一变分给各段测地；坐标严格三角不等式去角；驻点/停顿在像的意义下用法球等号唯一性处理 |
| Hopf–Rinow | 完备→基曲线极限→坐标速度有界/相空间紧→ODE延拓；从单基点完整指数先取小球面等号点，再用无角延伸，未预设远点最短线存在；最后得闭球为有限维闭球的连续像 |
| Jacobi | 二参数导数交换给方程及正号；平行标架线性ODE给2n初值，移动基点与初始速度实现任意场；共轭重数等于指数微分核，不与整体不单射混同 |
| 第二变分 | 固定端点使二阶边界项消失；E''含全场，L''只含法向场；负E''通过能量比较得到真正更短曲线，不要求变分各条常速 |
| 指标引理 | Jacobi矩阵A(0)=0、A'(0)=I，Wronskian对称；A=tB与端点零场v=tz确保零时刻的系数可除，积分边界/接头项逐一保留 |
| 内点共轭 | 截断Jacobi场给零指标，接头与选定W给负交叉项；用局部平滑的一致及导数L²收敛保持负指标，再实现光滑变分；终点共轭单列边界 |

曲率按R(X,Y)Z=∇X∇YZ−∇Y∇XZ−∇[X,Y]Z，故Jacobi为D_t²J+R(J,T)T=0，指标曲率项为负g(R(V,T)T,W)。球面法向系数为a sin(t/a)，首次正零πa；与第11章球面正曲率一致。

依赖顺序：第5章ODE/流、第10章测地喷流/移动、第11章Levi–Civita/曲率对称 → 指数/法坐标 → 参数交换/Gauss/局部最短 → 距离/第一变分/无角 → Hopf–Rinow → Jacobi/共轭/第二变分/指标引理。没有借用后面的曲率比较、一般割迹或指标定理反证前面的局部最短性。

全局距离和Hopf–Rinow要求连通、有限维、正定、无边界；未将Lorentz极长性混入。一般割迹、Morse指标、Rauch、Bonnet–Myers及Cartan–Hadamard未在本章证明；未从无共轭或指标正定直接推出全局唯一最短线。

## 来源与习题映射

- 放大查看梁上册第二版3.3印刷69–75/PDF85–91，以及原题9/10印刷85/PDF101。核对原题9所指3-3-2、3-3-3、3-3-5与法坐标定理3-3-8；共轭讨论及图3-3仅作动机。两道原题改述、一道文内主题练习化与五道原创题分别登记，不另造原题号。
- 读取Meinrenken, Riemannian Geometry, Toronto Spring2002，16–17节印刷/PDF43–50：[公开讲义](https://www.math.toronto.edu/mein/teaching/LectureNotes/rieall.pdf)。本章补写自然开定义域，并采用小球面等号点/去角延伸的完整等价证明，不沿用其中依赖尚未说明的统一注入半径论证。
- 从Regensburg官网下载Clara Löh, Differential Geometry I, Wintersemester2020/21，读取3.5印刷159–169/PDF167–177，核对二阶交换、第二变分、Jacobi初值、指数奇异性及内点共轭后的非最短性：[官方讲义](https://loeh.app.uni-regensburg.de/teaching/diffgeo_ws2021/lecture_notes.pdf)。矩阵指标引理、零时刻可除性及平滑负指标场由本工程另行补写。
- 本书12.1为原题9，12.2为原题10，12.3为文内定理3-3-8主题改编，12.4–12.8原创；双页码与新增边界见`references/EXERCISES.md`。周4.2及4.4的本地DjVu页码仍待核对，不登记为已逐页校勘。

## 例子核算与图示

一次性`tmp/math_ch12.py`用SymPy对球面指数的实际环境坐标公式求微分，核对Gauss径向恒等式与角向因子、零半径极限；核对三种Jacobi模型及其初值。对球面显式法向变分直接求能量二阶导数并积分，核对πa阈值；另核对混合曲率Jacobi矩阵的Wronskian/指标恒等式、仿射重参数ODE和半平面竖直单位测地线。这些具体核算不取代一般证明或独立审阅。

新增第10组模块`figures/modules/geodesics.tex`，3幅图均原创并通过统一接口提供：`gauss-radial`画附着在v的径向/角向输入及其微分像，不把指数画成整体等距；`hopf-rinow-step`画距离等号延伸，虚线不预设为最短线；`jacobi-models`用sin/t/sinh解析函数，负曲率面板纵轴单独缩放。catalog、SOURCES及调用说明同步。


## 本地构建与页面验收

- `scripts/check-sources.py`通过：23章、136个可达TeX文件，39个命名图、10组模块；该工具只检查结构，输出明确提示`mathematical correctness not checked.`
- 主书完整构建为240页；第12章PDF物理页190–210，即印刷181–201，共21页。第13章从物理页211开始，仍为写作计划。
- 独立图册39个默认图+5个变体，共44页；注册与`DG-PARAMETER-ISOLATION: PASS`通过。主书和图册最终日志均无LaTeX/Package/Class Warning、Overfull、Underfull、缺字或未定义引用。
- 渲染查看物理页1–10、189–211、235–240，覆盖本章全部21页及封面/前言/目录/相邻章/附录/参考文献；新增图册37–39页另行查看。对比首次输出与重编译，修复习题说明和Jacobi初值的两处长行溢出、无角引理的前页锚点、前言孤立尾行及附录末节分页。图册来源中的π改为数学模式，消除正文西文字体缺字。
- `tmp/qa_ch12.py`读取最终PDF、辅助文件和注释，22个具名目标的实际目标页与排印页一致，全书231个内部链接解析到有效页；`tmp/ch12-qa/report.json`的`errors`为空。两项补充讲义的PDF外链URI均与参考文献登记一致，地址核验不代表外站持续可用性。
- `tmp/math_ch12.py`的具体模型符号计算全部通过。8个习题标题对应8份解答，无本章计划占位、替换字符或新增源码行尾空白。空白检查`git -c core.safecrlf=false diff --check`通过；提供的类和样式文件未改。

### 具名目标页码

| 标签 | PDF物理页 | 印刷页 |
|---|---:|---:|
| ch:12-geodesics | 190 | 181 |
| def:exponential-domain | 191 | 182 |
| thm:normal-coordinates | 191 | 182 |
| lem:variation-commutation | 192 | 183 |
| thm:gauss-lemma | 192 | 183 |
| fig:gauss-radial | 193 | 184 |
| prop:radial-minimizing | 194 | 185 |
| def:riemannian-distance | 195 | 186 |
| prop:distance-topology | 195 | 186 |
| thm:first-variation | 196 | 187 |
| lem:no-geodesic-corner | 197 | 188 |
| lem:hopf-rinow-step | 198 | 189 |
| thm:hopf-rinow | 199 | 190 |
| cor:compact-riemannian-complete | 200 | 191 |
| fig:hopf-rinow-step | 200 | 191 |
| def:jacobi-field | 201 | 192 |
| thm:jacobi-variation | 201 | 192 |
| prop:conjugate-exponential | 202 | 193 |
| thm:second-variation | 203 | 194 |
| thm:index-lemma | 204 | 195 |
| fig:jacobi-models | 205 | 196 |
| thm:conjugate-nonminimizing | 205 | 196 |

### 复现与发布边界

在工程根目录运行下列命令，可完成结构检查、图册及主书构建（需本机TeX Live和Python）：

```powershell
./scripts/build.ps1 -PythonCommand 'C:/Users/Topmkter/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -WithFigureGallery
git -c core.safecrlf=false diff --check
```

`tmp/math_ch12.py`使用SymPy，`tmp/qa_ch12.py`使用PyMuPDF和Pillow；脚本、下载的补充讲义及渲染图为本轮临时核查材料。一般证明与来源/验收结论保留在正文和本记录中。本轮未提交或推送新的Git提交，未核查新的远端CI、artifact或Release。独立数学审阅尚未完成，第13–23章仍保留待写状态。
