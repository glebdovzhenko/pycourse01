let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  nativeBuildInputs = [ pkgs.qt5.qttools.dev ];

  propagatedBuildInputs = [
    (pkgs.python3.withPackages (ps: with ps; [
      matplotlib
      pyqt5
      setuptools
      numpy
      scipy
      pandas
      jupyterlab
      # before were course requirements
      # from this point on requirements are experimental
      nbformat
    ]))

  ];

  # Normally set by the wrapper, but we can't use it in nix-shell (?).
  QT_QPA_PLATFORM_PLUGIN_PATH="${pkgs.qt5.qtbase.bin}/lib/qt-${pkgs.qt5.qtbase.version}/plugins";
}

