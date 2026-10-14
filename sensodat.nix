let
nixpkgs = <nixpkgs>;
pkgs = import nixpkgs { config = {}; overlays = []; };
in
pkgs.stdenv.mkDerivation {
    pname = "sensodat";
    version = "1.1";
    src = pkgs.fetchFromGitHub {
        owner = "christianbirchler-org";
        repo = "sensodat";
        rev = "v1.1";
        hash = "sha256-kZux4ctoSo9Av/Dcx0OaAS2qz6KdqQzPlJ2ZrBFcSnA=";
    };
    
    nativeBuildInputs = [ pkgs.docker ];
    
    buildPhase = ''
    echo "test data" > data.txt
    '';
    
    installPhase = ''
    mkdir -p $out/share/doc/
    cp data.txt $out/share/doc/
    '';
}

