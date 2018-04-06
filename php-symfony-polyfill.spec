%define		php_min_version 5.3.3
Summary:	Symfony polyfills backporting features to lower PHP versions
Name:		php-symfony-polyfill
Version:	1.7.0
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/polyfill/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	751761359d26c55731c1858cc14a74c6
URL:		https://github.com/symfony/polyfill
Requires:	php(core) >= %{php_min_version}
Requires:	php-dirs >= 1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symfony polyfills backporting features to lower PHP versions.

%package php54
Summary:	Symfony polyfill backporting some PHP 5.4+ features to lower PHP versions
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description php54
Symfony polyfill backporting some PHP 5.4+ features to lower PHP
versions.

%package php55
Summary:	Symfony polyfill backporting some PHP 5.5+ features to lower PHP versions
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description php55
Symfony polyfill backporting some PHP 5.5+ features to lower PHP
versions.

%package php56
Summary:	Symfony polyfill backporting some PHP 5.6+ features to lower PHP versions
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description php56
Symfony polyfill backporting some PHP 5.6+ features to lower PHP
versions.

%package php70
Summary:	Symfony polyfill backporting some PHP 7.0+ features to lower PHP versions
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description php70
Symfony polyfill backporting some PHP 7.0+ features to lower PHP
versions.

%package php71
Summary:	Symfony polyfill backporting some PHP 7.1+ features to lower PHP versions
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description php71
Symfony polyfill backporting some PHP 7.1+ features to lower PHP
versions.

%package php72
Summary:	Symfony polyfill backporting some PHP 7.2+ features to lower PHP versions
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description php72
Symfony polyfill backporting some PHP 7.2+ features to lower PHP
versions.

%package util
Summary:	Symfony utilities for portability of PHP code
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description util
Symfony utilities for portability of PHP code.

%prep
%setup -qn polyfill-%{version}

# Docs
install -d -p docs/{Php54,Php55,Php56,Php70,Php71,Php72,Util}
mv *.md composer.json docs/
mv src/Php54/{*.md,composer.json} docs/Php54/
mv src/Php55/{*.md,composer.json} docs/Php55/
mv src/Php56/{*.md,composer.json} docs/Php56/
mv src/Php70/{*.md,composer.json} docs/Php70/
mv src/Php71/{*.md,composer.json} docs/Php71/
mv src/Php72/{*.md,composer.json} docs/Php72/
mv src/Util/{*.md,composer.json}  docs/Util/
# duplicates
rm src/*/LICENSE
rm src/Intl/*/LICENSE

# Remove unneeded polyfills
rm -r src/{Apcu,Iconv,Intl,Mbstring,Xml}
rm -r tests/{Apcu,Iconv,Intl,Mbstring}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Polyfill
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Polyfill

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%dir %{php_data_dir}/Symfony/Polyfill

%files php54
%defattr(644,root,root,755)
%doc docs/Php54/*
%{php_data_dir}/Symfony/Polyfill/Php54

%files php55
%defattr(644,root,root,755)
%doc docs/Php55/*
%{php_data_dir}/Symfony/Polyfill/Php55

%files php56
%defattr(644,root,root,755)
%doc docs/Php56/*
%{php_data_dir}/Symfony/Polyfill/Php56

%files php70
%defattr(644,root,root,755)
%doc docs/Php70/*
%{php_data_dir}/Symfony/Polyfill/Php70

%files php71
%defattr(644,root,root,755)
%doc docs/Php71/*
%{php_data_dir}/Symfony/Polyfill/Php71

%files php72
%defattr(644,root,root,755)
%doc docs/Php72/*
%{php_data_dir}/Symfony/Polyfill/Php72

%files util
%defattr(644,root,root,755)
%doc docs/Util/*
%{php_data_dir}/Symfony/Polyfill/Util
