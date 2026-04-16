"""Shell command execution helpers."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CommandResult:
    stdout: str
    stderr: str
    returncode: int
    timed_out: bool = False


def run_command(
    cmd: List[str],
    timeout: Optional[int] = None,
    stdin_data: Optional[str] = None,
) -> CommandResult:
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        input=stdin_data,
    )
    return CommandResult(stdout=proc.stdout, stderr=proc.stderr, returncode=proc.returncode)


def run_command_strict(
    cmd: List[str],
    timeout: Optional[int] = None,
    stdin_data: Optional[str] = None,
) -> str:
    result = run_command(cmd, timeout=timeout, stdin_data=stdin_data)
    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(cmd)}\n"
            f"STDOUT:\n{result.stdout.strip()}\n"
            f"STDERR:\n{result.stderr.strip()}"
        )
    return result.stdout


def run_command_allow_timeout(
    cmd: List[str],
    timeout: int,
    stdin_data: Optional[str] = None,
) -> CommandResult:
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        stdout, stderr = proc.communicate(input=stdin_data, timeout=timeout)
        return CommandResult(stdout=stdout, stderr=stderr, returncode=proc.returncode)
    except subprocess.TimeoutExpired:
        proc.terminate()
        try:
            stdout, stderr = proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()
            stdout, stderr = proc.communicate()
        return CommandResult(stdout=stdout, stderr=stderr, returncode=proc.returncode, timed_out=True)
