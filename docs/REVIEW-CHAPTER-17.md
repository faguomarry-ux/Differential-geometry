# 第17章初稿自查与验收

日期：2026-11-02（Asia/Shanghai）；版本：v0.18 复流形与Kahler几何初稿。入口`course-study/chapters/17-complex/chapter.tex`，装配complex、types、metrics、projective、chern、ricci、integrability、exercises八个正文文件。

本记录区分作者自查、来源核对、具体模型与版面验收；不是独立数学审阅或形式化证明。第1–17章为draft，第18–23章仍为planned。

## 数学主线、约定与依赖边界

| 项目 | 本章自查 |
|---|---|
| 复图册与J | J∂x=∂y；全纯换元微分与J交换，已有适配坐标之间相容；不把J²=−I当作坐标存在定理 |
| 全纯判据 | 对光滑函数用∂bar f=0及迭代单变量Cauchy公式给幂级数；单变量Cauchy公式为明确复分析先修，未在本书重证 |
| 类型分解 | 特征投影(I∓iJ)/2，余切用零化子；共轭为反线性，外幂不另加阶乘。dd=∂+bar∂与平方零只在已可积背景证明 |
| 几乎复反例 | 以barZ1=∂barz1、barZ2=∂barz2+barz1∂z1及共轭构成处处互补框架；括号为Z1，N=−4Z1，投影bar∂²z1非零，不混同底流形的其他复结构 |
| Hermite/体积 | 平均法给度量，基本形式ω(X,Y)=g(JX,Y)，ω^m/m!为复定向体积；几乎Kahler与Kahler分开 |
| 指标/尺度 | G_abbar=gC(∂a,∂barb)，g=2Re(G dz⊗dbarz)，Euclid G=I/2。共轭线性首变量的纤维矩阵H=G转置，不在联络公式中混用 |
| Kahler判别 | 在已有全纯坐标中从dω=0推偏导对称，再逐项Koszul得混合导数零及∇J=0；反向无挠交替给闭性。没有对一般几乎复J直接套此坐标证明 |
| 势函数 | 证明严格正复Hessian的给定实势产生Kahler度量，以及势差Re全纯函数不变；一般局部势存在依赖未补证的局部Dolbeault求解，显式外引 |
| CPm/FS | 用射影卡及秩一投影矩阵验证拓扑/复结构，局部势差log绝对值平方使二形式拼接；逐项算G、正定性和detG=(1+r²)^−(m+1) |
| Chern | 给定全纯丛起步，度量相容dH=A*H+HA及A^(0,1)=0迫使A=H逆∂H，证明拼接/唯一性；F=bar∂A且(2,0)抵消，不隐用Koszul–Malgrange反向可积性 |
| 两种联络 | 只有Kahler时LC复化保持T10且等于Chern；一般Hermite不把未保持子丛的LC“限制”直接叫作复联络；Chern挠率给偏导反对称 |
| Ricci号 | 以Z→R(Z,X)Y的实迹复化计算，rho(X,Y)=Ric(JX,Y)=i trF=−i∂bar∂logdetG；一般Hermite的Chern-Ricci不冒充LC-Ricci |
| Hopf与重言线丛 | CP1的FS半径1/√2、面积2π、K=2，前章单位球面度量是其两倍；Hopf F=iωFS，酉Chern归一化iF/(2π)积分−1 |
| 紧致障碍 | ω^m正积分及Stokes给[ω]^k≠0，结合第9章排除S^(2m)上m>1的Kahler结构；不由此排除非Kahler复结构 |
| NN及球面 | 证明N张量性/括号等价/必要性；NN充分性显式外引，实Frobenius不替代复PDE。球面几乎复分类和2026年新复结构构造完整证明未在本章核验 |

依赖链：第4–7章复化代数/形式 → 复图册/类型 → 第11章度量及Koszul → Hermite/Kahler/显式FS → 第10/16章换标架 → Chern与Ricci → 第8/9章Stokes与球面上同调障碍。没有先调用第18章Chern类或第20章指标定理。

## 来源、习题与研究动态

- 读取并缓存Moroianu《Lectures on Kähler Geometry》2004-03-16讲义版，97页，[Oxford教学托管PDF](https://people.maths.ox.ac.uk/joyce/Nairobi2019/MoroianuKahlerGeometry.pdf)。正文交叉核对第1–2节6–16页和第4–7节24–41页，习题页10、11、26、31、41另渲染查看。印刷页与PDF物理页相同。
- 17.1改述1.5题2/3，17.2取5.5题1的已可积情形并结合题2扩展，17.3改述4.3题4并加对偶/曲率，17.4改述7.4题2并改用显式坐标，17.8改述1.5题4并加特定度量非闭性。17.5–17.7为原创补充。8题均有对应详解，映射见`references/EXERCISES.md`；标准模型不宣称首次发现。周书本地DjVu页码与梁书对应题尚未核对。
- 球面问题必须区分几乎复存在、特定J可积和Kahler。核对[Engel的arXiv官方摘要](https://arxiv.org/abs/2609.38442v1)及[作者版25页PDF](https://philip-engel.github.io/S6.pdf)的引言/路线；官方提交日2026-09-29，作者版日期09-13。另核对[Viaclovsky的官方摘要](https://arxiv.org/abs/2609.33785v1)，提交日09-27。两篇均陈述S6复结构构造；本书记录为外部研究内容，未审查其每一步或确认期刊审稿状态。没有把历史讲义的“仍未解决”沿用成2026-11-02断言，也不将本章未核验等同于外部论文未有人核验。

## 具体模型与图示

新增`scripts/check-complex-kahler-models.py`，60项精确模型恒等式通过。含从势微分得到的二维FS系数/行列式/闭性与Ricci、非对角Hermite矩阵的Chern(2,0)抵消和规范协变、从实二维Christoffel独立算出的全部16个R分量与CP1尺度、重言线丛全纯/酉标架及面积/周期积分、变系数特征框架的Nijenhuis与bar∂平方、实行列式及共轭定向奇偶。核算仅验证具体模型，不替代一般证明。

新增第15组图模块`course-study/figures/modules/complex-kahler.tex`，含`complex-types`、`projective-potentials`、`complex-conditions`，均原创。图注分别限定复化直和、局部势拼接、NN外引及Kahler判别背景，不以示意图充当证明。

## 本地构建、页面与链接

- 主书334页，第17章PDF物理页294–310（17页，印刷284–300）；独立图册59页。源码检查通过（23章、189个可达TeX文件，54图、15模块），图目录和参数隔离通过；两份最终日志无警告、缺字、未定义引用或溢出。第17章24个具名目标页码一致，全书308个内部链接有效，60项精确模型核算通过。普通构建不依赖SymPy。
- 渲染并查看本章全部页面（PDF294–310）及前后衔接、封面/前言/完整目录、附录和参考文献。最终渲染页为[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334]，图册52–54页另行查看。图体参数隔离通过，三幅图的方向和适用范围与图注一致。
- 首轮检查发现习题17.4一处长行、Viaclovsky参考文献一处长行，均拆分后重建；把局部势图的差函数标签移到两卡上方，避免交叉箭头穿过文字。为短命题、Dolbeault命题、FS定理及习题节预留空间，修复两个跨页具名锚点（Dolbeault和FS）及页尾孤立习题节标题；压缩重复前言避免末段独占一页，为最后一条参考文献整体预留空间。
- 最终24个本章具名目标的实际PDF页与aux印刷页标签一致，报告`tmp/ch17-qa/report.json`的errors为空；4个新增来源URI在PDF注释中与登记一致。8题对应8份解答，本章无PlannedSection占位、替换字符或行尾空白，`git diff --check`通过。
- 成功构建日志位于忽略目录`tmp/ch17-final-build.log`、`tmp/ch17-anchor-build.log`、`tmp/ch17-accept-build.log`及最终334页对应的`tmp/ch17-accept-final.log`；最终联系表及整页图位于`tmp/ch17-qa/`。上述均为本地验收材料，不作为独立数学审阅。

## Git及保留范围

本轮改动未提交、推送或创建Release；本地成功不表示远端CI通过。独立数学审阅未完成。除表中外引边界外，Dolbeault层比较、一般Kahler局部势证明、Kahler恒等式/复Hodge分解、Kodaira嵌入、Calabi–Yau、球面几乎复分类及新构造的完整证明尚未建立。第18–23章为计划，下一章为示性类与Chern–Weil理论。

以上为v0.18写作轮的历史快照。后续第18章及v0.19同步见[工作记录](WORKLOG.md)和[当前进度](PROGRESS.md)；第17章24个具名目标在v0.19的352页PDF中亦复核通过，60项模型核算通过。
