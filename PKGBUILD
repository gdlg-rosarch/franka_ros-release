# Script generated with Bloom
pkgdesc="ROS - franka_ros is a metapackage for all Franka Emika ROS packages"
url='http://wiki.ros.org/franka_ros'

pkgname='ros-kinetic-franka-ros'
pkgver='0.4.0_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-franka-control'
'ros-kinetic-franka-description'
'ros-kinetic-franka-example-controllers'
'ros-kinetic-franka-gripper'
'ros-kinetic-franka-hw'
'ros-kinetic-franka-msgs'
'ros-kinetic-franka-visualization'
'ros-kinetic-panda-moveit-config'
)

conflicts=()
replaces=()

_dir=franka_ros
source=()
md5sums=()

prepare() {
    cp -R $startdir/franka_ros $srcdir/franka_ros
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

