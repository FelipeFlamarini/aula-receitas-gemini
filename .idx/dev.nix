{ pkgs, ... }: {
  channel = "stable-24.05"; # or "unstable"
  packages = [ pkgs.python3 pkgs.python311Packages.pip ];
  idx = {
    extensions = [ "ms-python.python" ];
    workspace = {
      onCreate = {
        install =
          "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
      };

      onStart = {
        flask-app = "./devserver.sh";
        default.openFiles = [ "app.py" ];
      };
    };
  };
}
