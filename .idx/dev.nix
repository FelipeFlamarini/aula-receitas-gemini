{ pkgs, ... }: {
  channel = "stable-24.05"; 
  packages = [ pkgs.python3 ];
  idx = {
    extensions = [ "ms-python.python" "rangav.vscode-thunder-client" ];
    workspace = {
      onCreate = {
        install =
          "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
        default.openFiles = [ "app.py" ];
      };
      onStart = { run-server = "./devserver.sh"; };
    };
  };
}
