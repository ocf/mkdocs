{ stdenvNoCC, python3Packages }:

stdenvNoCC.mkDerivation {
  name = "ocf-docs";
  src = ./.;

  nativeBuildInputs = with python3Packages; [
    mkdocs
    mkdocs-material
    mkdocs-rss-plugin
    mkdocs-git-revision-date-localized-plugin
    mkdocs-awesome-nav
  ];

  buildPhase = ''
    runHook preBuild
    mkdocs build
    runHook postBuild
  '';

  installPhase = ''
    runHook preInstall
    mv site $out
    runHook postInstall
  '';
}
