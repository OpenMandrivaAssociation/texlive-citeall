Name:		texlive-citeall
Version:	45975
Release:	1
Summary:	Cite all entries of a bbl created with BibLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/citeall
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/citeall.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/citeall.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package allows to cite all entries of a bbl-file
created with BibLaTeX (v1.9).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/citeall
%doc %{_texmfdistdir}/doc/latex/citeall

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
