$command = $args[0]

if ($command -eq "all") {
    # Get-ChildItem -Filter *.txt | Remove-Item -Force
    Remove-Item -Force -Recurse */__pycache__
    Remove-Item -Force -Recurse */*/__pycache__
    Remove-Item -Force -Recurse mediafiles
    Remove-Item db.sqlite3
}
elseif ($command -eq "migrations") {
    Remove-Item -Force -Recurse */migrations/* -Exclude __init__.py
}
else {
    Write-Host "Invalid command. Please use 'all' or 'migrations' as the first argument."
}
