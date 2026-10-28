# 现代微分几何与广义相对论

使用 LaTeX 编写的中文学习整理工程，入口为 [`main.tex`](main.tex)，内容集中在 [`course-study/`](course-study/)。目标是用统一符号、完整证明、可复现的 TikZ 图及配套习题串起现代微分几何与广义相对论。

**当前为 v0.2 基础扩充版，不是完整教材。** 已建立五部分、23章及两个附录的完整写作目录；第1章已写拓扑基础和梁书第1章全部16题改述及详细解答，分析与代数部分待补；第3章已写流形基础、主要例子、定理证明及6题解答。其余章节仍为明确标记的写作计划。编译成功不代表数学审稿通过。覆盖状态见 [PROGRESS](docs/PROGRESS.md)，下一步见 [TODO](docs/TODO.md)，变更见 [工作记录](docs/WORKLOG.md)。

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

输出 `build/main.pdf`。也可以在根目录对 `main.tex` 直接运行 XeLaTeX 至交叉引用稳定。根目录旧 `main.pdf` 是历史产物，不代表最新构建。GitHub Actions 自动编译并上传 PDF artifact；是否成功须查看对应提交的运行结果，不以 push 成功代替 CI 成功。当前不自动创建 Release。

若 Python 不在 PATH 中，PowerShell 脚本支持 `-PythonCommand 'Python可执行文件的绝对路径'`。本机验证使用此参数调用已安装的 Python 运行时。

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
