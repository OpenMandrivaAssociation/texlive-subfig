# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/subfig
# catalog-date 2010-05-10 00:41:23 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-subfig
Version:	1.3
Release:	1
Summary:	Figures broken into subfigures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subfig
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfig.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfig.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides support for the manipulation and reference
of small or 'sub' figures and tables within a single figure or
table environment. It is convenient to use this package when
your subfigures are to be separately captioned, referenced, or
are to be included in the List-of-Figures. A new \subfigure
command is introduced which can be used inside a figure
environment for each subfigure. An optional first argument is
used as the caption for that subfigure. This package supersedes
the subfigure package (which will continue to be supported, but
no longer maintained). The name has changed because the subfig
package is not completely backward compatible with the older
subfigure package due to an extensive rewrite to use the new
caption package to produce its subcaptions. The major advantage
to the new package is that the user interface is keyword/value
driven and easier to use. To ease the transition from the
subfigure package it includes a configuration file (subfig.cfg)
which nearly emulates the subfigure package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/subfig/altsf.cfg
%{_texmfdistdir}/tex/latex/subfig/subfig.sty
%doc %{_texmfdistdir}/doc/latex/subfig/README
%doc %{_texmfdistdir}/doc/latex/subfig/ltxdoc.cfg
%doc %{_texmfdistdir}/doc/latex/subfig/subfig.pdf
%doc %{_texmfdistdir}/doc/latex/subfig/test1.tex
%doc %{_texmfdistdir}/doc/latex/subfig/test2.tex
%doc %{_texmfdistdir}/doc/latex/subfig/test3.tex
%doc %{_texmfdistdir}/doc/latex/subfig/test4.tex
%doc %{_texmfdistdir}/doc/latex/subfig/test5.tex
%doc %{_texmfdistdir}/doc/latex/subfig/test6.tex
%doc %{_texmfdistdir}/doc/latex/subfig/test7.tex
#- source
%doc %{_texmfdistdir}/source/latex/subfig/Makefile
%doc %{_texmfdistdir}/source/latex/subfig/subfig.dtx
%doc %{_texmfdistdir}/source/latex/subfig/subfig.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}