Summary:	Archive of clip art that can be used for free for any use
Summary(pl):	Archiwum klipartów, które mo¿na u¿ywaæ w dowolny sposób za darmo
Name:		openclipart
Version:	0.07
Release:	0.1
Epoch:		0
License:	Creative Commons and/or Public Domain
Group:		Applications/Graphics
Source0:	http://www.openclipart.org/downloads/%{name}-%{version}.tgz
# Source0-md5:  dd92d04305efc8bdb8f7f77219a05bdc
URL:		http://www.openclipart.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to create an archive of clip art that can be used
for free for any use. All graphics submitted to the project should be
placed into the Public Domain according to the statement by the
Creative Commons. If you'd like to help out, please join the mailing
list. Also, browse the archives to review the project's history.

This package contains README and Examples files. For really clipart
please install openclipart-[type] package.

%description -l pl
Celem tego projektu jest stworzenie archiwum klipartów, które mo¿na
u¿ywaæ w dowolny sposób za darmo. Wszystkie grafiki przekazane do
tego projektu powinny byæ w³asno¶ci± publiczn± ("Public Domain")
zgodnie z o¶wiadczeniem Creative Commons. Je¶li kto¶ chce pomóc,
powinien zapisaæ siê na listê. Mo¿e tak¿e przejrzeæ archiwum, aby
poznaæ historiê projektu.

Ten pakiet zawiera pliki README i Examples. W³a¶ciwe kliparty znajduj±
siê w pakietach openclipart-[typ].

%package AUTHORS
Summary:	Authors List of all cliparts
Summary(pl):	Lista autorów wszystkich klipartów
Group:		Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description AUTHORS
Authors List of all cliparts from all openclipart-* packages.

%description AUTHORS -l pl
Lista autorów wszystkich klipartów z pakietów openclipart-*.

%package MISC
Summary:	Misc cliparts
Summary(pl):	Ró¿ne kliparty
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description MISC
Clipart categories: activities africa america animal Animal appicon
apple aqua Aqua architecture armoiries arrow asia automobiles baby
bacon ball beach beverages bicycle Biohazard bird book bouquet bowl
breizh britain BSD building business button Button callout candy
cartoon celebrity celtic che chicken Chicken clipboard clock coffe
communication countires cute daemon decorations devices eagle ecus
education emblems entertainment envelope europe face fanart farm Farm
festive fish flag Flag flight flourish flower fly french friends fruit
Galette game geography geometry glass grape great GTP guevara
handshake hen Hen historic icon improvisedkeywordparse insect insects
interface ladybug library linux Linux logo Logo logos magnifying mail
mammal mammals man map maps mascot meat meeting money music musicsym
navigation nicu northamerica note oceania office openclipart park pear
penguin pig place plane plant postage presentation scissors Scotland
shape shapes sign slides smiley soccer Software soup sports stamp star
steaming study summer sun symbol tea technical telephone tools toy
toys transport transportation tux Tux usmail vase vgcats vietnam
warning water weather wildlife wine work

%description MISC -l pl
Kategorie klipartów: activities africa america animal Animal appicon
apple aqua Aqua architecture armoiries arrow asia automobiles baby
bacon ball beach beverages bicycle Biohazard bird book bouquet bowl
breizh britain BSD building business button Button callout candy
cartoon celebrity celtic che chicken Chicken clipboard clock coffe
communication countires cute daemon decorations devices eagle ecus
education emblems entertainment envelope europe face fanart farm Farm
festive fish flag Flag flight flourish flower fly french friends fruit
Galette game geography geometry glass grape great GTP guevara
handshake hen Hen historic icon improvisedkeywordparse insect insects
interface ladybug library linux Linux logo Logo logos magnifying mail
mammal mammals man map maps mascot meat meeting money music musicsym
navigation nicu northamerica note oceania office openclipart park pear
penguin pig place plane plant postage presentation scissors Scotland
shape shapes sign slides smiley soccer Software soup sports stamp star
steaming study summer sun symbol tea technical telephone tools toy
toys transport transportation tux Tux usmail vase vgcats vietnam
warning water weather wildlife wine work

%package icons
Summary:	icons cliparts
Summary(pl):	Kliparty "icons"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description icons
74 cliparts from icons category.

%description icons -l pl
74 klipartów z kategorii "icons".

%package people
Summary:	people cliparts
Summary(pl):	Kliparty "people"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description people
11 cliparts from people category.

%description people -l pl
11 klipartów z kategorii "people".

%package ocal_logo
Summary:	ocal_logo cliparts
Summary(pl):	Kliparty "ocal_logo"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description ocal_logo
26 cliparts from ocal_logo category.

%description ocal_logo -l pl
26 klipartów z kategorii "ocal_logo".

%package gradients
Summary:	gradients cliparts
Summary(pl):	Kliparty "gradients"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description gradients
118 cliparts from gradients category.

%description gradients -l pl
118 klipartów z kategorii "gradients".

%package food
Summary:	food cliparts
Summary(pl):	Kliparty "food"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description food
19 cliparts from food category.

%description food -l pl
19 klipartów z kategorii "food".

%package mime-types
Summary:	mime-types cliparts
Summary(pl):	Kliparty "mime-types"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description mime-types
22 cliparts from mime-types category.

%description mime-types -l pl
22 klipartów z kategorii "mime-types".

%package actions
Summary:	actions cliparts
Summary(pl):	Kliparty "actions"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description actions
14 cliparts from actions category.

%description actions -l pl
14 klipartów z kategorii "actions".

%package computer
Summary:	computer cliparts
Summary(pl):	Kliparty "computer"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description computer
81 cliparts from computer category.

%description computer -l pl
81 klipartów z kategorii "computer".

%package filetype
Summary:	filetype cliparts
Summary(pl):	Kliparty "filetype"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description filetype
13 cliparts from filetype category.

%description filetype -l pl
13 klipartów z kategorii "filetype".

%package homes
Summary:	homes cliparts
Summary(pl):	Kliparty "homes"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description homes
20 cliparts from homes category.

%description homes -l pl
20 klipartów z kategorii "homes".

%package device
Summary:	device cliparts
Summary(pl):	Kliparty "device"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description device
30 cliparts from device category.

%description device -l pl
30 klipartów z kategorii "device".

%package application
Summary:	application cliparts
Summary(pl):	Kliparty "application"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description application
278 cliparts from application category.

%description application -l pl
278 klipartów z kategorii "application".

%package filesystems
Summary:	filesystems cliparts
Summary(pl):	Kliparty "filesystems"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description filesystems
10 cliparts from filesystems category.

%description filesystems -l pl
10 klipartów z kategorii "filesystems".

%package action
Summary:	action cliparts
Summary(pl):	Kliparty "action"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description action
599 cliparts from action category.

%description action -l pl
599 klipartów z kategorii "action".

%package apps
Summary:	apps cliparts
Summary(pl):	Kliparty "apps"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description apps
16 cliparts from apps category.

%description apps -l pl
16 klipartów z kategorii "apps".

%package map_symbols
Summary:	map_symbols cliparts
Summary(pl):	Kliparty "map_symbols"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description map_symbols
21 cliparts from map_symbols category.

%description map_symbols -l pl
21 klipartów z kategorii "map_symbols".

%package images
Summary:	images cliparts
Summary(pl):	Kliparty "images"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description images
13 cliparts from images category.

%description images -l pl
13 klipartów z kategorii "images".

%package animals
Summary:	animals cliparts
Summary(pl):	Kliparty "animals"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description animals
7 cliparts from animals category.

%description animals -l pl
7 klipartów z kategorii "animals".

%package signs
Summary:	signs cliparts
Summary(pl):	Kliparty "signs"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description signs
22 cliparts from signs category.

%description signs -l pl
22 klipartów z kategorii "signs".

%package unsorted
Summary:	unsorted cliparts
Summary(pl):	Kliparty "unsorted"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description unsorted
456 cliparts from unsorted category.

%description unsorted -l pl
456 klipartów z kategorii "unsorted".

%package filesystem
Summary:	filesystem cliparts
Summary(pl):	Kliparty "filesystem"
Group:		Applications/Graphics
Requires:	%{name}-AUTHORS = %{epoch}:%{version}-%{release}

%description filesystem
44 cliparts from filesystem category.

%description filesystem -l pl
44 klipartów z kategorii "filesystem".

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{activities,africa,america,animal,Animal,appicon,apple,aqua,Aqua,architecture,armoiries,arrow,asia,automobiles,baby,bacon,ball,beach,beverages,bicycle,Biohazard,bird,book,bouquet,bowl,breizh,britain,BSD,building,business,button,Button,callout,candy,cartoon,celebrity,celtic,che,chicken,Chicken,clipboard,clock,coffe,communication,countires,cute,daemon,decorations,devices,eagle,ecus,education,emblems,entertainment,envelope,europe,face,fanart,farm,Farm,festive,fish,flag,Flag,flight,flourish,flower,fly,french,friends,fruit,Galette,game,geography,geometry,glass,grape,great,GTP,guevara,handshake,hen,Hen,historic,icon,improvisedkeywordparse,insect,insects,interface,ladybug,library,linux,Linux,logo,Logo,logos,magnifying,mail,mammal,mammals,man,map,maps,mascot,meat,meeting,money,music,musicsym,navigation,nicu,northamerica,note,oceania,office,openclipart,park,pear,penguin,pig,place,plane,plant,postage,presentation,scissors,Scotland,shape,shapes,sign,slides,smiley,soccer,Software,soup,sports,stamp,star,steaming,study,summer,sun,symbol,tea,technical,telephone,tools,toy,toys,transport,transportation,tux,Tux,usmail,vase,vgcats,vietnam,warning,water,weather,wildlife,wine,work,icons,people,ocal_logo,gradients,food,mime-types,actions,computer,filetype,homes,device,application,filesystems,action,apps,map_symbols,images,animals,signs,unsorted,filesystem}

install activities/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/activities
rm -rf activities/*[!tT]
install africa/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/africa
rm -rf africa/*[!tT]
install america/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/america
rm -rf america/*[!tT]
install animal/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/animal
rm -rf animal/*[!tT]
install Animal/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Animal
rm -rf Animal/*[!tT]
install appicon/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/appicon
rm -rf appicon/*[!tT]
install apple/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/apple
rm -rf apple/*[!tT]
install aqua/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/aqua
rm -rf aqua/*[!tT]
install Aqua/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Aqua
rm -rf Aqua/*[!tT]
install architecture/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/architecture
rm -rf architecture/*[!tT]
install armoiries/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/armoiries
rm -rf armoiries/*[!tT]
install arrow/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/arrow
rm -rf arrow/*[!tT]
install asia/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/asia
rm -rf asia/*[!tT]
install automobiles/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/automobiles
rm -rf automobiles/*[!tT]
install baby/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/baby
rm -rf baby/*[!tT]
install bacon/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/bacon
rm -rf bacon/*[!tT]
install ball/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/ball
rm -rf ball/*[!tT]
install beach/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/beach
rm -rf beach/*[!tT]
install beverages/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/beverages
rm -rf beverages/*[!tT]
install bicycle/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/bicycle
rm -rf bicycle/*[!tT]
install Biohazard/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Biohazard
rm -rf Biohazard/*[!tT]
install bird/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/bird
rm -rf bird/*[!tT]
install book/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/book
rm -rf book/*[!tT]
install bouquet/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/bouquet
rm -rf bouquet/*[!tT]
install bowl/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/bowl
rm -rf bowl/*[!tT]
install breizh/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/breizh
rm -rf breizh/*[!tT]
install britain/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/britain
rm -rf britain/*[!tT]
install BSD/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/BSD
rm -rf BSD/*[!tT]
install building/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/building
rm -rf building/*[!tT]
install business/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/business
rm -rf business/*[!tT]
install button/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/button
rm -rf button/*[!tT]
install Button/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Button
rm -rf Button/*[!tT]
install callout/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/callout
rm -rf callout/*[!tT]
install candy/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/candy
rm -rf candy/*[!tT]
install cartoon/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/cartoon
rm -rf cartoon/*[!tT]
install celebrity/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/celebrity
rm -rf celebrity/*[!tT]
install celtic/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/celtic
rm -rf celtic/*[!tT]
install che/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/che
rm -rf che/*[!tT]
install chicken/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/chicken
rm -rf chicken/*[!tT]
install Chicken/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Chicken
rm -rf Chicken/*[!tT]
install clipboard/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/clipboard
rm -rf clipboard/*[!tT]
install clock/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/clock
rm -rf clock/*[!tT]
install coffe/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/coffe
rm -rf coffe/*[!tT]
install communication/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/communication
rm -rf communication/*[!tT]
install countires/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/countires
rm -rf countires/*[!tT]
install cute/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/cute
rm -rf cute/*[!tT]
install daemon/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/daemon
rm -rf daemon/*[!tT]
install decorations/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/decorations
rm -rf decorations/*[!tT]
install devices/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/devices
rm -rf devices/*[!tT]
install eagle/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/eagle
rm -rf eagle/*[!tT]
install ecus/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/ecus
rm -rf ecus/*[!tT]
install education/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/education
rm -rf education/*[!tT]
install emblems/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/emblems
rm -rf emblems/*[!tT]
install entertainment/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/entertainment
rm -rf entertainment/*[!tT]
install envelope/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/envelope
rm -rf envelope/*[!tT]
install europe/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/europe
rm -rf europe/*[!tT]
install face/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/face
rm -rf face/*[!tT]
install fanart/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/fanart
rm -rf fanart/*[!tT]
install farm/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/farm
rm -rf farm/*[!tT]
install Farm/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Farm
rm -rf Farm/*[!tT]
install festive/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/festive
rm -rf festive/*[!tT]
install fish/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/fish
rm -rf fish/*[!tT]
install flag/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/flag
rm -rf flag/*[!tT]
install Flag/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Flag
rm -rf Flag/*[!tT]
install flight/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/flight
rm -rf flight/*[!tT]
install flourish/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/flourish
rm -rf flourish/*[!tT]
install flower/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/flower
rm -rf flower/*[!tT]
install fly/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/fly
rm -rf fly/*[!tT]
install french/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/french
rm -rf french/*[!tT]
install friends/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/friends
rm -rf friends/*[!tT]
install fruit/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/fruit
rm -rf fruit/*[!tT]
install Galette/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Galette
rm -rf Galette/*[!tT]
install game/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/game
rm -rf game/*[!tT]
install geography/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/geography
rm -rf geography/*[!tT]
install geometry/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/geometry
rm -rf geometry/*[!tT]
install glass/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/glass
rm -rf glass/*[!tT]
install grape/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/grape
rm -rf grape/*[!tT]
install great/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/great
rm -rf great/*[!tT]
install GTP/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/GTP
rm -rf GTP/*[!tT]
install guevara/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/guevara
rm -rf guevara/*[!tT]
install handshake/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/handshake
rm -rf handshake/*[!tT]
install hen/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/hen
rm -rf hen/*[!tT]
install Hen/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Hen
rm -rf Hen/*[!tT]
install historic/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/historic
rm -rf historic/*[!tT]
install icon/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/icon
rm -rf icon/*[!tT]
install improvisedkeywordparse/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/improvisedkeywordparse
rm -rf improvisedkeywordparse/*[!tT]
install insect/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/insect
rm -rf insect/*[!tT]
install insects/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/insects
rm -rf insects/*[!tT]
install interface/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/interface
rm -rf interface/*[!tT]
install ladybug/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/ladybug
rm -rf ladybug/*[!tT]
install library/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/library
rm -rf library/*[!tT]
install linux/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/linux
rm -rf linux/*[!tT]
install Linux/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Linux
rm -rf Linux/*[!tT]
install logo/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/logo
rm -rf logo/*[!tT]
install Logo/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Logo
rm -rf Logo/*[!tT]
install logos/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/logos
rm -rf logos/*[!tT]
install magnifying/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/magnifying
rm -rf magnifying/*[!tT]
install mail/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/mail
rm -rf mail/*[!tT]
install mammal/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/mammal
rm -rf mammal/*[!tT]
install mammals/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/mammals
rm -rf mammals/*[!tT]
install man/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/man
rm -rf man/*[!tT]
install map/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/map
rm -rf map/*[!tT]
install maps/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/maps
rm -rf maps/*[!tT]
install mascot/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/mascot
rm -rf mascot/*[!tT]
install meat/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/meat
rm -rf meat/*[!tT]
install meeting/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/meeting
rm -rf meeting/*[!tT]
install money/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/money
rm -rf money/*[!tT]
install music/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/music
rm -rf music/*[!tT]
install musicsym/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/musicsym
rm -rf musicsym/*[!tT]
install navigation/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/navigation
rm -rf navigation/*[!tT]
install nicu/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/nicu
rm -rf nicu/*[!tT]
install northamerica/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/northamerica
rm -rf northamerica/*[!tT]
install note/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/note
rm -rf note/*[!tT]
install oceania/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/oceania
rm -rf oceania/*[!tT]
install office/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/office
rm -rf office/*[!tT]
install openclipart/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/openclipart
rm -rf openclipart/*[!tT]
install park/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/park
rm -rf park/*[!tT]
install pear/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/pear
rm -rf pear/*[!tT]
install penguin/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/penguin
rm -rf penguin/*[!tT]
install pig/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/pig
rm -rf pig/*[!tT]
install place/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/place
rm -rf place/*[!tT]
install plane/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/plane
rm -rf plane/*[!tT]
install plant/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/plant
rm -rf plant/*[!tT]
install postage/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/postage
rm -rf postage/*[!tT]
install presentation/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/presentation
rm -rf presentation/*[!tT]
install scissors/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/scissors
rm -rf scissors/*[!tT]
install Scotland/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Scotland
rm -rf Scotland/*[!tT]
install shape/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/shape
rm -rf shape/*[!tT]
install shapes/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/shapes
rm -rf shapes/*[!tT]
install sign/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/sign
rm -rf sign/*[!tT]
install slides/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/slides
rm -rf slides/*[!tT]
install smiley/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/smiley
rm -rf smiley/*[!tT]
install soccer/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/soccer
rm -rf soccer/*[!tT]
install Software/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Software
rm -rf Software/*[!tT]
install soup/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/soup
rm -rf soup/*[!tT]
install sports/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/sports
rm -rf sports/*[!tT]
install stamp/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/stamp
rm -rf stamp/*[!tT]
install star/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/star
rm -rf star/*[!tT]
install steaming/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/steaming
rm -rf steaming/*[!tT]
install study/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/study
rm -rf study/*[!tT]
install summer/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/summer
rm -rf summer/*[!tT]
install sun/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/sun
rm -rf sun/*[!tT]
install symbol/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/symbol
rm -rf symbol/*[!tT]
install tea/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/tea
rm -rf tea/*[!tT]
install technical/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/technical
rm -rf technical/*[!tT]
install telephone/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/telephone
rm -rf telephone/*[!tT]
install tools/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/tools
rm -rf tools/*[!tT]
install toy/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/toy
rm -rf toy/*[!tT]
install toys/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/toys
rm -rf toys/*[!tT]
install transport/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/transport
rm -rf transport/*[!tT]
install transportation/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/transportation
rm -rf transportation/*[!tT]
install tux/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/tux
rm -rf tux/*[!tT]
install Tux/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/Tux
rm -rf Tux/*[!tT]
install usmail/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/usmail
rm -rf usmail/*[!tT]
install vase/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/vase
rm -rf vase/*[!tT]
install vgcats/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/vgcats
rm -rf vgcats/*[!tT]
install vietnam/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/vietnam
rm -rf vietnam/*[!tT]
install warning/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/warning
rm -rf warning/*[!tT]
install water/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/water
rm -rf water/*[!tT]
install weather/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/weather
rm -rf weather/*[!tT]
install wildlife/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/wildlife
rm -rf wildlife/*[!tT]
install wine/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/wine
rm -rf wine/*[!tT]
install work/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/work
rm -rf work/*[!tT]
install icons/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
rm -rf icons/*[!tT]
install people/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/people
rm -rf people/*[!tT]
install ocal_logo/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/ocal_logo
rm -rf ocal_logo/*[!tT]
install gradients/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/gradients
rm -rf gradients/*[!tT]
install food/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/food
rm -rf food/*[!tT]
install mime-types/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/mime-types
rm -rf mime-types/*[!tT]
install actions/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/actions
rm -rf actions/*[!tT]
install computer/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/computer
rm -rf computer/*[!tT]
install filetype/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/filetype
rm -rf filetype/*[!tT]
install homes/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/homes
rm -rf homes/*[!tT]
install device/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/device
rm -rf device/*[!tT]
install application/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/application
rm -rf application/*[!tT]
install filesystems/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/filesystems
rm -rf filesystems/*[!tT]
install action/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/action
rm -rf action/*[!tT]
install apps/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/apps
rm -rf apps/*[!tT]
install map_symbols/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/map_symbols
rm -rf map_symbols/*[!tT]
install images/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/images
rm -rf images/*[!tT]
install animals/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/animals
rm -rf animals/*[!tT]
install signs/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/signs
rm -rf signs/*[!tT]
install unsorted/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/unsorted
rm -rf unsorted/*[!tT]
install filesystem/*[!tT] $RPM_BUILD_ROOT%{_datadir}/%{name}/filesystem
rm -rf filesystem/*[!tT]

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Examples README.txt LOG.txt
%dir %{_datadir}/%{name}

%files AUTHORS
%defattr(644,root,root,755)
%doc activities africa america animal Animal appicon apple aqua Aqua architecture armoiries arrow asia automobiles baby bacon ball beach beverages bicycle Biohazard bird book bouquet bowl breizh britain BSD building business button Button callout candy cartoon celebrity celtic che chicken Chicken clipboard clock coffe communication countires cute daemon decorations devices eagle ecus education emblems entertainment envelope europe face fanart farm Farm festive fish flag Flag flight flourish flower fly french friends fruit Galette game geography geometry glass grape great GTP guevara handshake hen Hen historic icon improvisedkeywordparse insect insects interface ladybug library linux Linux logo Logo logos magnifying mail mammal mammals man map maps mascot meat meeting money music musicsym navigation nicu northamerica note oceania office openclipart park pear penguin pig place plane plant postage presentation scissors Scotland shape shapes sign slides smiley soccer Software soup sports stamp star steaming study summer sun symbol tea technical telephone tools toy toys transport transportation tux Tux usmail vase vgcats vietnam warning water weather wildlife wine work icons people ocal_logo gradients food mime-types actions computer filetype homes device application filesystems action apps map_symbols images animals signs unsorted filesystem

%files MISC
%defattr(644,root,root,755)
%{_datadir}/%{name}/activities
%{_datadir}/%{name}/africa
%{_datadir}/%{name}/america
%{_datadir}/%{name}/animal
%{_datadir}/%{name}/Animal
%{_datadir}/%{name}/appicon
%{_datadir}/%{name}/apple
%{_datadir}/%{name}/aqua
%{_datadir}/%{name}/Aqua
%{_datadir}/%{name}/architecture
%{_datadir}/%{name}/armoiries
%{_datadir}/%{name}/arrow
%{_datadir}/%{name}/asia
%{_datadir}/%{name}/automobiles
%{_datadir}/%{name}/baby
%{_datadir}/%{name}/bacon
%{_datadir}/%{name}/ball
%{_datadir}/%{name}/beach
%{_datadir}/%{name}/beverages
%{_datadir}/%{name}/bicycle
%{_datadir}/%{name}/Biohazard
%{_datadir}/%{name}/bird
%{_datadir}/%{name}/book
%{_datadir}/%{name}/bouquet
%{_datadir}/%{name}/bowl
%{_datadir}/%{name}/breizh
%{_datadir}/%{name}/britain
%{_datadir}/%{name}/BSD
%{_datadir}/%{name}/building
%{_datadir}/%{name}/business
%{_datadir}/%{name}/button
%{_datadir}/%{name}/Button
%{_datadir}/%{name}/callout
%{_datadir}/%{name}/candy
%{_datadir}/%{name}/cartoon
%{_datadir}/%{name}/celebrity
%{_datadir}/%{name}/celtic
%{_datadir}/%{name}/che
%{_datadir}/%{name}/chicken
%{_datadir}/%{name}/Chicken
%{_datadir}/%{name}/clipboard
%{_datadir}/%{name}/clock
%{_datadir}/%{name}/coffe
%{_datadir}/%{name}/communication
%{_datadir}/%{name}/countires
%{_datadir}/%{name}/cute
%{_datadir}/%{name}/daemon
%{_datadir}/%{name}/decorations
%{_datadir}/%{name}/devices
%{_datadir}/%{name}/eagle
%{_datadir}/%{name}/ecus
%{_datadir}/%{name}/education
%{_datadir}/%{name}/emblems
%{_datadir}/%{name}/entertainment
%{_datadir}/%{name}/envelope
%{_datadir}/%{name}/europe
%{_datadir}/%{name}/face
%{_datadir}/%{name}/fanart
%{_datadir}/%{name}/farm
%{_datadir}/%{name}/Farm
%{_datadir}/%{name}/festive
%{_datadir}/%{name}/fish
%{_datadir}/%{name}/flag
%{_datadir}/%{name}/Flag
%{_datadir}/%{name}/flight
%{_datadir}/%{name}/flourish
%{_datadir}/%{name}/flower
%{_datadir}/%{name}/fly
%{_datadir}/%{name}/french
%{_datadir}/%{name}/friends
%{_datadir}/%{name}/fruit
%{_datadir}/%{name}/Galette
%{_datadir}/%{name}/game
%{_datadir}/%{name}/geography
%{_datadir}/%{name}/geometry
%{_datadir}/%{name}/glass
%{_datadir}/%{name}/grape
%{_datadir}/%{name}/great
%{_datadir}/%{name}/GTP
%{_datadir}/%{name}/guevara
%{_datadir}/%{name}/handshake
%{_datadir}/%{name}/hen
%{_datadir}/%{name}/Hen
%{_datadir}/%{name}/historic
%{_datadir}/%{name}/icon
%{_datadir}/%{name}/improvisedkeywordparse
%{_datadir}/%{name}/insect
%{_datadir}/%{name}/insects
%{_datadir}/%{name}/interface
%{_datadir}/%{name}/ladybug
%{_datadir}/%{name}/library
%{_datadir}/%{name}/linux
%{_datadir}/%{name}/Linux
%{_datadir}/%{name}/logo
%{_datadir}/%{name}/Logo
%{_datadir}/%{name}/logos
%{_datadir}/%{name}/magnifying
%{_datadir}/%{name}/mail
%{_datadir}/%{name}/mammal
%{_datadir}/%{name}/mammals
%{_datadir}/%{name}/man
%{_datadir}/%{name}/map
%{_datadir}/%{name}/maps
%{_datadir}/%{name}/mascot
%{_datadir}/%{name}/meat
%{_datadir}/%{name}/meeting
%{_datadir}/%{name}/money
%{_datadir}/%{name}/music
%{_datadir}/%{name}/musicsym
%{_datadir}/%{name}/navigation
%{_datadir}/%{name}/nicu
%{_datadir}/%{name}/northamerica
%{_datadir}/%{name}/note
%{_datadir}/%{name}/oceania
%{_datadir}/%{name}/office
%{_datadir}/%{name}/openclipart
%{_datadir}/%{name}/park
%{_datadir}/%{name}/pear
%{_datadir}/%{name}/penguin
%{_datadir}/%{name}/pig
%{_datadir}/%{name}/place
%{_datadir}/%{name}/plane
%{_datadir}/%{name}/plant
%{_datadir}/%{name}/postage
%{_datadir}/%{name}/presentation
%{_datadir}/%{name}/scissors
%{_datadir}/%{name}/Scotland
%{_datadir}/%{name}/shape
%{_datadir}/%{name}/shapes
%{_datadir}/%{name}/sign
%{_datadir}/%{name}/slides
%{_datadir}/%{name}/smiley
%{_datadir}/%{name}/soccer
%{_datadir}/%{name}/Software
%{_datadir}/%{name}/soup
%{_datadir}/%{name}/sports
%{_datadir}/%{name}/stamp
%{_datadir}/%{name}/star
%{_datadir}/%{name}/steaming
%{_datadir}/%{name}/study
%{_datadir}/%{name}/summer
%{_datadir}/%{name}/sun
%{_datadir}/%{name}/symbol
%{_datadir}/%{name}/tea
%{_datadir}/%{name}/technical
%{_datadir}/%{name}/telephone
%{_datadir}/%{name}/tools
%{_datadir}/%{name}/toy
%{_datadir}/%{name}/toys
%{_datadir}/%{name}/transport
%{_datadir}/%{name}/transportation
%{_datadir}/%{name}/tux
%{_datadir}/%{name}/Tux
%{_datadir}/%{name}/usmail
%{_datadir}/%{name}/vase
%{_datadir}/%{name}/vgcats
%{_datadir}/%{name}/vietnam
%{_datadir}/%{name}/warning
%{_datadir}/%{name}/water
%{_datadir}/%{name}/weather
%{_datadir}/%{name}/wildlife
%{_datadir}/%{name}/wine
%{_datadir}/%{name}/work
%files icons
%defattr(644,root,root,755)
#%%doc icons/*txt
%{_datadir}/%{name}/icons

%files people
%defattr(644,root,root,755)
#%%doc people/*txt
%{_datadir}/%{name}/people

%files ocal_logo
%defattr(644,root,root,755)
#%%doc ocal_logo/*txt
%{_datadir}/%{name}/ocal_logo

%files gradients
%defattr(644,root,root,755)
#%%doc gradients/*txt
%{_datadir}/%{name}/gradients

%files food
%defattr(644,root,root,755)
#%%doc food/*txt
%{_datadir}/%{name}/food

%files mime-types
%defattr(644,root,root,755)
#%%doc mime-types/*txt
%{_datadir}/%{name}/mime-types

%files actions
%defattr(644,root,root,755)
#%%doc actions/*txt
%{_datadir}/%{name}/actions

%files computer
%defattr(644,root,root,755)
#%%doc computer/*txt
%{_datadir}/%{name}/computer

%files filetype
%defattr(644,root,root,755)
#%%doc filetype/*txt
%{_datadir}/%{name}/filetype

%files homes
%defattr(644,root,root,755)
#%%doc homes/*txt
%{_datadir}/%{name}/homes

%files device
%defattr(644,root,root,755)
#%%doc device/*txt
%{_datadir}/%{name}/device

%files application
%defattr(644,root,root,755)
#%%doc application/*txt
%{_datadir}/%{name}/application

%files filesystems
%defattr(644,root,root,755)
#%%doc filesystems/*txt
%{_datadir}/%{name}/filesystems

%files action
%defattr(644,root,root,755)
#%%doc action/*txt
%{_datadir}/%{name}/action

%files apps
%defattr(644,root,root,755)
#%%doc apps/*txt
%{_datadir}/%{name}/apps

%files map_symbols
%defattr(644,root,root,755)
#%%doc map_symbols/*txt
%{_datadir}/%{name}/map_symbols

%files images
%defattr(644,root,root,755)
#%%doc images/*txt
%{_datadir}/%{name}/images

%files animals
%defattr(644,root,root,755)
#%%doc animals/*txt
%{_datadir}/%{name}/animals

%files signs
%defattr(644,root,root,755)
#%%doc signs/*txt
%{_datadir}/%{name}/signs

%files unsorted
%defattr(644,root,root,755)
#%%doc unsorted/*txt
%{_datadir}/%{name}/unsorted

%files filesystem
%defattr(644,root,root,755)
#%%doc filesystem/*txt
%{_datadir}/%{name}/filesystem
