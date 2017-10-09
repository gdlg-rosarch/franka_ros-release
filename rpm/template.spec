Name:           ros-kinetic-panda-moveit-config
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS panda_moveit_config package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/panda_moveit_config
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-franka-description
Requires:       ros-kinetic-joint-state-publisher
Requires:       ros-kinetic-joint-trajectory-controller
Requires:       ros-kinetic-moveit-commander
Requires:       ros-kinetic-moveit-kinematics
Requires:       ros-kinetic-moveit-planners-ompl
Requires:       ros-kinetic-moveit-ros-control-interface
Requires:       ros-kinetic-moveit-ros-move-group
Requires:       ros-kinetic-moveit-ros-visualization
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-xacro
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-franka-description

%description
A partly automatically generated package with all the configuration and launch
files for using Panda research with MoveIt!

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Oct 09 2017 Franka Emika GmbH <info@franka.de> - 0.1.1-0
- Autogenerated by Bloom

