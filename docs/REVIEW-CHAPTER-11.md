# 第11章初稿自查与验收

日期：2026-11-01（Asia/Shanghai）；版本：v0.12 黎曼度量与Levi–Civita联络初稿。入口为`course-study/chapters/11-riemannian/chapter.tex`，装配metric、levi-civita、symmetries、curvatures、exercises五个文件。

本记录为写作者的数学自查、来源核查及本地源码/版面/链接验收，不是另一位审阅者的独立数学审阅，也不是形式化证明检查。

## 数学主线与依赖边界

| 主线 | 自查内容 |
|---|---|
| 度量存在 | 用第8章单位分解拼接局部欧氏度量；卡外零延拓、局部有限及每点至少一个正权重分别解释；不要求定向或全局标架 |
| 线性代数 | 光滑Gram–Schmidt、正分母、逆矩阵及升降同构；区分正交标架与坐标基；拉回度量正定当且仅当浸入 |
| Koszul | 从相容/无挠推导必要性，逐槽验证右端的函数规则，以非退化度量定义向量，再验证无挠与相容；未省掉存在性检查 |
| 平行移动 | 给任意沿曲线场的内积求导式，证明相容与所有路径的等距移动互推；反向取任意初始三向量，不假设全局平行场 |
| 自然性 | 局部等距拉回联络后用唯一性；常数缩放及乘积都由Koszul验证；一般乘积场保留系数导数 |
| 标量算子 | 正向卡体积拼接、行列式求导、联络迹、散度和Laplace符号；积分分部要求定向及至少一个函数紧支，无边界 |
| 曲率对称 | 末二槽反对称来自诱导曲率作用于g；第一Bianchi用第10章无挠情形；成对交换用明确的代数展开，无须法坐标 |
| 极化与平坦 | 两次极化和前三槽交替推出曲率由截面值确定；R=0时由第10章平行标架及无挠交换流得欧氏坐标，不用下一章指数映射 |
| 曲率缩并 | 截面换基的分子/Gram行列式同乘行列式平方；Ricci迹定义、对称性及截面求和；四种曲率对象的缩放分别核对 |
| Bianchi/Schur | 两次缩并明确写出三个迹的正负，协变导数包含所有槽；Schur须n≥3且连通，二维非恒曲率反例另算 |
| 习题范围 | 8题均配详解，4题梁书改述扩展+4题原创；第11.8题仅构造Ricci为零的代数曲率张量，没有登记为Ricci平坦流形实例 |

保持第10章∇∂ᵢ∂ⱼ=Γᵏᵢⱼ∂ₖ及R(X,Y)Z=∇X∇YZ−∇Y∇XZ−∇[X,Y]Z。本章专记四槽𝓡(X,Y,Z,W)=g(R(X,Y)Z,W)，故球面𝓡₁₂₂₁为正、𝓡₁₂₁₂为负，Ricⱼₖ=Rⁱₖᵢⱼ。第2章切向投影联络的相容和无挠已与基本定理对接，Gauss曲率符号一致。

依赖顺序为第6章张量/丛、第8章单位分解/积分及第10章一般联络/诱导曲率/Bianchi → 度量存在 → Levi–Civita → 度规曲率对称/极化 → 截面缩并/Bianchi/Schur。法坐标、长度距离、指数映射、变分、完备性和常曲率空间整体分类未计入本章已证明内容。伪黎曼部分只在习题11.4补充二维逐点代数，未扩展本章积分和截面结论。

## 来源与习题核查

- 查看梁上册第二版3.2.2印刷64–65/PDF80–81的度规相容与唯一性、印刷78–79/PDF94–95的曲率对称与Ricci、印刷81–82/PDF97–98的平坦局部命题及散度；第3章原题7、12、13、17均在印刷85/PDF101，实际放大查看。
- 原题12所指式3-4-10在印刷78/PDF94；原题13的球面度规从同页原题10读取。原书曲率的余矢量号差与本书槽序分开处理，不直接复制下标数组。
- 交叉核对Meinrenken, *Riemannian Geometry*, Toronto Spring 2002：[公开讲义](https://www.math.toronto.edu/mein/teaching/LectureNotes/rieall.pdf)，12–13节印刷/PDF33–36、15.2页40–41及18节页51–53。本书重新组织证明；未沿用其中与本章无关的嵌入旁述。
- 11.1增加散度/单位标架/Laplace，11.2增加缺少Bianchi的代数反例，11.3增加Ricci/标量/缩放，11.4保留二维Einstein张量任务并说明非退化不定情形的逐点代数。11.5–11.8原创，原题映射与双页码见`references/EXERCISES.md`。周书4.1及4.3本地DjVu页码仍待核对。

## 例子与图示

一次性脚本`tmp/math_ch11.py`用SymPy直接从度量求Christoffel和曲率，核对三维欧氏球坐标全部系数及81个零曲率分量、球面曲率/Ricci/标量与半径缩放、一般二维共形度量曲率和完整缩并Bianchi。另逐项检查四维非零代数曲率张量的256组对称/循环恒等式及零Ricci，以及11.2反例的循环余项。这些具体计算不取代一般证明或独立审阅。

新增第9组模块`figures/modules/riemannian.tex`，三个命名图均原创：`metric-unit-balls`按相同坐标比例画I与diag(4,1)的单位集合；`metric-transport`用两个正交归一表示保持长度和夹角；`sectional-trace`只在投影切空间示意三维Ricci求和，不把平面当流形中的实际曲面。图注、catalog、SOURCES及调用说明同步。


## 本地构建与页面验收

- `scripts/check-sources.py`通过：23章、127个可达TeX文件，36个命名图、9组模块。该检查仅验证结构，输出明确提示`mathematical correctness not checked.`
- 主书最终完整构建为220页；第11章PDF物理页172–189，即印刷163–180，共18页。第12章从物理页190开始，尚为写作计划。
- 独立图册为36个默认图加5个参数变体，共41页；图注册与`DG-PARAMETER-ISOLATION: PASS`通过。主书和图册最终日志均无LaTeX/Package/Class Warning、Overfull、Underfull、缺字或未定义引用；fontspec的字体说明为Info级，并已按实际页面检查。
- 渲染并查看主书物理页1–10、171–190、216–220，覆盖本章全部18页及封面、前言、目录、相邻章、附录与参考文献；另查看新增图册页34–36。修复两处长行溢出、拉回度量证明的短尾分页、三处目标落在前页，以及单位椭圆公式与截面图标签间距。重编译后复看受影响页面。
- `tmp/qa_ch11.py`读取最终PDF与辅助文件，本章22个具名目标的PDF目标页与排印页均一致；全书227个内部链接解析到有效页。`tmp/ch11-qa/report.json`的`errors`为空；公开讲义的PDF URI与登记地址一致，不以地址检查代替持续外站可用性监控。
- 精确符号计算`tmp/math_ch11.py`全部通过；新增章的8个习题标题对应8份解答，无规划占位、替换字符或行尾空白。`git -c core.safecrlf=false diff --check`通过，提供的类/样式文件未改。

### 具名目标页码

| 标签 | PDF物理页 | 印刷页 |
|---|---:|---:|
| ch:11-riemannian | 172 | 163 |
| def:riemannian-metric | 173 | 164 |
| thm:metric-existence | 173 | 164 |
| fig:metric-unit-balls | 174 | 165 |
| prop:orthonormal-musical | 174 | 165 |
| prop:pullback-metric | 175 | 166 |
| cor:metric-christoffel | 176 | 167 |
| thm:levi-civita | 176 | 167 |
| fig:metric-transport | 177 | 168 |
| prop:metric-transport | 177 | 168 |
| prop:metric-divergence | 178 | 169 |
| prop:metric-naturality | 178 | 169 |
| thm:metric-curvature-symmetries | 179 | 170 |
| prop:curvature-polarization | 180 | 171 |
| prop:riemannian-flat | 180 | 171 |
| def:sectional-curvature | 181 | 172 |
| prop:constant-curvature-model | 181 | 172 |
| def:ricci-scalar | 182 | 173 |
| prop:ricci-traces | 182 | 173 |
| fig:sectional-trace | 183 | 174 |
| cor:schur | 184 | 175 |
| thm:contracted-bianchi | 184 | 175 |

### 复现与发布边界

在工程根目录运行以下命令，可完成结构检查、图册和主书构建（需本机TeX Live与Python）：

```powershell
./scripts/build.ps1 -PythonCommand 'C:/Users/Topmkter/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -WithFigureGallery
git -c core.safecrlf=false diff --check
```

`tmp/math_ch11.py`使用SymPy，`tmp/qa_ch11.py`使用PyMuPDF及Pillow；它们和渲染图为本轮临时验收材料，一般数学推导及结论保留在正文和本记录中。本轮未提交或推送新的Git提交，未核查新的远端CI、artifact或Release；独立数学审阅尚未完成。第12–23章继续保留待写状态。
