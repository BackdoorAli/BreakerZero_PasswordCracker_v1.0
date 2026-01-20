"""
BreakerZero v1.2.1 - Dynamic Password Cracking Toolkit by @BackdoorAli aka NotAlita
"""

import argparse
from core.plugin_loader import load_plugins
from utils.report_writer import ReportWriter

def main():
    parser = argparse.ArgumentParser(description="BreakerZero CLI")
    parser.add_argument("--tool", type=str, help="Plugin to run (e.g., ssh, http, ftp, hash)")
    parser.add_argument("--target", type=str, help="Target IP, URL or hash string")
    parser.add_argument("--user", type=str, help="Username for login attacks")
    parser.add_argument("--wordlist", type=str, help="Path to password wordlist")
    parser.add_argument("--hash-type", type=str, help="Hash type (md5, sha1, sha256)")
    parser.add_argument("--target-hash", type=str, help="Hash to be cracked (for hash module)")
    parser.add_argument("--report", action="store_true", help="Generate text report")
    parser.add_argument("--pdf", action="store_true", help="Generate PDF report")
    parser.add_argument("--html", action="store_true", help="Generate HTML report")
    parser.add_argument("--list", action="store_true", help="List all available plugins")
    args = parser.parse_args()

    results = []

    plugins = {name: module for name, module in load_plugins()}

    if args.list:
        print("Available Plugins:")
        for name in plugins.keys():
            print(f" - {name}")
        return

    if args.tool:
        selected = args.tool.lower()
        if selected not in plugins:
            print(f"[!] Plugin '{selected}' not found. Use --list to see available modules.")
            return

        plugin = plugins[selected]

        # Handle hash module separately
        if selected == "hash_cracker":
            if not (args.hash_type and args.target_hash and args.wordlist):
                print("[!] Missing arguments for hash module")
                return
            cracker = plugin.HashCracker(args.hash_type, args.target_hash, args.wordlist)
            result = cracker.run()
            results.append(f"HASH RESULT: {result}")
        else:
            if not (args.target and args.user and args.wordlist):
                print(f"[!] Missing required arguments for {selected}")
                return
            CrackerClass = getattr(plugin, [a for a in dir(plugin) if a.endswith("Cracker") or a.endswith("Forcer")][0])
            cracker = CrackerClass(args.target, args.user, args.wordlist)
            cracker.run()
            results.append(f"{selected.upper()} attack launched on {args.target} for user {args.user}")

    if args.report or args.pdf or args.html:
        reporter = ReportWriter()
        if args.report:
            reporter.generate_report(results)
        if args.pdf:
            reporter.generate_pdf(results)
        if args.html:
            reporter.generate_html(results)

if __name__ == "__main__":
    main()
