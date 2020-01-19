Summary:	Utilities for managing the XFS filesystem
Name:		xfsprogs
Version:	4.5.0
Release:	20%{?dist}
# Licensing based on generic "GNU GENERAL PUBLIC LICENSE"
# in source, with no mention of version.
# doc/COPYING file specifies what is GPL and what is LGPL
# but no mention of versions in the source.
License:	GPL+ and LGPLv2+
Group:		System Environment/Base
URL:		https://xfs.wiki.kernel.org
Source0:	http://kernel.org/pub/linux/utils/fs/xfs/xfsprogs/%{name}-%{version}.tar.gz
Source1:	xfsprogs-wrapper.h
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libtool, gettext, libattr-devel, libuuid-devel
BuildRequires:	readline-devel, libblkid-devel >= 2.17-0.1.git5e51568
Provides:	xfs-cmds
Obsoletes:	xfs-cmds <= %{version}
Provides:	xfsprogs-qa-devel
Obsoletes:	xfsprogs-qa-devel <= %{version}
Conflicts:	xfsdump < 3.0.1

Patch0:		xfsprogs-4.5.0-revert-AGFL-pack.patch
Patch1:		xfsprogs-4.5.0-change-mkfs-options.patch
Patch2:		xfsprogs-4.5.0-fix-headers.patch
Patch3:		xfsprogs-4.5.0-revert-xfs_db-sparse-inodes.patch
Patch4:		xfsprogs-4.5.0-xfs_repair-rtino-version.patch
Patch5:		xfsprogs-4.5.0-xfs_repair-quota-inodes.patch
Patch6:		xfsprogs-4.5.0-xfs_repair-exit-value-memory.patch
Patch7:		xfsprogs-4.7.0-defang-frag.patch
Patch8:		xfsprogs-4.7.0-fix-agf-limit-errors.patch
Patch9:		xfsprogs-4.7.0-quota-fixes.patch
Patch10:	xfsprogs-4.8.0-replace-ustat.patch
Patch11:	xfsprogs-revert-off64_t.patch
Patch12:	xfsprogs-4.9.0-junk-attr-leaf-count-zero.patch
Patch13:	xfsprogs-4.8.0-xfs_copy-UUID.patch
Patch14:	xfsprogs-4.10.0-xfs_metadump-ignore-0-entries.patch
Patch15:	xfsprogs-4.9-xfs_io-fix-m-option.patch
# RHEL-7.5
Patch16:	xfsprogs-4.8.0-mkfs.xfs-clarify-ftype-defaults-in-manpage.patch
Patch17:	xfsprogs-4.12.0-mkfs.xfs-allow-specification-of-0-data-stripe-width-.patch
Patch18:	xfsprogs-4.12.0-xfs_db-update-buffer-size-when-new-type-is-set.patch
Patch19:	xfsprogs-4.12.0-xfs_db-improve-argument-naming-in-set_cur-and-set_io.patch
Patch20:	xfsprogs-4.12.0-xfs_db-properly-set-inode-type.patch
Patch21:	xfsprogs-4.13.0-mkfs.xfs-Don-t-stagger-AG-for-a-single-disk.patch
Patch22:	xfsprogs-4.13.0-xfs_repair-don-t-use-do_warn-for-normal-log-message.patch
Patch23:	xfsprogs-4.11.0-xfs_repair-warn-about-dirty-log-with-n-option.patch
Patch24:	xfsprogs-4.8.0-xfs_repair-exit-with-status-2-if-log-dirtiness-is-un.patch
Patch25:	xfsprogs-4.16-xfs_repair-handle-corrupt-log.patch
# RHEL-7.6
Patch26:	xfsprogs-4.10.0-xfs_db-fix-the-source-command-when-passed-as-a-c-opt.patch
Patch27:	xfsprogs-4.14.0-db-increase-metadump-s-default-overly-long-extent-di.patch
Patch28:	xfsprogs-4.15.0-xfs_db-fix-crash-when-field-list-selector-string-has.patch
Patch29:	xfsprogs-4.15.0-xfsprogs-update-dead-urls.patch
Patch30:	xfsprogs-4.17.0-xfsprogs-be-careful-about-what-we-stat-in-platform_c.patch
Patch31:	xfsprogs-4.17.0-xfs_io-add-label-command.patch
Patch32:	xfsprogs-4.18-repair-root-parent.patch
# RHEL-7.7
Patch33:	xfsprogs-4.15.0-xfs_copy-accept-CRC-version-of-ABTB_MAGIC-in-ASSERT.patch
Patch34:	xfsprogs-4.20-xfs_quota-fix-false-error-reporting-of-project-inhertance-flag.patch
Patch35:	xfsprogs-4.20-xfs_repair-initialize-non-leaf-finobt-blocks-with-co.patch


%description
A set of commands to use the XFS filesystem, including mkfs.xfs.

XFS is a high performance journaling filesystem which originated
on the SGI IRIX platform.  It is completely multi-threaded, can
support large files and large filesystems, extended attributes,
variable block sizes, is extent based, and makes extensive use of
Btrees (directories, extents, free space) to aid both performance
and scalability.

%package devel
Summary: XFS filesystem-specific headers
Group: Development/Libraries
Requires: xfsprogs = %{version}-%{release}, libuuid-devel

%description devel
xfsprogs-devel contains the header files needed to develop XFS
filesystem-specific programs.

You should install xfsprogs-devel if you want to develop XFS
filesystem-specific programs,  If you install xfsprogs-devel, you'll
also want to install xfsprogs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1

%build
export tagname=CC
%configure \
        --enable-readline=yes	\
	--enable-blkid=yes

# Kill rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make V=1 DIST_ROOT=$RPM_BUILD_ROOT install install-dev \
	PKG_ROOT_SBIN_DIR=%{_sbindir} PKG_ROOT_LIB_DIR=%{_libdir}

# nuke .la files, etc
rm -f $RPM_BUILD_ROOT/{%{_lib}/*.{la,a,so},%{_libdir}/*.{la,a}}
chmod 0755 $RPM_BUILD_ROOT/%{_libdir}/libhandle.so.*.*.*

# remove non-versioned docs location
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/xfsprogs/

# xfs_check is deprecated; nuke it from orbit for RHEL7
rm -f $RPM_BUILD_ROOT/%{_sbindir}/xfs_check
rm -f $RPM_BUILD_ROOT/%{_mandir}/man8/xfs_check*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc doc/CHANGES doc/COPYING doc/CREDITS README
%{_libdir}/*.so.*
%{_mandir}/man8/*
%{_mandir}/man5/*
%{_sbindir}/*

%files devel
%defattr(-,root,root)
%{_mandir}/man3/*
%dir %{_includedir}/xfs
%{_includedir}/xfs/handle.h
%{_includedir}/xfs/jdm.h
%{_includedir}/xfs/linux.h
%{_includedir}/xfs/xfs.h
%{_includedir}/xfs/xfs_arch.h
%{_includedir}/xfs/xfs_fs.h
%{_includedir}/xfs/xfs_types.h
%{_includedir}/xfs/xfs_format.h
%{_includedir}/xfs/xfs_da_format.h
%{_includedir}/xfs/xfs_log_format.h
%{_includedir}/xfs/xqm.h

%{_libdir}/*.so

%changelog
* Mon Feb 11 2019 Eric Sandeen <sandeen@redhat.com> 4.5.0-20
- xfs_quota: fix errors if project flag is not set on regular files (#1663502)
- xfs_repair: initialize non-leaf finobt blocks with correct magic (#1670154)

* Mon Feb 11 2019 Eric Sandeen <sandeen@redhat.com> 4.5.0-19
- xfs_copy: accept CRC version of ABTB_MAGIC in ASSERT (#1641023)

* Wed Jun 20 2018 Eric Sandeen <sandeen@redhat.com> 4.5.0-18
- xfs_repar: Fix root inode's parent for sf directory (#1590334)

* Wed Jun 13 2018 Eric Sandeen <sandeen@redhat.com> 4.5.0-17
- xfs_io: add online label command (#1584912)

* Thu May 31 2018 Eric Sandeen <sandeen@redhat.com> 4.5.0-16
- xfs_db: fix the source command when passed as -c option (#1510279)
- xfs_metadump: allow much larger extent counts (#1502927)
- xfs_db: fix crash when field list selector has garbage (#1532271)
- mkfs.xfs, others: don't stat non-block devices on startup (#1573974)
- Update project URLs throughout the pkg, code and docs (#1550798)

* Tue Feb 27 2018 Eric Sandeen <sandeen@redhat.com> 4.5.0-15
- xfs_repair: allow repair of corrupt log (#1549525)

* Thu Jan 25 2018 Eric Sandeen <sandeen@redhat.com> 4.5.0-14
- xfs_repair: fix incorrect exit status (#1523008)

* Fri Oct 06 2017 Eric Sandeen <sandeen@redhat.com> 4.5.0-13
- mkfs.xfs: clarify ftype defaults in manpage (#1488124)
- mkfs.xfs: allow specification of 0 data stripe width (#1444166)
- mkfs.xfs: Don't stagger AG for a single disk (#1492552)
- xfs_db: xfs_db-update-buffer-size-when-new-type-is-set (#1458670)

* Tue May 09 2017 Eric Sandeen <sandeen@redhat.com> 4.5.0-12
- xfs_io: Fix initial -m option (#1447270)

* Mon Mar 27 2017 Eric Sandeen <sandeen@redhat.com> 4.5.0-11
- xfs_metadump: ignore attr leaf with 0 entries (#1402944)

* Wed Mar 01 2017 Eric Sandeen <sandeen@redhat.com> 4.5.0-10
- xfs_copy: Fix meta UUID handling on multiple copies (#1377931)

* Fri Dec 16 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-9
- xfs_repair: junk leaf attribute if count == 0 (#1402944)

* Thu Sep 08 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-8
- revert loff_t to off64_t change to preserve xfs.h behavior (#1366291)
- accomodate lack of ustat() on some arches (#1373605)

* Wed Sep 07 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-7
- rebuild with libattr-devel dependency to fix xfs_fsr (#1372939)

* Tue Aug 09 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-6
- xfs_quota: misc fixes (#1365256)
- xfs_db: clarify frag command (#1365256)

* Mon Jul 18 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-5
- xfs_repair: Don't let low memory indicate corruption on exit (#1355929)

* Tue Jun 28 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-4
- xfs_db: Fix multi-inode-record chunks in 4.5.0 (#1346927)
- xfs_repair: Fix special inode handling in 4.5.0 (#1347698)
- xfs_repair: Fix quota inode handling in 4.5.0 (#1347719)

* Mon Jun 13 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-3
- mkfs.xfs: disable finobt by default, disable sparse inodes entirely (#1345961)
- Fix header files for compatibility (#1340553)

* Mon Jun 06 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-2
- Revert AGFL header packing (#1336920)

* Tue Mar 15 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-1
- Rebase to upstream v4.5.0 (#1309498)
- mkfs: default to CRC enabled filesystems
- mkfs: default to ftype enabled filesystems
- mkfs.xfs.8: Clarify mkfs vs. mount block size limits. (#1263535)
- xfs_copy: fix copy of hard 4k devices (#1231841)
- xfs_quota: use Q_XGETNEXTQUOTA for faster repquota (#1164652)
- xfs_fsr: more fixes for extent swaps with selinux (#1083833)
- xfs_copy: Allow UUID changes on V5 filesystems (#1072283)

* Fri Aug 07 2015 Eric Sandeen <sandeen@redhat.com> 3.2.2-2
- Fix xfs_metadump disclosure flaw, CVE-2012-2150  (#1251118)

* Mon Jun 15 2015 Eric Sandeen <sandeen@redhat.com> 3.2.2-1
- Update to upstream v3.2.2, plus fixes from v3.2.3 (#1223991)
- repair: fix unnecessary secondary scan if only last sb is corrupt (#1201238)
- repair: check ino alignment value to avoid mod by zero (#1223444)

* Fri Dec 19 2014 Eric Sandeen <sandeen@redhat.com> 3.2.1-6
- xfs_repair: fix maximum block offset test (#1173146)
- xfs_copy: fix assert failure on 4k sector devices (#1162414)
- xfs_quota: man page updates (#175133, #1175627)

* Fri Oct 24 2014 Eric Sandeen <sandeen@redhat.com> 3.2.1-5
- xfs_repair: copy stripe geometry from backup supers if needed (#1150857)

* Wed Sep 17 2014 Eric Sandeen <sandeen@redhat.com> 3.2.1-3
- Add supported file attributes to xfs.5 manpage (#1142555)

* Mon Sep 15 2014 Eric Sandeen <sandeen@redhat.com> 3.2.1-2
- xfs_quota: fix segfault when reporting on nonexistant path (#1077826)
- xfs_quota: fix reporting on symlinked paths (#1077841)

* Tue Jul 15 2014 Eric Sandeen <sandeen@redhat.com> 3.2.1-1
- New upstream release (#1119940)
- xfs_copy: fix data corruption of target (#1105170)
- mkfs.xfs: handle mkfs of file on 4k block device (#1101236)
- xfs_copy: don't exit with error code on success (#1100376)

* Tue Mar 11 2014 Eric Sandeen <sandeen@redhat.com> 3.2.0-0.10.alpha2
- Fix bug in xfs_repair's inode prefetch (#1083820)

* Tue Mar 11 2014 Eric Sandeen <sandeen@redhat.com> 3.2.0-0.9.alpha2
- Sync up with upstream's latest CRC enhancements (#1074037)

* Fri Feb 28 2014 Eric Sandeen <sandeen@redhat.com> 3.2.0-0.8.alpha2
- mkfs.xfs fix default log size for small filesystems (#1034003)
- xfs_copy: partial fixups for CRC filesystems (#1043570)
- xfs_logprint: Don't error out after split items lose context (#1043591)

* Tue Feb 24 2014 Eric Sandeen <sandeen@redhat.com> 3.2.0-0.7.alpha2
- xfs_metadump: Really add xfs_metadump -F option (#1040921)
- xfs_check: Remove xfs_check manpage, xfs_check is deprecated (#1029458)

* Mon Feb 24 2014 Eric Sandeen <sandeen@redhat.com> 3.2.0-0.6.alpha2
- xfs_metadump: Require -F if proper SB magic is not found (#1040921)
- xfs_repair: fix bad block pointer found in large directories (#1034157)
- libxfs: Don't mark single-map blockmaps as discontiguous (#1033480)
- libxfs: Clear stale buffer errors on write (1033480)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.2.0-0.5.alpha2
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.2.0-0.4.alpha2
- Mass rebuild 2013-12-27

* Mon Nov 25 2013 Eric Sandeen <sandeen@redhat.com> 3.2.0-0.3.alpha2
- New upstream alpha release (#1034445)
- Remove xfs_check reference from fsck.xfs output (#1029455)
- Fix xfs_fsr on some files with selinux attributes (#1034013)

* Fri Nov 15 2013 Eric Sandeen <sandeen@redhat.com> 3.2.0-0.2.alpha1
- Move xfs_types.h from xfsprogs-qa-devel to xfsprogs-devel (#1024048)
- Remove deprecated xfs_check from package (#1029458)

* Thu Sep 26 2013 Eric Sandeen <sandeen@redhat.com> 3.2.0-0.1.alpha1
- New upstream alpha release with preliminary CRC support (#1015632)
- Additional patches beyon 3.2.0-alpha1:
- Fix big endian build
- Handle symlinks in xfs_quota arguments (#1013668)
- Don't report non-regular files as xfsctl-capable (#1012412)
- Fix log recovery on 4k filesystems

* Thu Aug 15 2013 Eric Sandeen <sandeen@redhat.com> 3.1.11-3
- mkfs.xfs: fix protofile name create block reservation (#918473)

* Mon Jul 22 2013 Eric Sandeen <sandeen@redhat.com> 3.1.11-2
- Update xfs_metadump manpage re: frozen filesystems (#953442)

* Wed May 08 2013 Eric Sandeen <sandeen@redhat.com> 3.1.11-1
- New upstream release.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Eric Sandeen <sandeen@redhat.com> 3.1.10-1
- New upstream release, with non-broken tarball.

* Wed Dec 12 2012 Eric Sandeen <sandeen@redhat.com> 3.1.9-1
- New upstream release.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 30 2012 Eric Sandeen <sandeen@redhat.com> 3.1.8-4
- Rebuild against new RPM (RHBZ#808250)

* Wed Mar 28 2012 Eric Sandeen <sandeen@redhat.com> 3.1.8-3
- Move files out of /lib64 to /usr/lib64

* Wed Mar 28 2012 Eric Sandeen <sandeen@redhat.com> 3.1.8-2
- Move files out of /sbin to /usr/sbin

* Fri Mar 23 2012 Eric Sandeen <sandeen@redhat.com> 3.1.8-1
- New upstream release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Eric Sandeen <sandeen@redhat.com> 3.1.7-1
- New upstream release.

* Mon Oct 17 2011 Eric Sandeen <sandeen@redhat.com> 3.1.6-2
- Remove mistaken "test" in release string

* Fri Oct 14 2011 Eric Sandeen <sandeen@redhat.com> 3.1.6-1.test
- New upstream release.  Drop -DNDEBUG build flag.

* Thu Mar 31 2011 Eric Sandeen <sandeen@redhat.com> 3.1.5-1
- New upstream release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 18 2010 Eric Sandeen <sandeen@redhat.com> 3.1.4-1
- New upstream release; disable DEBUG for now to build

* Sat Aug 28 2010 Eric Sandeen <sandeen@redhat.com> 3.1.3-1
- New upstream release

* Fri May 07 2010 Eric Sandeen <sandeen@redhat.com> 3.1.2-1
- New upstream release

* Thu Apr 01 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-7
- make devel pkg require libuuid-devel (#576296)

* Mon Mar 15 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-6
- Fix missing locking for btree manipulation in xfs_repair

* Fri Feb 12 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-5
- --enable-static=no doesn't work; just nuke static libs

* Fri Feb 12 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-4
- Fix up -devel package descriptions

* Fri Feb 12 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-3
- Drop static libs (#556102)

* Mon Feb 01 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-2
- Fix mkfs of target with nothing blkid can recognize (#561870)
 
* Mon Feb 01 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-1
- New upstream release
- Fix fd validity test for device-less mkfs invocation
 
* Sun Jan 17 2010 Eric Sandeen <sandeen@redhat.com> 3.1.0-2
- Post-release mkfs fixes (#555847)

* Wed Jan 13 2010 Eric Sandeen <sandeen@redhat.com> 3.1.0-1
- New upstream release
- Minor fixups for new glibc headers
- Fixes default mkfs.xfs on 4k sector device (#539553)

* Tue Dec 08 2009 Eric Sandeen <sandeen@redhat.com> 3.0.3-5
- And finally, BuildRequire libblkid-devel

* Mon Dec 07 2009 Eric Sandeen <sandeen@redhat.com> 3.0.3-4
- Actually patch & run configure script w/ blkid bits...
- Kill rpath in xfs_fsr

* Fri Nov 20 2009 Eric Sandeen <sandeen@redhat.com> 3.0.3-3
- Fix up build issues w.r.t. off64_t

* Tue Nov 10 2009 Eric Sandeen <sandeen@redhat.com> 3.0.3-2
- Add trim/discard & libblkid support

* Tue Sep 01 2009 Eric Sandeen <sandeen@redhat.com> 3.0.3-1
- New upstream release

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-9
- Fix block overflows in xfs_repair and xfs_metadump

* Tue Jun 30 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-8
- Fix up build-requires after e2fsprogs splitup

* Thu Jun 18 2009 Dennis Gilmore <dennis@ausil.us> 3.0.1-7
- update sparc multilib handling

* Mon Jun 15 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-6
- Make lazy superblock counters the default

* Mon Jun 15 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-5
- Add fallocate command to config script & fix for 32-bit

* Mon Jun 15 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-4
- Add fallocate command to xfs_io

* Fri May 15 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-3
- Fix and re-enable readline

* Tue May 05 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-2
- Conflict with xfsdump < 3.0.1 since files moved between them

* Tue May 05 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-1
- New upstream release

* Sat Apr 18 2009 Eric Sandeen <sandeen@redhat.com> 3.0.0-4
- Fix build for non-multilib arches, oops.

* Sat Apr 18 2009 Eric Sandeen <sandeen@redhat.com> 3.0.0-3
- Create new xfsprogs-qa-devel subpackage

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Eric Sandeen <sandeen@redhat.com> 3.0.0-1
- New upstream release

* Thu Jan 08 2009 Eric Sandeen <sandeen@redhat.com> 2.10.2-3
- Fix perms of libhandle.so in specfile, not makefile

* Wed Jan 07 2009 Eric Sandeen <sandeen@redhat.com> 2.10.2-2
- Fix perms of libhandle.so so that it's properly stripped

* Sun Dec 07 2008 Eric Sandeen <sandeen@redhat.com> 2.10.2-1
- New upstream release, bugfix only.

* Wed Nov 26 2008 Eric Sandeen <sandeen@redhat.com> 2.10.1-4
- Add protection from borken sys_ustat
- Add final upstream versions of gfs2 & parallel build patches

* Wed Nov 12 2008 Eric Sandeen <sandeen@redhat.com> 2.10.1-2
- Recognize gfs/gfs2 in libdisk
- Enable parallel builds

* Fri Sep 05 2008 Eric Sandeen <sandeen@redhat.com> 2.10.1-1
- Update to xfsprogs 2.10.1
- Add ASCII case-insensitive support to xfsprogs.
- xfs_repair fixes

* Wed Jun 04 2008 Dennis Gilmore <dennis@ausil.us> 2.9.8-3
- sparc32 is built using the sparcv9 variant 

* Wed Jun 04 2008 Eric Sandeen <sandeen@redhat.com> 2.9.8-2
- Tidy up multilib hack for non-multilib arches & add sparc (#448452)

* Wed Apr 23 2008 Eric Sandeen <sandeen@redhat.com> 2.9.8-1
- Update to xfsprogs 2.9.8
- Add support for sb_features2 in wrong location
- Add -c option to xfs_admin to turn lazy-counters on/off
- Added support for mdp in libdisk/mkfs.xfs

* Sun Mar 02 2008 Eric Sandeen <sandeen@redhat.com> 2.9.7-1
- Update to xfsprogs 2.9.7
- Lazy sb counters back off by default; other misc fixes

* Wed Feb 06 2008 Eric Sandeen <sandeen@redhat.com> 2.9.6-1
- Update to xfsprogs 2.9.6 - fixes mkfs sizing problem.
- Trim down BuildRequires to what's actually required now

* Mon Jan 21 2008 Eric Sandeen <sandeen@redhat.com> 2.9.5-1
- Update to xfsprogs 2.9.5
- Contains more optimal mkfs defaults
- specfile cleanup, & don't restate config defaults

* Tue Oct 23 2007 Eric Sandeen <sandeen@redhat.com> 2.9.4-4
- Add arm to multilib header wrapper

* Tue Oct 02 2007 Eric Sandeen <sandeen@redhat.com> 2.9.4-3
- mkfs.xfs: Fix wiping old AG headers and purge whack buffers

* Mon Oct 01 2007 Eric Sandeen <sandeen@redhat.com> 2.9.4-2
- Add alpha to the multilib wrapper (#310411)

* Mon Sep 10 2007 Eric Sandeen <sandeen@redhat.com> 2.9.4-1
- Update to xfsprogs 2.9.4

* Fri Aug 24 2007 Eric Sandeen <sandeen@redhat.com> 2.9.3-3
- Add gawk to buildrequires

* Thu Aug 16 2007 Eric Sandeen <sandeen@redhat.com> 2.9.3-2
- Update license tag

* Thu Jul 26 2007 Eric Sandeen <sandeen@redhat.com> 2.9.3-1
- Upgrade to xfsprogs 2.9.2, quota, xfs_repair, and filestreams changes

* Thu Jul  6 2007 Eric Sandeen <sandeen@redhat.com> 2.8.21-1
- Upgrade to xfsprogs 2.8.21, lazy sb counters enabled,
  xfs_quota fix (#236746)

* Thu May 31 2007 Eric Sandeen <sandeen@redhat.com> 2.8.20-2
- Fix ppc64 build... again

* Fri May 25 2007 Eric Sandeen <sandeen@redhat.com> 2.8.20-1
- Upgrade to xfsprogs 2.8.20, several xfs_repair fixes

* Tue Mar 06 2007 Miroslav Lichvar <mlichvar@redhat.com> 2.8.18-3
- Remove libtermcap-devel from BuildRequires

* Wed Feb 14 2007 Miroslav Lichvar <mlichvar@redhat.com> 2.8.18-2
- Disable readline support for now (#223781)

* Sun Feb 04 2007 Jarod Wilson <jwilson@redhat.com> 2.8.18-1
- Post-facto changelog addition to note bump to 2.8.18

* Wed Sep 27 2006 Russell Cattelan <cattelan@thebarn.com> 2.8.11-3
- bump build version to 3 for a new brew build

* Tue Sep 26 2006 Russell Cattelan <cattelan@thebarn.com> 2.8.11-2
- add ppc64 build patch

* Thu Sep 21 2006 Russell Cattelan <cattelan@redhat.com> 2.8.11-1
- Upgrade to xfsprogs 2.8.11 Need to pick up important repair fixes

* Tue Jul 18 2006 Jeremy Katz <katzj@redhat.com> - 2.8.4-3
- exclude arch ppc64 for now (#199315)

* Mon Jul 17 2006 Jesse Keating <jkeating@redhat.com> - 2.8.4-2
- rebuild

* Tue Jul 04 2006 Robert Scheck <redhat@linuxnetz.de> 2.8.4-1
- Upgrade to 2.8.4 (#196599 #c2)

* Sun Jun 25 2006 Robert Scheck <redhat@linuxnetz.de> 2.8.3-1
- Upgrade to 2.8.3 (#196599)
- Applied Russell Coker's suggested patch to improve the
  performance for SELinux machines significantly (#120622)

* Sun Jun 25 2006 Robert Scheck <redhat@linuxnetz.de> 2.7.11-2
- Fixed multilib conflict of xfs/platform_defs.h (#192755)

* Sun Mar 12 2006 Robert Scheck <redhat@linuxnetz.de> 2.7.11-1
- Upgrade to 2.7.11 and spec file cleanup (#185234)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.7.3-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.7.3-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Oct 31 2005 Robert Scheck <redhat@linuxnetz.de> 2.7.3-1
- Upgrade to 2.7.3 and enabled termcap support (#154323)

* Wed Sep 28 2005 Florian La Roche <laroche@redhat.com>
- fixup building with current rpm

* Wed Apr 20 2005 Dave Jones <davej@redhat.com>
- Disable debug. (#151438)
- Rebuild with gcc4

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> - 2.6.13-3
- Rebuilt for new readline.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May  5 2004 Jeremy Katz <katzj@redhat.com> - 2.6.13-1
- update to 2.6.13 per request of upstream
- fixes mount by label of xfs on former raid partition (#122043)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan  8 2004 Jeremy Katz <katzj@redhat.com> 2.6.0-2
- add defattr (reported by Matthias)

* Tue Dec 23 2003 Elliot Lee <sopwith@redhat.com> 2.6.0-3
- Fix tyops in dependencies

* Mon Dec 22 2003 Jeremy Katz <katzj@redhat.com> 2.6.0-1
- build for Fedora Core
- switch to more explicit file lists, nuke .la files

* Tue Dec 16 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 2.6.0
- Update to 2.6.0.

* Sat Sep 13 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Sync with XFS 1.3.0.
- Update to 2.5.6.

* Thu Apr 10 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 2.3.9-0_2.90at
- Rebuilt for Red Hat 9.
