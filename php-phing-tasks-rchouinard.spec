Summary:	Extra Phing tasks: LessCompiler, ManifestFile, YuiCompressor
Name:		php-phing-tasks-rchouinard
Version:	0.1
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/rchouinard/phing-tasks/tarball/master#/tasks.tgz
# Source0-md5:	9b10803f17807058c3a8650305af841f
Patch0:		fixes.patch
Requires:	php-phing
Suggests:	lessphp
Suggests:	yuicompressor
Provides:	php-phing-task-lesscompiler
Provides:	php-phing-task-manifestfile
Provides:	php-phing-task-yuicompressor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		phingdir	%{php_data_dir}/phing
%define		tasksdir	%{phingdir}/tasks/ext

%description
A collection of custom Phing tasks from Ryan Chouinard:
- LessCompilerTask
- ManifestFileTask
- YuiCompressorTask

%prep
%setup -qc
mv rchouinard-phing-tasks-*/* .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tasksdir}
cp -a classes/rych/tasks/*Task.php $RPM_BUILD_ROOT%{tasksdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{tasksdir}/LessCompilerTask.php
%{tasksdir}/ManifestFileTask.php
%{tasksdir}/YuiCompressorTask.php
