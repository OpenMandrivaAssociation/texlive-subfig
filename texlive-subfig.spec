%global tl_name subfig
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Figures broken into subfigures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/subfig
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfig.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfig.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfig.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for the manipulation and reference of small
or 'sub' figures and tables within a single figure or table environment.
It is convenient to use this package when your subfigures are to be
separately captioned, referenced, or are to be included in the List-of-
Figures. A new \subfigure command is introduced which can be used inside
a figure environment for each subfigure. An optional first argument is
used as the caption for that subfigure. This package supersedes the
subfigure package (which is no longer maintained). The name was changed
since the package is not completely backward compatible with the older
package The major advantage of the new package is that the user
interface is keyword/value driven and easier to use. To ease the
transition from the subfigure package, the distribution includes a
configuration file (subfig.cfg) which nearly emulates the subfigure
package. The functionality of the package is provided by the (more
recent still) subcaption package.

