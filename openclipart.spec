Summary:	Archive of clip art that can be used for free for any use
Summary(pl):	Archiwum klipartów, które mo¿na u¿ywaæ w dowolny sposób za darmo
Name:		openclipart
Version:	0.18
Release:	3
Epoch:		0
License:	Creative Commons and/or Public Domain
Group:		Applications/Graphics
Source0:	http://www.openclipart.org/downloads/%{version}/%{name}-%{version}-full.tar.bz2
# Source0-md5:	f13a58a7fcab9d8647ea528d28c4b813
URL:		http://www.openclipart.org/
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}
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

%description -l pl
Celem tego projektu jest stworzenie archiwum klipartów, które mo¿na
u¿ywaæ w dowolny sposób za darmo. Wszystkie grafiki przekazane do
tego projektu powinny byæ w³asno¶ci± publiczn± ("Public Domain")
zgodnie z o¶wiadczeniem Creative Commons. Je¶li kto¶ chce pomóc,
powinien zapisaæ siê na listê. Mo¿e tak¿e przejrzeæ archiwum, aby
poznaæ historiê projektu.

%package AUTHORS
Summary:	Authors List of all cliparts
Summary(pl):	Lista autorów wszystkich klipartów
Group:		Applications/Graphics

%description AUTHORS
Authors List of all cliparts from all openclipart packages.

%description AUTHORS -l pl
Lista autorów wszystkich klipartów z pakietów openclipart.

%package png
Summary:	PNG Openclipart
Summary(pl):	Kliparty w wersji PNG
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description png
PNG version of Openclipart.

%description png -l pl
Kliparty w wersji PNG.

%prep
%setup -q -n %{name}-%{version}-full

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

install_data() {
	echo "Using cp -a$l to copy files"
	for src in "$@"; do
		dst=${src#clipart/}
		echo "- $dst"
		install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/$dst
		diradd=0
		if ls $src/*.svg > /dev/null 2>&1; then
			diradd=1
			echo " svg: $dst"
			cp -a$l $src/*.svg $RPM_BUILD_ROOT%{_datadir}/%{name}/$dst
			echo "%{_datadir}/%{name}/$dst/*.svg" >> %{name}-svg.txt
		fi
		if ls $src/*.png > /dev/null 2>&1; then
			diradd=1
			echo " png: $dst"
			cp -a$l $src/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/$dst
			echo "%{_datadir}/%{name}/$dst/*.png" >> %{name}-png.txt
		fi
		if ls $src/*.txt > /dev/null 2>&1; then
			diradd=1
			echo " txt: $dst"
			cp -a$l $src/*.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/$dst
			echo "%{_datadir}/%{name}/$dst/*.txt" >> %{name}-txt.txt
		fi
		if [ $diradd = 1 ]; then
			echo "%dir %{_datadir}/%{name}/$dst" >> %{name}-txt.txt
		fi
	done
}

rm -f %{name}-{txt,svg,png}.txt

# test if we can hardlink -- src and dest on the same partition
if cp -al README $RPM_BUILD_ROOT/README 2>/dev/null; then
	l=l
	rm -f $RPM_BUILD_ROOT/README
fi
install_data $(find clipart ! -name clipart -type d)

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-svg.txt
%defattr(644,root,root,755)

%files png -f %{name}-png.txt
%defattr(644,root,root,755)

%files AUTHORS -f %{name}-txt.txt
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/special/examples
