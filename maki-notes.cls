\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{maki-notes}[2026/04/12 Maki lecture notes class]

\RequirePackage{kvoptions}
\SetupKeyvalOptions{
	family=maki,
	prefix=maki@
}
\DeclareStringOption[common]{fontpreset}
\DeclareStringOption[default]{theme}
\DeclareStringOption[plain]{sectionstyle}
\DeclareBoolOption[false]{answers}
\DeclareStringOption[inline]{solutions}
% MindFlow-compatible spelling. The key-value form is preferred, but these
% aliases make existing notes easier to migrate.
\DeclareVoidOption{secstyle-classic}{\def\maki@sectionstyle{classic}}
\DeclareVoidOption{secstyle-modern}{\def\maki@sectionstyle{modern}}
\DeclareVoidOption{secstyle-minimal}{\def\maki@sectionstyle{minimal}}
\DeclareVoidOption{secstyle-boxed}{\def\maki@sectionstyle{boxed}}
\DeclareVoidOption{secstyle-elegant}{\def\maki@sectionstyle{elegant}}
\DeclareVoidOption{secstyle-neon}{\def\maki@sectionstyle{neon}}
\DeclareVoidOption{secstyle-terminal}{\def\maki@sectionstyle{terminal}}
\DeclareVoidOption{secstyle-gradient}{\def\maki@sectionstyle{gradient}}
\DeclareVoidOption{secstyle-blueprint}{\def\maki@sectionstyle{blueprint}}
\DeclareVoidOption{secstyle-ribbon}{\def\maki@sectionstyle{ribbon}}
\DeclareDefaultOption{\PassOptionsToClass{\CurrentOption}{ctexbook}}
\ProcessKeyvalOptions*

\LoadClass[fontset=none]{ctexbook}

\newcommand{\LectureNotesTitle}{讲义标题}
\newcommand{\AuthorInfo}{作者信息}
\newcommand{\CoverTitle}{\LectureNotesTitle}
\newcommand{\CoverAuthorBlock}{作者署名}
\newcommand{\CoverFooterBlock}{日期}
\newcommand{\MakiFontPreset}{common}
\newcommand{\MakiTheme}{default}
\newcommand{\MakiSectionStyle}{plain}
\newif\ifMakiShowAnswers
\edef\MakiFontPreset{\maki@fontpreset}
\edef\MakiTheme{\maki@theme}
\edef\MakiSectionStyle{\maki@sectionstyle}
\ifmaki@answers
	\MakiShowAnswerstrue
\else
	\MakiShowAnswersfalse
\fi
\newcommand{\MakiSolutionsMode}{inline}
\edef\MakiSolutionsMode{\maki@solutions}

\RequirePackage{maki-notes}

\newcommand{\MakeTitlePage}{%
	\begin{titlepage}
		\centering
		\vspace*{5cm}

		{\fontsize{48pt}{60pt}\selectfont\heavykaishu \color{LogicColor} \CoverTitle\par}

		\vfill

		{\LARGE \kaishu
			\CoverAuthorBlock\par
		}

		\vspace{2.3cm}

		{\Large \kaishu
			\CoverFooterBlock\par
		}

		\vspace{2cm}
	\end{titlepage}%
}

\renewcommand{\maketitle}{\MakeTitlePage}
