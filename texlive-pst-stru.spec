# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-stru
# catalog-date 2008-08-23 00:25:16 +0200
# catalog-license lppl
# catalog-version 0.11
Name:		texlive-pst-stru
Version:	0.11
Release:	2
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
%{_texmfdistdir}/tex/generic/pst-stru/pst-stru.tex
%{_texmfdistdir}/tex/latex/pst-stru/pst-stru.sty
%doc %{_texmfdistdir}/doc/generic/pst-stru/Changes
%doc %{_texmfdistdir}/doc/generic/pst-stru/README
%doc %{_texmfdistdir}/doc/generic/pst-stru/pst-stru-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-stru/pst-stru-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.11-2
+ Revision: 755481
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.11-1
+ Revision: 719399
- texlive-pst-stru
- texlive-pst-stru
- texlive-pst-stru
- texlive-pst-stru

