"""Run the documented verification suite; fail on any failed check."""
import os
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def run(command):
    print('+ ' + ' '.join(map(str, command)), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)

def main():
    run([sys.executable, 'tools/verify_counting.py'])
    run([sys.executable, 'tools/verify_networks.py'])
    with tempfile.TemporaryDirectory() as tmp:
        executable = str(Path(tmp)/'verify_worst_case')
        run([os.environ.get('CXX', 'c++'), '-O3', '-std=c++17', 'tools/verify_worst_case.cpp', '-o', executable])
        baseline = json.loads((ROOT/'data/worst_case_baseline.json').read_text())
        from verify_networks import validate_structure
        validate_structure(baseline)
        nets = json.loads((ROOT/'data/networks.json').read_text())['networks']
        contribution, = [n for n in nets if n['category']=='worst_case_swaps']
        network_file = Path(tmp)/'networks.txt'
        network_file.write_text(''.join(f'{i} {j}\n' for net in [baseline, contribution]
                                        for layer in net['layers'] for i,j in layer))
        run([executable, str(network_file)])
    print('PASS: verification suite complete. Large-input average values remain upstream-reported, not locally recomputed.')

if __name__ == '__main__':
    main()
