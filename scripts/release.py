#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def run(*cmd, check=True):
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr.strip() or result.stdout.strip()}")
        sys.exit(1)
    return result.stdout.strip()


def bump(version, kind):
    major, minor, patch = map(int, version.lstrip("v").split("."))
    if kind == "major":
        return f"v{major + 1}.0.0"
    if kind == "minor":
        return f"v{major}.{minor + 1}.0"
    return f"v{major}.{minor}.{patch + 1}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", "-n", action="store_true", help="Show what would happen without making any changes")
    parser.add_argument("--force", "-f", action="store_true", help="Allow releasing from a branch other than main")
    args = parser.parse_args()
    dry_run = args.dry_run

    if dry_run:
        print("Dry run — no files will be written, no commits or tags created.\n")

    branch = run("git", "rev-parse", "--abbrev-ref", "HEAD")
    if branch != "main" and not args.force and not dry_run:
        print(f"Must be on main to release (currently on '{branch}'). Use --force to override.")
        sys.exit(1)

    dirty = run("git", "status", "--porcelain")
    if dirty and not dry_run:
        print("Working tree has uncommitted changes. Commit or stash first.")
        sys.exit(1)

    result = subprocess.run(
        ["git", "describe", "--tags", "--abbrev=0"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        current = "v0.0.0"
        print("No existing tags found, starting from v0.0.0")
    else:
        current = result.stdout.strip()
        print(f"Current version: {current}")

    print("\nBump type:")
    print("  1) major")
    print("  2) minor")
    print("  3) bugfix (patch)")

    choice = input("\nSelect [1/2/3]: ").strip()
    kinds = {"1": "major", "2": "minor", "3": "bugfix"}
    if choice not in kinds:
        print("Invalid selection.")
        sys.exit(1)

    new_version = bump(current, kinds[choice])

    confirm = input(f"\nRelease as {new_version}? [y/N]: ").strip().lower()
    if confirm != "y":
        print("Aborted.")
        sys.exit(0)

    if dry_run:
        print(f"\nWould write package.json version → {new_version.lstrip('v')}")
        print(f"Would write version.json → {new_version.lstrip('v')}")
        print(f"Would run: git add package.json")
        print(f"Would run: git commit -m 'release {new_version}'")
        print(f"Would run: git tag {new_version}")
        print(f"Would run: git push && git push --tags")
        return

    pkg_path = ROOT / "package.json"
    pkg = json.loads(pkg_path.read_text())
    pkg["version"] = new_version.lstrip("v")
    pkg_path.write_text(json.dumps(pkg, indent=2) + "\n")

    version_path = ROOT / "version.json"
    version_path.write_text(
        json.dumps({"docsVersion": new_version.lstrip("v")}) + "\n"
    )

    run("git", "add", "package.json")
    run("git", "commit", "-m", f"release {new_version}")
    run("git", "tag", new_version)

    print(f"\nTagged {new_version}.")

    push = input("\nPush now? [y/N]: ").strip().lower()
    if push == "y":
        run("git", "push")
        run("git", "push", "--tags")
        print("Pushed.")
    else:
        print("\nTo push:")
        print("  git push && git push --tags")


if __name__ == "__main__":
    main()
