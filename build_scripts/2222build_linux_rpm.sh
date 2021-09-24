#!/bin/bash



pip install setuptools_scm

WEED_INSTALLER_VERSION=$(python installer-version.py)

npm install electron-packager -g
npm install electron-installer-redhat -g


pip install pyinstaller==4.5
SPEC_FILE=$(python -c 'import weed; print(weed.PYINSTALLER_SPEC_PATH)')
pyinstaller --log-level=INFO "$SPEC_FILE"

cp -r dist/daemon ../weed-blockchain-gui
npm install
npm audit fix
npm run build_scripts


# sets the version for weed-blockchain in package.json
cp package.json package.json.orig
jq --arg VER "$WEED_INSTALLER_VERSION" '.version=$VER' package.json > temp.json && mv temp.json package.json

electron-packager . weed-blockchain --asar.unpack="**/daemon/**" --platform=linux \
--icon=src/assets/img/Weed.icns --overwrite --app-bundle-id=net.weed.blockchain \
--appVersion=$WEED_INSTALLER_VERSION



# reset the package.json to the original
mv package.json.orig package.json

if [ "$LAST_EXIT_CODE" -ne 0 ]; then
	echo >&2 "electron-packager failed!"
	exit $LAST_EXIT_CODE
fi

mv $DIR_NAME ../build_scripts/dist/
cd ../build_scripts || exit

if [ "$REDHAT_PLATFORM" = "x86_64" ]; then
	echo "Create weed-blockchain-$WEED_INSTALLER_VERSION.rpm"

	# shellcheck disable=SC2046
	NODE_ROOT="$(dirname $(dirname $(which node)))"

	# Disables build links from the generated rpm so that we dont conflict with other packages. See https://github.com/Weed-Network/weed-blockchain/issues/3846
	# shellcheck disable=SC2086
	sed -i '1s/^/%define _build_id_links none\n%global _enable_debug_package 0\n%global debug_package %{nil}\n%global __os_install_post \/usr\/lib\/rpm\/brp-compress %{nil}\n/' "$NODE_ROOT/lib/node_modules/electron-installer-redhat/resources/spec.ejs"

	# Updates the requirements for building an RPM on Centos 7 to allow older version of rpm-build and not use the boolean dependencies
	# See https://github.com/electron-userland/electron-installer-redhat/issues/157
	# shellcheck disable=SC2086
	sed -i "s#throw new Error('Please upgrade to RPM 4.13.*#console.warn('You are using RPM < 4.13')\n      return { requires: [ 'gtk3', 'libnotify', 'nss', 'libXScrnSaver', 'libXtst', 'xdg-utils', 'at-spi2-core', 'libdrm', 'mesa-libgbm', 'libxcb' ] }#g" $NODE_ROOT/lib/node_modules/electron-installer-redhat/src/dependencies.js

  electron-installer-redhat --src dist/$DIR_NAME/ --dest final_installer/ \
  --arch "$REDHAT_PLATFORM" --options.version $WEED_INSTALLER_VERSION \
  --license ../LICENSE
  LAST_EXIT_CODE=$?
  if [ "$LAST_EXIT_CODE" -ne 0 ]; then
	  echo >&2 "electron-installer-redhat failed!"
	  exit $LAST_EXIT_CODE
  fi
fi

ls final_installer/
