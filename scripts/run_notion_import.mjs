import { spawnSync } from "node:child_process";

const importerArgs = [
  "scripts/import_notion_export.py",
  "--all",
  "--overwrite",
  "--allow-empty",
];

const candidates = process.platform === "win32"
  ? [["py", "-3"], ["python"]]
  : [["python3"], ["python"]];

for (const [command, ...prefixArgs] of candidates) {
  const result = spawnSync(command, [...prefixArgs, ...importerArgs], {
    stdio: "inherit",
  });

  if (result.error?.code === "ENOENT") continue;
  if (result.error) throw result.error;
  process.exit(result.status ?? 1);
}

throw new Error("Python 3 is required to import Notion ZIP files.");
