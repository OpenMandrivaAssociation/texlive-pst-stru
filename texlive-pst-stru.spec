Name:		texlive-pst-stru
Version:	0.13
Release:	1
Summary:	Civil engineering diagrams, using pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-stru
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-stru.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-stru.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pst-stru is a PSTricks-based package to draw structural schemes
in civil engineering analysis, for beams, portals, arches and
piles.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-stru
%{_texmfdistdir}/tex/latex/pst-stru
%doc %{_texmfdistdir}/doc/generic/pst-stru

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
