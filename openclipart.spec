Summary:	Archive of clip art that can be used for free for any use
Summary(pl.UTF-8):   Archiwum klipartów, które można używać w dowolny sposób za darmo
Name:		openclipart
Version:	0.18
Release:	1
Epoch:		0
License:	Creative Commons and/or Public Domain
Group:		Applications/Graphics
Source0:	http://www.openclipart.org/downloads/%{version}/%{name}-%{version}-full.tar.bz2
# Source0-md5:	f13a58a7fcab9d8647ea528d28c4b813
URL:		http://www.openclipart.org/
BuildRequires:	findutils
Requires:       %{name}-AUTHORS = %{epoch}:%{version}-%{release}
Obsoletes:	openclipart-MISC
Obsoletes:	openclipart-action
Obsoletes:	openclipart-actions
Obsoletes:	openclipart-animals
Obsoletes:	openclipart-application
Obsoletes:	openclipart-apps
Obsoletes:	openclipart-computer
Obsoletes:	openclipart-device
Obsoletes:	openclipart-filesystem
Obsoletes:	openclipart-filesystems
Obsoletes:	openclipart-filetype
Obsoletes:	openclipart-food
Obsoletes:	openclipart-gradients
Obsoletes:	openclipart-homes
Obsoletes:	openclipart-icons
Obsoletes:	openclipart-images
Obsoletes:	openclipart-map_symbols
Obsoletes:	openclipart-mime-types
Obsoletes:	openclipart-ocal_logo
Obsoletes:	openclipart-people
Obsoletes:	openclipart-signs
Obsoletes:	openclipart-unsorted
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to create an archive of clip art that can be used
for free for any use. All graphics submitted to the project should be
placed into the Public Domain according to the statement by the
Creative Commons. If you'd like to help out, please join the mailing
list. Also, browse the archives to review the project's history.

%description -l pl.UTF-8
Celem tego projektu jest stworzenie archiwum klipartów, które można
używać w dowolny sposób za darmo. Wszystkie grafiki przekazane do
tego projektu powinny być własnością publiczną ("Public Domain")
zgodnie z oświadczeniem Creative Commons. Jeśli ktoś chce pomóc,
powinien zapisać się na listę. Może także przejrzeć archiwum, aby
poznać historię projektu.

%package AUTHORS
Summary:	Authors List of all cliparts
Summary(pl.UTF-8):   Lista autorów wszystkich klipartów
Group:		Applications/Graphics

%description AUTHORS
Authors List of all cliparts from all openclipart packages.

%description AUTHORS -l pl.UTF-8
Lista autorów wszystkich klipartów z pakietów openclipart.

%package png
Summary:	PNG Openclipart
Summary(pl.UTF-8):   Kliparty w wersji PNG
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description png
PNG version of Openclipart.

%description png -l pl.UTF-8
Kliparty w wersji PNG.

%prep
%setup -q -n %{name}-%{version}-full

%build
find . -empty -type d -exec rmdir "{}" ";" || :

%install
rm -rf $RPM_BUILD_ROOT

:> %{name}-txt.txt
:> %{name}-svg.txt
:> %{name}-png.txt

for dir in `find . ! -name '.' -type d -print`; do
	install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/${dir}
	if (install ${dir}/*.svg $RPM_BUILD_ROOT%{_datadir}/%{name}/${dir}); then
		echo "%dir %{_datadir}/%{name}/${dir}" >> %{name}-svg.txt
		echo "%{_datadir}/%{name}/${dir}/*.svg" >> %{name}-svg.txt
	fi
	if (install ${dir}/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/${dir}); then
		echo "%dir %{_datadir}/%{name}/${dir}" >> %{name}-png.txt
		echo "%{_datadir}/%{name}/${dir}/*.png" >> %{name}-png.txt
	fi
	if (install ${dir}/*.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/${dir}); then
		echo "%{_datadir}/%{name}/${dir}/*.txt" >> %{name}-txt.txt
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-svg.txt
%defattr(644,root,root,755)

%files png -f %{name}-png.txt
%defattr(644,root,root,755)

%files AUTHORS -f %{name}-txt.txt
%defattr(644,root,root,755)
%doc README ChangeLog
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/clipart
%dir %{_datadir}/%{name}/clipart/special
%dir %{_datadir}/%{name}/clipart/special/examples
%dir %{_datadir}/%{name}/nsis
%dir %{_datadir}/%{name}/nsis/Licenses
