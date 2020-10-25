import sys
import subprocess as sp
import pathlib as pl

def run(path):
	path = pl.Path(path)

	if not path.exists():
		raise FileNotFoundError(path)

	args = [path, *sys.argv[1:]]

	proc = sp.run(
		args,
		shell = True,
		stdin = sys.stdin,
		cwd = path.parent)

	sys.exit(proc.returncode)
