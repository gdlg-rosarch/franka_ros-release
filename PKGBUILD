# Script generated with Bloom
pkgdesc="ROS - A partly automatically generated package with all the configuration and launch files for using Panda research with MoveIt!"
url='http://wiki.ros.org/panda_moveit_config'

pkgname='ros-kinetic-panda-moveit-config'
pkgver='0.4.0_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-franka-description'
)

depends=('ros-kinetic-franka-description'
'ros-kinetic-joint-state-publisher'
'ros-kinetic-joint-trajectory-controller'
'ros-kinetic-moveit-commander'
'ros-kinetic-moveit-fake-controller-manager'
'ros-kinetic-moveit-kinematics'
'ros-kinetic-moveit-planners-ompl'
'ros-kinetic-moveit-ros-control-interface'
'ros-kinetic-moveit-ros-move-group'
'ros-kinetic-moveit-ros-visualization'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-rospy'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=panda_moveit_config
source=()
md5sums=()

prepare() {
    cp -R $startdir/panda_moveit_config $srcdir/panda_moveit_config
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

