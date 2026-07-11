%global tl_name pst-stru
%global tl_revision 38613

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.13
Release:	%{tl_revision}.1
Summary:	Civil engineering diagrams, using PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-stru
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-stru.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-stru.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This PSTricks-based package provides facilities to draw structural
schemes in civil engineering analysis, for beams, portals, arches and
piles.

