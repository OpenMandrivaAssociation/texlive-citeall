%global tl_name citeall
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Cite all entries of a bbl created with BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/citeall
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/citeall.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/citeall.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package allows to cite all entries of a bbl-file created with
BibLaTeX (v1.9).

