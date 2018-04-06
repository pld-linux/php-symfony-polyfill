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
rm -r {src,tests}/{Apcu,Iconv,Intl,Mbstring}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Polyfill
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Polyfill

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* LICENSE
%{php_data_dir}/Symfony/Polyfill
