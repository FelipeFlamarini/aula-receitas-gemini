{ pkgs, ... }: {
  channel = "stable-24.05"; 
  packages = [ pkgs.python3 pkgs.python311Packages.pip ];
  idx = {
    extensions = [ "ms-python.python" ];
    workspace = {
      onCreate = {
        install =
          "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
        default.openFiles = [ "app.py" ];
      };
      onStart = { run-server = "./devserver.sh"; };
    };
    previews = {
      enable = true;
      previews = {
        web = {
          command = ["flask" "run" "--debug"];
          manager = "web";
        };
      };
    };

  };
}
