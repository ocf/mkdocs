{ stdenvNoCC, python3Packages }:

stdenvNoCC.mkDerivation {
  name = "ocf-docs";
  src = ./.;

  nativeBuildInputs = with python3Packages; [
    mkdocs
    mkdocs-material
    mkdocs-rss-plugin
    mkdocs-git-revision-date-localized-plugin
  ];

  buildPhase = ''
    mkdocs build
  '';

  installPhase = ''
    mv site $out
  '';
}
