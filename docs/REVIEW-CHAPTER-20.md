# 第20章初稿自查与验收

日期：2026-11-09（Asia/Shanghai）；版本：v0.21 指标与规范场初稿。入口为course-study/chapters/20-index-gauge/chapter.tex，装配elliptic、fredholm、index、yang-mills、self-duality、deformation、seiberg-witten、exercises八个文件。

本记录是作者自查、来源核对、具体模型与版面验收，不是独立数学审阅或形式化证明。第1–20章为draft，第21–23章为planned。

## 数学主线与证明边界

| 项目 | 已写入及适用范围 |
|---|---|
| 符号与函数空间 | 采用∂→iξ；先给H1→L2有界映射。只对两侧符号平方为长度平方的一阶Dirac型算子直接证明Fredholm，不假装已建立一般椭圆参数子 |
| 一阶估计 | 冻结系数、吸收小误差与有限单位分解；分布L2解先用卷积交换子获得H1，再用第14章标量主部差商证明逐阶正则性，未循环预设余核光滑 |
| Fredholm | 由紧嵌入证核有限维、核正交补估计、闭像；把L2余核识别为分布伴随核并证明光滑。紧致无边界假设不能删除 |
| 指标稳定 | 有限维Schur消元证明局部稳定；模紧误差逆证明紧扰动Fredholm，沿路径得同指标。一般Hilbert版本把有界逆定理列作外部分析先修 |
| AS公式 | 仅精确外引闭Spin流形的扭手征公式；特征形式展开与条件性推论另行证明。热核/超迹/Getzler或K理论/Thom/Bott的完整路线均未在本书建立 |
| Yang–Mills | 联络仿射变分、规范不变性、dA*F=0；能量无1/2因子，SU2用定义表示的负矩阵迹。平凡与非平凡线丛的分部积分区别明确 |
| 四维能量 | k=∫c2=∫tr(F²)/(8π²)，8π²k=‖F−‖²−‖F+‖²；k>0等号ASD，反向定向同步交换正负。一般整数性仍需整类比较 |
| 具体联络 | 整数通量T4上线丛及L⊕L逆的SU2下降构造，计算k=−2ab和能量8π²(a²+b²)，包含临界而不达下界的反例；不宣称给出不可约BPST构造 |
| ASD形变 | 仅在F+=0时为复形；符号正合，dA*⊕√2dA+满足Dirac型符号。用变分解及闭像说明H0/H1/H2缺陷公式；不从线性指标推断非线性模空间光滑 |
| Spin-c数据 | 假定给定Spin-c提升与相容旋量丛；给出自对偶虚二形式到无迹Hermite矩阵的三基计算。存在性、w2比较与拓扑分类未证明 |
| SW尺度与消失 | 行列式联络B的旋量中心项为B/2，主动规范作用减2u逆du；取c(FB+)=q(ψ)，平方修正c(FB+)/2，积分四次正项为‖ψ‖四次/4。Scal≥0排除非零旋量，不排除可约解 |
| 模空间与不变量 | 实虚维数公式外引；Sobolev乘积/切片、横截、紧性、定向、配边及b2+=1壁穿越均未建立，不能称已构造Donaldson或SW不变量 |

依赖链：第14章Sobolev/紧性/标量主部正则性 → 本章一阶估计及分布正则性 → Dirac型Fredholm → 指标稳定；第16章联络/曲率/Bianchi + 第18章特征形式 + 第14章星 → Yang–Mills变分/能量及ASD符号；第19章Fock/平方 + 给定Spin-c提升 → SW局部方程与积分消失。AS等式不是Fredholm性质的证明前提。

## 来源核对及题图归属

- Xianzhe Dai，[Lectures on Dirac Operators and Index Theory](https://web.math.ucsb.edu/~dai/book.pdf)，首页日期2015-01-07，73页。核对第3.1节与3.3节；扭Spin公式为定理3.3.4，印刷/PDF51。该页的Chern特征二次展开存在少一个c2系数的排印问题；本书按第18章迹/行列式恒等式使用ch2=(c1²−2c2)/2，未照抄该行。公式本身的证明仍外引。
- José Figueroa-O’Farrill，2006 [课程索引](https://webhomes.maths.ed.ac.uk/~jmf/Teaching/GT/index.html)，[讲义3](https://webhomes.maths.ed.ac.uk/~jmf/Teaching/GT/Lect3.pdf)印刷19–23/PDF1–5，[讲义4](https://webhomes.maths.ed.ac.uk/~jmf/Teaching/GT/Lect4.pdf)印刷24–27/PDF1–4，[讲义5](https://webhomes.maths.ed.ac.uk/~jmf/Teaching/GT/Lect5.pdf)印刷28–31/PDF1–4。交叉核对能量变分、自对偶和规范退化。讲义4印刷25/PDF2中，先写导数等于2dTr(τ∧Ft)，后又排成1/2，前后不一致；本书沿用第18章已经重推的系数2，不把该排印行当证明。来源以伴随Pontryagin数及另一种内积归一化表述下界，本书以SU2定义表示的c2重新计算。
- Timothy Perutz，[Smooth 4-manifolds and the Seiberg–Witten equations](https://web.ma.utexas.edu/users/perutz/GaugeTheory/FullCourse.pdf)，首页标明UT Austin Spring 2018，151页。第19.4–19.5节印刷/PDF96–99核对方程与虚维数。来源曲率方程为c(FB+)/2=q(phi)，本书为c(FB+)=q(ψ)，以ψ=√2 phi换算；不混写两套四次项系数。相关拓扑与模空间理论只登记依赖。
- 关键来源页已下载至忽略目录tmp/ch20-sources并渲染核对；周书DjVu与梁书相关主题的本地版次、原题与双页码继续待核对。
- 20.1–20.8均为原创补充并配详细解答，包含概念、计算、证明及反例；20.3–20.4明确依赖外引AS。三图均为原创TikZ组织，无原书图号，第18组模块index-gauge，总63默认图。

## 精确模型核算

scripts/check-index-gauge-models.py的76项精确恒等式通过，含四维星与投影、任意余向量的ASD符号范数、非交换SU2二形式的迹楔积和能量、从多项式联络独立计算的曲率/能量变分、A-hat到八次形式展开、四维Fock自对偶作用、SW二次映射/规范因子与四次项、整数通量环面。模型不验证一般证明、拓扑存在性或模空间构造；普通构建不依赖SymPy。

## 本地页面、链接及构建

主书387页，第20章PDF物理页351–367（17页，印刷340–356）；独立图册68页。源码登记通过（23章、225个可达TeX文件、63图/18模块），图目录与参数隔离通过；两份最终日志无警告、缺字、未定义引用或溢出。第20章21个具名目标页码一致，全书389个内部链接有效，76项精确模型恒等式通过。新增正文全部页面、三图、封面/前言/目录和相关附录/参考文献已渲染检查。

本章物理页351–367逐页渲染，另查前后衔接、封面/前言/完整目录、约定与参考文献；图册61–63页查看三图。修复正文与附录的长行、参考文献换行、AS章节孤立标题及前言末行孤页。报告tmp/ch20-qa/report.json的errors为空，8题对应8份解答，无PlannedSection占位。最终日志tmp/ch20-final-build.log。生成PDF、日志、来源下载和临时材料留在忽略目录。写作轮结束时尚未提交推送；后续GitHub同步见[工作记录](WORKLOG.md)，不据本地验收报告远端CI成功。

## 后续工作

独立数学审阅与来源补核未完成；AS完整证明、一般整类比较、Spin-c拓扑、非紧/带边算子、非线性规范切片/紧性/不变量仍为待办。下一写作章为第21章Lorentz几何，先核对梁书本地资料覆盖。此轮不创建Release。
