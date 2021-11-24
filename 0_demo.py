from utils import get_config, run_process
from utils_commands import cmd_python

print(get_config())

run_process(
    cmd_python('print(1==1)')
)