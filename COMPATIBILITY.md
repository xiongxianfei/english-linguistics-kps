# Compatibility

## Key takeaway
KPS 12 uses canonical role-based Markdown and generated graph projections; KPS 9 tooling is not expected to parse the new metadata.

## Summary
This package migrated from base commit `034f21daa6946b744b367515cb4dbfc6a6720c4f`. Old role-bearing IDs remain aliases, but `type`, role-specific dependency fields and `references/` are no longer active conventions.

## Supported environment

Python 3.10 or newer, with no third-party runtime packages. Ordinary relative Markdown links remain canonical. Generated JSON format 12 is intended for this repository profile and should not be presented as a published external standard.

## Migration boundary

See [MIGRATION](MIGRATION.md). Git history preserves the KPS 9 state; the active tree does not duplicate it as a second knowledge store.
